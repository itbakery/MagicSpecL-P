Name: lensfun
Version: 0.2.5
Release: 2%{?dist}
Summary: A photographic lens database and a library for accessing it
Summary(zh_CN.UTF-8): 镜头校正库
Group: System Environment/Libraries
Group(zh_CN.UTF-8): 系统环境/库
License: GPLv2+
URL: http://lensfun.berlios.de
Source0: http://download.berlios.de/lensfun/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


%description
The goal of the lensfun library is to provide a open source database
of photographic lenses and their characteristics. In the past there
was a effort in this direction (see http://www.epaperpress.com/ptlens/),
but then author decided to take the commercial route and the database
froze at the last public stage. This database was used as the basement
on which lensfun database grew, thanks to PTLens author which gave his
permission for this, while the code was totally rewritten from scratch
(and the database was converted to a totally new, XML-based format).

The lensfun library not only provides a way to read the database and
search for specific things in it, but also provides a set of algorithms
for correcting images based on detailed knowledge of lens properties
and calibration data. Right now lensfun is designed to correct distortion,
transversal (also known as lateral) chromatic aberrations, vignetting
and colour contribution index of the lens.


%description -l zh_CN.UTF-8
%{name} 是用于镜头校正的库。

%package devel
Summary: lensfun development files
Summary(zh_CN.UTF-8): lensfun 的开发文件
Group: Development/Libraries
Group(zh_CN.UTF-8): 开发/库
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
Header and library definition files for developing applications
that use the lensfun library/database.

%description devel -l zh_CN.UTF-8
%{name}-devel 软件包包含了使用 %{name} 开发程序所需的库和头文件。

%prep
%setup -q


%build
./configure \
        --cflags="${CFLAGS:-%optflags}" \
        --cxxflags="${CXXFLAGS:-%optflags}" \
        --prefix=%{_prefix} \
        --bindir=%{_bindir} \
        --sysconfdir=%{_sysconfdir} \
        --datadir=%{_datadir}/lensfun \
        --libdir=%{_libdir} \
        --includedir=%{_includedir} \
        --libexecdir=%{_libexecdir}

make AUTODEP=0 %{?_smp_mflags} lensfun manual


%install
rm -rf %{buildroot}
make AUTODEP=0 INSTALL_PREFIX=%{?buildroot:%{buildroot}} install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%clean
rm -rf %{buildroot} %{_builddir}/%{buildsubdir}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,0755)
%doc %{_datadir}/doc/%{name}-%{version}/README
%doc %{_datadir}/doc/%{name}-%{version}/lgpl-3.0.txt
%doc %{_datadir}/doc/%{name}-%{version}/gpl-3.0.txt
%doc %{_datadir}/doc/%{name}-%{version}/cc-by-sa-3.0.txt
%{_libdir}/*.so.*
%{_datadir}/lensfun/*.xml

%files devel
%defattr(-,root,root,-)
%doc %{_datadir}/doc/%{name}-%{version}/manual
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Sun Jan 25 2009 Ni Hui <shuizhuyuanluo@126.com> - 0.2.3-0.1mgc
- 更新至 0.2.3
- 戊子  十二月三十

* Thu Jun 12 2008 Ni Hui <shuizhuyuanluo@126.com> - 0.2.2b-0.1mgc
- 首次生成 rpm 包
- 戊子  五月初九
