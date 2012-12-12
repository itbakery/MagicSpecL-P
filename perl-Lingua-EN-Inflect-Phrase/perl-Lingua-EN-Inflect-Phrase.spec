Name:           perl-Lingua-EN-Inflect-Phrase
Version:        0.12
Release:        3%{?dist}
Summary:        Inflect short English Phrases
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Lingua-EN-Inflect-Phrase/
Source0:        http://www.cpan.org/authors/id/R/RK/RKITOVER/Lingua-EN-Inflect-Phrase-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Lingua::EN::Inflect) >= 1.891
BuildRequires:  perl(Lingua::EN::Inflect::Number) >= 1.1
BuildRequires:  perl(Lingua::EN::Tagger) >= 0.15
BuildRequires:  perl(Test::More) >= 0.94
Requires:       perl(Lingua::EN::Inflect) >= 1.891
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%?perl_default_filter

%description
Attempts to pluralize or singularize short English phrases.

%prep
%setup -q -n Lingua-EN-Inflect-Phrase-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check


%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.12-3
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.12-2
- 为 Magic 3.0 重建

* Fri Jan 20 2012 Iain Arnell <iarnell@gmail.com> 0.12-1
- update to latest upstream version

* Thu Jan 05 2012 Iain Arnell <iarnell@gmail.com> 0.11-1
- update to latest upstream version

* Tue Oct 18 2011 Iain Arnell <iarnell@gmail.com> 0.10-1
- update to latest upstream version

* Fri Oct 14 2011 Iain Arnell <iarnell@gmail.com> 0.08-1
- update to latest upstream version
- use perl_default_filter and DESTDIR

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.04-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Aug 16 2010 Iain Arnell <iarnell@epo.org> 0.04-1
- Specfile autogenerated by cpanspec 1.78.
