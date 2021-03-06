Name:           perl-Test-HexString
Version:        0.03
Release:        5%{?dist}
Summary:        Test binary strings with hex dump diagnostics
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Test-HexString/
Source0:        http://www.cpan.org/authors/id/P/PE/PEVANS/Test-HexString-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::More)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(Test::Builder)

%{?perl_default_filter}

%description
This testing module provides a single function, is_hexstr(), which asserts
that the given string matches what was expected. When the strings match
(i.e. compare equal using the eq operator), the behaviour is identical to
the usual is() function provided by Test::More.

%prep
%setup -q -n Test-HexString-%{version}


%build
%{__perl} Build.PL installdirs=vendor
./Build


%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*


%check
./Build test


%files
%defattr(-,root,root,-)
%doc Changes LICENSE README
%{perl_vendorlib}/Test
%{_mandir}/man3/Test::HexString*


%changelog
* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.03-5
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 10 2012 Petr Pisar <ppisar@redhat.com> - 0.03-3
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 19 2011 Mathieu Bridon <bochecha@fedoraproject.org> - 0.03-1
- Update to latest upstream release.
- Fix based on Remi's review feedback.

* Thu Sep 15 2011 Mathieu Bridon <bochecha@fedoraproject.org> - 0.02-1
- Specfile autogenerated by cpanspec 1.78.
