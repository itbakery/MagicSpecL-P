Summary: 	A simple text editor for Xfce
Summary(zh_CN):	Xfce下的简单文本编辑器
Name: 		mousepad
Version: 	0.2.16
Release: 	1%{?dist}
License:	GPL
URL: 		http://www.xfce.org/
Source0: 	http://archive.xfce.org/src/apps/mousepad/0.2/%{name}-%{version}.tar.bz2
Group: 		User Interface/Desktops
Group(zh_CN):	用户界面/桌面
BuildRoot: 	%{_tmppath}/%{name}-root

%description
A simple text editor for Xfce

%description -l zh_CN
Xfce下的简单文本编辑器。

%prep
%setup -q

%build
%configure --enable-final
make

%install
rm -rf $RPM_BUILD_ROOT
make install-strip DESTDIR=$RPM_BUILD_ROOT mandir=%{_mandir}
magic_rpm_clean.sh

%clean
rm -rf $RPM_BUILD_ROOT

%post
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
   %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%postun
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
   %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%files
%defattr(-,root,root)
%doc README ChangeLog INSTALL COPYING AUTHORS
%{_bindir}/
%{_datadir}/

%changelog
* Thu Feb 21 2008 Liu Di <liudidi@gmail.com> - 0.2.13-1mgc
- update to 0.2.13

* Tue Jan 30 2007 Liu Di <liudidi@gmail.com> - 0.2.12-1mgc
- update to 0.2.12
