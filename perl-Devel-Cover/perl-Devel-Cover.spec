Name:           perl-Devel-Cover
Version:        0.78
Release:        5%{?dist}
Summary:        Code coverage metrics for Perl

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Devel-Cover/
Source0:        http://www.cpan.org/authors/id/P/PJ/PJCJ/Devel-Cover-%{version}.tar.gz

BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(Template)
BuildRequires:  perl(PPI::HTML) >= 1.07
BuildRequires:  perl(Perl::Tidy) >= 20060719
BuildRequires:  perl(Pod::Coverage)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(Pod::Coverage)
Requires:       perl(Test::Differences)
# Optional modules
# Requires:       perl(PPI::HTML) >= 1.07
# Requires:       perl(Perl::Tidy) >= 20060719

%{?perl_default_filter}

%description
This module provides code coverage metrics for Perl.


%prep
%setup -q -n Devel-Cover-%{version}

find lib -type f -print0 | xargs -0 chmod 0644

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}


%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check



%files
%doc CHANGES README docs/BUGS docs/TODO
%{_bindir}/*
%{perl_vendorarch}/Devel/
%{perl_vendorarch}/auto/Devel/
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3pm*


%changelog
* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.78-5
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.78-4
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.78-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.78-2
- Perl mass rebuild

* Thu May 19 2011 Iain Arnell <iarnell@gmail.com> 0.78-1
- update to latest upstream version
- clean up spec for modern rpmbuild
- use perl_default_filter

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.66-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.66-2
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.66-1
- Mass rebuild with perl-5.12.0 & update

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.65-2
- Mass rebuild with perl-5.12.0

* Thu Jan 14 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 0.65-1
- update to 0.65

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.64-4
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.64-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.64-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jun 13 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.64-1
- update to 0.64

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.63-3
- Rebuild for new perl

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.63-2
- Autorebuild for GCC 4.3

* Wed Nov 28 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 0.63-1
- 0.63

* Mon Oct 15 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 0.61-1.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Thu Jan 11 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.61-1
- Update to 0.61.

* Thu Jan  4 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.60-1
- Update to 0.60.

* Wed Sep  6 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.59-1
- Update to 0.59.
- Dropped PPI::HTML from the requirements list (optional module).

* Wed Aug  9 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.58-1
- Update to 0.58.

* Fri Aug  4 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.57-1
- Update to 0.57.

* Thu Aug  3 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.56-1
- Update to 0.56.

* Fri May 12 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.55-2
- Removed dependencies pulled in by a documentation file (#191110).

* Thu May 04 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.55-1
- First build.
