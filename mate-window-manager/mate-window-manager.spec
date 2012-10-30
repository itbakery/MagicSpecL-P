%{?filter_setup:
%filter_from_requires /^libmarco-private.so/d;
%filter_setup
}


Name:           mate-window-manager
Version:        1.4.1
Release:        12%{?dist}
Summary:        MATE Desktop window manager
License:        LGPLv2+ and GPLv2+
URL:            http://mate-desktop.org
# https://github.com/mate-desktop/mate-window-manager/issues/9
Source0:        http://vicodan.fedorapeople.org/mate-window-manager-1.4.1-GIT.tar.gz
# https://bugzilla.gnome.org/show_bug.cgi?id=622517
Patch0:         Allow-breaking-out-from-maximization-during-mouse.patch
# https://bugs.launchpad.net/ubuntu/+source/metacity/+bug/583847
Patch1:         initialise_all_workspace_names.patch

BuildRequires: desktop-file-utils
BuildRequires: gtk2-devel
BuildRequires: libcanberra-devel
BuildRequires: libsoup-devel
BuildRequires: mate-common
BuildRequires: mate-doc-utils
BuildRequires: mate-conf-devel
BuildRequires: mate-corba-devel
BuildRequires: mate-dialogs
BuildRequires: libSM-devel
BuildRequires: libICE-devel
BuildRequires: startup-notification-devel

Requires:       mate-themes
# for /usr/share/mate-control-center/keybindings, /usr/share/mate/wm-properties
Requires:       mate-control-center 

Requires(pre):  mate-conf
Requires(post): mate-conf
Requires(preun): mate-conf

Obsoletes: mate-window-manager-libs < 1.4.1-2

%description
MATE Desktop window manager

%package devel
Summary: Development files for mate-window-manager
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for mate-window-manager


%prep
%setup -q
%patch0 -p1
%patch1 -p1
NOCONFIGURE=1 ./autogen.sh


%build
%configure --disable-static --disable-schemas-install

SHOULD_HAVE_DEFINED="HAVE_SM HAVE_XINERAMA HAVE_XFREE_XINERAMA HAVE_SHAPE HAVE_RANDR HAVE_STARTUP_NOTIFICATION"

for I in $SHOULD_HAVE_DEFINED; do
  if ! grep -q "define $I" config.h; then
    echo "$I was not defined in config.h"
    grep "$I" config.h
    exit 1
  else
    echo "$I was defined as it should have been"
    grep "$I" config.h
  fi
done

make %{?_smp_mflags} V=1


%install
export MATECONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=%{buildroot}
magic_rpm_clean.sh
%find_lang %{name} --all-name

find %{buildroot} -name '*.la' -exec rm -vf {} ';'

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/marco.desktop


%pre
%mateconf_schema_prepare marco

%preun
%mateconf_schema_remove marco

%post
/usr/sbin/ldconfig
%mateconf_schema_upgrade marco

%postun -p /usr/sbin/ldconfig

%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_mandir}/man1/*
%{_sysconfdir}/mateconf/schemas/marco.schemas
%{_bindir}/marco
%{_bindir}/marco-message
%{_bindir}/marco-theme-viewer
%{_bindir}/marco-window-demo
%{_datadir}/applications/marco.desktop
%{_datadir}/themes/ClearlooksRe/
%{_datadir}/themes/Dopple-Left/
%{_datadir}/themes/Dopple/
%{_datadir}/themes/DustBlue/
%{_datadir}/themes/Spidey-Left/
%{_datadir}/themes/Spidey/
%{_datadir}/themes/Splint-Left/
%{_datadir}/themes/Splint/
%{_datadir}/themes/WinMe/
%{_datadir}/themes/eOS/
%{_datadir}/marco/
%{_datadir}/mate-control-center/keybindings/50-marco-desktop-key.xml
%{_datadir}/mate-control-center/keybindings/50-marco-key.xml
%{_datadir}/mate/help/creating-marco-themes/C/creating-marco-themes.xml
%{_datadir}/mate/wm-properties/
%{_libdir}/libmarco-private.so.0*

%files devel
%{_includedir}/marco-1/
%{_libdir}/libmarco-private.so
%{_libdir}/pkgconfig/libmarco-private.pc


%changelog
* Wed Oct 17 2012 Leigh Scott <leigh123linux@googlemail.com> - 1.4.1-12
- Fix crash if you have lots of workspaces

* Tue Oct 16 2012 Leigh Scott <leigh123linux@googlemail.com> - 1.4.1-11
- filter provides
- fix build requires
- fix reqires
- define some defaults
- Add patch to allow breaking out from maximization during mouse resize
  (gnome bz 622517)

* Wed Sep 26 2012 Rex Dieter <rdieter@fedoraproject.org> - 1.4.1-10
- fix ldconfig scriptlets
- use desktop-file-validate again
- own %%{_datadir}/mate/wm-properties/

* Tue Sep 25 2012 Dan Mashal <dan.mashal@fedoraproject.org> 1.4.1-9
- Remove mateconf obsolete scriplet

* Mon Sep 24 2012 Dan Mashal <dan.mashal@fedoraproject.org> 1.4.1-8
- rerefix mate-conf scriptlets. Add export line to REALLY not install schemas with make install.
- comment out desktop-file-validate.

* Mon Sep 17 2012 Rex Dieter <rdieter@fedoraproject.org> 1.4.1-7
- fix/simplify dir ownership
- omit not-needed/broken Obsoletes
- (re)fix scriptlets :)

* Sat Sep 15 2012 Dan Mashal <dan.mashal@fedoraproject.org> 1.4.1-6
- Move post and postun scriptlets to proper location

* Sat Sep 15 2012 Dan Mashal <dan.mashal@fedoraproject.org> 1.4.1-5
- Remove onlyshowin since it is not needed any more with updated desktop-file-utils

* Sat Sep 15 2012 Dan Mashal <dan.mashal@fedoraproject.org> 1.4.1-4
Update source to note git version.

* Sun Sep 09 2012 Dan Mashal <dan.mashal@fedoraproject.org> 1.4.1-3
- Fix broken dependencies, update to latest github version which contains fixes for desktop-file-utils

* Mon Sep 03 2012 Dan Mashal <dan.mashal@fedoraproject.org> 1.4.1-2
- Add environment variable to install section and further obsoletes to prevent dependency breakage

* Sun Sep 02 2012 Dan Mashal <dan.mashal@fedoraproject.org> 1.4.1-1
- Upgrade to new upstream version.

* Mon Aug 27 2012 Rex Dieter <rdieter@fedoraproject.org> 1.4.0-5
- drop unneeded python-related build deps
- %%configure --disable-schemas-install
- fix/simplify some parent-dir ownership

* Mon Aug 27 2012 Rex Dieter <rdieter@fedoraproject.org>  1.4.0-4
- main pkg Requires: %%name-libs
- drop needless icon scriptlets
- s|MATE|X-MATE| .desktop Categories on < f18 only
- License: GPLv2+

* Sun Aug 26 2012 Dan Mashal <dan.mashal@fedoraproject.org> 1.4.0-3
- Own theme directories that are being installed, switch from po_package to namefor lang files, bump release version

* Sun Aug 26 2012 Dan Mashal <dan.mashal@fedoraproject.org> 1.4.0-2
- Add mateconf scriptlets

* Sun Aug 12 2012 Dan Mashal <dan.mashal@fedoraproject.org> 1.4.0-1
- Initial build
