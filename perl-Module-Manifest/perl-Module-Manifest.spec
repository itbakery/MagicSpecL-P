Name:           perl-Module-Manifest
Version:        1.08
Release:        9%{?dist}
Summary:        Parse and examine a Perl distribution MANIFEST file
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Module-Manifest/
Source0:        http://www.cpan.org/authors/id/A/AD/ADAMK/Module-Manifest-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(inc::Module::Install::DSL) >= 0.99
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(File::Spec) >= 0.80
BuildRequires:  perl(File::Spec::Unix)
BuildRequires:  perl(Params::Util) >= 0.10
# Tests:
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Test::Exception) >= 0.27
BuildRequires:  perl(Test::More) >= 0.42
BuildRequires:  perl(Test::Warn) >= 0.11
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(File::Spec) >= 0.80
Requires:       perl(Params::Util) >= 0.10

# Do not export under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((File::Spec|Params::Util)\\)

%description
Module::Manifest can load a MANIFEST file that comes in a Perl distribution
tarball, examine the contents, and perform some simple tasks. It can also load
the MANIFEST.SKIP file and check that.

%prep
%setup -q -n Module-Manifest-%{version}
chmod -x examples/*
# Remove bundled modules
rm -rf inc/*

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check


%files
%doc Changes LICENSE README examples
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 1.08-9
- 为 Magic 3.0 重建

* Thu Aug 09 2012 Petr Pisar <ppisar@redhat.com> - 1.08-8
- Modernize spec file
- Specify all dependencies

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 14 2012 Petr Pisar <ppisar@redhat.com> - 1.08-6
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 1.08-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.08-2
- 661697 rebuild for fixing problems with vendorach/lib

* Thu Sep 16 2010 Petr Pisar <ppisar@redhat.com> - 1.08-1
- 1.08 bump

* Mon May 03 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.07-2
- Mass rebuild with perl-5.12.0

* Tue Apr 20 2010 Petr Pisar <ppisar@redhat.com> - 0.07-1
- version bump
- new Test::Exception and Test::Warn BuildRequires
- explicit perl-File-Spec >= 0.80 run-time dependency version
- add examples

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.03-4
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Sep 24 2008 Marcela Mašláňová <mmaslano@redhat.com> 0.03-1
- Specfile autogenerated by cpanspec 1.77.
