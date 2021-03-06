Name:		perl-Test-use-ok
Version:	0.11
Release:	2%{?dist}
Summary:	Alternative to Test::More::use_ok
License:	CC0 
Group:		Development/Libraries
URL:		http://search.cpan.org/dist/Test-use-ok/
Source0:	http://search.cpan.org/CPAN/authors/id/A/AU/AUDREYT/Test-use-ok-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(id -nu)
BuildArch:	noarch
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Test::More)
# Requires of bundled library inc::Module::Install
BuildRequires:	perl(Cwd)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::Spec)
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
According to the Test::More documentation, it is recommended to run
use_ok() inside a BEGIN block, so functions are exported at compile-time
and prototypes are properly honored.

However, people often either forget to add "BEGIN", or mistakenly group 
"use_ok" with other tests in a single "BEGIN" block, which can create
subtle differences in execution order.

With this module, simply change all "use_ok" in test scripts to "use ok", 
and they will be executed at "BEGIN" time. The explicit space after "use"
makes it clear that this is a single compile-time action.

%prep
%setup -q -n Test-use-ok-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
%{_fixperms} %{buildroot}

%check


%clean
rm -rf %{buildroot}

%files
%doc Changes README t/
%{perl_vendorlib}/ok.pm
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::use::ok.3pm*
%{_mandir}/man3/ok.3pm*

%changelog
* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.11-2
- 为 Magic 3.0 重建

* Tue Sep 11 2012 Paul Howarth <paul@city-fan.org> - 0.11-1
- Update to 0.11
  - LICENSING CHANGE: this compilation and all individual files in it are now
    under the nullary CC0 1.0 Universal terms:
    To the extent possible under law, 唐鳳 has waived all copyright and
    related or neighboring rights to Test-use-ok
  - Update t/01-basic.t to work with Test::Simple 0.98_02 and later
- License changed from MIT to CC0
- BR: perl(File::Spec)

* Tue Aug 28 2012 Jitka Plesnikova <jplesnik@redhat.com> - 0.02-16
- Specify all dependencies

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.02-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 08 2012 Petr Pisar <ppisar@redhat.com> - 0.02-14
- Perl 5.16 rebuild

* Sun Mar 25 2012 Paul Howarth <paul@city-fan.org> - 0.02-13
- Drop buildreq perl ≥ 0:5.005, satisfied by all Perls in living memory
- Drop redundant buildreq perl(Test::Harness)
- Don't need to remove empty directories from buildroot
- Don't use macros for commands
- Make %%files list more explicit
- Use DESTDIR rather than PERL_INSTALL_ROOT
- Use tabs
- Drop %%defattr, redundant since rpm 4.4

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.02-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.02-11
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.02-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.02-9
- Rebuild to fix problems with vendorarch/lib (#661697)

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.02-8
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.02-7
- Rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.02-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.02-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Mar  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.02-4
- Rebuild for new perl

* Mon Apr 30 2007 Chris Weyl <cweyl@alumni.drew.edu> - 0.02-3
- Bump

* Tue Apr 10 2007 Chris Weyl <cweyl@alumni.drew.edu> - 0.02-2
- Updated with core modules as BR's

* Tue Apr 10 2007 Chris Weyl <cweyl@alumni.drew.edu> - 0.02-1
- Specfile autogenerated by cpanspec 1.70
