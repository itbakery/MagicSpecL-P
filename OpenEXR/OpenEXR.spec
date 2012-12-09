
# make -libs subpkg
%define libs 1

Name:	 OpenEXR
Version: 1.7.0
Release: 2%{?dist}
Summary: A high dynamic-range (HDR) image file format
Summary(zh_CN.UTF-8): 一个高度动态范围 (HDR) 的图像文件格式

Group:	 System Environment/Libraries
Group(zh_CN.UTF-8): 系统环境/库
License: BSD
URL:	 http://www.openexr.com/
Source0: http://download.savannah.nongnu.org/releases/openexr/openexr-%{version}.tar.gz
Source1: http://download.savannah.nongnu.org/releases/openexr/openexr-%{version}.tar.gz.sig
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Obsoletes: openexr < %{version}-%{release}
Provides:  openexr = %{version}-%{release}

Patch1: OpenEXR-1.6.1-pkgconfig.patch
Patch2: openexr-1.7.0-gcc46.patch

BuildRequires:  automake libtool
BuildRequires:  ilmbase-devel
BuildRequires:  zlib-devel

%if 0%{?libs}
Requires: %{name}-libs = %{version}-%{release}
%else
Obsoletes: %{name}-libs < %{version}-%{release}
Provides:  %{name}-libs = %{version}-%{release}
%endif

%description
OpenEXR is a high dynamic-range (HDR) image file format developed by Industrial
Light & Magic for use in computer imaging applications. This package contains
libraries and sample applications for handling the format.

%description -l zh_CN.UTF-8
一个高度动态范围 (HDR) 的图像文件格式。

%package devel
Summary: Headers and libraries for building apps that use %{name} 
Summary(zh_CN.UTF-8): %{name} 的开发文件
Group:	 Development/Libraries
Group(zh_CN.UTF-8): 开发/库
Obsoletes: openexr-devel < %{version}-%{release}
Provides:  openexr-devel = %{version}-%{release}
Requires: %{name}-libs = %{version}-%{release}
Requires: ilmbase-devel
Requires: pkgconfig
%description devel
%{summary}.
%description devel -l zh_CN.UTF-8
%{name} 的开发文件

%package libs
Summary: %{name} runtime libraries
Summary(zh_CN.UTF-8): %{name} 运行库
Group:   System Environment/Libraries
Group(zh_CN.UTF-8): 系统环境/库
%description libs
%{summary}.
%description libs -l zh_CN.UTF-8
%{name} 运行库

%prep
%setup -q -n openexr-%{version}

%patch1 -p1 -b .pkgconfig
%patch2 -p1

# work to remove rpaths, recheck on new releases
aclocal -Im4
libtoolize --force
rm -f configure
autoconf


%build
%configure --disable-static

# hack to omit unused-direct-shlib-dependencies
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

# unpackaged files
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
rm -f  $RPM_BUILD_ROOT%{_libdir}/lib*.la

# prepare docs
mkdir -p rpmdocs
cp -a IlmImfExamples rpmdocs/examples
rm -rf rpmdocs/examples/.deps


%check
# Not enabled, by default, takes a *very* long time. -- Rex
%{?_with_check:make check}


%clean
rm -rf $RPM_BUILD_ROOT


%if 0%{?libs}
%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig
%else
%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig
%endif


%files
%defattr(-,root,root,-)
%{_bindir}/*

%if 0%{?libs}
%files libs
%defattr(-,root,root,-)
%endif
%doc AUTHORS ChangeLog LICENSE NEWS README
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root,-)
#omit for now, they're mostly useless, and include multilib conflicts (#342781)
#doc rpmdocs/examples 
%{_datadir}/aclocal/*
%{_includedir}/OpenEXR/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*


%changelog
* Sun Dec 09 2012 Liu Di <liudidi@gmail.com> - 1.7.0-2
- 为 Magic 3.0 重建

* Thu Oct 16 2008 Liu Di <liudidi@gmail.com> - 1.6.1-1mgc
- 更新到 1.6.1

