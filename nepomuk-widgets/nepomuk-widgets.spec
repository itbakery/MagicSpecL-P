%define shared_desktop_ontologies_ver 0.10.0
%define soprano_ver 2.8.0
%define rversion %{kde4_kdelibs_version}

%global shared_desktop_ontologies_version %(pkg-config --modversion shared-desktop-ontologies 2>/dev/null || echo %{shared_desktop_ontologies_ver})
%global soprano_version %(pkg-config --modversion soprano 2>/dev/null || echo %{soprano_ver})

# undef or set to 0 to disable items for a faster build
#global tests 1

Name:    nepomuk-widgets
Version: %{rversion}
Release: 1%{?dist}
Summary: Nepomuk Core utilities and libraries

License: LGPLv2 or LGPLv3
URL:     http://www.kde.org/

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: ftp://ftp.kde.org/pub/kde/%{stable}/%{version}/src/%{name}-%{version}.tar.xz

%define sysctl 1
Source1: nepomuk-inotify.conf

## upstream patches
# proposed by dfaure, should help fix http://bugzilla.redhat.com/858271
Patch100: nepomuk-core-4.9.2-isEmpty_crash.patch

BuildRequires:  doxygen
BuildRequires:  kdelibs4-devel >= %{version}
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(soprano) >= %{soprano_ver}
BuildRequires:  pkgconfig(libstreamanalyzer) pkgconfig(libstreams)
BuildRequires:  pkgconfig(shared-desktop-ontologies)
%if  0%{?tests}
BuildRequires:  dbus-x11
BuildRequires:  virtuoso-opensource
%endif

Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: kdelibs4%{?_isa} >= %{version}
Requires: shared-desktop-ontologies >= %{shared_desktop_ontologies_version}
Provides: soprano-backend-virtuoso >= %{soprano_version}
Requires: virtuoso-opensource

# moved from kde-runtime in 4.8.80 (nepomuk common has nepomuk-core preference)
Conflicts: kde-runtime < 4.8.80-2

%description
%{summary}.

%package devel
Summary:  Developer files for %{name}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: kdelibs4-devel
%description devel
%{summary}.

%package libs
Summary:  Runtime libraries for %{name}
Requires: kdelibs4%{?_isa} >= %{version}
%description libs
%{summary}.


%prep
%setup -q

#%patch100 -p1 -b .isEmpty_crash


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install

make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

magic_rpm_clean.sh

%check
%if 0%{?tests}
make -C %{_target_platform}/autotests/test test  ||:
%endif


%files devel
%{kde4_includedir}/nepomuk2/*.h
%{kde4_libdir}/cmake/NepomukWidgets/*.cmake
%{kde4_libdir}/libnepomukwidgets.so

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files libs
%{kde4_libdir}/libnepomukwidgets.so.*

%changelog
* Sat Dec 08 2012 Liu Di <liudidi@gmail.com> - 4.9.3-6
- 为 Magic 3.0 重建

* Wed Oct 03 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.2-5
- respin isEmpty_crash based on 32b44881 upstream commit (#858271)

* Tue Oct 02 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.2-4
- respin isEmpty_crash patch to guard against NULL (#858271)

* Tue Oct 02 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.2-3
- sysctl.d/nepomuk-inotify.conf: fs.inotify.max_user_watches=524288 (f18+)

* Mon Oct 01 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.2-2
- proposed patch to fix/workaround isEmpty crash (#858271)

* Fri Sep 28 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.2-1
- 4.9.2

* Mon Sep 03 2012 Than Ngo <than@redhat.com> - 4.9.1-1
- 4.9.1

* Fri Aug 10 2012 Rex Dieter <rdieter@fedoraproject.org> 
- 4.9.0-3.20120810git
- sync 4.9-branch patches
- %%check: do autotests
- Requires: +soprano-backend-virtuoso +virtuoso-opensource

* Thu Aug 02 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.0-2
- respin

* Thu Jul 26 2012 Lukas Tinkl <ltinkl@redhat.com> - 4.9.0-1
- 4.9.0

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.97-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 11 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.8.97-1
- 4.8.97

* Wed Jun 27 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.95-1
- 4.8.95

* Tue Jun 12 2012 Rex Dieter <rdieter@fedoraproject.org> 
- 4.8.90-2
- move libkdeinit_* to base pkg (no need for multilib) 
- .spec cleanup
- add shared-desktop-ontologies, soprano runtime deps

* Sat Jun 09 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.8.90-1
- 4.8.90

* Fri Jun 01 2012 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.8.80-4
- BR kdelibs4-devel instead of kdelibs-devel, fixes minimum version (no Epoch)

* Fri Jun 01 2012 Jaroslav Reznik <jreznik@redhat.com> 4.8.80-3
- respin

* Wed May 30 2012 Jaroslav Reznik <jreznik@redhat.com> 4.8.80-2
- split -libs
- fix license

* Sat May 26 2012 Jaroslav Reznik <jreznik@redhat.com> 4.8.80-1
- initial try
