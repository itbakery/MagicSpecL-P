%global cache /var/cache/man

Summary: Tools for searching and reading man pages
Name: man-db
Version: 2.6.0.2
Release: 2%{?dist}
# project man-db  GPLv2+
# Gnulib part     GPLv3+
License: GPLv2+ and GPLv3+
Group: System Environment/Base
URL: http://www.nongnu.org/man-db/
Source0: http://mirrors.igsobe.com/nongnu/man-db/%{name}-%{version}.tar.gz
Source1: man-db.crondaily
Source2: man-db.sysconfig
# Resolves: #655385 - use old format of nroff output
Patch1: man-db-2.5.9-sgr.patch
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Obsoletes: man < 2.0
Provides: man-pages-reader = %{version}
Provides: man = %{version}
BuildRequires: less
Requires: less, coreutils, grep, groff, gzip, crontabs
BuildRequires: gdbm-devel, groff, gettext, zlib-devel
BuildRequires: libpipeline-devel

%description
The man-db package includes five tools for browsing man-pages:
man, whatis, apropos, manpath and lexgrog. man preformats and displays
manual pages. whatis searches the manual page names. apropos searches the
manual page names and descriptions. manpath determines search path
for manual pages. lexgrog directly reads header information in
manual pages.

%prep
%setup -q
%patch1 -p1 -b .sgr

%build
%configure\
    --with-sections="1 1p 8 2 3 3p 4 5 6 7 9 0p n l p o 1x 2x 3x 4x 5x 6x 7x 8x"  \
    --disable-setuid --with-browser=elinks

make CC="%{__cc} %{optflags}" %{?_smp_mflags} V=1

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT prefix=%{_prefix} \
             INSTALL='install -p'

# move the documentation to relevant place
mv $RPM_BUILD_ROOT%{_datadir}/doc/man-db/* ./

# remove zsoelim - part of groff package
rm $RPM_BUILD_ROOT%{_bindir}/zsoelim
rm $RPM_BUILD_ROOT%{_datadir}/man/man1/zsoelim.1

# remove pages which are also in  man-pages-de
rm $RPM_BUILD_ROOT%{_mandir}/de/man1/zsoelim.1
rm $RPM_BUILD_ROOT%{_mandir}/de/man1/manpath.1
rm $RPM_BUILD_ROOT%{_mandir}/de/man5/manpath.5
rm $RPM_BUILD_ROOT%{_mandir}/de/man8/catman.8
rm $RPM_BUILD_ROOT%{_mandir}/de/man8/mandb.8

# remove libtool archives
rm $RPM_BUILD_ROOT%{_libdir}/man-db/*.la

# install cache directory
install -d -m 0755  $RPM_BUILD_ROOT%{cache}

# install cron script for man-db creation/update
install -D -p -m 0755 %{SOURCE1} $RPM_BUILD_ROOT/etc/cron.daily/man-db.cron

# config for cron script
install -D -p -m 0644 %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/man-db

%find_lang %{name}
%find_lang %{name}-gnulib

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang -f %{name}-gnulib.lang
%defattr(-,root,root,-)
%doc README man-db-manual.txt man-db-manual.ps docs/COPYING ChangeLog NEWS
%config(noreplace) %{_sysconfdir}/man_db.conf
%config(noreplace) %{_sysconfdir}/sysconfig/man-db
%{_sysconfdir}/cron.daily/man-db.cron
%{_sbindir}/accessdb
%{_bindir}/man
%{_bindir}/whatis
%{_bindir}/apropos
%{_bindir}/manpath
%{_bindir}/lexgrog
%{_bindir}/catman
%{_bindir}/mandb
%{_libdir}/man-db/*.so
%dir %{_libexecdir}/man-db
%{_libexecdir}/man-db/globbing
%{_libexecdir}/man-db/manconv
%attr(0755,root,root)   %dir %{cache}
# documentation and translation
%{_mandir}/man1/apropos.1*
%{_mandir}/man1/lexgrog.1*
%{_mandir}/man1/man.1*
%{_mandir}/man1/manconv.1*
%{_mandir}/man1/manpath.1*
%{_mandir}/man1/whatis.1*
%{_mandir}/man5/manpath.5*
%{_mandir}/man8/accessdb.8*
%{_mandir}/man8/catman.8*
%{_mandir}/man8/mandb.8*
%lang(de)   %{_datadir}/man/de/man*/*
%lang(es)   %{_datadir}/man/es/man*/*
%lang(it)   %{_datadir}/man/it/man*/*
%lang(ja)   %{_datadir}/man/ja/man*/*

%changelog
* Thu Apr 21 2011 Ivana Hutarova Varekova <varekova@redhat.com> - 2.6.0.2-1
- update to 2.6.0.2
- remove obsolete patches
- add libpipe dependency

* Wed Mar 23 2011 Ivana Hutarova Varekova <varekova@redhat.com> - 2.5.9-6
- Build with zlib support.
- Use elinks as default HTML browser.
   thanks Ville Skyttä

* Wed Mar 23 2011 Ivana Hutarova Varekova <varekova@redhat.com> - 2.5.9-5
* Resolves: #684977
  backport upstream patch

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 27 2011 Ivana Hutarova Varekova <varekova@redhat.com> - 2.5.9-3
- Resolves: #659292
  use ionice in man cron job

* Wed Nov 24 2010 Ivana Hutarova Varekova <varekova@redhat.com> - 2.5.9-2
- Resolves: #655385 - use old format of nroff output

* Mon Nov 22 2010 Ivana Hutarova Varekova <varekova@redhat.com> - 2.5.9-1
- update to 2.5.9

* Fri Oct  1 2010 Ivana Hutarova Varekova <varekova@redhat.com> - 2.5.7-8
- add less buildrequire

* Wed Sep 29 2010 jkeating - 2.5.7-7
- Rebuilt for gcc bug 634757

* Fri Sep 24 2010 Ivana Hutarova Varekova <varekova@redhat.com> - 2.5.7-6
- Resolves: #630506 (change the description)
- minor spec file changes

* Mon Aug 30 2010 Dennis Gilmore <dennis@ausil.us> - 2.5.7-5
- Provide Versioned man

* Mon Aug 16 2010 Ivana Hutarova Varekova <varekova@redhat.com> - 2.5.7-4
- remove obsolete conflict flag

* Mon Aug 16 2010 Ivana Hutarova Varekova <varekova@redhat.com> - 2.5.7-3
- provides man tag
- resolves: #621688
  remove problematic man-pages (now in man-pages-de package)

* Fri Apr 16 2010 Ivana Hutarova Varekova <varekova@redhat.com> - 2.5.7-2
- add conflicts tag

* Wed Feb 17 2010 Ivana Hutarova Varekova <varekova@redhat.com> - 2.5.7-1
- initial build
