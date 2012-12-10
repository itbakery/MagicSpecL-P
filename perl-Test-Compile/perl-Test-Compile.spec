Name:           perl-Test-Compile
Version:        0.21
Release:        2%{?dist}
Summary:        Check whether Perl module files compile correctly
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Test-Compile/
Source0:        http://search.cpan.org/CPAN/authors/id/E/EG/EGILES/Test-Compile-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time
# Devel::CheckOS is needed only on VMS. See Changes.
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(UNIVERSAL::require)
# Tests
# Test::More version is described in Changes
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%{?perl_default_filter}

%description
Test::Compile lets you check the validity of a Perl module file or Perl script
file, and report its results in standard Test::Simple fashion.

%prep
%setup -q -n Test-Compile-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} %{buildroot}/*

%check


%files
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Dec 10 2012 Liu Di <liudidi@gmail.com> - 0.21-2
- 为 Magic 3.0 重建

* Thu Sep 13 2012 Jitka Plesnikova <jplesnik@redhat.com> - 0.21-1
- 0.21 bump
- Remove the filter of ::Internal module. It is no longer 'beta' and could
  be used directly to test a CPAN distribution.

* Thu Aug 09 2012 Petr Šabata <contyk@redhat.com> - 0.20-1
- 0.20 bump

* Wed Aug 08 2012 Petr Šabata <contyk@redhat.com> - 0.19-2
- Filter the ::Internal module from requires too

* Mon Aug 06 2012 Petr Šabata <contyk@redhat.com> - 0.19-1
- 0.19 bump

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-1
- 0.18 bump

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 0.17-2
- Perl 5.16 rebuild

* Fri Feb 24 2012 Petr Šabata <contyk@redhat.com> - 0.17-1
- 0.17 bump

* Mon Feb 20 2012 Petr Šabata <contyk@redhat.com> - 0.16-1
- 0.16 bump

* Fri Feb 03 2012 Petr Pisar <ppisar@redhat.com> - 0.15-1
- 0.15 bump

* Fri Jan 13 2012 Marcela Mašláňová <mmaslano@redhat.com> - 0.14-1
- bump to 0.14

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.13-5
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.13-3
- 661697 rebuild for fixing problems with vendorach/lib

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.13-2
- Mass rebuild with perl-5.12.0

* Sat Mar 20 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.13-1
- PERL_INSTALL_ROOT => DESTDIR, perl_default_filter
- auto-update to 0.13 (by cpan-spec-update 0.01)
- altered br on perl(ExtUtils::MakeMaker) (0 => 6.42)
- altered br on perl(Test::More) (0.70 => 0.88)
- added a new br on CPAN (inc::Module::AutoInstall found)

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.08-4
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec 16 2008 Marcela Mašláňová <mmaslano@redhat.com> 0.08-1
- Specfile autogenerated by cpanspec 1.77.
