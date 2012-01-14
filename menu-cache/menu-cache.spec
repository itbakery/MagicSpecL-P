Name:           menu-cache
Version:        0.3.2
Release:        2%{?dist}
Summary:        Caching mechanism for freedesktop.org compliant menus

Group:          System Environment/Libraries
License:        LGPLv2+ and GPLv2+
URL:            http://lxde.org
Source0:        http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  glib2-devel >= 2.16.0
Requires:       redhat-menus

%description
Menu-cache is a caching mechanism for freedesktop.org compliant menus to 
speed up parsing of the menu entries. It is currently used by some of 
components of the LXDE desktop environment such as LXPanel or LXLauncher.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
%configure --disable-static
# remove rpath in menu-cache-gen
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
#FIXME: add ChangeLog and NEWS if there is content
%doc AUTHORS COPYING README
%{_libexecdir}/menu-cache-gen
%{_libexecdir}/menu-cached
%{_libdir}/libmenu-cache.so.*
#%{_mandir}/man*/*.gz


%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/menu-cache/
%{_includedir}/menu-cache/*.h
%{_libdir}/libmenu-cache.so
%{_libdir}/pkgconfig/libmenu-cache.pc


%changelog
* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Feb 27 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.2-1
- Update to 0.3.2

* Sun Feb 21 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.1-1
- Update to 0.3.1

* Tue Nov 10 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.6-1
- Update to 0.2.6

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 28 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.5-1
- Update to 0.2.5

* Mon Apr 20 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.4-1
- Update to 0.2.4

* Tue Mar 31 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.3-1
- Update to 0.2.3

* Wed Dec 10 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.2-1
- Update to 0.2.2

* Tue Dec 09 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0
- Split into base and devel package

* Sun Dec 07 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.3-1
- Initial Fedora package
