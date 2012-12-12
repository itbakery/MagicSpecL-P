Name:           perl-Test-Base
Version:        0.60
Release:        6%{?dist}
Summary:        Data Driven Testing Framework
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Test-Base/
Source0:        http://www.cpan.org/authors/id/I/IN/INGY/Test-Base-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Spiffy) >= 0.30
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More) >= 0.62
BuildRequires:  perl(Test::Tester)
BuildRequires:  perl(Text::Diff) >= 0.35
BuildRequires:  perl(YAML)
Requires:       perl(Text::Diff) >= 0.35
Requires:       perl(LWP::Simple)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Testing is usually the ugly part of Perl module authoring. Perl gives you a
standard way to run tests with Test::Harness, and basic testing primitives
with Test::More. After that you are pretty much on your own to develop a
testing framework and philosophy. Test::More encourages you to make your
own framework by subclassing Test::Builder, but that is not trivial.

%prep
%setup -q -n Test-Base-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check


%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.60-6
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 0.60-4
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 29 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.60-2
- Perl mass rebuild

* Sat May 14 2011 Iain Arnell <iarnell@gmail.com> 0.60-1
- update to latest upstream version
- clean up spec for modern rpmbuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.59-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.59-2
- 661697 rebuild for fixing problems with vendorach/lib

* Mon Dec 13 2010 Steven Pritchard <steve@kspei.com> 0.59-1
- Update to 0.59.

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.58-4
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.58-3
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.58-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 17 2009 Steven Pritchard <steve@kspei.com> 0.58-1
- Update to 0.58.
- BR Test::Deep and Test::Tester.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.55-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec 10 2008 Steven Pritchard <steve@kspei.com> 0.55-1
- Update to 0.55.
- Explicitly BR Test::More >= 0.62.
- BR YAML.

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.54-3
- Rebuild for new perl

* Sat Jul 07 2007 Steven Pritchard <steve@kspei.com> 0.54-2
- BR Test::More.

* Mon Jul 02 2007 Steven Pritchard <steve@kspei.com> 0.54-1
- Update to 0.54.

* Wed Apr 18 2007 Steven Pritchard <steve@kspei.com> 0.53-2
- BR ExtUtils::MakeMaker.

* Sat Dec 09 2006 Steven Pritchard <steve@kspei.com> 0.53-1
- Update to 0.53.
- Use fixperms macro instead of our own chmod incantation.

* Sat Sep 16 2006 Steven Pritchard <steve@kspei.com> 0.52-2
- Fix find option order.

* Sat Jul 01 2006 Steven Pritchard <steve@kspei.com> 0.52-1
- Update to 0.52.

* Mon May 08 2006 Steven Pritchard <steve@kspei.com> 0.50-2
- Add explicit dependencies for Text::Diff and LWP::Simple.

* Thu May 04 2006 Steven Pritchard <steve@kspei.com> 0.50-1
- Specfile autogenerated by cpanspec 1.65.
- Remove explicit BR: perl and Requires: perl(Spiffy).
