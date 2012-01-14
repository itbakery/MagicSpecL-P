%define ver 2.3

Summary: Lian Lian Kan for Linux
Summary(zh_CN.UTF-8): Linux下的连连看
Name: llk
Version: %{ver}
Release: 1%{?dist}
License: GPL
URL: http://llk-linux.sourceforge.net
Group: Amusements/Games
Group(zh_CN.UTF-8): 娱乐/游戏
BuildRoot: %{_tmppath}/%{name}-%{ver}-%{release}-buildroot
Source0:%{name}_linux-%{ver}beta1.tar.gz
Source1:llk_linux.desktop
Prefix: %{_prefix}
Requires: glib2,gtk2
Packager: KanKer<kanker@163.com>

%description
Lian Lian Kan for Linux. It is an arcade game.

%description -l zh_CN.UTF-8
Linux下的连连看。它是一个街机游戏。

%package devel
Summary: %{name} development package
Summary(zh_CN.UTF-8): %{name} 开发包
Group: Development/Libraries
Group(zh_CN.UTF-8): 开发/库
Requires: %{name} = %{version}-%{release}
 
%description devel
%{name} development package
 
%description devel -l zh_CN.UTF-8
%{name} 开发包

%prep
%setup -q -n %{name}_linux-%{version}

%build
%configure
sed -i 's/lrt/lrt \-lX11/g' src/Makefile
make

%install
make DESTDIR=$RPM_BUILD_ROOT install
mkdir -p $RPM_BUILD_ROOT/usr/share/applications
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT/usr/share/applications/

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%{_bindir}
%{_datadir}
%exclude /usr/*/debug*

%files devel
%defattr(-,root,root)
/usr/doc/*
%{_includedir}/*

%changelog
* Tue Feb 9 2006 KanKer <kanker@163.com>
- update 2.3beta1
* Sun Dec 11 2005 KanKer <kanker@163.com>
- first spec

