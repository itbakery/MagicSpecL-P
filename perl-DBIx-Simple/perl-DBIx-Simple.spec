Name:           perl-DBIx-Simple
Summary:        Easy-to-use OO interface to DBI
Version:        1.35
Release:        7%{?dist}
License:        Public Domain
Group:          Development/Libraries
Source0:        http://search.cpan.org/CPAN/authors/id/J/JU/JUERD/DBIx-Simple-%{version}.tar.gz 
URL:            http://search.cpan.org/dist/DBIx-Simple/
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildArch:      noarch

BuildRequires:  perl(DBI) >= 1.21
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
Requires:       perl(DBI) >= 1.21


%{?perl_default_filter}

%description
DBIx::Simple provides a simplified interface to DBI, Perl's powerful
database module.

%prep
%setup -q -n DBIx-Simple-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 1.35-7
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.35-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 16 2012 Petr Pisar <ppisar@redhat.com> - 1.35-5
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.35-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.35-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan  6 2011 Marcela Mašláňová <mmaslano@redhat.com> 1.35-1
- update to 1.35 
- incompatible change: RaiseError is now enabled by default

* Wed Jan 05 2011 Marcela Mašláňová <mmaslano@redhat.com> 1.34-1
- update by Fedora::App::MaintainerTools 0.006
- updating to latest GA CPAN version (1.34)
- replaced old BR on perl(Test::Simple) with Test::More
- added a new req on perl(DBI) (version 1.21)

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.32-6
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.32-5
- Mass rebuild with perl-5.12.0

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.32-4
- Mass rebuild with perl-5.12.0

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.32-3
- Mass rebuild with perl-5.12.0

* Fri Jan 15 2010 Stepan Kasal <skasal@redhat.com> - 1.32-2
- rebuild against perl 5.10.1

* Wed Aug 12 2009 Marcela Mašláňová <mmaslano@redhat.com> 1.32-1
- Specfile autogenerated by cpanspec 1.78.
