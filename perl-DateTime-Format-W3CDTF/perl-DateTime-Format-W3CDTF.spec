Name:           perl-DateTime-Format-W3CDTF
Version:        0.06
Release:        3%{?dist}
Summary:        Parse and format W3CDTF datetime strings
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/DateTime-Format-W3CDTF/
Source0:        http://search.cpan.org/CPAN/authors/id/G/GW/GWILLIAMS/DateTime-Format-W3CDTF-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::TimeZone)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module understands the W3CDTF date/time format, an ISO 8601 profile,
defined at http://www.w3.org/TR/NOTE-datetime. This format as the native
date format of RSS 1.0.

%prep
%setup -q -n DateTime-Format-W3CDTF-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} %{buildroot}/*

%check


%files
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.06-3
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jan 03 2012 Petr Šabata <contyk@redhat.com> - 0.06-1
- 0.06 bump (#770260)
- Source updated
- Removed now obsolete Buildroot and defattr

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 0.05-6
- Perl mass rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.05-5
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.05-3
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.05-2
- Mass rebuild with perl-5.12.0

* Sat Feb 13 2010 Steven Pritchard <steve@kspei.com> 0.05-1
- Update to 0.05.
- Update Source0 URL.
- Build with Module::Build.

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.04-8
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.04-5
- Rebuild for perl 5.10 (again)

* Thu Jan 24 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.04-4
- rebuild for new perl

* Thu Jan 03 2008 Ralf Corsépius <rc040203@freenet.de> 0.04-3
- Adjust License-tag.
- BR: perl(Test::More) (BZ 419631).

* Tue Apr 17 2007 Steven Pritchard <steve@kspei.com> 0.04-2
- Use fixperms macro instead of our own chmod incantation.
- BR ExtUtils::MakeMaker.

* Sat Aug 26 2006 Steven Pritchard <steve@kspei.com> 0.04-1
- Specfile autogenerated by cpanspec 1.68.
- Fix License tag.
