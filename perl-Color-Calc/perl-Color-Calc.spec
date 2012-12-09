Name:           perl-Color-Calc
Version:        1.072
Release:        5%{?dist}
Summary:        Simple calculations with RGB colors
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Color-Calc/
Source0:        http://www.cpan.org/authors/id/C/CF/CFAERBER/Color-Calc-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Graphics::ColorNames)
BuildRequires:  perl(Graphics::ColorNames::WWW)
BuildRequires:  perl(Params::Validate)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Pod)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
The Color::Calc module implements simple calculations with RGB colors. This
can be used to create a full color scheme from a few colors.

%prep
%setup -q -n Color-Calc-%{version}
iconv --from=ISO-8859-1 --to=UTF-8 README > README.utf-8
mv README.utf-8 README


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check


%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Dec 09 2012 Liu Di <liudidi@gmail.com> - 1.072-5
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 1.072-4
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 1.072-3
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.072-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec  9 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 1.072-1
- Update to 1.072
- Spec clean up

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 1.071-2
- Perl mass rebuild

* Mon Mar 07 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 1.071-1
- Update to 1.071

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.070-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct 21 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 1.070-1
- Update to 1.070

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.061-2
- Mass rebuild with perl-5.12.0

* Thu Feb 11 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 1.061-1
- Update to 1.061

* Fri Jan  1 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 1.060-1
- Update to 1.060

* Tue Dec 14 2009 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 1.052-1
- Update to 1.052

* Sun Dec 13 2009 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 1.051-1
- Update to 1.051

* Mon Oct 05 2009 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 1.05-1
- Specfile autogenerated by cpanspec 1.78.
