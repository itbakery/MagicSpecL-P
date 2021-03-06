Name:           perl-Error
Version:        0.17018
Release:        5%{?dist}
Epoch:          1
Summary:        Error/exception handling in an OO-ish way
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Error/
Source0:        http://www.cpan.org/authors/id/S/SH/SHLOMIF/Error-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Build)
# Run-requires:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Scalar::Util)
# Tests:
BuildRequires:  perl(base)
BuildRequires:  perl(Test::More)
# Optional tests:
%if !%{defined perl_bootstrap}
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(Carp)

%description
The Error package provides two interfaces. Firstly Error provides a
procedural interface to exception handling. Secondly Error is a base class
for errors/exceptions that can either be thrown, for subsequent catch, or
can simply be recorded.

%prep
%setup -q -n Error-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
rm -rf $RPM_BUILD_ROOT

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc ChangeLog README examples/
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 1:0.17018-5
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.17018-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Petr Pisar <ppisar@redhat.com> - 1:0.17018-3
- Perl 5.16 re-rebuild of bootstrapped packages

* Thu Jun 07 2012 Petr Pisar <ppisar@redhat.com> - 1:0.17018-2
- Perl 5.16 rebuild

* Thu Jun 07 2012 Petr Pisar <ppisar@redhat.com> - 1:0.17018-1
- 0.17018 bump
- Specify all dependencies
- Skip POD tests on bootstrap

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.17016-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1:0.17016-6
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.17016-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 1:0.17016-4
- 661697 rebuild for fixing problems with vendorach/lib

* Sat May 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 1:0.17016-3
- Mass rebuild with perl-5.12.0

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1:0.17016-2
- Mass rebuild with perl-5.12.0

* Mon Jan 18 2010 Marcela Mašláňová <mmaslano@redhat.com> - 1:0.1716-1
- update

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1:0.17015-4
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.17015-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.17015-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Aug 02 2008 Steven Pritchard <steve@kspei.com> 1:0.17015-1
- Update to 0.17015.

* Sat May 31 2008 Steven Pritchard <steve@kspei.com> 1:0.17014-1
- Update to 0.17014.

* Tue Feb  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1:0.17012-2
- rebuild for new perl

* Mon Jan 28 2008 Steven Pritchard <steve@kspei.com> 1:0.17012-1
- Update to 0.17012.

* Mon Jan 07 2008 Steven Pritchard <steve@kspei.com> 1:0.17011-1
- Update to 0.17011.
- Canonicalize Source0 URL.
- Fix find option order.
- Use fixperms macro instead of our own chmod incantation.
- Improve Summary.
- Reformat to match cpanspec output.
- Build with Module::Build.

* Tue Dec 04 2007 Ralf Corsépius <rc040203@freenet.de> - 1:0.17010-1
- Upstream update.
- Update license tag.

* Sat Oct 28 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1:0.17008-1
- Update to 0.17008.

* Wed Oct 18 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1:0.17007-1
- Update to 0.17007.

* Sat Oct  7 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1:0.17006-1
- Update to 0.17006.
- New build requirements: Test::Pod and Test::Pod::Coverage.

* Wed Oct  4 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1:0.17005-1
- Update to 0.17005.

* Mon Sep  4 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1:0.17004-1
- Update to 0.17004.

* Mon Aug 28 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1:0.17003-1
- Update to 0.17003.

* Wed Aug  9 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1:0.17001-1
- Update to 0.17001.

* Fri Jul 14 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1:0.17-1
- Update to 0.17.

* Tue Jul 11 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1:0.16-1
- Update to 0.16.

* Fri Apr 28 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.15009-1
- Update to 0.15009.

* Wed Apr 19 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.15008-1
- Update to 0.15008.

* Fri Feb 17 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.15-4
- Rebuild for FC5 (perl 5.8.8).

* Thu Dec 29 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.15-3
- Dist tag.

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.15-2
- rebuilt

* Fri Jun 11 2004 Steven Pritchard <steve@kspei.com> 0:0.15-1
- Specfile autogenerated.
