Name:           perl-Catalyst-Engine-Apache
Version:        1.16
Release:        8%{?dist}
Summary:        Catalyst Apache Engines
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Catalyst-Engine-Apache/
Source0:        http://www.cpan.org/authors/id/F/FL/FLORA/Catalyst-Engine-Apache-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Catalyst::Runtime)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
Requires:       perl(Catalyst::Runtime)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
These classes provide mod_perl support for Catalyst.

%prep
%setup -q -n Catalyst-Engine-Apache-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

# remove MP13 and MP19 as they are not used in Fedora
find %{buildroot} -type f -name '*MP13.*' -exec rm -f {} \;
find %{buildroot} -type f -name '*MP19.*' -exec rm -f {} \;

%{_fixperms} %{buildroot}/*

%check


%files
%defattr(-,root,root,-)
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Dec 10 2012 Liu Di <liudidi@gmail.com> - 1.16-8
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 1.16-7
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 1.16-6
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 1.16-5
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 1.16-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct 07 2010 Iain Arnell <iarnell@gmail.com> 1.16-1
- update to latest upstream
- clean up spec for modern rpmbuild

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.12-6
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.12-5
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Nov 13 2008 Iain Arnell <iarnell@gmail.com> 1.12-2
- exclude MP13 and MP19

* Mon Sep 15 2008 Iain Arnell <iarnell@gmail.com> 1.12-1
- Specfile autogenerated by cpanspec 1.77.
