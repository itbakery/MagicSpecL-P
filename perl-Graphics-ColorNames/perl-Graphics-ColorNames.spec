Name:           perl-Graphics-ColorNames
Version:        2.11
Release:        12%{?dist}
Summary:        Defines RGB values for common color names
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Graphics-ColorNames/
Source0:        http://www.cpan.org/authors/id/R/RR/RRWO/Graphics-ColorNames-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(Color::Library) >= 0.02
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Load) >= 0.10
BuildRequires:  perl(Module::Loaded)
BuildRequires:  perl(Pod::Readme) >= 0.09
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Pod) >= 1
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::Portability::Files)
# Not in Fedora (yet)
# BuildRequires:  perl(Tie::Sub)
Requires:       perl(Module::Load) >= 0.10
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module provides a common interface for obtaining the RGB values of
colors by standard names. The intention is to (1) provide a common module
that authors can use with other modules to specify colors by name; and (2)
free module authors from having to "re-invent the wheel" whenever they
decide to give the users the option of specifying a color by name rather
than RGB value.

%prep
%setup -q -n Graphics-ColorNames-%{version}
%{__perl} -pi -e 's/\r//g' Changes README

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
rm -rf $RPM_BUILD_ROOT

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
DEVEL_TESTS=1 ./Build test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 2.11-12
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.11-10
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 17 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.11-8
- 661697 rebuild for fixing problems with vendorach/lib

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.11-7
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 2.11-6
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Mar 07 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.11-3
- disable BR on Tie::Sub (optional, and not in Fedora yet)

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.11-2
- Rebuild for new perl

* Mon Jan 28 2008 Steven Pritchard <steve@kspei.com> 2.11-1
- Update to 2.11.
- BR Color::Library, Module::Loaded, Test::Exception, and Tie::Sub.

* Mon Jan 07 2008 Steven Pritchard <steve@kspei.com> 2.04-1
- Update to 2.04.
- Update License tag.
- Drop Pod::Coverage and Test::Prereq BR.
- BR Pod::Readme, Test::Pod::Coverage, and Test::Portability::Files.
- Update description.
- Enable DEVEL_TESTS tests.

* Tue Apr 17 2007 Steven Pritchard <steve@kspei.com> 1.06-4
- Use fixperms macro instead of our own chmod incantation.
- Use the __perl macro.

* Sat Sep 16 2006 Steven Pritchard <steve@kspei.com> 1.06-3
- Fix find option order.

* Fri Jun 02 2006 Steven Pritchard <steve@kspei.com> 1.06-2
- Rebuild.

* Fri Mar 24 2006 Steven Pritchard <steve@kspei.com> 1.06-1
- Specfile autogenerated by cpanspec 1.64.
- Drop some explicit Requires.
- Drop explicit BR: perl.
- dos2unix Changes and README.
