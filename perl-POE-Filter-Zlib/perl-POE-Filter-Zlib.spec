Name:           perl-POE-Filter-Zlib
Version:        2.02
Release:        11%{?dist}
Summary:        POE filter wrapped around Compress::Zlib
# note license definition in Makefile.PL
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/POE-Filter-Zlib/
Source0:        http://search.cpan.org/CPAN/authors/id/B/BI/BINGOS/POE-Filter-Zlib-%{version}.tar.gz
# just to be thorough, see also:
Source1:        LICENSE.readme
BuildArch:      noarch
BuildRequires:  perl(Carp)
BuildRequires:  perl(Compress::Raw::Zlib) >= 2
BuildRequires:  perl(Compress::Zlib) >= 1.34
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires:  perl(POE)
BuildRequires:  perl(POE::Filter)
BuildRequires:  perl(POE::Filter::Line)
BuildRequires:  perl(POE::Filter::Stackable)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00
BuildRequires:  perl(Test::More) >= 0.47
Requires:       perl(POE::Filter)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
POE::Filter::Zlib provides a POE filter for performing compression and
uncompression using Compress::Zlib. It is suitable for use with
POE::Filter::Stackable.

%prep
%setup -q -n POE-Filter-Zlib-%{version}
# deal with our licensing....
cp %{SOURCE1} .

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} %{buildroot}/*

%check


%files
%doc README LICENSE*
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Dec 09 2012 Liu Di <liudidi@gmail.com> - 2.02-11
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.02-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 2.02-9
- Perl 5.16 rebuild

* Mon Jan 16 2012 Petr Šabata <contyk@redhat.com> - 2.02-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild
- Spec cleanup, fix build, remove useless generated licenses

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 2.02-7
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.02-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.02-5
- 661697 rebuild for fixing problems with vendorach/lib

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.02-4
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 2.02-3
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jun 07 2009 Chris Weyl <cweyl@alumni.drew.edu> 2.02-1
- auto-update to 2.02 (by cpan-spec-update 0.01)
- added a new br on perl(ExtUtils::MakeMaker) (version 6.42)
- added a new br on perl(POE::Filter) (version 0)
- altered br on perl(POE) (0.3501 => 0.38)
- added a new br on perl(Test::More) (version 0.47)
- added a new br on perl(Compress::Raw::Zlib) (version 2)
- added a new br on perl(POE::Filter::Line) (version 0)
- added a new br on perl(POE::Filter::Stackable) (version 0)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Oct 26 2008 Chris Weyl <cweyl@alumni.drew.edu> 2.01-1
- update to 2.01

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.8-2
- rebuild for new perl

* Fri Dec 15 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.8-1
- update to 1.8

* Fri Sep 29 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.7-1
- update to 1.7, basically just clarifies some licensing bits

* Wed Sep 13 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.6-1
- update to 1.6

* Wed Sep 06 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.5-1
- update to 1.5
- add new BR's (Test::Pod && Test::Pod::Coverage) for testing

* Wed Sep 06 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.4-2
- bump

* Fri Sep 01 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.4-1
- Specfile autogenerated by cpanspec 1.69.1.
