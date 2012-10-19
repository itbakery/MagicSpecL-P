Name:           perl-Tk-CursorControl
Version:        0.4
Release:        4%{?dist}
Summary:        Manipulate the mouse cursor programmatically
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Tk-CursorControl/
Source0:        http://www.cpan.org/authors/id/D/DU/DUNNIGANJ/Tk-CursorControl-%{version}.tar.gz
# don't install cursor.pl demo - add to docs instead
Patch0:         perl-Tk-CursorControl-no-demos.patch
# disable interactive tests (reenable --with interactive-tests)
Patch1:         perl-Tk-CursorControl-no-interactive-test.patch
%bcond_with     interactive_tests
BuildArch:      noarch
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Tk) >= 800.015
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
This module offers a Tk programmer the functionality of warping, moving,
confining or hiding a mouse cursor.

%prep
%setup -q -n Tk-CursorControl-%{version}
%patch0 -p1
%if %{without interactive_tests}
%patch1 -p1
%endif

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
make test

%files
%doc Changes README demos/cursor.pl
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 0.4-3
- Perl 5.16 rebuild

* Wed Feb 22 2012 Iain Arnell <iarnell@gmail.com> 0.4-2
- BR perl(Carp) following review

* Mon Feb 20 2012 Iain Arnell <iarnell@gmail.com> 0.4-1
- Specfile autogenerated by cpanspec 1.79.
- disable interactive tests
- install demos as documentation
