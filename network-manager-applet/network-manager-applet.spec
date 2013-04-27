%define gtk3_version    3.0.1
%define glib2_version   2.26.0
%define dbus_version    1.4
%define dbus_glib_version 0.86
%define nm_version      1:0.9.8.0
%define obsoletes_ver   1:0.9.7

%define snapshot %{nil}
%define realversion 0.9.8.0

Name: network-manager-applet
Summary: A network control and status applet for NetworkManager
Version: 0.9.8.0
Release: 1%{snapshot}%{?dist}
Group: Applications/System
License: GPLv2+
URL: http://www.gnome.org/projects/NetworkManager/
Obsoletes: NetworkManager-gnome < %{obsoletes_ver}

Source: http://ftp.gnome.org/pub/GNOME/sources/network-manager-applet/0.9/%{name}-%{realversion}%{snapshot}.tar.xz
Patch0: nm-applet-no-notifications.patch
Patch1: nm-applet-wifi-dialog-ui-fixes.patch
Patch2: applet-ignore-deprecated.patch

Requires: NetworkManager >= %{nm_version}
Requires: NetworkManager-glib >= %{nm_version}
Requires: libnm-gtk = %{version}-%{release}
Requires: dbus >= 1.4
Requires: dbus-glib >= 0.94
Requires: libnotify >= 0.4.3
Requires: gnome-keyring
Requires: gnome-icon-theme
Requires: nm-connection-editor = %{version}-%{release}

BuildRequires: NetworkManager-devel >= %{nm_version}
BuildRequires: NetworkManager-glib-devel >= %{nm_version}
BuildRequires: dbus-devel >= %{dbus_version}
BuildRequires: dbus-glib-devel >= %{dbus_glib_version}
BuildRequires: glib2-devel >= %{glib2_version}
BuildRequires: gtk3-devel >= %{gtk3_version}
BuildRequires: GConf2-devel
BuildRequires: libgnome-keyring-devel
BuildRequires: gobject-introspection-devel >= 0.10.3
BuildRequires: gettext-devel
BuildRequires: /usr/bin/autopoint
BuildRequires: pkgconfig
BuildRequires: libnotify-devel >= 0.4
BuildRequires: automake autoconf intltool libtool
BuildRequires: gtk-doc
BuildRequires: desktop-file-utils
# No bluetooth on s390
%ifnarch s390 s390x
BuildRequires: gnome-bluetooth-libs-devel >= 2.27.7.1-1
%endif
BuildRequires: iso-codes-devel
BuildRequires: libgudev1-devel >= 147
BuildRequires: libsecret-devel >= 0.12

%description
This package contains a network control and status notification area applet
for use with NetworkManager.

%package -n nm-connection-editor
Summary: A network connection configuration editor for NetworkManager
Requires: NetworkManager-glib >= %{nm_version}
Requires: libnm-gtk = %{version}-%{release}
Requires: dbus >= 1.4
Requires: dbus-glib >= 0.94
Requires: gnome-keyring
Requires: gnome-icon-theme
Requires(post): /usr/bin/gtk-update-icon-cache

%description -n nm-connection-editor
This package contains a network configuration editor and Bluetooth modem
utility for use with NetworkManager.


%package -n libnm-gtk
Summary: Private libraries for NetworkManager GUI support
Group: Development/Libraries
Requires: gtk3 >= %{gtk3_version}
Requires: mobile-broadband-provider-info >= 0.20090602
Obsoletes: NetworkManager-gtk < %{obsoletes_ver}

%description -n libnm-gtk
This package contains private libraries to be used only by nm-applet,
nm-connection editor, and the GNOME Control Center.

%package -n libnm-gtk-devel
Summary: Private header files for NetworkManager GUI support
Group: Development/Libraries
Requires: NetworkManager-devel >= %{nm_version}
Requires: NetworkManager-glib-devel >= %{nm_version}
Obsoletes: NetworkManager-gtk-devel < %{obsoletes_ver}
Requires: libnm-gtk = %{version}-%{release}
Requires: gtk3-devel
Requires: pkgconfig

%description -n libnm-gtk-devel
This package contains private header and pkg-config files to be used only by
nm-applet, nm-connection-editor, and the GNOME control center.


%prep
%setup -q -n network-manager-applet-%{realversion}

%patch0 -p1 -b .no-notifications
%patch1 -p1 -b .applet-wifi-ui
%patch2 -p1 -b .no-deprecated

%build
autoreconf -i -f
intltoolize --force
%configure \
    --disable-static \
    --with-bluetooth \
    --enable-more-warnings=yes \
    --with-gtkver=3
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/gnome-vpn-properties

%find_lang nm-applet
cat nm-applet.lang >> %{name}.lang

rm -f $RPM_BUILD_ROOT%{_libdir}/gnome-bluetooth/plugins/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

# validate .desktop and autostart files
desktop-file-validate $RPM_BUILD_ROOT%{_sysconfdir}/xdg/autostart/nm-applet.desktop
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/nm-connection-editor.desktop


%post	-n libnm-gtk -p /sbin/ldconfig
%postun	-n libnm-gtk -p /sbin/ldconfig

%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%post -n nm-connection-editor
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :

%postun -n nm-connection-editor
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi
glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :

%posttrans -n nm-connection-editor
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :

%files
%defattr(-,root,root,0755)
%doc COPYING NEWS AUTHORS README CONTRIBUTING
%dir %{_datadir}/nm-applet
%{_bindir}/nm-applet
%{_libexecdir}/nm-applet-migration-tool
%{_datadir}/applications/nm-applet.desktop
%{_datadir}/nm-applet/8021x.ui
%{_datadir}/nm-applet/info.ui
%{_datadir}/nm-applet/gsm-unlock.ui
%{_datadir}/nm-applet/keyring.png
%{_datadir}/icons/hicolor/22x22/apps/nm-adhoc.png
%{_datadir}/icons/hicolor/22x22/apps/nm-mb-roam.png
%{_datadir}/icons/hicolor/22x22/apps/nm-secure-lock.png
%{_datadir}/icons/hicolor/22x22/apps/nm-signal-*.png
%{_datadir}/icons/hicolor/22x22/apps/nm-stage*-connecting*.png
%{_datadir}/icons/hicolor/22x22/apps/nm-tech-*.png
%{_datadir}/icons/hicolor/22x22/apps/nm-vpn-active-lock.png
%{_datadir}/icons/hicolor/22x22/apps/nm-vpn-connecting*.png
%{_datadir}/icons/hicolor/22x22/apps/nm-wwan-tower.png
%{_datadir}/GConf/gsettings/nm-applet.convert
%{_sysconfdir}/xdg/autostart/nm-applet.desktop
%{_mandir}/man1/nm-applet*

# Yes, lang files for the applet go in nm-connection-editor RPM since it
# is the RPM that everything else depends on
%files -n nm-connection-editor -f %{name}.lang
%dir %{_datadir}/nm-applet
%{_bindir}/nm-connection-editor
%{_datadir}/applications/nm-connection-editor.desktop
%{_datadir}/nm-applet/ce-*.ui
%{_datadir}/nm-applet/eap-method-*.ui
%{_datadir}/nm-applet/ws-*.ui
%{_datadir}/nm-applet/nag-user-dialog.ui
%{_datadir}/nm-applet/nm-connection-editor.ui
%{_datadir}/icons/hicolor/*/apps/nm-device-*.*
%{_datadir}/icons/hicolor/*/apps/nm-no-connection.*
%{_datadir}/icons/hicolor/16x16/apps/nm-vpn-standalone-lock.png
%{_datadir}/glib-2.0/schemas/org.gnome.nm-applet.gschema.xml
%{_mandir}/man1/nm-connection-editor*
%dir %{_datadir}/gnome-vpn-properties
%ifnarch s390 s390x
%{_libdir}/gnome-bluetooth/plugins/*
%endif

%files -n libnm-gtk
%defattr(-,root,root,0755)
%{_libdir}/libnm-gtk.so.*
%dir %{_datadir}/libnm-gtk
%{_datadir}/libnm-gtk/*.ui
%{_libdir}/girepository-1.0/NMGtk-1.0.typelib

%files -n libnm-gtk-devel
%defattr(-,root,root,0755)
%dir %{_includedir}/libnm-gtk
%{_includedir}/libnm-gtk/*.h
%{_libdir}/pkgconfig/libnm-gtk.pc
%{_libdir}/libnm-gtk.so
%{_datadir}/gir-1.0/NMGtk-1.0.gir

%changelog
* Wed Mar 27 2013 Dan Williams <dcbw@redhat.com> - 0.9.8.1-1.git20130327
- Update to 0.9.8.2 snapshot
- Updated translations
- editor: don't overwrite bridge/bond master interface name with UUID
- applet: fix WWAN PIN dialog invalid "label1" entry widget
- editor: fix allowed values for VLAN ID and MTU
- editor: preserve existing PPP connection LCP echo failure and reply values
- editor: ensure changes to the STP checkbox are saved
- editor: hide BSSID for AdHoc connection (rh #906133)
- editor: fix random data sneaking into IPv6 route gateway fields
- editor: fix handling of initial entry for MAC address widgets

* Wed Feb 27 2013 Jiří Klimeš <jklimes@redhat.com> - 0.9.8.0-1
- Update to 0.9.8.0

* Fri Feb  8 2013 Dan Williams <dcbw@redhat.com> - 0.9.7.997-1
- Update to 0.9.7.997 (0.9.8-beta2)
- editor: better handling of gateway entry for IPv4
- editor: fix some mnemonics (rh #893466)
- editor: fix saving connection when ignoring CA certificate
- editor: enable Bridge connection editing
- editor: hide widgets not relevant for VPN connections

* Tue Dec 11 2012 Jiří Klimeš <jklimes@redhat.com> - 0.9.7.0-6.git20121211
- editor: fix populating Firewall zone in 'General' tab

* Tue Dec 11 2012 Jiří Klimeš <jklimes@redhat.com> - 0.9.7.0-5.git20121211
- Update to git snapshot (git20121211) without bridges

* Thu Nov 08 2012 Kalev Lember <kalevlember@gmail.com> - 0.9.7.0-4.git20121016
- Update the versioned obsoletes for the new F17 NM build

* Tue Oct 16 2012 Jiří Klimeš <jklimes@redhat.com> - 0.9.7.0-3.git20121016
- Update to git snapshot (git20121016)
- editor: fix a crash when no VPN plugins are installed

* Thu Oct  4 2012 Dan Winship <danw@redhat.com> - 0.9.7.0-3.git20121004
- Update to git snapshot

* Wed Sep 12 2012 Jiří Klimeš <jklimes@redhat.com> - 0.9.7.0-3.git20120820
- move GSettings schema XML to nm-connection-editor rpm (rh #852792)

* Thu Aug 30 2012 Jiří Klimeš <jklimes@redhat.com> - 0.9.7.0-2.git20120820
- run glib-compile-schemas in %post scriplet (rh #852792)

* Tue Aug 21 2012 Dan Winship <danw@redhat.com> - 0.9.7.0-1.git20120820
- Update to 0.9.7.0 snapshot

* Tue Aug 14 2012 Daniel Drake <dsd@laptop.org> - 0.9.5.96-2
- Rebuild for libgnome-bluetooth.so.11

* Mon Jul 23 2012 Dan Williams <dcbw@redhat.com> - 0.9.5.96-1
- Update to 0.9.6-rc2
- lib: recognize PKCS#12 files exported from Firefox
- lib: fix some wireless dialog crashes

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5.95-3.git20120713
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jul 14 2012 Kalev Lember <kalevlember@gmail.com> - 0.9.5.95-2.git20120713
- Fix the versioned obsoletes

* Fri Jul 13 2012 Jiří Klimeš <jklimes@redhat.com> - 0.9.5.95-1.git20120713
- update to 0.9.5.95 (0.9.6-rc1)  snapshot
- editor: fixed UI mnemonics
- editor: fix defaults for PPP echo values
- applet: various crash and stability fixes
- applet: show IPv6 addressing page for VPN plugins that support it
- applet: port to GSettings and split out 0.8 -> 0.9 migration code into standalone tool

* Mon May 21 2012 Jiří Klimeš <jklimes@redhat.com> - 0.9.4-4
- update to git snapshot

* Wed May  2 2012 Jiří Klimeš <jklimes@redhat.com> - 0.9.4-3
- update to git snapshot

* Mon Mar 19 2012 Dan Williams <dcbw@redhat.com> - 0.9.3.997-1
- Initial package split from NetworkManager

