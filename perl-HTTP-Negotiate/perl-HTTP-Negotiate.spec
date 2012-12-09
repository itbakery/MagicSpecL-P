Name:           perl-HTTP-Negotiate
Version:        6.01
Release:        4%{?dist}
Summary:        Choose a variant to serve
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/HTTP-Negotiate/
Source0:        http://www.cpan.org/authors/id/G/GA/GAAS/HTTP-Negotiate-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTTP::Headers) >= 6
# Tests only:
BuildRequires:  perl(Test)
BuildRequires:  perl(HTTP::Request)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(HTTP::Headers) >= 6
Conflicts:      perl-libwww-perl < 6

# Remove underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(HTTP::Headers\\)$

%description
This module provides a complete implementation of the HTTP content
negotiation algorithm specified in draft-ietf-http-v11-spec-00.ps chapter
12. Content negotiation allows for the selection of a preferred content
representation based upon attributes of the negotiable variants and the
value of the various Accept* header fields in the request.

%prep
%setup -q -n HTTP-Negotiate-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check


%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Dec 09 2012 Liu Di <liudidi@gmail.com> - 6.01-4
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.01-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 6.01-2
- Perl 5.16 rebuild

* Mon Feb 20 2012 Petr Pisar <ppisar@redhat.com> - 6.01-1
- 6.01 bump

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.00-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 25 2011 Marcela Mašláňová <mmaslano@redhat.com> - 6.00-3
- add new filter

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 6.00-2
- Perl mass rebuild

* Thu Mar 17 2011 Petr Pisar <ppisar@redhat.com> 6.00-1
- Specfile autogenerated by cpanspec 1.78.
- Remove BuildRoot stuff
- Conflicts with perl-libwww-perl-5* and older
