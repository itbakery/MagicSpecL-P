Name:           perl-Data-Visitor
Version:        0.28
Release:        3%{?dist}
Summary:        Visitor style traversal of Perl data structures
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Data-Visitor/
Source0:        http://search.cpan.org/CPAN/authors/id/D/DO/DOY/Data-Visitor-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

BuildRequires:  perl(Class::Load)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Moose) >= 0.89
BuildRequires:  perl(namespace::clean) >= 0.19
BuildRequires:  perl(Task::Weaken)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Tie::ToObject) >= 0.01

%{?perl_default_filter}

%description
This module is a simple visitor implementation for Perl values.

%prep
%setup -q -n Data-Visitor-%{version}

# silence rpmlint warnings
sed -i '1s,^#!.*perl,#!%{__perl},' t/*.t

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} +
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes LICENSE README t/
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 0.28-2
- Perl 5.16 rebuild

* Sun Feb 19 2012 Iain Arnell <iarnell@gmail.com> 0.28-1
- update to latest upstream version
- clean up spec for modern rpmbuild
- use perl_default_filter and DESTDIR
- add LICENSE and README to docs

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.27-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 0.27-5
- Perl mass rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.27-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.27-2
- 661697 rebuild for fixing problems with vendorach/lib

* Tue Jun  1 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.27-1
- update

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.26-2
- Mass rebuild with perl-5.12.0

* Mon Jan 04 2010 Iain Arnell <iarnell@gmail.com> 0.26-1
- update to latest upstream version
- BR perl(Moose), not perl(Any::Moose)

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.25-3
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May 21 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.25-1
- auto-update to 0.25 (by cpan-spec-update 0.01)
- altered br on perl(Any::Moose) (0 => 0.09)
- altered br on perl(Tie::ToObject) (0 => 0.01)
- altered br on perl(namespace::clean) (0 => 0.08)

* Tue May 05 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.24-1
- update to 0.24

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 10 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.22-1
- update to 0.22

* Wed Nov 12 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.21-1
- update to 0.21

* Sat Sep 06 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.19-1
- update to 0.19

* Wed Mar 05 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.09-2
- rebuild for new perl

* Sun Oct 21 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.09-1
- update to 0.09
- update license tag: GPL -> GPL+
- add t/ to doc
- back to good old Makefile.PL; Build.PL seems to have gone away

* Thu May 03 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.05-2
- bump

* Tue Apr 10 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.05-1
- Specfile autogenerated by cpanspec 1.70.
