Summary: Magic specific rpm configuration files.
Summary(zh_CN.UTF-8): Magic 特定的 rpm 配置文件
Name: magic-rpm-config
Version: 3.0
Release: 1%{?dist}
License: GPL+
Group: Development/System
Group(zh_CN.UTF-8): 开发/系统
Source0: magic-rpm-config-%{version}.tar.bz2
Source1: magic_rpm_clean.sh
Source2: rpmdel
Source3: macros.magic
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-root
Provides: redhat-rpm-config >= 9.1

%description
Magic specific rpm configuration files.

%description -l zh_CN.UTF-8
Magic 特定的 rpm 配置文件。

%prep
%setup -q

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}%{_prefix}/lib/rpm
( cd ${RPM_BUILD_ROOT}%{_prefix}/lib/rpm; tar xjvf %{SOURCE0}; mv %{name}-%{version} mBuild; ln -s mBuild redhat; rm -f mBuild/*.spec )

# fix perms of config.{guess,sub}
cp -p %{_datadir}/libtool/config/config.{guess,sub} ${RPM_BUILD_ROOT}/usr/lib/rpm/redhat/
chmod a+x ${RPM_BUILD_ROOT}%{_prefix}/lib/rpm/mBuild/config.{guess,sub}

#install some tools by magiclinux
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
install -m 755 %{SOURCE1} ${RPM_BUILD_ROOT}%{_bindir}
install -m 755 %{SOURCE2} ${RPM_BUILD_ROOT}%{_bindir}

mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/rpm
install -m 644 %{SOURCE3} ${RPM_BUILD_ROOT}%{_sysconfdir}/rpm



%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%{_prefix}/lib/rpm/mBuild
%{_prefix}/lib/rpm/redhat
%{_bindir}/*
%{_sysconfdir}/*

%changelog
* Tue Jul 28 2009 Ni Hui <shuizhuyuanluo@126.com> - 2.5-4mgc
- magic_rpm_clean.sh 增加 /opt/kde4/ 路径目录，添加一些语言

* Wed May 06 2009 Liu Di <liudidi@gmail.com> - 2.5-3
- 将 Payload 从 bz2 压缩调整成 lzma

* Fri Jul 25 2008 Liu Di <liudidi@gmail.com> - 2.5-1mgc
- 为 rpm 4.5 版本打包

* Sat Jan 06 2007 Liu Di <liudidi@gmail.com> - 2.0-7mgc
- add some lang to magic_rpm_clean.sh

* Wed Feb 8 2006 kde <jack@linux.net.cn> 2.0-6mgc
- remove the redundant blank spaces in the following definitions of the macros file:
__global_cflags		-O2 -g -pipe -D_FORTIFY_SOURCE=2
optflags			-O2 -g -pipe

* Wed Feb 1 2006 kde <jack@linux.net.cn> 2.0-5mgc
- add 1 definitions (%make) in the macros for compatibility
- fix the wrong definitions (%_menudir, %_iconsdir, %_miconsdir, %_liconsdir)

* Thu Dec 27 2005 KanKer <kanker@163.com> 2.0-4mgc
- set rpm package format default bzip2
- add 4 definitions (%_menudir, %_iconsdir, %_miconsdir, %_liconsdir) in the macros for compatibility

* Mon Dec 19 2005 KanKer <kanker@163.com>
- update magic_rpm_clean.sh

* Sat Dec 17 2005 kde <jack@linux.net.cn>
 - modify  '/usr/lib/rpm/mBuild/macros' for magiclinux 2.0

* Sat Dec 10 2005 KanKer <kanker@163.com>
- add some tools for magiclinux

* Sun Nov 6 2005 KanKer <kanker@163.com>
- set arch and buildarch default to i686
