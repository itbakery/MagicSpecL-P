Name:           perl-DBIx-Class-Cursor-Cached
Version:        1.001002
Release:        4%{?dist}
Summary:        Cursor class with built-in caching support
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/DBIx-Class-Cursor-Cached/
Source0:        http://www.cpan.org/authors/id/A/AR/ARCANEZ/DBIx-Class-Cursor-Cached-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl >= 1:5.8.1
BuildRequires:  perl(Cache::FileCache)
BuildRequires:  perl(Carp::Clan) >= 6.0
BuildRequires:  perl(DBD::SQLite) >= 1.25
BuildRequires:  perl(DBIx::Class) >= 0.08124
BuildRequires:  perl(DBIx::Class::Core)
BuildRequires:  perl(DBIx::Class::Schema)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
Requires:       perl(Carp::Clan) >= 6.0
Requires:       perl(DBIx::Class) >= 0.08124
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?filter_setup:
%filter_from_requires /perl(Carp::Clan)$/d
}
%?perl_default_filter
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(Carp::Clan\\)$

%description
This module provides a DBIx cursor class with built-in caching support.

%prep
%setup -q -n DBIx-Class-Cursor-Cached-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor --skipdeps
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check


%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Dec 10 2012 Liu Di <liudidi@gmail.com> - 1.001002-4
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 1.001002-3
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.001002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Aug 27 2011 Iain Arnell <iarnell@gmail.com> 1.001002-1
- update to latest upstream version

* Thu Jul 21 2011 Iain Arnell <iarnell@gmail.com> 1.001001-3
- update filtering for rpm 4.9

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 1.001001-2
- Perl mass rebuild

* Thu Mar 31 2011 Iain Arnell <iarnell@gmail.com> 1.001001-1
- update to latest upstream version

* Wed Mar 16 2011 Iain Arnell <iarnell@gmail.com> 1.001000-3
- use skipdeps for Module::AutoInstall

* Mon Mar 14 2011 Iain Arnell <iarnell@gmail.com> 1.001000-2
- R/BR perl(DBIx::Class) >= 0.8124 to avoid test failures

* Sun Mar 13 2011 Iain Arnell <iarnell@gmail.com> 1.001000-1
- Specfile autogenerated by cpanspec 1.79.
