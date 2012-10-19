Name:           perl-JSON-Path
Version:        0.101
Release:        4%{?dist}
Summary:        Search nested hashref/arrayref structures using JSONPath

License:        MIT
URL:            http://search.cpan.org/dist/JSON-Path/
Source0:        http://www.cpan.org/authors/id/T/TO/TOBYINK/JSON-Path-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  perl >= 1:5.8.0
BuildRequires:  perl(common::sense)
BuildRequires:  perl(Error)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(JSON)
BuildRequires:  perl(Test::More) >= 0.61

# Those are only needed when building for RHEL, on Fedora they come in as
# dependencies of the above
%if 0%{?rhel} < 7
BuildRequires:  perl(CPAN)
%endif

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(common::sense)
Requires:       perl(Error)
Requires:       perl(JSON)

%description
This module implements JSONPath, an XPath-like language for searching JSON-
like structures.


%prep
%setup -q -n JSON-Path-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*


%check
make test


%files
%defattr(-,root,root,-)
%doc Changes Changes.ttl Changes.xml README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.101-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 16 2012 Petr Pisar <ppisar@redhat.com> - 0.101-3
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.101-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct 21 2011 Mathieu Bridon <bochecha@fedoraproject.org> 0.101-1
- Specfile autogenerated by cpanspec 1.78. (with a couple of tweaks)
