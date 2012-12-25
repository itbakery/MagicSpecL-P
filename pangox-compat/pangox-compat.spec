Name:           pangox-compat
Version:        0.0.2
Release:        1%{?dist}
Summary:        Compatibility library for pangox

License:        LGPLv2+
URL:            http://ftp.gnome.org/pub/GNOME/sources/pangox-compat/0.0/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/pangox-compat/0.0/%{name}-%{version}.tar.xz

BuildRequires:  pango-devel

%description
This is a compatibility library providing the obsolete pangox library
that is not shipped by Pango itself anymore.  

%package devel
Summary: Development files for pangox-compat
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q


%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc README COPYING NEWS AUTHORS
%{_libdir}/libpango*-*.so.*
%config %{_sysconfdir}/pango/pangox.aliases

%files devel
%{_libdir}/libpango*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*

%changelog
* Fri Nov 09 2012 Kalev Lember <kalevlember@gmail.com> - 0.0.2-1
- Update to 0.0.2

* Tue Aug 28 2012 Parag Nemade <pnemade AT redhat DOT com> - 0.0.1-1
- Initial package
