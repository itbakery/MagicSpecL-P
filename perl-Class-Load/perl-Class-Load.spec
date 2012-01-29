Name:		perl-Class-Load
Version:	0.13
Release:	4%{?dist}
Summary:	A working (require "Class::Name") and more
Group:		Development/Libraries
License:	GPL+ or Artistic
URL:		http://search.cpan.org/dist/Class-Load/
Source0:	http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/Class-Load-%{version}.tar.gz
BuildArch:	noarch
# ===================================================================
# Module build requirements
# ===================================================================
BuildRequires:	perl(ExtUtils::MakeMaker)
# ===================================================================
# Module requirements
# ===================================================================
BuildRequires:	perl(Data::OptList)
BuildRequires:	perl(Module::Runtime) >= 0.011
BuildRequires:	perl(Package::Stash) >= 0.32
BuildRequires:	perl(Try::Tiny)
# ===================================================================
# Regular test suite requirements
# ===================================================================
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Without::Module)
BuildRequires:	perl(version)
# ===================================================================
# Author/Release test requirements
# ===================================================================
BuildRequires:	perl(Test::EOL)
BuildRequires:	perl(Test::NoTabs)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Pod::Coverage)
BuildRequires:	perl(Test::Spelling), aspell-en
BuildRequires:	perl(Test::Requires)
BuildRequires:	perl(Pod::Coverage::Moose)
BuildRequires:	perl(Test::CPAN::Changes)
# ===================================================================
# Runtime requirements
# ===================================================================
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:	perl(Module::Runtime) >= 0.011
Requires:	perl(Package::Stash) >= 0.32
# Also requires core module perl(Exporter) via a "use base" construct

%description
require EXPR only accepts Class/Name.pm style module names, not Class::Name.
How frustrating! For that, we provide load_class 'Class::Name'.

It's often useful to test whether a module can be loaded, instead of throwing
an error when it's not available. For that, we provide
try_load_class 'Class::Name'.

Finally, sometimes we need to know whether a particular class has been loaded.
Asking %%INC is an option, but that will miss inner packages and any class for
which the filename does not correspond to the package name. For that, we
provide is_class_loaded 'Class::Name'.

%prep
%setup -q -n Class-Load-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} ';' 2>/dev/null
%{_fixperms} %{buildroot}

%check
 RELEASE_TESTING=1

%files
%doc Changes LICENSE README
%{perl_vendorlib}/Class/
%{_mandir}/man3/Class::Load.3pm*

%changelog
* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.13-4
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.13-3
- 为 Magic 3.0 重建

* Tue Jan 10 2012 Paul Howarth <paul@city-fan.org> - 0.13-2
- Fedora 17 mass rebuild

* Thu Dec 22 2011 Paul Howarth <paul@city-fan.org> - 0.13-1
- Update to 0.13:
  - Fix some bugs with our use of Try::Tiny, which could cause warnings on some
    systems where Class::Load::XS wasn't installed (CPAN RT#72345)
- BR: perl(Test::Without::Module)

* Tue Oct 25 2011 Paul Howarth <paul@city-fan.org> - 0.12-1
- Update to 0.12:
  - Require Module::Runtime ≥ 0.011, which fixes problems with Catalyst under
    Perl 5.8 and 5.10
- Add versioned runtime dependencies for Module::Runtime and Package::Stash

* Wed Oct  5 2011 Paul Howarth <paul@city-fan.org> - 0.11-1
- Update to 0.11:
  - Don't accept package names that start with a digit
  - Rewrite some of the guts to use Module::Runtime rather than reimplementing
    its functionality
- BR: perl(Module::Runtime) ≥ 0.009
- Drop all support for older distributions as required module
  Module::Runtime ≥ 0.009 will not be available prior to F-16

* Tue Sep  6 2011 Paul Howarth <paul@city-fan.org> - 0.10-1
- Update to 0.10:
  - Fix is_class_loaded to ignore $ISA (but still look for @ISA) when trying to
    determine whether a class is loaded
  - Lots of internals cleanup
- BR: perl(Package::Stash) ≥ 0.32 and perl(Try::Tiny)
- Update patches to apply cleanly

* Tue Aug 16 2011 Paul Howarth <paul@city-fan.org> - 0.08-1
- Update to 0.08:
  - The previous version was missing a prereq declaration for Data::OptList
    (CPAN RT#70285)
- This release by DROLSKY -> update source URL
- Package new documentation: LICENSE and README
- Add build requirements for new release tests and run them:
  - perl(Pod::Coverage::Moose)
  - perl(Test::CPAN::Changes)
  - perl(Test::EOL)
  - perl(Test::NoTabs)
  - perl(Test::Pod)
  - perl(Test::Pod::Coverage)
  - perl(Test::Requires)
  - perl(Test::Spelling) and aspell-en
- Add patch for building with ExtUtils::MakeMaker < 6.30
- Add patch for building with Test::More < 0.88
- Add patch for building without Test::Requires
- Add patch for fixing spell checker word list
- Don't try to run the POD Coverage test if we don't have Pod::Coverage::Moose

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.06-5
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Paul Howarth <paul@city-fan.org> - 0.06-3
- Drop explicit dependency on core module perl(Exporter) (#656408)

* Tue Nov 23 2010 Paul Howarth <paul@city-fan.org> - 0.06-2
- Sanitize spec for Fedora submission

* Mon Nov 22 2010 Paul Howarth <paul@city-fan.org> - 0.06-1
- Initial RPM version
