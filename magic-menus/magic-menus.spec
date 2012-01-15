%define gettext_package redhat-menus
#临时
%define real_name redhat-menus

Summary: Configuration and data files for the desktop menus
Name: magic-menus
Version: 12.0.2
Release: 5%{?dist}
URL: http://www.redhat.com
#FIXME-> There is no hosting website for this project.
Source0: %{real_name}-%{version}.tar.gz
License: GPL+
Group: User Interface/Desktops
BuildArch: noarch
BuildRequires: desktop-file-utils
BuildRequires: intltool
Provides: %real_name

%description
This package contains the XML files that describe the menu layout for
GNOME and KDE, and the .desktop files that define the names and icons
of "subdirectories" in the menus.

%prep
%setup -q -n %{real_name}-%{version}

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

%find_lang %{gettext_package}

# create the settings-merged to prevent gamin from looking for it
# in a loop
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/xdg/menus/settings-merged ||:

%post
update-desktop-database &> /dev/null || :

%postun
update-desktop-database &> /dev/null || :

%files  -f %{gettext_package}.lang
%defattr(-,root,root,-)
%doc COPYING
%dir %{_sysconfdir}/xdg/menus
%dir %{_sysconfdir}/xdg/menus/applications-merged
%dir %{_sysconfdir}/xdg/menus/preferences-merged
%dir %{_sysconfdir}/xdg/menus/preferences-post-merged
%dir %{_sysconfdir}/xdg/menus/settings-merged
%config %{_sysconfdir}/xdg/menus/*.menu
%exclude %{_sysconfdir}/xdg/menus/applications.menu
%exclude %{_datadir}/desktop-menu-patches/*.desktop
%{_datadir}/desktop-directories/*.directory

%changelog
* Sun Jan 15 2012 Liu Di <liudidi@gmail.com> - 12.0.2-5
- 为 Magic 3.0 重建


