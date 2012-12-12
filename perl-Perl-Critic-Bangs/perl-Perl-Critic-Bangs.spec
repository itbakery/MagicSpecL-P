Name:           perl-Perl-Critic-Bangs
Version:        1.10
Release:        2%{?dist}
Summary:        Collection of handy Perl::Critic policies
License:        Artistic 2.0
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Perl-Critic-Bangs/
Source0:        http://www.cpan.org/authors/id/P/PE/PETDANCE/Perl-Critic-Bangs-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(base)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Perl::Critic) >= 1.098
BuildRequires:  perl(Perl::Critic::Policy)
BuildRequires:  perl(Perl::Critic::Utils)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Perl::Critic) >= 1.01
# Tests only:
BuildRequires:  perl(File::Find)
BuildRequires:  perl(Perl::Critic::PolicyFactory)
BuildRequires:  perl(Perl::Critic::PolicyParameter)
BuildRequires:  perl(Perl::Critic::TestUtils)
BuildRequires:  perl(Perl::Critic::UserProfile)
BuildRequires:  perl(Perl::Critic::Violation)
BuildRequires:  perl(PPI::Cache)
BuildRequires:  perl(PPI::Document)
# Optional tests only:
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.06
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(Perl::Critic) >= 1.098
Requires:       perl(Test::More)
Requires:       perl(Test::Perl::Critic) >= 1.01

%description
The rules included with the Perl::Critic::Bangs group include:
  - Commented-out code is usually noise.  It should be removed.
  - Watch for comments like "XXX", "TODO", etc.
  - Tests should have a plan.
  - Variables like $user and $user2 are insufficiently distinguished.
  - Determining the class in a constructor by using "ref($proto) || $proto".
  - Adding modifiers to a regular expression made up entirely of a variable
  created with qr() is usually not doing what you expect.
  - Vague variables like $data or $info are not descriptive enough.

%prep
%setup -q -n Perl-Critic-Bangs-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=perl
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check


%files
%doc Changes perlcriticrc README TODO
%{perl_privlib}/*
%{_mandir}/man3/*

%changelog
* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 1.10-2
- 为 Magic 3.0 重建

* Tue Aug 21 2012 Petr Pisar <ppisar@redhat.com> - 1.10-1
- 1.10 bump

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 20 2012 Petr Pisar <ppisar@redhat.com> - 1.08-5
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 1.08-3
- Perl mass rebuild

* Tue Jun 21 2011 Petr Pisar <ppisar@redhat.com> - 1.08-2
- BuildRequire perl(base)

* Tue Jun 21 2011 Petr Pisar <ppisar@redhat.com> - 1.08-1
- 1.08 bump
- License changed to Artistic 2.0 only.
- Drops dependency on Perl::Critic::Utils::PPIRegexp to work with perl 5.14

* Thu Jan 27 2011 Petr Pisar <ppisar@redhat.com> 1.06-1
- Specfile autogenerated by cpanspec 1.78.
- Remove BuildRoot stuff
- Write description according POD.
- Install into perl core directory.
