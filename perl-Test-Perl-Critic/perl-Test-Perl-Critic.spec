Name:           perl-Test-Perl-Critic
Summary:        Use Perl::Critic in test programs
Version:        1.02
Release:        6%{?dist}
License:        GPL+ or Artistic
Group:          Development/Libraries
Source0:        http://search.cpan.org/CPAN/authors/id/T/TH/THALJEF/Test-Perl-Critic-%{version}.tar.gz 
URL:            http://search.cpan.org/dist/Test-Perl-Critic/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildArch:      noarch

BuildRequires:  perl(Carp)
BuildRequires:  perl(English)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Module::Build) >= 0.35
BuildRequires:  perl(Perl::Critic) >= 1.105
BuildRequires:  perl(Perl::Critic::Utils) >= 1.105
BuildRequires:  perl(Perl::Critic::Violation) >= 1.105
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More)

Requires:       perl(Carp)
Requires:       perl(English)
Requires:       perl(Perl::Critic) >= 1.105
Requires:       perl(Perl::Critic::Utils) >= 1.105
Requires:       perl(Perl::Critic::Violation) >= 1.105
Requires:       perl(Test::Builder)


%{?perl_default_filter}
%{?perl_default_subpackage_tests}

%description
Test::Perl::Critic wraps the Perl::Critic engine in a convenient
subroutine suitable for test programs written using the Test::More
framework. This makes it easy to integrate coding-standards enforcement
into the build process. For ultimate convenience (at the expense of some
flexibility), see the criticism pragma.


%prep
%setup -q -n Test-Perl-Critic-%{version}


%build
%{__perl} Build.PL installdirs=vendor
./Build


%install
rm -rf $RPM_BUILD_ROOT
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*


%check
# Tests are failing with odd unpack errors.
# TEST_AUTHOR=1 ./Build test
./Build test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes LICENSE README
%{perl_vendorlib}/Test/
%{_mandir}/man3/*.3pm*


%changelog
* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.02-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 1.02-5
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.02-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.02-3
- 661697 rebuild for fixing problems with vendorach/lib

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.02-2
- Mass rebuild with perl-5.12.0

* Sun Mar 14 2010 Chris Weyl <cweyl@alumni.drew.edu> 1.02-1
- update by Fedora::App::MaintainerTools 0.006
- updating to latest GA CPAN version (1.02)
- added a new br on perl(Carp) (version 0)
- added a new br on perl(English) (version 0)
- altered br on perl(Module::Build) (0 => 0.35)
- altered br on perl(Perl::Critic) (0.21 => 1.105)
- added a new br on perl(Perl::Critic::Utils) (version 1.105)
- added a new br on perl(Perl::Critic::Violation) (version 1.105)
- added a new br on perl(Test::Builder) (version 0)
- added a new br on perl(Test::More) (version 0)
- force-adding ExtUtils::MakeMaker as a BR
- dropped old BR on perl(Test::Pod)
- dropped old BR on perl(Test::Pod::Coverage)
- added a new req on perl(Carp) (version 0)
- added a new req on perl(English) (version 0)
- added a new req on perl(Perl::Critic) (version 1.105)
- added a new req on perl(Perl::Critic::Utils) (version 1.105)
- added a new req on perl(Perl::Critic::Violation) (version 1.105)
- added a new req on perl(Test::Builder) (version 0)

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 1.01-8
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.01-5
- Rebuild for perl 5.10 (again)

* Tue Jan 15 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.01-4
- disable tests, take out patch, doesn't fix test failures

* Tue Jan 15 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.01-3
- patch for test failure

* Mon Jan 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.01-2
- rebuild for new perl

* Sat Jan 27 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.01-1
- Update to 1.01.

* Sun Nov 12 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.08-1
- Update to 0.08.

* Sat Sep 23 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.07-1
- First build.
