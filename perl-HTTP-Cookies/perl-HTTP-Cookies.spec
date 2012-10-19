Name:           perl-HTTP-Cookies
Version:        6.01
Release:        3%{?dist}
Summary:        HTTP cookie jars
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/HTTP-Cookies/
Source0:        http://www.cpan.org/authors/id/G/GA/GAAS/HTTP-Cookies-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTTP::Date) >= 6
BuildRequires:  perl(HTTP::Headers::Util) >= 6
# Tests only:
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(Test)
BuildRequires:  perl(URI)
# Time::Local needed on MacOS only
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(HTTP::Date) >= 6
Requires:       perl(HTTP::Headers::Util) >= 6
Conflicts:      perl-libwww-perl < 6

# Remove underspecified dependencies
%filter_from_requires /^perl(HTTP::Date)\s*$/d
%filter_from_requires /^perl(HTTP::Headers::Util)\s*$/d
# One function of provided HTTP::Cookies::Microsoft works on Win32 only, other
# function do not need it. This keep the module, but remove dependency.
%filter_from_requires /^perl(Win32)/d
%filter_setup
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(Win32|HTTP::Date|HTTP::Headers::Util\\)$


%description
This class is for objects that represent a "cookie jar" -- that is, a
database of all the HTTP cookies that a given LWP::UserAgent object
knows about.

%prep
%setup -q -n HTTP-Cookies-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.01-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 6.01-2
- Perl 5.16 rebuild

* Thu Feb 16 2012 Petr Pisar <ppisar@redhat.com> - 6.01-1
- 6.01 bump

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.00-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 25 2011 Marcela Mašláňová <mmaslano@redhat.com> - 6.00-3
- add new filter

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 6.00-2
- Perl mass rebuild

* Wed Mar 16 2011 Petr Pisar <ppisar@redhat.com> 6.00-1
- Specfile autogenerated by cpanspec 1.78.
- Remove BuildRoot stuff
- Conflicts with perl-libwww-perl-5* and older
