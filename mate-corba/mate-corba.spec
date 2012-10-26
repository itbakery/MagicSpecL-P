Name:	mate-corba
Summary:	CORBA Object Request Broker for MATE Desktop
Version:	1.4.0
Release:	10%{?dist}
License:	LGPLv2+ and GPLv2+
URL:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz

Provides: MateCORBA-2.0

BuildRequires:	mate-common glib2-devel libIDL-devel pkgconfig libtool autoconf automake gtk-doc

%description
MateCORBA is a fork of GNOME's Orbit

%package devel
Summary: Development libraries, header files and utilities for mate-corba
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: indent
%description devel
This package contains the header files for MATE CORBA, libraries and utilities
necessary to write programs that use CORBA technology.

%prep
%setup -q -n %{name}-%{version}
NOCONFIGURE=1 ./autogen.sh

%build
%configure --enable-gtk-doc-html --enable-purify --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

rm -fv $RPM_BUILD_ROOT%{_libdir}/libMateCORBA-2.la
rm -fv $RPM_BUILD_ROOT%{_libdir}/libMateCORBA-imodule-2.la
rm -fv $RPM_BUILD_ROOT%{_libdir}/libMateCORBACosNaming-2.la
rm -fv $RPM_BUILD_ROOT%{_libdir}/matecorba-2.0/Everything_module.la
magic_rpm_clean.sh

%clean
rm -rf %{buildroot}


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc AUTHORS COPYING README TODO
%{_bindir}/matecorba-idl-2
%{_bindir}/matecorba-ior-decode-2
%{_bindir}/matecorba-linc-cleanup-sockets
%{_bindir}/matecorba-typelib-dump
%{_libdir}/libMateCORBA-2.so.0*
%{_libdir}/libMateCORBA-imodule-2.so.0*
%{_libdir}/libMateCORBACosNaming-2.so.0*
%{_libdir}/matecorba-2.0/

%files devel
%{_bindir}/matecorba2-config
%{_libdir}/libMateCORBA-2.so
%{_libdir}/libMateCORBACosNaming-2.so
%{_libdir}/libMateCORBA-imodule-2.so
%{_includedir}/matecorba-2.0/
%{_libdir}/libname-matecorba-server-2.a
%{_libdir}/pkgconfig/MateCORBA*-2.0.pc
%{_bindir}/matecorba-idl-2
%{_bindir}/matecorba-typelib-dump
%{_bindir}/matecorba-ior-decode-2
%{_datadir}/aclocal/MateCORBA2.m4
%{_datadir}/idl/matecorba-2.0/
%{_bindir}/matecorba-linc-cleanup-sockets
%{_datadir}/gtk-doc/

%changelog
* Fri Aug 10 2012 Rex Dieter <rdieter@fedoraproject.org> 1.4.0-10
- include gtk-doc stuff in -devel exclusively

* Fri Aug 10 2012 Rex Dieter <rdieter@fedoraproject.org> 1.4.0-9
- cleanup file lists
- omit auto-pkgconfig-related deps
- own %%{_libdir}/matecorba-2.0/
- drop deprecated stuff like Group:, %%defattr

* Tue Jul 24 2012 Dan Mashal <dan.mashal@fedoraproject.org. 1.4.0-8
- Clean up spec file per Rex's suggestions.

* Tue Jul 24 2012 Dan Mashal <dan.mashal@fedoraproject.org> 1.4.0-7
- Clean up spec file further.

* Sun Jul 22 2012 Dan Mashal <dan.mashal@fedoraproject.org> 1.4.0-6
- Cleanup spec file.

* Sat Jul 21 2012 Dan Mashal <dan.mashal@fedoraproject.org> 1.4.0-5
- Fix requirements, clean up spec file

* Tue Jul 17 2012 Dan Mashal <dan.mashal@fedoraproject.org> 1.4.0-4
- Update requirements, licensing and description

* Sat Jul 14 2012 Dan Mashal <dan.mashal@fedoraproject.org> 1.4.0-3
- Incorporate Rex's changes, clean up spec file, update licensing.

* Fri Jul 13 2012 Rex Dieter <rdieter@fedoraproject.org> 1.4.0-2
- omit Group: tag
- fix URL, Source0
- use %%configure macro
- BuildArch: noarch

* Thu Jul 12 2012 Dan Mashal <dan.mashal@fedoraproject.org> 1.4.0-1
- Initial build
