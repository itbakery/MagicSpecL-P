Name:           perl-POE-Test-Loops
Summary:        Reusable tests for POE::Loop authors
Version:        1.350
Release:        2%{?dist}
License:        GPL+ or Artistic
Group:          Development/Libraries
Source0:        http://search.cpan.org/CPAN/authors/id/R/RC/RCAPUTO/POE-Test-Loops-%{version}.tar.gz 
URL:            http://search.cpan.org/dist/POE-Test-Loops
BuildArch:      noarch
BuildRequires:  perl(constant)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(POE)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::More) >= 0.94
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# RPM 4.8 style
%{?filter_from_provides: %filter_from_provides /perl([DIFMOSU].*)/d; /perl(POE::MySession)/d; /perl(POE::Kernel)/d; /perl(PoeTestWorker)/d; /perl(Switch)/d }
%{?perl_default_filter}
%{?perl_default_subpackage_tests}
# RPM 4.9 style
%global __provides_exclude %{?__provides_exclude:__requires_exclude|}^perl\\(POE::MySession\\)
%global __provides_exclude %__provides_exclude|perl\\(POE::Kernel\\)
%global __provides_exclude %__provides_exclude|perl\\(PoeTestWorker\\)
%global __provides_exclude %__provides_exclude|perl\\([DIFMOSU].*\\)
%global __provides_exclude %__provides_exclude|perl\\(Switch\\)

%description
POE::Test::Loops contains one function, generate(), which will generate
all the loop tests for one or more POE::Loop subclasses. The SYNOPSIS
example is a version of poe-gen-tests, which is a stand-alone utility
to generate the actual tests. The poe-gen-tests manual page also documents
the POE::Test::Loops system in more detail.

%prep
%setup -q -n POE-Test-Loops-%{version}
find . -type f -exec chmod -c -x {} ';'

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
%doc CHANGES README
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*
%{_bindir}/poe-gen-tests
%{_mandir}/man1/poe-gen-tests.1.gz

%changelog
* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.350-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 21 2011 Petr Šabata <contyk@redhat.com> - 1.350-1
- 1.350 bump

* Fri Aug  5 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.312-2
- filter also Switch from provides, just to be sure

* Wed Jul 27 2011 Petr Sabata <contyk@redhat.com> - 1.312-1
- 1.312 bump (needed by current POE)
- Drop Buildroot and defattr support
- Fix dependencies a bit
- Add RPM 4.9 style filters
- Filter POE::Kernel and PoeTestWorker from Provides

* Thu Jun 16 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.035-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.035-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.035-2
- 661697 rebuild for fixing problems with vendorach/lib

* Mon Jun  7 2010 Petr Pisar <ppisar@redhat.com> - 1.035-1
- 1.035 bump
- Orthography fix in description

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.033-2
- Mass rebuild with perl-5.12.0

* Sun Mar 14 2010 Chris Weyl <cweyl@alumni.drew.edu> 1.033-1
- update by Fedora::App::MaintainerTools 0.006
- PERL_INSTALL_ROOT => DESTDIR
- updating to latest GA CPAN version (1.033)

* Sun Sep 27 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.022-1
- update filtering
- auto-update to 1.022 (by cpan-spec-update 0.01)

* Tue Aug 11 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.021-1
- auto-update to 1.021 (by cpan-spec-update 0.01)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.005-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Apr 10 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.005-1
- update for submission

* Fri Apr 10 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.005-0
- initial RPM packaging
- generated with cpan2dist (CPANPLUS::Dist::RPM version 0.0.8)
