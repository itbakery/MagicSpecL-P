Summary: K Desktop Environment - Configuration files
Summary(zh_CN.UTF-8): K 桌面环境(KDE4) - 配置文件
Name: magic-kde4-config
Version: 4.3.x.20090614
Release: 3%{?dist}
License: GPL
URL: http://www.magiclinux.org
Group: User Interface/Desktops
Group(zh_CN.UTF-8): 用户界面/桌面
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot-%(%{__id_u} -n)
Source0: magic-kde4-config-%{version}.tar.bz2
Source1: kdm-np.pamd
Source2: kdm.pamd
Source3: kcheckpass.pamd
Source4: kscreensaver.pamd
Requires: kdelibs4, magic-system-config
Conflicts: magic-kde-config
#Requires: konversation

%description
Configuration filess for KDE by MagicLinux.

%description -l zh_CN.UTF-8
MagicLinux 下 KDE 的配置文件。

%package -n magic-kdm4-config
Summary: K Desktop Environment - KDM Configuration files
Summary(zh_CN.UTF-8): K 桌面环境(KDE) - 登录管理器 (KDM) 配置文件
Group: User Interface/Desktops
Group(zh_CN.UTF-8): 用户界面/桌面
Requires: kde4-kdm >= 4.2
Requires: %{name} = %{version}-%{release}

%description
Configuration filess for KDM by MagicLinux.

%description -n magic-kdm4-config -l zh_CN.UTF-8
MagicLinux 下 KDM4 的配置文件。


%prep
%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}

# install config files
cp -rf etc usr %{buildroot}/


#pushd %{buildroot}
#find etc/skel/ -type f | xargs chmod 0644
#find etc/skel/ -type d | xargs chmod 0755
#find usr/share/config -type f | xargs chmod 0644
#popd

# install config files to root
#mkdir -p %{buildroot}/root
#chmod 750 %{buildroot}/root
#cp -af %{buildroot}/etc/skel/* %{buildroot}/root/
#cp -af %{buildroot}/etc/skel/.kderc %{buildroot}/root/
#cp -raf %{buildroot}/etc/skel/.kde %{buildroot}/root/

#install kdm config files
#mkdir -p %{buildroot}/usr/share/config/
#ln -sf /etc/kde/kdm %{buildroot}/usr/share/config/
#pushd %{buildroot}/etc/kde/kdm
#for i in GiveConsole kdmrc TakeConsole Xaccess xdm-config Xreset Xresources Xservers Xsession Xsetup Xsetup_0 Xstartup Xwilling; do
#	ln -sf /etc/X11/xdm/$i ;
#done
#popd

mkdir -p $RPM_BUILD_ROOT/etc/pam.d
install -p -m644 -D %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/kdm-np
install -p -m644 -D %{SOURCE2} $RPM_BUILD_ROOT/etc/pam.d/kdm
install -p -m644 -D %{SOURCE3} $RPM_BUILD_ROOT/etc/pam.d/kcheckpass
install -p -m644 -D %{SOURCE4} $RPM_BUILD_ROOT/etc/pam.d/kscreensaver

magic_rpm_clean.sh

%post
## Enable "Start New Session" magic
grep "^:1" /etc/X11/xdm/Xservers >& /dev/null ||
echo ":1 local reserve /usr/bin/X :1 -dpi 96" >> /etc/X11/xdm/Xservers
## make kdm and KDE sessions the default, if not otherwise specified
grep "^DESKTOP=" /etc/sysconfig/desktop >& /dev/null ||
echo "DESKTOP=KDE4" >> /etc/sysconfig/desktop
grep "^DISPLAYMANAGER=" /etc/sysconfig/desktop >& /dev/null ||
echo "DISPLAYMANAGER=KDE4" >> /etc/sysconfig/desktop


%clean
rm -rf %{buildroot} %{_builddir}/%{buildsubdir}

%files
%defattr(-,root,root)

%files -n magic-kdm4-config
%defattr(-,root,root)
/etc/pam.d/*

%changelog
* Fri Dec 07 2012 Liu Di <liudidi@gmail.com> - 4.3.x.20090614-3
- 为 Magic 3.0 重建

