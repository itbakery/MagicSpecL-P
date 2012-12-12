Name:           perl-Spiffy
Version:        0.30
Release:        21%{?dist}
Summary:        Framework for doing object oriented (OO) programming in Perl
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Spiffy/
Source0:        http://www.cpan.org/authors/id/I/IN/INGY/Spiffy-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Filter::Util::Call)
BuildRequires:  perl(lib)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(YAML)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# Filter bogus provide of perl(DB) (rpm < 4.9)
%global provfilt /bin/sh -c "%{__perl_provides} | sed -e '/^perl(DB)$/d'"
%define __perl_provides %{provfilt}

# Equivalent filter for rpm 4.9 onwards
%global __provides_exclude ^perl\\(DB\\)

%description
"Spiffy" is a framework and methodology for doing object oriented (OO)
programming in Perl. Spiffy combines the best parts of Exporter.pm,
base.pm, mixin.pm and SUPER.pm into one magic foundation class. It attempts
to fix all the nits and warts of traditional Perl OO, in a clean,
straightforward and (perhaps someday) standard way.

%prep
%setup -q -n Spiffy-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

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
%{perl_vendorlib}/Spiffy.pm
%{_mandir}/man3/Spiffy.3pm*

%changelog
* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.30-21
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.30-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.30-19
- Perl 5.16 rebuild
- Specify all dependencies

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.30-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.30-17
- Perl mass rebuild

* Tue Apr 19 2011 Paul Howarth <paul@city-fan.org> - 0.30-16
- Make the provides filter work with rpm 4.9 too

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.30-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.30-14
- Rebuild to fix problems with vendorarch/lib (#661697)

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.30-13
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.30-12
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.30-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.30-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 02 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.30-9
- rebuild for new perl

* Wed Jan 02 2008 Ralf Corsépius <rc040203@freenet.de> 0.30-8
- Adjust License-tag.
- BR: perl(Test::More) (BZ 419631).

* Wed Apr 18 2007 Steven Pritchard <steve@kspei.com> 0.30-7
- Use fixperms macro instead of our own chmod incantation.
- BR ExtUtils::MakeMaker.

* Mon Sep 04 2006 Steven Pritchard <steve@kspei.com> 0.30-6
- Rework spec to look more like current cpanspec output.

* Tue Feb 28 2006 Steven Pritchard <steve@kspei.com> 0.30-5
- Improve filter.

* Mon Feb 27 2006 Steven Pritchard <steve@kspei.com> 0.30-4
- Drop dummy mixin.pm.

* Mon Feb 27 2006 Steven Pritchard <steve@kspei.com> 0.30-3
- Filter out Provides: perl(DB).

* Mon Feb 27 2006 Steven Pritchard <steve@kspei.com> 0.30-2
- Drop explicit Provides: mixin.
- Add dummy mixin.pm.
- Improve Summary.
- Fix Source0.

* Sat Feb 25 2006 Steven Pritchard <steve@kspei.com> 0.30-1
- Update to 0.30.
- Drop explicit perl BR.

* Wed Dec 28 2005 Steven Pritchard <steve@kspei.com> 0.24-1
- Specfile autogenerated.
