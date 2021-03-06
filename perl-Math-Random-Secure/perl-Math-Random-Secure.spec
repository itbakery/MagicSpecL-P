Name:           perl-Math-Random-Secure
Version:        0.06
Release:        6%{?dist}
Summary:        Cryptographically-secure, cross-platform replacement for rand()
License:        Artistic 2.0
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Math-Random-Secure/
Source0:        http://www.cpan.org/authors/id/M/MK/MKANAT/Math-Random-Secure-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Any::Moose)
BuildRequires:  perl(Crypt::Random::Source::Factory)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Math::Random::ISAAC)
BuildRequires:  perl(Test::LeakTrace)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warn)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
This module is intended to provide a cryptographically-secure replacement
for Perl's built-in rand function.

%prep
%setup -q -n Math-Random-Secure-%{version}

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


%files
%defattr(-,root,root,-)
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.06-6
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.06-5
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.06-3
- Perl mass rebuild

* Sun Feb 27 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.06-2
- Add needed BuildRequires

* Mon Feb 14 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 0.06-1
- Specfile autogenerated by cpanspec 1.78.
