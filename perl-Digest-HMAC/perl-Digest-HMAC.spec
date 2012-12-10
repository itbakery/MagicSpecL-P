Name:           perl-Digest-HMAC
Version:        1.03
Release:        5%{?dist}
Summary:        Keyed-Hashing for Message Authentication
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Digest-HMAC/
Source0:        http://www.cpan.org/authors/id/G/GA/GAAS/Digest-HMAC-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(Digest::MD5), perl(Digest::SHA1), perl(ExtUtils::MakeMaker)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
HMAC is used for message integrity checks between two parties that
share a secret key, and works in combination with some other Digest
algorithm, usually MD5 or SHA-1. The HMAC mechanism is described in
RFC 2104.

HMAC follow the common Digest:: interface, but the constructor takes
the secret key and the name of some other simple Digest:: as argument.


%prep
%setup -q -n Digest-HMAC-%{version} 


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check



%files
%doc Changes README
%{perl_vendorlib}/Digest/
%{_mandir}/man3/*.3*


%changelog
* Mon Dec 10 2012 Liu Di <liudidi@gmail.com> - 1.03-5
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 1.03-3
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Sep 22 2011 Marcela Mašláňová <mmaslano@redhat.com> 1.03-1
- update to 1.03

* Sun Jun 19 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.02-6
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.02-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.02-4
- 661697 rebuild for fixing problems with vendorach/lib

* Sat May 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.02-3
- Mass rebuild with perl-5.12.0

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.02-2
- Mass rebuild with perl-5.12.0

* Tue Apr 20 2010 Petr Pisar <ppisar@redhat.com> - 1.02-1
- version bump
- rfc2104.txt removed by upstream 

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.01-22
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.01-19
- Rebuild for perl 5.10 (again)

* Sun Jan 20 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.01-18
- rebuild for new perl

* Wed Oct 24 2007 Robin Norwood <rnorwood@redhat.com> - 1.01-17
- fix various issues from package review

* Mon Aug 27 2007 Robin Norwood <rnorwood@redhat.com> - 1.01-16
- Fix license tag
- add %%doc section
- Add BuildRequire: perl(ExtUtils::MakeMaker)

* Fri Jul 14 2006 Jesse Keating <jkeating@redhat.com> - 1.01-15
- rebuild for new perl-5.8.8

* Fri Feb 03 2006 Jason Vas Dias <jvdias@redhat.com> - 1.01-14.2
- rebuild for new perl-5.8.8

* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcc

* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcj

* Mon Apr 25 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.01-14
- Bring up to date with current Fedora.Extras perl spec template. (#155912)

* Wed Sep 22 2004 Chip Turner <cturner@redhat.com> 1.01-13
- rebuild

* Fri Apr 23 2004 Chip Turner <cturner@redhat.com> 1.01-12
- bump

* Mon Jan 27 2003 Chip Turner <cturner@redhat.com>
- version bump and rebuild

* Tue Aug  6 2002 Chip Turner <cturner@redhat.com>
- automated release bump and build

* Thu Jun 27 2002 Chip Turner <cturner@redhat.com>
- description update

* Wed Jun 26 2002 cturner@redhat.com
- Specfile autogenerated

