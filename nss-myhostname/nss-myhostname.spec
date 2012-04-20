Name:           nss-myhostname
Summary:        glibc plugin for local system host name resolution
Version:        0.3
Release:        2%{?dist}
License:        LGPLv2+
URL:            http://0pointer.de/lennart/projects/nss-myhostname/
Group:          System Environment/Libraries
Source:         http://0pointer.de/lennart/projects/nss-myhostname/nss-myhostname-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       /usr/sbin/ldconfig
Requires:       /bin/sh
Requires:       /bin/sed

%description
nss-myhostname is a plugin for the GNU Name Service Switch (NSS)
functionality of the GNU C Library (glibc) providing host name
resolution for the locally configured system hostname as returned by
gethostname(2). Various software relies on an always resolvable local
host name. When using dynamic hostnames this is usually achieved by
patching /etc/hosts at the same time as changing the host name. This
however is not ideal since it requires a writable /etc file system and
is fragile because the file might be edited by the administrator at
the same time. nss-myhostname simply returns all locally configure
public IP addresses, or -- if none are configured -- the IPv4 address
127.0.0.2 (wich is on the local loopback) and the IPv6 address ::1
(which is the local host) for whatever system hostname is configured
locally. Patching /etc/hosts is thus no longer necessary.

%prep
%setup -q

%build
%configure --prefix=/usr --libdir=%{_libdir}
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
rm -rf %{buildroot}/usr/share/doc/nss-myhostname
magic_rpm_clean.sh

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/ldconfig
# sed-fu to add myhostname to the hosts line of /etc/nsswitch.conf
if [ -f /etc/nsswitch.conf ] ; then
        sed -i.bak -e '
                /^hosts:/ !b
                /\<myhostname\>/ b
                s/[[:blank:]]*$/ myhostname/
                ' /etc/nsswitch.conf
fi

%preun
# sed-fu to remove myhostname from the hosts line of /etc/nsswitch.conf
if [ "$1" -eq 0 -a -f /etc/nsswitch.conf ] ; then
        sed -i.bak -e '
                /^hosts:/ !b
                s/[[:blank:]]\+myhostname\>//
                ' /etc/nsswitch.conf
fi

%postun -p /usr/sbin/ldconfig

%files
%defattr(-, root, root)
%doc README
%doc LICENSE
%{_libdir}/libnss*.so*

%changelog
* Fri Apr 20 2012 Liu Di <liudidi@gmail.com> - 0.3-2
- 为 Magic 3.0 重建

* Wed May 11 2011 Lennart Poettering <lpoetter@redhat.com> - 0.3-1
- New upstream version

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Mar 19 2009 - Lennart Poettering <lpoetter@redhat.com> - 0.2-2
- Add missing dependencies

* Mon Oct 27 2008 - Lennart Poettering <lpoetter@redhat.com> - 0.2-1
- Initial packaging
