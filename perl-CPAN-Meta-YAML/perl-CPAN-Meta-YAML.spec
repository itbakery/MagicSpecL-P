# We don't really need ExtUtils::MakeMaker ≥ 6.30
%global old_eumm %(perl -MExtUtils::MakeMaker -e 'print (($ExtUtils::MakeMaker::VERSION < 6.30) ? 1 : 0);' 2>/dev/null || echo 0)

# We need to patch the test suite if we have Test::More < 0.88
%global old_test_more %(perl -MTest::More -e 'print (($Test::More::VERSION < 0.88) ? 1 : 0);' 2>/dev/null || echo 0)

Name:		perl-CPAN-Meta-YAML
Version:	0.005
Release:	3%{?dist}
Summary:	Read and write a subset of YAML for CPAN Meta files
License:	GPL+ or Artistic
Group:		Development/Libraries
URL:		http://search.cpan.org/dist/CPAN-Meta-YAML/
Source0:	http://search.cpan.org/CPAN/authors/id/D/DA/DAGOLDEN/CPAN-Meta-YAML-%{version}.tar.gz
Patch0:		CPAN-Meta-YAML-0.004-old-EU::MM.patch
Patch1:		CPAN-Meta-YAML-0.004-old-Test::More.patch
Patch2:		CPAN-Meta-YAML-0.004-old-Scalar::Util.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(id -nu)
BuildArch:	noarch
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Test::CPAN::Meta)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Pod)
# RHEL <= 6 doesn't have a recent enough perl(version) for perl(Test::Version)
%if 0%{?fedora} || 0%{?rhel} > 6
BuildRequires:	perl(Test::Version)
%endif
BuildRequires:	perl(YAML)
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
This module implements a subset of the YAML specification for use in reading
and writing CPAN metadata files like META.yml and MYMETA.yml. It should not be
used for any other general YAML parsing or generation task.

%prep
%setup -q -n CPAN-Meta-YAML-%{version}

# We don't really need ExtUtils::MakeMaker ≥ 6.30
%if %{old_eumm}
%patch0 -p1
%endif

# We need to patch the test suite if we have Test::More < 0.88
%if %{old_test_more}
%patch1 -p1
%endif

# Fix operation with Scalar::Util < 1.18 properly (CPAN RT#53490)
%patch2 -p1

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
make test TEST_FILES="t/*.t xt/*/*.t"

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc Changes LICENSE README
%{perl_vendorlib}/CPAN/
%{_mandir}/man3/CPAN::Meta::YAML.3pm*

%changelog
* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.005-3
- 为 Magic 3.0 重建

* Tue Jan 10 2012 Paul Howarth <paul@city-fan.org> - 0.005-2
- Fedora 17 mass rebuild

* Tue Dec 13 2011 Paul Howarth <paul@city-fan.org> - 0.005-1
- Update to 0.005:
  - Fix documentation to clarify that users are responsible for UTF-8
    encoding/decoding

* Wed Sep  7 2011 Paul Howarth <paul@city-fan.org> - 0.004-1
- Update to 0.004:
  - Generated from ADAMK/YAML-Tiny-1.50.tar.gz
- BR: perl(Test::Version) for additional test coverage
- Update patch for building with ExtUtils::MakeMaker < 6.30
- Add patch to support building with Test::More < 0.88
- Add patch to fix operation with Scalar::Util < 1.18

* Tue Aug 16 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.003-7
- Install to vendor perl directories to avoid potential debuginfo conflicts
  with the main perl package if this module ever becomes arch-specific

* Wed Jun 29 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.003-6
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.003-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 27 2011 Paul Howarth <paul@city-fan.org> - 0.003-3
- Trim %%description (#672807)

* Wed Jan 26 2011 Paul Howarth <paul@city-fan.org> - 0.003-2
- Sanitize for Fedora submission

* Tue Jan 25 2011 Paul Howarth <paul@city-fan.org> - 0.003-1
- Initial RPM version
