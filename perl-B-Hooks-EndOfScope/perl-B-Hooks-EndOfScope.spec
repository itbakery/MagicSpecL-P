Name:		perl-B-Hooks-EndOfScope
Version:	0.09
Release:	2%{?dist}
License:	GPL+ or Artistic
Group:		Development/Libraries
Summary:	Execute code after scope compilation finishes
Url:		http://search.cpan.org/dist/B-Hooks-EndOfScope
Source:		http://search.cpan.org/CPAN/authors/id/F/FL/FLORA/B-Hooks-EndOfScope-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(id -nu)
BuildArch:	noarch
# Build
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.31
# Module
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl(Variable::Magic) >= 0.34
# Test suite
BuildRequires:	perl(Test::More)
# Release tests
BuildRequires:	perl(Pod::Coverage::TrustPod)
BuildRequires:	perl(Test::Pod) >= 1.41
BuildRequires:	perl(Test::Pod::Coverage) >= 1.08
# Runtime
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
This module allows you to execute code when Perl has finished compiling the
surrounding scope.

%prep
%setup -q -n B-Hooks-EndOfScope-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} ';' 2>/dev/null
%{_fixperms} %{buildroot}

%check
make test RELEASE_TESTING=1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc Changes README t/
%{perl_vendorlib}/B/
%{_mandir}/man3/B::Hooks::EndOfScope.3pm*

%changelog
* Sat Jan 28 2012 Liu Di <liudidi@gmail.com> - 0.09-2
- 为 Magic 3.0 重建

* Tue Jan 17 2012 Paul Howarth <paul@city-fan.org> - 0.09-1
- Update to 0.09 (improve distribution metadata)
- Run release tests too
- BR: perl(Pod::Coverage::TrustPod), perl(Test::Pod) and
  perl(Test::Pod::Coverage) for release tests
- Spec clean-up:
  - Make %%files list more explicit
  - Use DESTDIR rather than PERL_INSTALL_ROOT
  - Use tabs
  - Split buildreqs by Build/Module/Tests/Release tests

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.08-7
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.08-5
- Rebuild to fix problems with vendorarch/lib (#661697)

* Thu Apr 29 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.08-4
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.08-3
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 17 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.08-1
- auto-update to 0.08 (by cpan-spec-update 0.01)
- altered br on perl(ExtUtils::MakeMaker) (0 => 6.42)
- altered br on perl(Variable::Magic) (0.31 => 0.34)

* Sun Mar 08 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.07-1
- update to 0.07

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 08 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.04-1
- update for submission

* Sat Nov 08 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.04-0.1
- initial RPM packaging
- generated with cpan2dist (CPANPLUS::Dist::RPM version 0.0.5)
