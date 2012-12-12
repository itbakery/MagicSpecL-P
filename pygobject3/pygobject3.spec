# Last updated for version 2.21.0
%define glib2_version                  2.22.4
%define gobject_introspection_version  0.10.8
%define python2_version                2.3.5

%if 0%{?fedora} > 12 || 0%{?rhel} > 6
%global with_python3 1
%define python3_version                3.1
%endif

### Abstract ###

Name: pygobject3
Version: 3.0.2
Release: 2%{?dist}
License: LGPLv2+ and MIT
Group: Development/Languages
Summary: Python 2 bindings for GObject Introspection
URL: https://live.gnome.org/PyGObject
BuildRoot: %{_tmppath}/%{name}-%{version}-root
#VCS: git:git://git.gnome.org/pygobject
Source: http://ftp.gnome.org/pub/GNOME/sources/pygobject/3.0/pygobject-%{version}.tar.xz

### Patches ###
Patch0: lm.patch

### Build Dependencies ###

BuildRequires: glib2-devel >= %{glib2_version}
BuildRequires: gobject-introspection-devel >= %{gobject_introspection_version}
BuildRequires: python2-devel >= %{python2_version}
%if 0%{?with_python3}
BuildRequires: python3-devel >= %{python3_version}
BuildRequires: python3-cairo-devel
%endif # if with_python3

BuildRequires: pycairo-devel
BuildRequires: automake, autoconf, libtool

# The cairo override module depends on this
Requires: pycairo

Requires: gobject-introspection >= %{gobject_introspection_version}

%description
The %{name} package provides a convenient wrapper for the GObject library
for use in Python programs.

%package devel
Summary: Development files for embedding PyGObject introspection support
Group: Development/Languages
Requires: %{name} = %{version}-%{release}
Requires: glib2-devel
Requires: gobject-introspection-devel
Requires: pkgconfig

%description devel
This package contains files required to embed PyGObject

%if 0%{?with_python3}
%package -n python3-gobject
Summary: Python 3 bindings for GObject Introspection
Group: Development/Languages

# The cairo override module depends on this
Requires: python3-cairo
Requires: gobject-introspection >= %{gobject_introspection_version}

%description -n python3-gobject
The python3-gobject package provides a convenient wrapper for the GObject 
library and and other libraries that are compatible with GObject Introspection, 
for use in Python 3 programs.

%endif # with_python3

%prep
%setup -q -n pygobject-%{version}
%patch0 -p1 -b .lm

autoreconf

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
find %{py3dir} -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'
%endif # with_python3

find -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python}|'

%build
PYTHON=%{__python} 
export PYTHON
%configure
make %{?_smp_mflags}

%if 0%{?with_python3}
pushd %{py3dir}
PYTHON=%{__python3}
export PYTHON
%configure
make %{_smp_mflags}
popd
%endif # with_python3

%install
rm -rf $RPM_BUILD_ROOT

%if 0%{?with_python3}
pushd %{py3dir}
PYTHON=%{__python3}
export PYTHON
make DESTDIR=$RPM_BUILD_ROOT install
popd

%endif # with_python3

make DESTDIR=$RPM_BUILD_ROOT install
find $RPM_BUILD_ROOT -name '*.la' -delete
find $RPM_BUILD_ROOT -name '*.a' -delete

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(644, root, root, 755)
%doc AUTHORS NEWS README COPYING
%doc examples

%{_libdir}/libpyglib-gi-2.0-python.so*
%dir %{python_sitearch}/gi
%{python_sitearch}/gi/*

%files devel
%defattr(644, root, root, 755)
%dir %{_includedir}/pygobject-3.0/
%{_includedir}/pygobject-3.0/pygobject.h
%{_libdir}/pkgconfig/pygobject-3.0.pc

%if 0%{?with_python3}
%files -n python3-gobject
%defattr(644, root, root, 755)
%doc AUTHORS NEWS README COPYING
%doc examples

%{_libdir}/libpyglib-gi-2.0-python3.so*
%dir %{python3_sitearch}/gi

%{python3_sitearch}/gi/*

%endif # with_python3

%changelog
* Sat Dec 08 2012 Liu Di <liudidi@gmail.com> - 3.0.2-2
- 为 Magic 3.0 重建

* Sat Oct 22 2011 Ignacio Casal Quinteiro <icq@gnome.org> - 3.0.2-1
- udpate to 3.0.2

* Fri Sep 30 2011 Ignacio Casal Quinteiro <icq@gnome.org> - 3.0.1-1
- udpate to 3.0.1

* Tue Sep 20 2011 Matthias Clasen <mclasen@redhat.com> - 3.0.0-1
- Update to 3.0.0

* Thu Sep 15 2011 John (J5) Palmieri <johnp@gnome.org> - 2.90.4-1
- update to 2.90.4
- get rid of packaging cruft that is taken care of by upstream now

* Wed Aug 31 2011 Ignacio Casal Quinteiro <icq@gnome.org> - 2.90.3-1
- udpate to 2.90.3

* Thu Aug 22 2011 John (J5) Palmieri <johnp@redhat.com> - 2.90.2-3
- remove some old requires

* Thu Aug 19 2011 John (J5) Palmieri <johnp@redhat.com> - 2.90.2-2
- fix up issues uncovered during package review
- disable docs because they still reference the static bindings 
  and upstream is working on new documentation

* Thu Aug 18 2011 John (J5) Palmieri <johnp@redhat.com> - 2.90.2-1
- Initial package
