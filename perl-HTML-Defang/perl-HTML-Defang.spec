Name:           perl-HTML-Defang
Version:        1.04
Release:        6%{?dist}
Summary:        Cleans HTML and CSS of executable contents
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/HTML-Defang/
Source0:        http://www.cpan.org/authors/id/K/KU/KURIANJA/HTML-Defang-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module accepts an input HTML and/or CSS string and removes any
executable code including scripting, embedded objects, applets, etc., and
neutralises any XSS attacks. A whitelist based approach is used which means
only HTML known to be safe is allowed through.

%prep
%setup -q -n HTML-Defang-%{version}

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
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Dec 09 2012 Liu Di <liudidi@gmail.com> - 1.04-6
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 1.04-5
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.04-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 06 2011 Iain Arnell <iarnell@gmail.com> 1.04-1
- update to latest upstream version
- clean up spec for modern rpmbuild

* Fri Dec 17 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.03-2
- 661697 rebuild for fixing problems with vendorach/lib

* Tue Jun 15 2010 Iain Arnell <iarnell@gmail.com> 1.03-1
- update to latest upstream

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.02-3
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.02-2
- rebuild against perl 5.10.1

* Sat Aug 29 2009 Iain Arnell <iarnell@gmail.com> 1.02-1
- update to latest upstream version

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 10 2009 Iain Arnell 1.01-1
- Specfile autogenerated by cpanspec 1.77.
