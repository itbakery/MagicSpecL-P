Summary: MagicLinux BugPatch Package
Summary(zh_CN.UTF-8): MagicLinux Java 配置包
Name: magic-java-config
Version: 3.0
Release: 1%{?dist}
Source0: %{name}.tar.gz
License: GPL
Group: Development/Libraries
Group(zh_CN.UTF-8): 开发/库
BuildRoot:%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Obsoletes: mgc-patch
Requires:  jdk = 2000:1.7.0_11

%description
- Config java chinese font;

%description -l zh_CN.UTF-8
- 配置java中文字体

%prep
%setup -q -n %{name}

#%build

%install
mkdir -p $RPM_BUILD_ROOT
cp -rf * $RPM_BUILD_ROOT


%post

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/etc/*
/usr/*


%changelog
* Fri Dec 07 2012 Liu Di <liudidi@gmail.com> - 2.5-4
- 为 Magic 3.0 重建

