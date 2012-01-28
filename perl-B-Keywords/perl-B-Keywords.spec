Name:           perl-B-Keywords
Version:        1.11
Release:        2%{?dist}
Summary:        Lists of reserved barewords and symbol names
Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/B-Keywords/
Source0:        http://search.cpan.org/CPAN/authors/id/F/FL/FLORA/B-Keywords-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(YAML)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))


%description
%{summary}.


%prep
%setup -q -n B-Keywords-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} ';' 2>/dev/null
%{_fixperms} $RPM_BUILD_ROOT


%check
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes LICENSE
%{perl_vendorlib}/B/
%{_mandir}/man3/B::Keywords.3pm*


%changelog
* Sat Jan 28 2012 Liu Di <liudidi@gmail.com> - 1.11-2
- 为 Magic 3.0 重建

* Wed Jan 11 2012 Paul Howarth <paul@city-fan.org> - 1.11-1
- Update to 1.11
  - Add new keywords for 5.16: __SUB__ and evalbytes
- Use DESTDIR rather than PERL_INSTALL_ROOT

* Wed Jun 29 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.10-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Sep  5 2010 Paul Howarth <paul@city-fan.org> - 1.10-1
- Update to 1.10 (fix typo in SYNOPSIS)
- This release by FLORA -> update source URL

* Thu Apr 29 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.09-5
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.09-4
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Mar 28 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.09-2
- BR Test -> Test::More

* Sat Mar 28 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.09-1
- update to 1.09

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat May 31 2008 Chris Weyl <cweyl@alumni.drew.edu> 1.08-2
- update buildrequires

* Sat Mar 15 2008 Chris Weyl <cweyl@alumni.drew.edu> 1.08-1
- update to 1.08

* Thu Feb 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.06-4
- Rebuild normally, second pass

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.06-3
- Rebuild for perl 5.10 (again), disable tests for first pass

* Mon Jan 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.06-2
- rebuild normally, second pass

* Fri Jan 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.06-1.1
- rebuild for new perl
- disable Test-Pod-Coverage, tests for first pass

* Thu Feb 15 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.06-1
- Update to 1.06.

* Sat Jan 20 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.05-1
- First build.
