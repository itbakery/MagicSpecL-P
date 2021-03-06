Name:           perl-WWW-Pastebin-PastebinCom-Create
Version:        0.004
Release:        3%{?dist}
Summary:        Paste to http://pastebin.com from Perl
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/WWW-Pastebin-PastebinCom-Create/
Source0:        http://www.cpan.org/authors/id/Z/ZO/ZOFFIX/WWW-Pastebin-PastebinCom-Create-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(LWP::UserAgent) >= 2.036
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::Kwalitee)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(URI) >= 1.35
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
The module provides means of pasting large texts into http://pastebin.com
pastebin site.

%prep
%setup -q -n WWW-Pastebin-PastebinCom-Create-%{version}

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
%doc Changes README examples
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.004-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 23 2012 Petr Pisar <ppisar@redhat.com> - 0.004-2
- Perl 5.16 rebuild

* Fri Jan 06 2012 Iain Arnell <iarnell@gmail.com> 0.004-1
- update to latest upstream version
- clean up spec for modern rpmbuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.003-5
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.003-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 23 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.003-3
- 661697 rebuild for fixing problems with vendorach/lib

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.003-2
- Mass rebuild with perl-5.12.0

* Fri Mar 19 2010 Iain Arnell <iarnell@gmail.com> 0.003-1
- update to latest upstream
- use perl_default_filter

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.002-4
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.002-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Apr 23 2009 Iain Arnell <iarnell@gmail.com> 0.002-2
- add examples as documentation

* Sun Apr 19 2009 Iain Arnell 0.002-1
- Specfile autogenerated by cpanspec 1.77.
