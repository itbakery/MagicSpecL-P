Name:		perl-Params-Coerce
Version:	0.14
Release:	14%{?dist}
Summary:	Allows your classes to do coercion of parameters
License:	GPL+ or Artistic
Group:		Development/Libraries
URL:		http://search.cpan.org/dist/Params-Coerce/
Source0:	http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/Params-Coerce-%{version}.tar.gz
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(id -nu)
BuildRequires:	perl(Carp)
BuildRequires:	perl(Params::Util) >= 0.05
BuildRequires:	perl(Scalar::Util) >= 1.11
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Pod) >= 1.00
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
A big part of good API design is that we should be able to be flexible in
the ways that we take parameters. Params::Coerce attempts to encourage this,
by making it easier to take a variety of different arguments, while adding 
negligible additional complexity to your code.

%prep
%setup -q -n Params-Coerce-%{version}

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
 AUTOMATED_TESTING=1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc Changes LICENSE README
%{perl_vendorlib}/Params/
%{_mandir}/man3/Params::Coerce.3pm*

%changelog
* Mon Dec 10 2012 Liu Di <liudidi@gmail.com> - 0.14-14
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 0.14-12
- Perl 5.16 rebuild

* Wed Feb 15 2012 Paul Howarth <paul@city-fan.org> - 0.14-11
- Spec clean-up:
  - Drop redundant perl and perl(ExtUtils::AutoInstall) buildreqs
  - BR: perl(Carp), perl(Scalar::Util) ≥ 1.11, perl(Test::More)
  - Use DESTDIR rather than PERL_INSTALL_ROOT
  - Set AUTOMATED_TESTING=1 to enable Pod test
  - Use search.cpan.org source URL
  - Fix typo in %%description
  - Make %%files list more explicit
  - Don't use macros for commands
  - Use tabs

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.14-9
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.14-7
- Rebuild to fix problems with vendorarch/lib (#661697)

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.14-6
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.14-5
- Rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Mar  4 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.14-2
- Rebuild for new perl

* Sun Oct 15 2006 Chris Weyl <cweyl@alumni.drew.edu> - 0.14-1
- Update to 0.14

* Thu Sep 07 2006 Chris Weyl <cweyl@alumni.drew.edu> - 0.13-2
- Add additional verbosity to %%description 

* Tue Sep 05 2006 Chris Weyl <cweyl@alumni.drew.edu> - 0.13-1
- Specfile autogenerated by cpanspec 1.69.1
