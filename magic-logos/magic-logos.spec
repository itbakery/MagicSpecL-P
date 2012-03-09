Name: magic-logos
Summary: Magic-related icons and pictures
Version: 30.0.0
Release: 1%{?dist}
Group: System Environment/Base
URL: http://git.fedorahosted.org/git/fedora-logos.git/
License: Licensed only for approved usage, see COPYING for details. 

BuildArch: noarch
Obsoletes: redhat-logos
Obsoletes: gnome-logos
Provides: redhat-logos = %{version}-%{release}
Provides: gnome-logos = %{version}-%{release}
Provides: system-logos = %{version}-%{release}

%description
Magic-related icons and pictures

%prep

%build

%install

%post

%postun

%files

%changelog

