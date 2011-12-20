Name: netmanager
Summary: Networking manager tools
Summary(zh_CN.UTF-8): 一霉
Version: 0.1.6
Release: 2mgc
License: GPL v2
Group: System Environment/Base
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Source0: %{name}-%{version}.tar.gz
Source1: netmanager.desktop
Packager: stronghill <stronghill {at} 163 {dot} com>
Distribution: MagicLinux
URL: http://www.linuxfans.org/
Vendor: MGC Group
Requires: libQtCore.so.4
Requires: libQtGui.so.4
Requires: libc.so.6
Requires: libc.so.6(GLIBC_2.0)
Requires: libc.so.6(GLIBC_2.1)
Requires: libc.so.6(GLIBC_2.1.3)
Requires: libgcc_s.so.1
Requires: libgcc_s.so.1(GCC_3.0)
Requires: libm.so.6
Requires: libpthread.so.0
Requires: libpthread.so.0(GLIBC_2.0)
Requires: libstdc++.so.6
Requires: libstdc++.so.6(CXXABI_1.3)
Requires: libstdc++.so.6(GLIBCXX_3.4)
Requires: rtld(GNU_HASH)
Requires: libstdc++.so.6(GLIBCXX_3.4.9)
Requires: libstdc++.so.6(GLIBCXX_3.4.11)

%description
Netmanager Tools

Author:
	stronghill

%description -l zh_CN.UTF-8
一虻サ摺

%prep
%setup -q

%build
make clean
qmake4
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/pixmaps/%{name}
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/applications

install -m 755 %{name} %{buildroot}%{_bindir}/%{name}
install -m 644 tong.jpg %{buildroot}%{_datadir}/pixmaps/%{name}/tong.jpg
install -m 644 butong.jpg %{buildroot}%{_datadir}/pixmaps/%{name}/butong.jpg
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/applications
install -m 644 netmanagerzh_CN.UTF-8.qm %{buildroot}%{_datadir}/%{name}/netmanagerzh_CN.UTF-8.qm
install -m 644 netmanagerzh_CN.UTF-8.qm %{buildroot}%{_datadir}/%{name}/netmanagerzh_CN.UTF-8.qm
install -m 644 netmanager.qm %{buildroot}%{_datadir}/%{name}/netmanager.qm
install -m 644 netmanager.ts %{buildroot}%{_datadir}/%{name}/netmanager.ts

magic_rpm_clean.sh

%clean
rm -rf $RPM_BUILD_ROOT

%post


%preun


%postun


%files
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/pixmaps/%{name}/*
%{_datadir}/applications/*
/usr/share/netmanager/netmanager.qm
/usr/share/netmanager/netmanager.ts
/usr/share/netmanager/netmanagerzh_CN.UTF-8.qm
/usr/share/netmanager/netmanagerzh_CN.UTF-8.qm

%changelog
* Tue Dec 20 2011 Liu Di <liudidi@gmail.com> - 0.1.6-2mgc
- 为 Magic 3.0 重建

* Mon Apr 5 2010 Version 0.1.6. Package rebuild with Easy RPM Builder
- 0.1.6 2010-04-05
- 澧炲姞浜嗘棤绾跨綉缁渨pa鍔犲瘑鏂瑰紡鐨勬敮鎸侊紝鍦╳pa-psk鐨則kip妯″紡涓嬫祴璇曢