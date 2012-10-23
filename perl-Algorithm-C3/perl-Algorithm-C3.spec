Name:		perl-Algorithm-C3
Version:	0.08
Release:	11%{?dist}
Summary:	Module for merging hierarchies using the C3 algorithm
License:	GPL+ or Artistic
Group:		Development/Libraries
URL:		http://search.cpan.org/dist/Algorithm-C3/
Source0:	http://search.cpan.org/CPAN/authors/id/F/FL/FLORA/Algorithm-C3-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(id -nu)
BuildArch:	noarch
# Build
BuildRequires:	perl(Module::Build)
# Module
BuildRequires:	perl(Carp) >= 0.01
# Test
BuildRequires:	perl(Test::More) >= 0.47
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Pod::Coverage)
# Runtime
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
This module implements the C3 algorithm.  Most of the uses I have for C3
revolve around class building and metamodels but it could also be used for
things like dependency resolution as well since it tends to do such a nice
job of preserving local precedence orderings.

%prep
%setup -q -n Algorithm-C3-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -depth -type d -exec rmdir {} \; 2>/dev/null
%{_fixperms} %{buildroot}

%check
./Build test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc Changes README t/
%{perl_vendorlib}/Algorithm/
%{_mandir}/man3/Algorithm::C3.3pm*

%changelog
* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 0.08-10
- Perl 5.16 rebuild

* Mon Jan 16 2012 Paul Howarth <paul@city-fan.org> - 0.08-9
- Spec clean-up:
  - Make %%files list more explicit
  - Categorize build requirements for build/module/test
  - Don't use macros for commands
  - Use tabs
  - Fix typo in %%description

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.08-7
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 14 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.08-5
- Rebuild to fixproblems with vendorarch/lib (#661697)

* Thu Apr 29 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.08-4
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.08-3
- Rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jun 07 2009 Chris Weyl <cweyl@alumni.drew.edu> - 0.08-1
- Auto-update to 0.08 (by cpan-spec-update 0.01)
- Altered br on perl(Test::More) (0 => 0.47)
- Added a new br on perl(Carp) (version 0.01)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Mar 04 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.07-2
- Rebuild for new perl

* Thu May 31 2007 Chris Weyl <cweyl@alumni.drew.edu> - 0.07-1
- Update to 0.07
- Include t/ in doc
- Minor spec reworkage to deal with the once and future perl split

* Tue Nov 21 2006 Chris Weyl <cweyl@alumni.drew.edu> - 0.06-1
- Update to 0.06

* Wed Sep 06 2006 Chris Weyl <cweyl@alumni.drew.edu> - 0.05-2
- Bump

* Tue Sep 05 2006 Chris Weyl <cweyl@alumni.drew.edu> - 0.05-1
- Specfile autogenerated by cpanspec 1.69.1
