Name:           perl-Symbol-Util
Version:        0.0203
Release:        3%{?dist}
Summary:        Additional utilities for Perl symbols manipulation
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Symbol-Util/
Source0:        http://www.cpan.org/authors/id/D/DE/DEXTER/Symbol-Util-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
This module provides a set of additional functions useful for Perl symbols
manipulation.

%prep
%setup -q -n Symbol-Util-%{version}
chmod -x xt/cover.pl
chmod -x examples/delete_glob.pl

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes examples LICENSE README xt
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0203-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.0203-2
- Perl 5.16 rebuild

* Mon Mar 19 2012 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.0203-1
- Update to 0.0203

* Sun Mar 11 2012 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.0202-9
- Clean up spec file

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0202-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 15 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.0202-7
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0202-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.0202-5
- 661697 rebuild for fixing problems with vendorach/lib

* Tue Jun 22 2010 Petr Pisar <ppisar@redhat.com> - 0.0202-4
- Rebuild against perl-5.12

* Tue May 04 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.0202-3
- Remove perl from BuildRequires.

* Mon May 03 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.0202-2
- Add missing BuildRequires

* Mon Apr 12 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 0.0202-1
- Specfile autogenerated by cpanspec 1.78.
