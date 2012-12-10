Name:           perl-Array-Utils
Version:        0.5
Release:        6%{?dist}
Summary:        Small utils for array manipulation
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Array-Utils/
Source0:        http://www.cpan.org/authors/id/Z/ZM/ZMIJ/Array/Array-Utils-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
A small pure-perl module containing list manipulation routines,
to avoid code duplication, idioms.


%prep
%setup -q -n Array-Utils-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*


%check



%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Mon Dec 10 2012 Liu Di <liudidi@gmail.com> - 0.5-6
- 为 Magic 3.0 重建

* Sat Jan 28 2012 Liu Di <liudidi@gmail.com> - 0.5-5
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.5-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 30 2010 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> 0.5-1
- Rebase to a later release

* Fri Nov 26 2010 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> 0.3-2
- Add Test::More BR
- Tidy up

* Thu Jul 17 2008 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> 0.3-1
- Specfile autogenerated by cpanspec 1.75.
