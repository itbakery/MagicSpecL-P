Name:		perl-Test-Distribution
Version:	2.00
Release:	14%{?dist}
Summary:	Perform tests on all modules of a distribution
License:	GPL+ or Artistic
Group:		Development/Libraries
URL:		http://search.cpan.org/dist/Test-Distribution/
Source0:	http://search.cpan.org/CPAN/authors/id/S/SR/SRSHAH/Test-Distribution-%{version}.tar.gz
Patch0:		Test-Distribution-2.00-utf8.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(id -nu)
BuildArch:	noarch
BuildRequires:	perl(ExtUtils::Manifest)
BuildRequires:	perl(File::Find::Rule) >= 0.03
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Module::CoreList) >= 1.93
BuildRequires:	perl(Pod::Coverage) >= 0.17
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Pod) >= 0.95
BuildRequires:	perl(Test::Pod::Coverage)
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
# these are considered "optional"; autoreq doesn't pick them up
Requires:	perl(File::Find::Rule) >= 0.03
Requires:	perl(Module::CoreList) >= 1.93
Requires:	perl(Module::Signature)
Requires:	perl(Pod::Coverage) >= 0.17
Requires:	perl(Test::Pod) >= 0.95
Requires:	perl(Test::Pod::Coverage)

%description
When using this module in a test script, it goes through all the modules in
your distribution, checks their POD, checks that they compile OK and checks
that they all define a $VERSION.

%prep
%setup -q -n Test-Distribution-%{version}

# Fix character encoding of documentation
%patch0

%build
perl Build.PL installdirs=vendor
./Build

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}

%check
./Build test

%clean
rm -rf %{buildroot}

%files
%doc Changes.pod README
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::Distribution.3pm*

%changelog
* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 2.00-14
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.00-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 2.00-12
- Perl 5.16 rebuild

* Sat Mar 10 2012 Paul Howarth <paul@city-fan.org> - 2.00-11
- BR:perl(ExtUtils::Manifest) and perl(Test::More)
- Drop workarounds for no-longer-shipped signature test
- Drop BR: perl(Module::Signature)
- Don't need to remove empty directories from buildroot
- Don't use macros for commands
- Drop %%defattr, redundant since rpm 4.4
- Make %%files list more explicit
- Use tabs

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.00-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 24 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.00-9
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.00-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.00-7
- Rebuild to fix problems with vendorarch/lib (#661697)

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.00-6
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 2.00-5
- Rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.00-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.00-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Oct 26 2008 Chris Weyl <cweyl@alumni.drew.edu> - 2.00-2
- Changes -> Changes.pod in doc

* Sun Oct 26 2008 Chris Weyl <cweyl@alumni.drew.edu> - 2.00-1
- Update to 2.00

* Wed Mar  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.26-5
- Rebuild for new perl

* Sat Mar 10 2007 Chris Weyl <cweyl@alumni.drew.edu> - 1.26-4
- Don't mess with debuginfo, just disable it
- Appease Module::Signature/gpg

* Thu Mar 01 2007 Chris Weyl <cweyl@alumni.drew.edu> - 1.26-3
- Cause rm to not fail on non-existance of debug*list in %%check

* Wed Dec 06 2006 Chris Weyl <cweyl@alumni.drew.edu> - 1.26-2
- Bump

* Wed Dec 06 2006 Chris Weyl <cweyl@alumni.drew.edu> - 1.26-1
- Specfile autogenerated by cpanspec 1.69.1
