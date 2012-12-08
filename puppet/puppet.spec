# Augeas and SELinux requirements may be disabled at build time by passing
# --without augeas and/or --without selinux to rpmbuild or mock

# F-17 and above have ruby-1.9.x, and place libs in a different location
%if 0%{?fedora} >= 17
%global puppet_libdir   %(ruby -rrbconfig -e 'puts RbConfig::CONFIG["vendorlibdir"]')
%else
%global puppet_libdir   %(ruby -rrbconfig -e 'puts RbConfig::CONFIG["sitelibdir"]')
%endif

%global confdir         conf/redhat
%global ruby_version    %(ruby -rrbconfig -e 'puts RbConfig::CONFIG["ruby_version"]')

%define _without_selinux 1

Name:           puppet
Version:        2.7.18
Release:        2%{?dist}
Summary:        A network tool for managing many disparate systems
License:        ASL 2.0
URL:            http://puppetlabs.com
Source0:        http://downloads.puppetlabs.com/%{name}/%{name}-%{version}.tar.gz
Source1:        http://downloads.puppetlabs.com/%{name}/%{name}-%{version}.tar.gz.asc
Source2:        puppetstoredconfigclean.rb
Source3:        puppet-nm-dispatcher
# https://projects.puppetlabs.com/issues/11325
# https://github.com/puppetlabs/puppet/commit/a71208ba
Patch0:         0001-Ruby-1.9.3-has-a-different-error-when-require-fails.patch
Patch1:         0001-Preserve-timestamps-when-installing-files.patch

Group:          System Environment/Base

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  facter >= 1.5
BuildRequires:  ruby >= 1.8.5

%if 0%{?fedora} || 0%{?rhel} >= 5
BuildArch:      noarch
# Work around the lack of ruby in the default mock buildroot
%if "%{ruby_version}"
Requires:       ruby(abi) = %{ruby_version}
%endif
Requires:       ruby(shadow)
%endif

# Pull in ruby selinux bindings where available
%if 0%{?fedora} || 0%{?rhel} >= 6
%{!?_without_selinux:Requires: ruby(selinux), libselinux-utils}
%else
%if 0%{?rhel} && 0%{?rhel} == 5
%{!?_without_selinux:Requires: libselinux-ruby, libselinux-utils}
%endif
%endif

Requires:       facter >= 1.5
%if "%{ruby_version}" == "1.8"
Requires:       ruby >= 1.8.5
%endif
%{!?_without_augeas:Requires: ruby(augeas)}

Requires(pre):  shadow-utils
Requires(post): chkconfig
Requires(preun): chkconfig
Requires(preun): initscripts
Requires(postun): initscripts

%description
Puppet lets you centrally manage every important aspect of your system using a
cross-platform specification language that manages all the separate elements
normally aggregated in different files, like users, cron jobs, and hosts,
along with obviously discrete elements like packages, services, and files.

%package server
Group:          System Environment/Base
Summary:        Server for the puppet system management tool
Requires:       puppet = %{version}-%{release}
Requires(post): chkconfig
Requires(preun): chkconfig
Requires(preun): initscripts
Requires(postun): initscripts

%description server
Provides the central puppet server daemon which provides manifests to clients.
The server can also function as a certificate authority and file server.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
patch -s -p1 < conf/redhat/rundir-perms.patch

# Fix some rpmlint complaints
for f in mac_dscl.pp mac_dscl_revert.pp \
         mac_pkgdmg.pp ; do
    sed -i -e'1d' examples/$f
    chmod a-x examples/$f
done
for f in external/nagios.rb network/http_server/mongrel.rb relationship.rb; do
    sed -i -e '1d' lib/puppet/$f
done
chmod +x ext/puppet-load.rb ext/regexp_nodes/regexp_nodes.rb

find examples/ -type f -empty | xargs rm
find examples/ -type f | xargs chmod a-x

# puppet-queue.conf is more of an example, used for stompserver
mv conf/puppet-queue.conf examples/etc/puppet/

%build
# Nothing to build

%install
rm -rf %{buildroot}
ruby install.rb --destdir=%{buildroot} --quick --no-rdoc --sitelibdir=%{puppet_libdir}

install -d -m0755 %{buildroot}%{_sysconfdir}/puppet/manifests
install -d -m0755 %{buildroot}%{_datadir}/%{name}/modules
install -d -m0755 %{buildroot}%{_localstatedir}/lib/puppet
install -d -m0755 %{buildroot}%{_localstatedir}/run/puppet
install -d -m0750 %{buildroot}%{_localstatedir}/log/puppet
install -Dp -m0644 %{confdir}/client.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/puppet
install -Dp -m0755 %{confdir}/client.init %{buildroot}%{_initrddir}/puppet
install -Dp -m0644 %{confdir}/server.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/puppetmaster
install -Dp -m0755 %{confdir}/server.init %{buildroot}%{_initrddir}/puppetmaster
install -Dp -m0644 %{confdir}/fileserver.conf %{buildroot}%{_sysconfdir}/puppet/fileserver.conf
install -Dp -m0644 %{confdir}/puppet.conf %{buildroot}%{_sysconfdir}/puppet/puppet.conf
install -Dp -m0644 %{confdir}/logrotate %{buildroot}%{_sysconfdir}/logrotate.d/puppet

# We need something for these ghosted files, otherwise rpmbuild
# will complain loudly. They won't be included in the binary packages
touch %{buildroot}%{_sysconfdir}/puppet/puppetmasterd.conf
touch %{buildroot}%{_sysconfdir}/puppet/puppetca.conf
touch %{buildroot}%{_sysconfdir}/puppet/puppetd.conf

# Replace redundant man pages with links to the canonical man page
pushd %{buildroot}%{_mandir}/man8 >/dev/null
ln -svf puppet-cert.8.gz puppetca.8.gz
ln -svf puppet-queue.8.gz puppetqd.8.gz
ln -svf puppet-kick.8.gz puppetrun.8.gz
ln -svf puppet-describe.8.gz pi.8.gz
ln -svf puppet-master.8.gz puppetmasterd.8.gz
ln -svf puppet-filebucket.8.gz filebucket.8.gz
ln -svf puppet-agent.8.gz puppetd.8.gz
ln -svf puppet-doc.8.gz puppetdoc.8.gz
ln -svf puppet-resource.8.gz ralsh.8.gz
popd >/dev/null

# Install a NetworkManager dispatcher script to pickup changes to
# /etc/resolv.conf and such (https://bugzilla.redhat.com/532085).
install -Dpv %{SOURCE3} \
    %{buildroot}%{_sysconfdir}/NetworkManager/dispatcher.d/98-%{name}

# Install the ext/ directory to %%{_datadir}/%%{name}
install -d %{buildroot}%{_datadir}/%{name}
cp -a ext/ %{buildroot}%{_datadir}/%{name}
# emacs and vim bits are installed elsewhere
rm -rf %{buildroot}%{_datadir}/%{name}/ext/{emacs,vim}

# The puppetstoredconfigclean script was removed now that puppet node clean
# does this job and more.  For folks that were using this, let's provide the
# script and give them a hint to use puppet node clean.  Remove this for the
# next major release after 2.7.
install -pv %{SOURCE2} %{buildroot}%{_datadir}/%{name}/ext/

# Install emacs mode files
emacsdir=%{buildroot}%{_datadir}/emacs/site-lisp
install -Dp -m0644 ext/emacs/puppet-mode.el $emacsdir/puppet-mode.el
install -Dp -m0644 ext/emacs/puppet-mode-init.el \
    $emacsdir/site-start.d/puppet-mode-init.el

# Install vim syntax files
vimdir=%{buildroot}%{_datadir}/vim/vimfiles
install -Dp -m0644 ext/vim/ftdetect/puppet.vim $vimdir/ftdetect/puppet.vim
install -Dp -m0644 ext/vim/syntax/puppet.vim $vimdir/syntax/puppet.vim

%if 0%{?fedora} >= 15
# Setup tmpfiles.d config
mkdir -p %{buildroot}%{_sysconfdir}/tmpfiles.d
echo "D /var/run/%{name} 0755 %{name} %{name} -" > \
    %{buildroot}%{_sysconfdir}/tmpfiles.d/%{name}.conf
%endif

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG LICENSE README.md examples
%{_bindir}/pi
%{_bindir}/puppet
%{_bindir}/ralsh
%{_bindir}/filebucket
%{_bindir}/puppetdoc
%{_sbindir}/puppetca
%{_sbindir}/puppetd
%{puppet_libdir}/*
%{_initrddir}/puppet
%dir %{_sysconfdir}/puppet
%if 0%{?fedora} >= 15
%config(noreplace) %{_sysconfdir}/tmpfiles.d/%{name}.conf
%endif
%config(noreplace) %{_sysconfdir}/sysconfig/puppet
%config(noreplace) %{_sysconfdir}/puppet/puppet.conf
%config(noreplace) %{_sysconfdir}/puppet/auth.conf
%ghost %config(noreplace,missingok) %{_sysconfdir}/puppet/puppetca.conf
%ghost %config(noreplace,missingok) %{_sysconfdir}/puppet/puppetd.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/puppet
%dir %{_sysconfdir}/NetworkManager
%dir %{_sysconfdir}/NetworkManager/dispatcher.d
%{_sysconfdir}/NetworkManager/dispatcher.d/98-puppet
# We don't want to require emacs or vim, so we need to own these dirs
%{_datadir}/emacs
%{_datadir}/vim
%{_datadir}/%{name}
# These need to be owned by puppet so the server can
# write to them
%attr(-, puppet, puppet) %{_localstatedir}/run/puppet
%attr(0750, puppet, puppet) %{_localstatedir}/log/puppet
%attr(-, puppet, puppet) %{_localstatedir}/lib/puppet
# Exclude man pages from the server package
%exclude %{_mandir}/man8/puppet-kick.8.gz
%exclude %{_mandir}/man8/puppet-master.8.gz
%exclude %{_mandir}/man8/puppet-queue.8.gz
%exclude %{_mandir}/man8/puppetmasterd.8.gz
%exclude %{_mandir}/man8/puppetqd.8.gz
%exclude %{_mandir}/man8/puppetrun.8.gz
%{_mandir}/man5/puppet.conf.5.gz
%{_mandir}/man8/*.8.gz

%files server
%defattr(-, root, root, 0755)
%{_sbindir}/puppetmasterd
%{_sbindir}/puppetrun
%{_sbindir}/puppetqd
%{_initrddir}/puppetmaster
%config(noreplace) %{_sysconfdir}/puppet/fileserver.conf
%dir %{_sysconfdir}/puppet/manifests
%config(noreplace) %{_sysconfdir}/sysconfig/puppetmaster
%ghost %config(noreplace,missingok) %{_sysconfdir}/puppet/puppetmasterd.conf
# Ensure that man pages listed here are excluded from the main package
%{_mandir}/man8/puppet-kick.8.gz
%{_mandir}/man8/puppet-master.8.gz
%{_mandir}/man8/puppet-queue.8.gz
%{_mandir}/man8/puppetmasterd.8.gz
%{_mandir}/man8/puppetqd.8.gz
%{_mandir}/man8/puppetrun.8.gz

# Fixed uid/gid were assigned in bz 472073 (Fedora), 471918 (RHEL-5),
# and 471919 (RHEL-4)
%pre
getent group puppet &>/dev/null || groupadd -r puppet -g 52 &>/dev/null
getent passwd puppet &>/dev/null || \
useradd -r -u 52 -g puppet -d %{_localstatedir}/lib/puppet -s /sbin/nologin \
    -c "Puppet" puppet &>/dev/null
# ensure that old setups have the right puppet home dir
if [ $1 -gt 1 ] ; then
  usermod -d %{_localstatedir}/lib/puppet puppet &>/dev/null
fi
exit 0

%post
/sbin/chkconfig --add puppet || :

%post server
/sbin/chkconfig --add puppetmaster || :

%preun
if [ "$1" = 0 ] ; then
  /sbin/service puppet stop >/dev/null 2>&1
  /sbin/chkconfig --del puppet || :
fi

%preun server
if [ "$1" = 0 ] ; then
  /sbin/service puppetmaster stop >/dev/null 2>&1
  /sbin/chkconfig --del puppetmaster || :
fi

%postun
if [ "$1" -ge 1 ]; then
  /sbin/service puppet condrestart >/dev/null 2>&1 || :
fi

%postun server
if [ "$1" -ge 1 ]; then
  /sbin/service puppetmaster condrestart >/dev/null 2>&1 || :
fi

%clean
rm -rf %{buildroot}

%changelog
* Sat Dec 08 2012 Liu Di <liudidi@gmail.com> - 2.7.18-2
- 为 Magic 3.0 重建

* Wed Jul 11 2012 Todd Zullinger <tmz@pobox.com> - 2.7.18-1
- Update to 2.7.17, fixes CVE-2012-3864, CVE-2012-3865, CVE-2012-3866,
  CVE-2012-3867
- Improve NetworkManager compatibility, thanks to Orion Poplawski (#532085)
- Preserve timestamps when installing files

* Wed Apr 25 2012 Todd Zullinger <tmz@pobox.com> - 2.7.13-1
- Update to 2.7.13
- Change license from GPLv2 to ASL 2.0
- Drop %%post hacks to deal with upgrades from 0.25
- Minor rpmlint fixes
- Backport patch to silence confine warnings in ruby-1.9.3

* Wed Apr 11 2012 Todd Zullinger <tmz@pobox.com> - 2.6.16-1
- Update to 2.6.16, fixes CVE-2012-1986, CVE-2012-1987, and CVE-2012-1988
- Correct permissions of /var/log/puppet (0750)

* Wed Feb 22 2012 Todd Zullinger <tmz@pobox.com> - 2.6.14-1
- Update to 2.6.14, fixes CVE-2012-1053 and CVE-2012-1054

* Mon Feb 13 2012 Todd Zullinger <tmz@pobox.com> - 2.6.13-3
- Move rpmlint fixes to %%prep, add a few additional fixes
- Bump minimum ruby version to 1.8.5 now that EL-4 is all but dead
- Update install locations for Fedora-17 / Ruby-1.9
- Use ruby($lib) for augeas and shadow requirements
- Only try to run 0.25.x -> 2.6.x pid file updates on EL

* Thu Jan 05 2012 Todd Zullinger <tmz@pobox.com> - 2.6.13-2
- Revert to minimal patch for augeas >= 0.10 (bz#771097)

* Wed Dec 14 2011 Todd Zullinger <tmz@pobox.com> - 2.6.13-1
- Update to 2.6.13
- Cherry-pick various augeas fixes from upstream (bz#771097)

* Sun Oct 23 2011 Todd Zullinger <tmz@pobox.com> - 2.6.12-1
- Update to 2.6.12, fixes CVE-2011-3872
- Add upstream patch to restore Mongrel XMLRPC functionality (upstream #10244)
- Apply partial fix for upstream #9167 (tagmail report sends email when nothing
  happens)

* Thu Sep 29 2011 Todd Zullinger <tmz@pobox.com> - 2.6.6-3
- Apply upstream patches for CVE-2011-3869, CVE-2011-3870, CVE-2011-3871, and
  upstream #9793

* Tue Sep 27 2011 Todd Zullinger <tmz@pobox.com> - 2.6.6-2
- Apply upstream patch for CVE-2011-3848

* Wed Mar 16 2011 Todd Zullinger <tmz@pobox.com> - 2.6.6-1
- Update to 2.6.6
- Ensure %%pre exits cleanly
- Fix License tag, puppet is now GPLv2 only
- Create and own /usr/share/puppet/modules (#615432)
- Properly restart puppet agent/master daemons on upgrades from 0.25.x
- Require libselinux-utils when selinux support is enabled
- Support tmpfiles.d for Fedora >= 15 (#656677)
- Apply a few upstream fixes for 0.25.5 regressions

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon May 17 2010 Todd Zullinger <tmz@pobox.com> - 0.25.5-1
- Update to 0.25.5
- Adjust selinux conditional for EL-6
- Apply rundir-perms patch from tarball rather than including it separately
- Update URL's to reflect the new puppetlabs.com domain

* Fri Jan 29 2010 Todd Zullinger <tmz@pobox.com> - 0.25.4-1
- Update to 0.25.4

* Tue Jan 19 2010 Todd Zullinger <tmz@pobox.com> - 0.25.3-2
- Apply upstream patch to fix cron resources (upstream #2845)

* Mon Jan 11 2010 Todd Zullinger <tmz@pobox.com> - 0.25.3-1
- Update to 0.25.3

* Tue Jan 05 2010 Todd Zullinger <tmz@pobox.com> - 0.25.2-1.1
- Replace %%define with %%global for macros

* Tue Jan 05 2010 Todd Zullinger <tmz@pobox.com> - 0.25.2-1
- Update to 0.25.2
- Fixes CVE-2010-0156, tmpfile security issue (#502881)
- Install auth.conf, puppetqd manpage, and queuing examples/docs

* Wed Nov 25 2009 Jeroen van Meeuwen <j.van.meeuwen@ogd.nl> - 0.25.1-1
- New upstream version

* Tue Oct 27 2009 Todd Zullinger <tmz@pobox.com> - 0.25.1-0.3
- Update to 0.25.1
- Include the pi program and man page (R.I.Pienaar)

* Sat Oct 17 2009 Todd Zullinger <tmz@pobox.com> - 0.25.1-0.2.rc2
- Update to 0.25.1rc2

* Tue Sep 22 2009 Todd Zullinger <tmz@pobox.com> - 0.25.1-0.1.rc1
- Update to 0.25.1rc1
- Move puppetca to puppet package, it has uses on client systems
- Drop redundant %%doc from manpage %%file listings

* Fri Sep 04 2009 Todd Zullinger <tmz@pobox.com> - 0.25.0-1
- Update to 0.25.0
- Fix permissions on /var/log/puppet (#495096)
- Install emacs mode and vim syntax files (#491437)
- Install ext/ directory in %%{_datadir}/%%{name} (/usr/share/puppet)

* Mon May 04 2009 Todd Zullinger <tmz@pobox.com> - 0.25.0-0.1.beta1
- Update to 0.25.0beta1
- Make Augeas and SELinux requirements build time options

* Mon Mar 23 2009 Todd Zullinger <tmz@pobox.com> - 0.24.8-1
- Update to 0.24.8
- Quiet output from %%pre
- Use upstream install script
- Increase required facter version to >= 1.5

* Tue Dec 16 2008 Todd Zullinger <tmz@pobox.com> - 0.24.7-4
- Remove redundant useradd from %%pre

* Tue Dec 16 2008 Jeroen van Meeuwen <kanarip@kanarip.com> - 0.24.7-3
- New upstream version
- Set a static uid and gid (#472073, #471918, #471919)
- Add a conditional requirement on libselinux-ruby for Fedora >= 9
- Add a dependency on ruby-augeas

* Wed Oct 22 2008 Todd Zullinger <tmz@pobox.com> - 0.24.6-1
- Update to 0.24.6
- Require ruby-shadow on Fedora and RHEL >= 5
- Simplify Fedora/RHEL version checks for ruby(abi) and BuildArch
- Require chkconfig and initstripts for preun, post, and postun scripts
- Conditionally restart puppet in %%postun
- Ensure %%preun, %%post, and %%postun scripts exit cleanly
- Create puppet user/group according to Fedora packaging guidelines
- Quiet a few rpmlint complaints
- Remove useless %%pbuild macro
- Make specfile more like the Fedora/EPEL template

* Mon Jul 28 2008 David Lutterkort <dlutter@redhat.com> - 0.24.5-1
- Add /usr/bin/puppetdoc

* Thu Jul 24 2008 Brenton Leanhardt <bleanhar@redhat.com>
- New version
- man pages now ship with tarball
- examples/code moved to root examples dir in upstream tarball

* Tue Mar 25 2008 David Lutterkort <dlutter@redhat.com> - 0.24.4-1
- Add man pages (from separate tarball, upstream will fix to
  include in main tarball)

* Mon Mar 24 2008 David Lutterkort <dlutter@redhat.com> - 0.24.3-1
- New version

* Wed Mar  5 2008 David Lutterkort <dlutter@redhat.com> - 0.24.2-1
- New version

* Sat Dec 22 2007 David Lutterkort <dlutter@redhat.com> - 0.24.1-1
- New version

* Mon Dec 17 2007 David Lutterkort <dlutter@redhat.com> - 0.24.0-2
- Use updated upstream tarball that contains yumhelper.py

* Fri Dec 14 2007 David Lutterkort <dlutter@redhat.com> - 0.24.0-1
- Fixed license
- Munge examples/ to make rpmlint happier

* Wed Aug 22 2007 David Lutterkort <dlutter@redhat.com> - 0.23.2-1
- New version

* Thu Jul 26 2007 David Lutterkort <dlutter@redhat.com> - 0.23.1-1
- Remove old config files

* Wed Jun 20 2007 David Lutterkort <dlutter@redhat.com> - 0.23.0-1
- Install one puppet.conf instead of old config files, keep old configs
  around to ease update
- Use plain shell commands in install instead of macros

* Wed May  2 2007 David Lutterkort <dlutter@redhat.com> - 0.22.4-1
- New version

* Thu Mar 29 2007 David Lutterkort <dlutter@redhat.com> - 0.22.3-1
- Claim ownership of _sysconfdir/puppet (bz 233908)

* Mon Mar 19 2007 David Lutterkort <dlutter@redhat.com> - 0.22.2-1
- Set puppet's homedir to /var/lib/puppet, not /var/puppet
- Remove no-lockdir patch, not needed anymore

* Mon Feb 12 2007 David Lutterkort <dlutter@redhat.com> - 0.22.1-2
- Fix bogus config parameter in puppetd.conf

* Sat Feb  3 2007 David Lutterkort <dlutter@redhat.com> - 0.22.1-1
- New version

* Fri Jan  5 2007 David Lutterkort <dlutter@redhat.com> - 0.22.0-1
- New version

* Mon Nov 20 2006 David Lutterkort <dlutter@redhat.com> - 0.20.1-2
- Make require ruby(abi) and buildarch: noarch conditional for fedora 5 or
  later to allow building on older fedora releases

* Mon Nov 13 2006 David Lutterkort <dlutter@redhat.com> - 0.20.1-1
- New version

* Mon Oct 23 2006 David Lutterkort <dlutter@redhat.com> - 0.20.0-1
- New version

* Tue Sep 26 2006 David Lutterkort <dlutter@redhat.com> - 0.19.3-1
- New version

* Mon Sep 18 2006 David Lutterkort <dlutter@redhat.com> - 0.19.1-1
- New version

* Thu Sep  7 2006 David Lutterkort <dlutter@redhat.com> - 0.19.0-1
- New version

* Tue Aug  1 2006 David Lutterkort <dlutter@redhat.com> - 0.18.4-2
- Use /usr/bin/ruby directly instead of /usr/bin/env ruby in
  executables. Otherwise, initscripts break since pidof can't find the
  right process

* Tue Aug  1 2006 David Lutterkort <dlutter@redhat.com> - 0.18.4-1
- New version

* Fri Jul 14 2006 David Lutterkort <dlutter@redhat.com> - 0.18.3-1
- New version

* Wed Jul  5 2006 David Lutterkort <dlutter@redhat.com> - 0.18.2-1
- New version

* Wed Jun 28 2006 David Lutterkort <dlutter@redhat.com> - 0.18.1-1
- Removed lsb-config.patch and yumrepo.patch since they are upstream now

* Mon Jun 19 2006 David Lutterkort <dlutter@redhat.com> - 0.18.0-1
- Patch config for LSB compliance (lsb-config.patch)
- Changed config moves /var/puppet to /var/lib/puppet, /etc/puppet/ssl
  to /var/lib/puppet, /etc/puppet/clases.txt to /var/lib/puppet/classes.txt,
  /etc/puppet/localconfig.yaml to /var/lib/puppet/localconfig.yaml

* Fri May 19 2006 David Lutterkort <dlutter@redhat.com> - 0.17.2-1
- Added /usr/bin/puppetrun to server subpackage
- Backported patch for yumrepo type (yumrepo.patch)

* Wed May  3 2006 David Lutterkort <dlutter@redhat.com> - 0.16.4-1
- Rebuilt

* Fri Apr 21 2006 David Lutterkort <dlutter@redhat.com> - 0.16.0-1
- Fix default file permissions in server subpackage
- Run puppetmaster as user puppet
- rebuilt for 0.16.0

* Mon Apr 17 2006 David Lutterkort <dlutter@redhat.com> - 0.15.3-2
- Don't create empty log files in post-install scriptlet

* Fri Apr  7 2006 David Lutterkort <dlutter@redhat.com> - 0.15.3-1
- Rebuilt for new version

* Wed Mar 22 2006 David Lutterkort <dlutter@redhat.com> - 0.15.1-1
- Patch0: Run puppetmaster as root; running as puppet is not ready
  for primetime

* Mon Mar 13 2006 David Lutterkort <dlutter@redhat.com> - 0.15.0-1
- Commented out noarch; requires fix for bz184199

* Mon Mar  6 2006 David Lutterkort <dlutter@redhat.com> - 0.14.0-1
- Added BuildRequires for ruby

* Wed Mar  1 2006 David Lutterkort <dlutter@redhat.com> - 0.13.5-1
- Removed use of fedora-usermgmt. It is not required for Fedora Extras and
  makes it unnecessarily hard to use this rpm outside of Fedora. Just
  allocate the puppet uid/gid dynamically

* Sun Feb 19 2006 David Lutterkort <dlutter@redhat.com> - 0.13.0-4
- Use fedora-usermgmt to create puppet user/group. Use uid/gid 24. Fixed
problem with listing fileserver.conf and puppetmaster.conf twice

* Wed Feb  8 2006 David Lutterkort <dlutter@redhat.com> - 0.13.0-3
- Fix puppetd.conf

* Wed Feb  8 2006 David Lutterkort <dlutter@redhat.com> - 0.13.0-2
- Changes to run puppetmaster as user puppet

* Mon Feb  6 2006 David Lutterkort <dlutter@redhat.com> - 0.13.0-1
- Don't mark initscripts as config files

* Mon Feb  6 2006 David Lutterkort <dlutter@redhat.com> - 0.12.0-2
- Fix BuildRoot. Add dist to release

* Tue Jan 17 2006 David Lutterkort <dlutter@redhat.com> - 0.11.0-1
- Rebuild

* Thu Jan 12 2006 David Lutterkort <dlutter@redhat.com> - 0.10.2-1
- Updated for 0.10.2 Fixed minor kink in how Source is given

* Wed Jan 11 2006 David Lutterkort <dlutter@redhat.com> - 0.10.1-3
- Added basic fileserver.conf

* Wed Jan 11 2006 David Lutterkort <dlutter@redhat.com> - 0.10.1-1
- Updated. Moved installation of library files to sitelibdir. Pulled
initscripts into separate files. Folded tools rpm into server

* Thu Nov 24 2005 Duane Griffin <d.griffin@psenterprise.com>
- Added init scripts for the client

* Wed Nov 23 2005 Duane Griffin <d.griffin@psenterprise.com>
- First packaging
