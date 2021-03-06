Name:           perl-Lingua-Stem-Snowball-Da
Version:        1.01
Release:        7%{?dist}
Summary:        Porter's stemming algorithm for Danish
License:        GPLv2
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Lingua-Stem-Snowball-Da/
Source0:        http://www.cpan.org/authors/id/C/CI/CINE/Lingua-Stem-Snowball-Da-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
The stem function takes a scalar as a parameter and stems the word
according to Martin Porter's Danish stemming algorithm, which can be found
at the Snowball website: http://snowball.tartarus.org/.

%prep
%setup -q -n Lingua-Stem-Snowball-Da-%{version}

# for consistency with Snowball-Norwegian and -Swedish
mv stemmer.pl stemmer-da

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

install -D -m 0755 stemmer-da $RPM_BUILD_ROOT/%{_bindir}/stemmer-da

%check


%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_bindir}/*
%{_mandir}/man3/*

%changelog
* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 1.01-7
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 1.01-6
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 15 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.01-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.01-2
- 661697 rebuild for fixing problems with vendorach/lib

* Mon Aug 16 2010 Iain Arnell <iarnell@epo.org> 1.01-1
- Specfile autogenerated by cpanspec 1.78.
