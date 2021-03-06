Name:           perl-Alien-SeleniumRC
Version:        2.90
Release:        4%{?dist}
Summary:        Packages the Selenium Remote Control server
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Alien-SeleniumRC/
Source0:        http://search.cpan.org/CPAN/authors/id/H/HI/HISSO/Alien-SeleniumRC-%{version}.tar.gz
Patch0:         Alien-Selenium-system-jar.diff
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       selenium-server

%{?perl_default_filter}

%description
Selenium Remote Control is a test tool that allows you to write automated
web application UI tests in any programming language against any HTTP
website using any mainstream JavaScript-enabled browser. It provides a
Selenium Server, which can automatically start/stop/control any supported
browser. It works by using Selenium Core, a pure-HTML+JS library that
performs automated tasks in JavaScript.

%prep
%setup -q -n Alien-SeleniumRC-%{version}
%patch0 -p0
rm t/seleniumrc.t
rm lib/Alien/SeleniumRC/selenium-server.jar

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
%{_bindir}/selenium-rc
%{_mandir}/man3/*

%changelog
* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 2.90-4
- 为 Magic 3.0 重建

* Fri Jan 27 2012 Liu Di <liudidi@gmail.com> - 2.90-3
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Oct 27 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 2.90-1
- Update to 2.90

* Fri Oct 14 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 2.81-1
- Update to 2.81
- Drop perl(CPAN) from the BuildRequires (not needed).

* Wed Oct 12 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 2.80-1
- Update to 2.80
- Clean up spec-file

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.03-7
- Perl mass rebuild

* Thu Jun 09 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.03-6
- Perl 5.14 mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 14 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.03-4
- 661697 rebuild for fixing problems with vendorach/lib

* Sun May 23 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 1.03-3
- Remove selenium-server.jar from the archive
- Remove test on the internal selenium-server
- Tell Alien::SeleniumRC to use the system selenium server
- Add selenium-server to the Requires

* Thu Apr 29 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.03-2
- Mass rebuild with perl-5.12.0

* Sat Feb 27 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 1.03-1
- Update to 1.03
- Change Source0 URL
- Add Perl default filter

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.01-2
- rebuild against perl 5.10.1

* Tue Sep 15 2009 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 1.01-1
- Update to 1.01

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 14 2009 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 1.00-1
- Update to 1.00

* Wed Nov 05 2008 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 0.91-2
- Specfile autogenerated by cpanspec 1.77.
