# Remove once apocalypse gets into build root. But keep the BuildRequires
# conditional blocks to utlize apocalypse during futher package life.
%define perl_bootstrap 1

Name:           perl-Test-Pod-No404s
Version:        0.01
Release:        5%{?dist}
Summary:        Checks POD for HTTP 404 links
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Test-Pod-No404s/
Source0:        http://www.cpan.org/authors/id/A/AP/APOCAL/Test-Pod-No404s-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Module::Build)
# Run-Time:
BuildRequires:  perl(LWP::UserAgent) >= 5.834
BuildRequires:  perl(Pod::Simple::Text) >= 3.13
BuildRequires:  perl(Test::Builder) >= 0.94
BuildRequires:  perl(Test::Pod) >= 1.40
BuildRequires:  perl(URI::Find) >= 20090319
# Tests:
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(Test::NoWarnings)
# Break build-time cycle with perl-Test-Apocalypse
%if %{undefined perl_bootstrap}
BuildRequires:  perl(Test::Apocalypse)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(LWP::UserAgent) >= 5.834
Requires:       perl(Pod::Simple::Text) >= 3.13
Requires:       perl(Test::Builder) >= 0.94
Requires:       perl(Test::Pod) >= 1.40
Requires:       perl(URI::Find) >= 20090319

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((LWP::UserAgent|Pod::Simple::Text|Test::Builder|Test::Pod|URI::Find)\\)$

%description
This module looks for any HTTP(S) links in your POD and verifies that they
will not return a 404. It uses LWP::UserAgent for the heavy lifting, and
simply lets you know if it failed to retrieve the document. More specifically,
it uses $response->is_error as the "test".

%prep
%setup -q -n Test-Pod-No404s-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes examples LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Dec 10 2012 Liu Di <liudidi@gmail.com> - 0.01-5
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.01-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Petr Pisar <ppisar@redhat.com> - 0.01-3
- Perl 5.16 re-rebuild of bootstrapped packages

* Fri Jun 15 2012 Petr Pisar <ppisar@redhat.com> - 0.01-2
- Perl 5.16 rebuild

* Thu Apr 26 2012 Petr Pisar <ppisar@redhat.com> 0.01-1
- Specfile autogenerated by cpanspec 1.78.
