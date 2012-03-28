%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name: lcms
Summary: Color Management System
Summary(zh_CN.GB18030): ÑÕÉ«¹ÜÀíÏµÍ³
Version: 1.19
Release: 3%{?dist}
Group: Applications/Productivity
Group(zh_CN.GB18030): Ó¦ÓÃ³ÌĞò/Éú²úÁ¦
License: LGPL
Source: http://www.littlecms.com/lcms-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot-%(%{__id_u} -n)
URL: http://www.littlecms.com/
Prefix: %{_prefix}
Packager: Ni Hui <shuizhuyuanluo@126.com>
BuildRequires: libjpeg-devel
BuildRequires: libtiff-devel
BuildRequires: pkgconfig
BuildRequires: python-devel
BuildRequires: swig >= 1.3.12
BuildRequires: zlib-devel
Provides: littlecms = %{version}-%{release}

%description
LittleCMS intends to be a small-footprint, speed optimized color management
engine in open source form.

%description -l zh_CN.GB18030
LittleCMS ÒâÔÚ³ÉÎªÒ»¸öÒÔ¿ªÔ´ĞÎÊ½µÄÇáÁ¿¼¶£¬ËÙ¶ÈÓÅ»¯µÄÑÕÉ«¹ÜÀíÒıÇæ¡£

%package -n python-%{name}
Summary: Python interface to LittleCMS
Summary(zh_CN.GB18030): LittleCMS µÄ python ½Ó¿Ú
Group: Development/Libraries
Group(zh_CN.GB18030): ¿ª·¢/¿â
Requires: python
Provides: python-littlecms = %{version}-%{release}

%description -n python-%{name}
Python interface to LittleCMS.

%description -n python-%{name} -l zh_CN.GB18030
LittleCMS µÄ python ½Ó¿Ú¡£

%package devel
Summary: Development files for LittleCMS
Summary(zh_CN.GB18030): LittleCMS µÄ¿ª·¢ÎÄ¼ş
Group: Development/Libraries
Group(zh_CN.GB18030): ¿ª·¢/¿â
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig
Provides: littlecms-devel = %{version}-%{release}

%description devel
Development files for LittleCMS.

%description devel -l zh_CN.GB18030
LittleCMS µÄ¿ª·¢ÎÄ¼ş¡£

%prep
%setup -q

%build
%configure --with-python
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} DESTDIR=%{buildroot} install

# ËÑË÷²¢É¾³ı"*.la"ÎÄ¼ş
find ${RPM_BUILD_ROOT} -type f -name "*.la" -exec rm -f {} ';'
rm %{buildroot}%{python_sitearch}/*.a -f

%clean
%{__rm} -rf %{buildroot} %{_builddir}/%{buildsubdir}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README.1ST doc/TUTORIAL.TXT
%{_bindir}/*
%{_libdir}/*.so.*
%{_mandir}/man1/*

%files devel
%defattr(-,root,root)
%doc doc/LCMSAPI.TXT
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

%files -n python-%{name}
%defattr(-,root,root)
%{python_sitearch}/lcms.py*
%{python_sitearch}/_lcms.so

%changelog
* Wed Mar 28 2012 Liu Di <liudidi@gmail.com> - 1.19-3
- ä¸º Magic 3.0 é‡å»º

* Fri Jan 13 2012 Liu Di <liudidi@gmail.com> - 1.19-2
- ä¸º Magic 3.0 é‡å»º

* Wed Aug 8 2007 Ni Hui <shuizhuyuanluo@126.com> - 1.17-0.1mgc
- initialize the first spec file for MagicLinux-2.1
