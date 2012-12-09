Name:           perl-Catalyst-Plugin-I18N
Version:        0.10
Release:        8%{?dist}
Summary:        I18N for Catalyst
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Catalyst-Plugin-I18N/
Source0:        http://search.cpan.org/CPAN/authors/id/B/BO/BOBTFISH/Catalyst-Plugin-I18N-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(Catalyst::Runtime)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Locale::Maketext::Lexicon)
BuildRequires:  perl(Locale::Maketext::Simple) >= 0.19
BuildRequires:  perl(MRO::Compat) >= 0.10
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
# not automatically detected
Requires:       perl(Locale::Maketext::Lexicon)

%{?perl_default_filter}

%description
Supports mo/po files and Maketext classes under your applications I18N
namespace.

%prep
%setup -q -n Catalyst-Plugin-I18N-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
TEST_POD=1 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Dec 09 2012 Liu Di <liudidi@gmail.com> - 0.10-8
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.10-7
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.10-6
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.10-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.10-2
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Jun 18 2010 Iain Arnell <iarnell@gmail.com> 0.10-1
- update to latest upstream
- use perl_default_filter and DESTDIR
- update buildrequires

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.09-5
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.09-4
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 24 2009 Iain Arnell <iarnell@gmail.com> 0.09-2
- add missing requires perl(Locale::Maketext::Lexicon)

* Wed Apr 22 2009 Iain Arnell <iarnell@gmail.com> 0.09-1
- update to 0.09
- BR perl(MRO::Compat) and perl(Test::Pod::Coverage)

* Wed Feb 25 2009 Iain Arnell <iarnell@gmail.com> 0.08-2
- remove unecessary requires/buildrequires

* Sun Feb 22 2009 Iain Arnell 0.08-1
- Specfile autogenerated by cpanspec 1.77.
- enable pod tests
