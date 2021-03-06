Name:           perl-HTML-TreeBuilder-XPath
Version:        0.14
Release:        6%{?dist}
Summary:        Add XPath support to HTML::TreeBuilder
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/HTML-TreeBuilder-XPath/
Source0:        http://www.cpan.org/authors/id/M/MI/MIROD/HTML-TreeBuilder-XPath-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTML::TreeBuilder)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(XML::XPathEngine) >= 0.12
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?filter_setup:
%filter_from_provides /perl(HTML::Element)/d
%?perl_default_filter}
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(HTML::Element\\)

%description
This module adds typical XPath methods to HTML::TreeBuilder, to make it
easy to query a document.

%prep
%setup -q -n HTML-TreeBuilder-XPath-%{version}

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
* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.14-6
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 14 2012 Petr Pisar <ppisar@redhat.com> - 0.14-4
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep 23 2011 Iain Arnell <iarnell@gmail.com> 0.14-2
- update filtering for compatibility with older filter_setup macros

* Fri Sep 23 2011 Iain Arnell <iarnell@gmail.com> 0.14-1
- update to latest upstream version

* Wed Jun 29 2011 Iain Arnell <iarnell@gmail.com> 0.13-1
- update to latest upstream version

* Fri Jun 24 2011 Iain Arnell <iarnell@gmail.com> 0.12-5
- update filtering for rpm 4.9 macros

* Fri Jun 24 2011 Iain Arnell <iarnell@gmail.com> 0.12-4
- update filtering for perl-5.12 macros

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.12-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Oct 03 2010 Iain Arnell <iarnell@gmail.com> 0.12-1
- update to latest upstream
- clean up spec for modern rpmbuild

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.11-4
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.11-3
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 23 2009 Iain Arnell <iarnell@gmail.com> 0.11-1
- update to latest upstream

* Tue May 05 2009 Iain Arnell 0.10-1
- Specfile autogenerated by cpanspec 1.77.
