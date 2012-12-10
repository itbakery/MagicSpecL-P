Name:           perl-Tk-ToolBar
Version:        0.10
Release:        6%{?dist}
Summary:        Toolbar widget for Perl/Tk
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Tk-ToolBar/
Source0:        http://www.cpan.org/authors/id/C/CH/CHORNY/Tk-ToolBar-%{version}.zip
# don't install toolbar.pl demo - add to docs instead
Patch0:         perl-Tk-ToolBar-no-demos.patch
BuildArch:      noarch
BuildRequires:  perl >= 0:5.005
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Tk)
BuildRequires:  perl(Tk::Balloon)
BuildRequires:  perl(Tk::CursorControl)
BuildRequires:  perl(Tk::Frame)
BuildRequires:  perl(Tk::LabEntry)
BuildRequires:  perl(Tk::widgets)
Requires:       perl(Tk::CursorControl)
Requires:       perl(Tk::LabEntry)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
This module implements a dockable toolbar. It is in the same spirit as the
"short-cut" toolbars found in most major applications, such as most web
browsers and text editors (where you find the "back" or "save" and other
shortcut buttons).

%prep
%setup -q -n Tk-ToolBar-%{version}
%patch0 -p1

# strip CRLF
find -type f -print0 | xargs -0 sed -i 's/\r$//'

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check


%files
%doc Changes README toolbar.pl
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Dec 10 2012 Liu Di <liudidi@gmail.com> - 0.10-6
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 0.10-4
- Perl 5.16 rebuild

* Mon Feb 27 2012 Iain Arnell <iarnell@gmail.com> 0.10-3
- additional (build-)dependencies following review

* Wed Feb 22 2012 Iain Arnell <iarnell@gmail.com> 0.10-2
- R/BR perl(Tk::CursorControl) now that it's available

* Mon Feb 20 2012 Iain Arnell <iarnell@gmail.com> 0.10-1
- Specfile autogenerated by cpanspec 1.79.
