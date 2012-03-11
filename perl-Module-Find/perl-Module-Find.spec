Name:		perl-Module-Find
Version:	0.10
Release:	4%{?dist}
Summary:	Find and use installed modules in a (sub)category
Group:		Development/Libraries
License:	GPL+ or Artistic
URL:		http://search.cpan.org/dist/Module-Find/
Source0:	http://search.cpan.org/CPAN/authors/id/C/CR/CRENZ/Module-Find-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(id -nu)
BuildArch:	noarch
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Pod::Perldoc)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Pod::Coverage)
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
Module::Find lets you find and use modules in categories. This can be very
useful for auto-detecting driver or plug-in modules. You can differentiate
between looking in the category itself or in all subcategories.

%prep
%setup -q -n Module-Find-%{version}

# Generate Changes file from POD
perldoc -t Find.pm |
	perl -n -e 'if (/^HISTORY/ ... !/^[[:space:]]/) { print if /^[[:space:]]/ }' > Changes

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
%doc Changes README examples/
%{perl_vendorlib}/Module/
%{_mandir}/man3/Module::Find.3pm*

%changelog
* Wed Jan 25 2012 Paul Howarth <paul@city-fan.org> - 0.10-4
- BR: perl(ExtUtils::MakeMaker), perl(File::Find), perl(File::Spec) and
  perl(Pod::Perldoc)
- Use DESTDIR rather than PERL_INSTALL_ROOT
- Use search.cpan.org source URL
- Don't use macros for commands
- Use tabs

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.10-2
- Perl mass rebuild

* Tue Mar 15 2011 Paul Howarth <paul@city-fan.org> - 0.10-1
- Update to 0.10:
  - Fixed META.yml generation (CPAN RT#38302)
  - Removed Unicode BOM from Find.pm (CPAN RT#55010)
- Generate Changes file from POD in Find.pm

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.08-4
- Rebuild to fix problems with vendorarch/lib (#661697)

* Mon May 03 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.08-3
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.08-2
- Rebuild against perl 5.10.1

* Wed Oct  7 2009 Stepan Kasal <skasal@redhat.com> - 0.08-1
- New upstream version

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul 02 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.06-1
- Update to 0.06
- Add examples/

* Fri Feb  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.05-2
- Rebuild for new perl

* Tue Dec 19 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.05-1
- First build
