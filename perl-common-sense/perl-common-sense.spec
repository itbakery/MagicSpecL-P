Name:		perl-common-sense
Summary:	"Common sense" Perl defaults 
Version:	3.4
Release:	5%{?dist}
License:	GPL+ or Artistic
Group:		Development/Libraries
Source0:	http://search.cpan.org/CPAN/authors/id/M/ML/MLEHMANN/common-sense-%{version}.tar.gz 
URL:		http://search.cpan.org/dist/common-sense
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(id -nu)
BuildArch:	noarch
BuildRequires:	perl(ExtUtils::MakeMaker)
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

# Obsolete/provide old -tests subpackage (can be removed in F19 development cycle)
Obsoletes:	%{name}-tests < %{version}-%{release}
Provides:	%{name}-tests = %{version}-%{release}

%description
This module implements some sane defaults for Perl programs, as defined
by two typical (or not so typical - use your common sense) specimens of
Perl coders:

  use strict qw(vars subs);
  use feature qw(say state switch);
  no warnings;

%prep
%setup -q -n common-sense-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} \; 2>/dev/null
%{_fixperms} %{buildroot}

%check
make test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE Changes README t/
%{perl_vendorlib}/common/
%{_mandir}/man3/common::sense.3pm*

%changelog
* Sat Jan 21 2012 Paul Howarth <paul@city-fan.org> - 3.4-5
- Obsolete/provide old -tests subpackage to support upgrades

* Thu Jan 19 2012 Paul Howarth <paul@city-fan.org> - 3.4-4
- Reinstate compatibility with older distributions like EL-5
- Drop -tests subpackage (general lack of interest in this), but include
  them as documentation for the main package
- Don't use macros for commands
- Make %%files list more explicit
- Use tabs

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 3.4-2
- Perl mass rebuild

* Sat May 07 2011 Iain Arnell <iarnell@gmail.com> - 3.4-1
- Update to latest upstream version

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Dec 18 2010 Iain Arnell <iarnell@gmail.com> 3.3-1
- Update to latest upstream version
- Clean up spec for modern rpmbuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 3.0-3
- Rebuild to fix problems with vendorarch/lib (#661697)

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 3.0-2
- Mass rebuild with perl-5.12.0

* Sun Mar 14 2010 Chris Weyl <cweyl@alumni.drew.edu> - 3.0-1
- Update by Fedora::App::MaintainerTools 0.006
- PERL_INSTALL_ROOT => DESTDIR
- Updating to latest GA CPAN version (3.0)

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 1.0-3
- Rebuild against perl 5.10.1

* Sun Sep 27 2009 Chris Weyl <cweyl@alumni.drew.edu> - 1.0-2
- Update summary (though now we deviate from upstream)

* Mon Aug 31 2009 Chris Weyl <cweyl@alumni.drew.edu> - 1.0-1
- Auto-update to 1.0 (by cpan-spec-update 0.01)

* Fri Aug 21 2009 Chris Weyl <cweyl@alumni.drew.edu> - 0.04-0
- Initial RPM packaging
- Generated with cpan2dist (CPANPLUS::Dist::RPM version 0.0.8)
