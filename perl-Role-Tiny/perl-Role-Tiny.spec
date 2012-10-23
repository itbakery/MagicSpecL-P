Name:           perl-Role-Tiny
Version:        1.002000
Release:        1%{?dist}
Summary:        A nouvelle cuisine portion size slice of Moose
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Role-Tiny/
Source0:        http://www.cpan.org/authors/id/M/MS/MSTROUT/Role-Tiny-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(constant)
BuildRequires:  perl(Class::Method::Modifiers)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Test::Fatal) >= 0.003
BuildRequires:  perl(Test::More) >= 0.96
%if !0%{?perl_bootstrap}
BuildRequires:  perl(Moo)
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# perl-Role-Tiny was split from perl-Moo
Conflicts:      perl-Moo < 0.009014

%{?perl_default_filter}

%description
Role::Tiny is a minimalist role composition tool.

%prep
%setup -q -n Role-Tiny-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Oct 20 2012 Iain Arnell <iarnell@gmail.com> 1.002000-1
- update to latest upstream version

* Sun Jul 29 2012 Iain Arnell <iarnell@gmail.com> 1.001005-1
- update to latest upstream version

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.001004-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 17 2012 Iain Arnell <iarnell@gmail.com> 1.001004-1
- update to latest upstream version

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 1.001002-2
- Perl 5.16 rebuild

* Tue May 08 2012 Iain Arnell <iarnell@gmail.com> 1.001002-1
- update to latest upstream version

* Fri Apr 27 2012 Iain Arnell <iarnell@gmail.com> 1.001001-1
- update to latest upstream version
- don't explicity require Class::Method::Modifiers

* Wed Apr 04 2012 Iain Arnell <iarnell@gmail.com> 1.000001-1
- update to latest upstream version

* Mon Apr 02 2012 Iain Arnell <iarnell@gmail.com> 1.000000-3
- explicitly conflict with perl-Moo < 0.009014; this module used to be
  distributed as part of Moo

* Mon Apr 02 2012 Iain Arnell <iarnell@gmail.com> 1.000000-2
- fix spelling of cuisine in summary

* Sun Apr 01 2012 Iain Arnell <iarnell@gmail.com> 1.000000-1
- Specfile autogenerated by cpanspec 1.79.
