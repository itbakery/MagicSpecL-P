Name:           perl-Data-ObjectDriver
Version:        0.09
Release:        6%{?dist}
Summary:        Simple, transparent data interface, with caching
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Data-ObjectDriver/
Source0:        http://search.cpan.org/CPAN/authors/id/S/SI/SIXAPART/Data-ObjectDriver-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(DBI)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(Class::Data::Inheritable)
BuildRequires:  perl(Class::Trigger)
Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}
%global __requires_exclude_from %{?__requires_exclude_from:%__requires_exclude_from|}%{perl_vendorlib}/Data/ObjectDriver/Driver/DBD/Oracle.pm

%description
Data::ObjectDriver is an object relational mapper, meaning that it maps object-
oriented design concepts onto a relational database.

%prep
%setup -q -n Data-ObjectDriver-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check



%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.09-6
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.09-5
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Iain Arnell <iarnell@gmail.com> 0.09-3
- update filtering for rpm 4.9
- clean up spec for modern rpmbuild

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.09-2
- Perl mass rebuild

* Sun May 08 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.09-1
- Update to 0.09

* Sun Feb 13 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.08-3
- Add perl default filter
- Filter the Oracle stuff

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 07 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.08-1
- Update to 0.08

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.07-2
- Mass rebuild with perl-5.12.0

* Mon Mar 30 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.07-1
- Update to 0.07, dropping upstreamed patch

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.06-5
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Apr 16 2009 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 0.06-3
- Re-enable auto-Requires, for real this time
- Add DBD::SQLite to the BuildRequires
- Patch t/02-basic.t to pass on sqlite 3.5.9

* Wed Apr 15 2009 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 0.06-2
- Re-enable auto-Requires
- Exclude DBD::Oracle from them

* Sun Apr 11 2009 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 0.06-1
- Use Module::Install calls rather than ./Build.PL ones
- run tests in the check section
- clean up Requires
- Update to 0.06

* Mon Dec 29 2008 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 0.05-1
- Specfile autogenerated by cpanspec 1.77.
