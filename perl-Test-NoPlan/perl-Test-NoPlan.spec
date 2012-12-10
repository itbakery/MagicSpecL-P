Name:           perl-Test-NoPlan
Version:        0.0.6
Release:        4%{?dist}
Summary:        Check perl test files for no_plan
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Test-NoPlan/
Source0:        http://www.cpan.org/authors/id/D/DU/DUNCS/Test-NoPlan-v%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Module::Build)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(version)
# Tests:
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.22
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
BuildRequires:  perl(Pod::Coverage) >= 0.18
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
It is a good idea to ensure you have defined how many tests should be run
within each test script - to catch cases where tests bomb out part way through
so you know how many tests were not actually run. This module checks all your
test plan files to ensure 'no_plan' is not used.

%prep
%setup -q -n Test-NoPlan-v%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc AUTHORS Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Dec 10 2012 Liu Di <liudidi@gmail.com> - 0.0.6-4
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 0.0.6-2
- Perl 5.16 rebuild

* Thu Apr 26 2012 Petr Pisar <ppisar@redhat.com> 0.0.6-1
- Specfile autogenerated by cpanspec 1.78.
