Name:           perl-DateTime-TimeZone
Version:        1.42
Release:        3%{?dist}
Summary:        Time zone object base class and factory
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/DateTime-TimeZone/
Source0:        http://www.cpan.org/authors/id/D/DR/DROLSKY/DateTime-TimeZone-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(Class::Singleton) >= 1.03
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd) >= 3
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Params::Validate) >= 0.72
BuildRequires:  perl(parent)
BuildRequires:  perl(Pod::Man) >= 1.14
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Output)
# not automatically detected
Requires:       perl(Cwd) >= 3
Requires:       perl(File::Compare)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?filter_setup:
%filter_from_requires /^perl(Win32/d
%if 0%{?perl_bootstrap}
%filter_from_requires /^perl(DateTime\(::Duration\)?)/d
%endif
%?perl_default_filter}

%if 0%{?perl_bootstrap}
# avoid circular dependencies - DateTime strictly requires DateTime::TimeZone
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(DateTime\\)
%global __requires_exclude %{__requires_exclude}|perl\\(DateTime::Duration\\)
# perl-DateTime-TimeZone used to be bundled with perl-DateTime
# when bootstrapping, we can't require the unbundled version, so
# need to conflict with the old package
Conflicts:      perl-DateTime <= 1:0.7000-3.fc16
%else
# explicitly require the unbundled perl-DateTime to avoid implicit conflicts
Requires:       perl-DateTime >= 2:0.70-1
# and BR perl(DateTime) to enable testing
BuildRequires:  perl(DateTime)
%endif

%description
This class is the base class for all time zone objects. A time zone is
represented internally as a set of observances, each of which describes the
offset from GMT for a given time period.

%prep
%setup -q -n DateTime-TimeZone-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check


%files
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 1.42-3
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 09 2011 Iain Arnell <iarnell@gmail.com> 1.42-1
- update to latest upstream - Olson 2011n

* Tue Oct 25 2011 Iain Arnell <iarnell@gmail.com> 1.41-1
- update to latest upstream - Olson 2011m

* Tue Oct 11 2011 Iain Arnell <iarnell@gmail.com> 1.40-1
- update to latest upstream - Olson 2011l

* Tue Sep 27 2011 Iain Arnell <iarnell@gmail.com> 1.39-1
- update to latest upstream - Olson 2011k

* Wed Sep 14 2011 Iain Arnell <iarnell@gmail.com> 1.37-1
- update to latest upstream - Olson 2011j

* Tue Aug 30 2011 Iain Arnell <iarnell@gmail.com> 1.36-1
- update to latest upstream - Olson 2011i

* Thu Aug 18 2011 Iain Arnell <iarnell@gmail.com> 1.35-3
- rebuild against unbunled perl-DateTime

* Mon Aug 15 2011 Iain Arnell <iarnell@gmail.com> 1.35-2
- additional explicit (build)requires for core modules

* Mon Aug 15 2011 Iain Arnell <iarnell@gmail.com> 1.35-1
- Specfile autogenerated by cpanspec 1.78.
- Add bootstrapping logic
