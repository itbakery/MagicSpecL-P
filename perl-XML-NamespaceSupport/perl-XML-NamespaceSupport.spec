Name:           perl-XML-NamespaceSupport
Version:        1.11
Release:        6%{?dist}
Summary:        A simple generic namespace support class

Group:          Development/Libraries
License:        GPL+ or Artistic
Url:            http://search.cpan.org/dist/XML-NamespaceSupport/
Source0:        http://www.cpan.org/authors/id/P/PE/PERIGRIN/XML-NamespaceSupport-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires:  perl(Test::More) >= 0.47
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
%{summary}.


%prep
%setup -q -n XML-NamespaceSupport-%{version}
%{__chmod} 644 lib/XML/NamespaceSupport.pm

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/XML/
%{_mandir}/man3/*.3*


%changelog
* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.11-5
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 23 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.11-3
- 661697 rebuild for fixing problems with vendorach/lib

* Tue Jun 29 2010 Lubomir Rintel <lkundrak@v3.sk> - 1.11-2
- Rebuild 1.11 for perl 5.12 as well

* Tue May 11 2010 Petr Pisar <ppisar@redhat.com> - 1.11-1
- 1.11 version bump

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.10-4
- Mass rebuild with perl-5.12.0

* Wed Jan 27 2010 Stepan Kasal <skasal@redhat.com> - 1.10-3
- fix upstream URL

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.10-2
- rebuild against perl 5.10.1

* Tue Oct  6 2009 Marcela Mašláňová <mmaslano@redhat.com> - 1.10-1
- update to new upstream release

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.09-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.09-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.09-4
- Rebuild for perl 5.10 (again)

* Thu Jan 24 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.09-3
- rebuild for new perl

* Wed Oct 17 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 1.09-2.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Sat Feb 17 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.09-2
- Minor specfile cleanups.
- Dist tag.

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.09-1.2.1
- rebuild

* Fri Feb 03 2006 Jason Vas Dias <jvdias@redhat.com> - 1.09-1.2
- rebuild for new perl-5.8.8

* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcc

* Fri Sep  9 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.09-1
- Update to 1.09.

* Sat Apr 30 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.08-7
- Bring up to date with current Fedora.Extras perl spec template. (#156511)

* Wed Sep 22 2004 Chip Turner <cturner@redhat.com> 1.08-6
- rebuild

* Thu Oct 17 2002 cturner@redhat.com
- Specfile autogenerated

