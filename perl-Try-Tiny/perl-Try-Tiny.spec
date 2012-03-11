Name:           perl-Try-Tiny
Summary:        Minimal try/catch with proper localization of $@
Version:        0.11
Release:        3%{?dist}
License:        MIT
Group:          Development/Libraries
Source0:        http://search.cpan.org/CPAN/authors/id/D/DO/DOY/Try-Tiny-%{version}.tar.gz
URL:            http://search.cpan.org/dist/Try-Tiny
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildArch:      noarch

BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)

# obsolete/provide old tests subpackage
# can be removed during F19 development cycle
Obsoletes:      %{name}-tests < 0.11-3
Provides:       %{name}-tests = %{version}-%{release}

%{?perl_default_filter}

%description
The main focus of this module is to provide simple and reliable error
handling for those having a hard time installing TryCatch, but who still
want to write correct 'eval' blocks without 5 lines of boilerplate each
time.

%prep
%setup -q -n Try-Tiny-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes t/
%{perl_vendorlib}/Try/
%{_mandir}/man3/Try::Tiny.3pm*

%changelog
* Sun Jan 22 2012 Iain Arnell <iarnell@gmail.com> 0.11-3
- drop tests subpackage; move tests to main package documentation

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct 02 2011 Iain Arnell <iarnell@gmail.com> 0.11-1
- update to latest upstream version

* Wed Jun 15 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.09-2
- Perl mass rebuild

* Fri Mar 18 2011 Iain Arnell <iarnell@gmail.com> 0.09-1
- update to latest upstream version
- clean up spec for modern rpmbuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov  1 2010 Paul Howarth <paul@city-fan.org> 0.07-1
- update to 0.07:
  - allow multiple finally blocks
  - pass the error, if any, to finally blocks when called
  - documentation fixes and clarifications
- this release by RJBS -> update source URL

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.04-2
- Mass rebuild with perl-5.12.0

* Tue Mar 02 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.04-1
- update by Fedora::App::MaintainerTools 0.004
- PERL_INSTALL_ROOT => DESTDIR
- updating to latest GA CPAN version (0.04)

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.02-2
- rebuild against perl 5.10.1

* Tue Sep 15 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.02-1
- submission

* Tue Sep 15 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.02-0
- initial RPM packaging
- generated with cpan2dist (CPANPLUS::Dist::RPM version 0.0.8)
