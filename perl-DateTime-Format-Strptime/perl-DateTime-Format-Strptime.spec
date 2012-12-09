Name:           perl-DateTime-Format-Strptime
Version:        1.5000
Release:        8%{?dist}
Summary:        Parse and format strp and strf time patterns
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/DateTime-Format-Strptime/
Source0:        http://www.cpan.org/authors/id/R/RI/RICKM/DateTime-Format-Strptime-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(Class::ISA)
BuildRequires:  perl(DateTime) >= 0.44
BuildRequires:  perl(DateTime::Locale) >= 0.45
BuildRequires:  perl(DateTime::TimeZone) >= 0.79
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Params::Validate) >= 0.64
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module implements most of strptime(3), the POSIX function that is the
reverse of strftime(3), for DateTime. While strftime takes a DateTime and a
pattern and returns a string, strptime takes a string and a pattern and
returns the DateTime object associated.

%prep
%setup -q -n DateTime-Format-Strptime-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Dec 09 2012 Liu Di <liudidi@gmail.com> - 1.5000-8
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5000-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 20 2012 Petr Pisar <ppisar@redhat.com> - 1.5000-6
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5000-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 1.5000-4
- Perl mass rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 1.5000-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5000-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Steven Pritchard <steve@kspei.com> 1.5000-1
- Update to 1.5000.

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.2000-3
- 661697 rebuild for fixing problems with vendorach/lib

* Tue Jun 15 2010 Petr Sabata <psabata@redhat.com> - 1.2000-1
- Update to the latest upstream release

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.1000-2
- Mass rebuild with perl-5.12.0

* Tue Feb 16 2010 Paul Howarth <paul@city-fan.org> 1.1000-1
- Fix FTBFS (#564718) by bumping buildreq version of perl(DateTime) from 0.4304
  to 0.44 (RPM considers 0.4304 > 0.44, unlike perl) and bumping version to
  1.1000 for compatibility with DateTime::Locale 0.43 (upstream ticket 19)
- Update buildreq version requirement for perl(DateTime::Locale) to 0.43
- Drop test patch, no longer needed
- Run additional tests for full locale coverage

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> 1.0800-4
- Rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 1.0800-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 1.0800-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Aug 29 2008 Steven Pritchard <steve@kspei.com> 1.0800-1
- Update to 1.0800.
- Update versions on build dependencies.

* Tue Jul 08 2008 Steven Pritchard <steve@kspei.com> 1.0702-3
- Patch t/004_locale_defaults.t to work around change in DateTime::Locale.

* Tue Mar 04 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.0702-2
- Rebuild for new perl

* Thu Jan 03 2008 Steven Pritchard <steve@kspei.com> 1.0702-1
- Update to 1.0702.
- Drop charset patch.
- Update License tag.
- BR Test::More.

* Tue Apr 17 2007 Steven Pritchard <steve@kspei.com> 1.0700-3
- Use fixperms macro instead of our own chmod incantation.
- BR ExtUtils::MakeMaker.

* Sat Sep 16 2006 Steven Pritchard <steve@kspei.com> 1.0700-2
- Fix find option order.

* Mon Jul 03 2006 Steven Pritchard <steve@kspei.com> 1.0700-1
- Specfile autogenerated by cpanspec 1.66.
- Fix License.
- Remove versioned DateTime deps (0.1402 > 0.30 according to rpm).
- Remove versioned explicit dependencies that rpmbuild picks up.
- Substitute literal "©" for E<169> in pod documentation.  (The result
  should be the same, but apparently the man page conversion is generating
  something that rpmlint doesn't like.)
