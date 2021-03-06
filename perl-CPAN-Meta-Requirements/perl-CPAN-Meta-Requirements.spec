Name:           perl-CPAN-Meta-Requirements
Version:        2.122
Release:        7%{?dist}
Summary:        Set of version requirements for a CPAN dist
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/CPAN-Meta-Requirements/
Source0:        http://www.cpan.org/authors/id/D/DA/DAGOLDEN/CPAN-Meta-Requirements-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
%if !%{defined perl_bootstrap}
BuildRequires:  perl(Test::Script)
%endif
BuildRequires:  perl(version) >= 0.77
# for author/release tests
%if !%{defined perl_bootstrap} && ! ( 0%{?rhel} )
BuildRequires:  perl(Perl::Critic::Policy::Lax::ProhibitStringyEval::ExceptForRequire)
BuildRequires:  perl(Pod::Coverage::TrustPod)
BuildRequires:  perl(Pod::Wordlist::hanekomu)
BuildRequires:  perl(Test::CPAN::Meta)
BuildRequires:  perl(Test::Perl::Critic)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::Portability::Files)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Test::Spelling) aspell-en
BuildRequires:  perl(Test::Version)
%endif

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

# CPAN-Meta-Requirements was split from CPAN-Meta
Conflicts:      perl-CPAN-Meta < 2.120921
# and used to have six decimal places
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}perl\\(CPAN::Meta::Requirements\\)
Provides:       perl(CPAN::Meta::Requirements) = %{version}000

%description
A CPAN::Meta::Requirements object models a set of version constraints like
those specified in the META.yml or META.json files in CPAN distributions.
It can be built up by adding more and more constraints, and it will reduce
them to the simplest representation.

%prep
%setup -q -n CPAN-Meta-Requirements-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;

%{_fixperms} %{buildroot}/*

%check
%if %{defined perl_bootstrap} || ( 0%{?rhel} )
rm -rf xt
%endif
make test TEST_FILES="t/*.t xt/*/*.t"

%files
%doc Changes LICENSE perlcritic.rc README README.PATCHING
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.122-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Marcela Mašláňová <mmaslano@redhat.com> - 2.122-6
- Conditionalize Test::*

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.122-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Petr Pisar <ppisar@redhat.com> - 2.122-4
- Perl 5.16 re-rebuild of bootstrapped packages

* Wed Jun 06 2012 Petr Pisar <ppisar@redhat.com> - 2.122-3
- Perl 5.16 rebuild

* Fri Jun 01 2012 Petr Pisar <ppisar@redhat.com>
- Skip some tests on bootstrap

* Mon May 07 2012 Iain Arnell <iarnell@gmail.com> 2.122-1
- update to latest upstream version

* Tue Apr 03 2012 Iain Arnell <iarnell@gmail.com> 2.121-3
- provide perl(CPAN::Meta::Requirements) with six decimal places

* Mon Apr 02 2012 Iain Arnell <iarnell@gmail.com> 2.121-2
- clean up spec following review
- run release/author tests too

* Sun Apr 01 2012 Iain Arnell <iarnell@gmail.com> 2.121-1
- Specfile autogenerated by cpanspec 1.79.
