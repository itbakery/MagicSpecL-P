Name:           mach
Version:        1.0.0
Release:        1%{?dist}
Summary:        Make a chroot
Summary(zh_CN): 建立一个 chroot 环境

Group:          Applications/System
Group(zh_CN):	应用程序/系统
License:        GPLv2+
URL:            http://thomas.apestaart.org/projects/mach/
Source:         http://thomas.apestaart.org/download/mach/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

Requires:	python
Requires:	rpm
Requires:	rpm-build
Requires:	rpm-python
Requires:	yum
Requires:	createrepo
Requires:	sed
Requires:	cpio

BuildRequires:	python
BuildRequires:	gcc-c++

%if 0%{!?flavor:1}
%if 0%{?rhel}
%define flavor epel
%else
%define flavor updates
%endif
%endif
%{!?builduser:  %define builduser  machbuild}
%{!?buildgroup: %define buildgroup machbuild}

%description
mach makes a chroot.
Using yum or apt-get and a suid binary, it manages to install clean chroot
environments based on the original packages for that distribution.

The clean root can be used to run jail roots, to create image files, or
to build clean packages.

Authors:
--------
Thomas Vander Stichele (thomas (at) apestaart (dot) org)

%description -l zh_CN
一个自动打包环境。

%prep
%setup -q

%build
%configure \
	--with-flavor=%{flavor} \
	--enable-builduser=%{builduser} \
	--enable-buildgroup=%{buildgroup} 
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
install -d -m 2775 $RPM_BUILD_ROOT%{_localstatedir}/lib/mach
install -d -m 2775 $RPM_BUILD_ROOT%{_localstatedir}/lib/mach/states
install -d -m 2775 $RPM_BUILD_ROOT%{_localstatedir}/lib/mach/roots
install -d -m 2775 $RPM_BUILD_ROOT%{_localstatedir}/tmp/mach
install -d -m 775 $RPM_BUILD_ROOT%{_localstatedir}/cache/mach

find $RPM_BUILD_ROOT -name "*.la" -exec rm {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%pre
getent group mach >/dev/null || groupadd -r mach || :

%preun
if [ "$1" == 0 ];
then
  # last removal
  # be a good boy and clean out the dirs we filled with junk
  rm -rf %{_localstatedir}/lib/mach/states/*
  umount %{_localstatedir}/lib/mach/roots/*/proc > /dev/null 2>&1 || :
  rm -rf %{_localstatedir}/lib/mach/roots/*
  rm -rf %{_localstatedir}/cache/mach/* > /dev/null 2>&1 || :
  rmdir %{_localstatedir}/lib/mach/states > /dev/null 2>&1 || :
  rmdir %{_localstatedir}/lib/mach/roots > /dev/null 2>&1 || :
  rmdir %{_localstatedir}/cache/mach > /dev/null 2>&1 || :
  rm -rf %{_localstatedir}/tmp/mach > /dev/null 2>&1 || :
fi

%files
%defattr(-,root,root,-)
%doc ChangeLog COPYING README AUTHORS BUGS TODO FORGETMENOT RELEASE mach.doap
%dir %{_sysconfdir}/mach
%config %{_sysconfdir}/mach/conf
%config(noreplace) %{_sysconfdir}/mach/location
%config %{_sysconfdir}/mach/dist.d
%attr(2775,root,mach) %dir %{_localstatedir}/lib/mach
%attr(2775,root,mach) %dir %{_localstatedir}/lib/mach/states
%attr(2775,root,mach) %dir %{_localstatedir}/lib/mach/roots
%ghost %attr(2775,root,mach) %dir %{_localstatedir}/tmp/mach
%attr(2775,root,mach) %{_localstatedir}/cache/mach
%{_bindir}/mach
%attr(04750,root,mach) %{_sbindir}/mach-helper

%changelog

