%define _x_libraries /usr/%{_lib}

Summary: A client for peer-to-peer networks
Summary(zh_CN.UTF-8): 点对点网络客户端
Name: mldonkey
Version: 3.1.0
%define pkgversion %{version}
Release: 1%{?dist}

URL: http://mldonkey.sourceforge.net/
Source0: http://prdownloads.sourceforge.net/mldonkey/%{name}-%{pkgversion}.tar.bz2
Source1: mldonkey.init.in
Source2: mldonkey.sysconfig
Source3: mldonkey.desktop
Source4: mldw-header3_03.xpm
License: GPL
Group: Applications/Internet
Group(zh_CN.UTF-8): 应用程序/互联网
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: ocaml >= 3.09.0, lablgtk >= 2.10.0, gtk2-devel, autoconf >= 2.57, gcc-c++
BuildRequires: desktop-file-utils, zlib-devel, wget
BuildRequires: ncurses-devel, librsvg2-devel
BuildRequires: bzip2-devel, gd-devel
Requires: mldonkey-frontend, mldonkey-backend

%description
mldonkey is a new client to access the eDonkey network, a peer-to-peer
network particularly efficient for big files thanks to a multi-sources
download protocol. It is written in Objective-Caml, and comes with its
own GTK GUI, an HTTP interface and a telnet interface. It works on
most UNIX platforms.

%description -l zh_CN.UTF-8
mldonkey 是一款访问 eDonkey 网络、点对点网络专用、大文件传输的新客户端。
它是用 Objective-Caml 写的，有着自己的 GTK GUI，一个 HTTP 界面和一个
telnet 界面。它可以工作于大多数 UNIX 平台上。

%package backend
Summary: MLdonkey backend
Summary(zh_CN.UTF-8): MLdonkey 后端
Group: Applications/Internet
Group(zh_CN.UTF-8): 应用程序/互联网
Requires: nc
Requires: file

%description backend
mldonkey is a new client to access the eDonkey network, a peer-to-peer
network particularly efficient for big files thanks to a multi-sources
download protocol. It is written in Objective-Caml, and comes with its
own GTK GUI, an HTTP interface and a telnet interface. It works on
most UNIX platforms.

This package contains the mldonkey daemon.

%description backend -l zh_CN.UTF-8
mldonkey 是一款访问 eDonkey 网络、点对点网络专用、大文件传输的新客户端。
它是用 Objective-Caml 写的，有着自己的 GTK GUI，一个 HTTP 界面和一个
telnet 界面。它可以工作于大多数 UNIX 平台上。

本软件包包含了 mldonkey 的服务程序。

%package frontend
Summary: MLdonkey graphical user interfaces
Summary(zh_CN.UTF-8): MLdonkey 图形用户界面
Group: Applications/Internet
Group(zh_CN.UTF-8): 应用程序/互联网

%description frontend
mldonkey is a new client to access the eDonkey network, a peer-to-peer
network particularly efficient for big files thanks to a multi-sources
download protocol. It is written in Objective-Caml, and comes with its
own GTK GUI, an HTTP interface and a telnet interface. It works on
most UNIX platforms.

This package contains frontends for mldonkey.

%description frontend -l zh_CN.UTF-8
mldonkey 是一款访问 eDonkey 网络、点对点网络专用、大文件传输的新客户端。
它是用 Objective-Caml 写的，有着自己的 GTK GUI，一个 HTTP 界面和一个
telnet 界面。它可以工作于大多数 UNIX 平台上。

本软件包包含了 mldonkey 的前端。


%prep
%setup -q

%build
%configure --enable-pthread --enable-gui --disable-rpath \
           --enable-ocamlver=3.12.0
make depend
make opt
make utils

%install
rm -rf %{buildroot}
#mkdir -p %{buildroot}%{_bindir}
#install -p mlnet %{buildroot}%{_libdir}/mldonkey
#install -p mlgui mlim mlchat %{buildroot}%{_bindir}/
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_libdir}/mldonkey
mv %{buildroot}%{_bindir}/mlnet %{buildroot}%{_libdir}/mldonkey
mkdir -p %{buildroot}%{_localstatedir}/lib/mldonkey/chroot/bin


mkdir -p %{buildroot}%{_sysconfdir}/rc.d/init.d
sed -e's,@lib@,%{_lib},g' \
    -e's,@_x_libraries@,%{_x_libraries},' \
    < %{SOURCE1} > %{buildroot}%{_sysconfdir}/rc.d/init.d/mldonkey
chmod 0755 %{buildroot}%{_sysconfdir}/rc.d/init.d/mldonkey
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
install -p -m644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/mldonkey

mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/pixmaps
cp %{SOURCE4} %{buildroot}%{_datadir}/pixmaps
desktop-file-install --vendor MagicLinux \
  --dir %{buildroot}%{_datadir}/applications    \
  --add-category Application                    \
  --add-category Network                        \
  %{SOURCE3}

# for %doc
find . -type f | xargs chmod a-x

%clean
rm -rf %{buildroot} %{_builddir}/%{buildsubdir}

%files
%defattr(-,root,root,-)

%files backend
%defattr(-,root,root,-)
%doc Install.txt Copying.txt ChangeLog Developers.txt distrib docs
%{_libdir}/mldonkey
%{_sysconfdir}/rc.d/init.d/*
%config(noreplace) %{_sysconfdir}/sysconfig/mldonkey
/var/lib/mldonkey

%files frontend
%defattr(-,root,root,-)
%{_bindir}/*
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/pixmaps/mldw-header3_03.xpm

%pre backend
# Add the "mldonkey" user
/usr/sbin/useradd -c "mldonkey User" \
        -s /sbin/nologin -r -d /var/lib/mldonkey/home mldonkey 2> /dev/null || :

%post backend
/sbin/chkconfig --add mldonkey

%preun backend
if [ $1 = 0 ]; then
        /sbin/service mldonkey stop > /dev/null 2>&1
        /sbin/chkconfig --del mldonkey
fi

%changelog
* Tue Jun 10 2008 Ni Hui <shuizhuyuanluo@126.com> - 2.9.5-0.1mgc
- 更新至 2.9.5
- 恢复 frontend 的 gui 界面工具包
- 依赖 ocaml 编译
- 尝试移除依赖关系 compartment
- 戊子  五月初七

* Wed Oct 24 2007 Liu Di <liudidi@gmail.com> - 2.9.2-1mgc
- update to 2.9.2

* Fri Aug 10 2007 Liu Di <liudidi@gmail.com> - 2.9.0-1mgc
- updaet to 2.9.0

* Wed May 24 2006 Liu Di <liudidi@gmail.com> - 2.7.5-2mgc
- Add requires for compartment.
* Sat May 13 2006 Liu Di <liudidi@gmail.com> - 2.7.5-1mgc
- update to 2.7.5
* Fri Nov 25 2005 sejishikong <sejishikong@263.net>
- Repackage for Magiclinux 2.0rc1, Remove mlgui.
* Mon Oct  3 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 2.6.4.

* Mon Aug 22 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 2.6.3.

* Thu Jul 21 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 2.6.0.

* Wed Jul 13 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 2.5.30.17.

* Mon May  30 2005 Arjen Heidinga <dexter@beetjevreemd.nl>
- Update to 2.5.30.15.

* Mon May  30 2005 Arjen Heidinga <dexter@beetjevreemd.nl>
- Update to 2.5.30.9.

* Sat Apr  2 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 2.5.28.1.

* Fri Aug 20 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 2.5.28.

* Fri Aug  6 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 2.5.22.

* Thu May  6 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 2.5.21.

* Mon May  3 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 2.5.19.

* Sat Apr 17 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 2.5.18.

* Mon Mar  8 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 2.5.16.

* Sun Mar  7 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 2.5.14.

* Fri Feb  6 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 2.5.6.

* Mon Oct 13 2003 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 2.5-4.

* Sun Sep 14 2003 Axel Thimm <Axel.Thimm@ATrpms.net>
- Split package into frontend, backend and meta package.

* Thu Jun  5 2003 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 2.5-3.

* Sat May 24 2003 Axel Thimm <Axel.Thimm@ATrpms.net>
- Fixes reported by Cornelius Rossmanith <corni@gmx.net>.
- Make pid variable whitespace safe in init file.
- Add /tmp to chroot environment.

* Mon May 12 2003 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 2.4.

* Sun May 11 2003 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 2.04rc12.
- Added desktop entry.
- Remove explicit uid (was 92).

* Wed Mar  5 2003 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to cvs 2.02-27.

* Thu Dec 26 2002 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 2.02.

* Wed Dec 18 2002 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 2.01.

* Wed Nov 27 2002 Axel Thimm <Axel.Thimm@ATrpms.net>
- Initial build.


