Name:           perl-B-Utils
Version:        0.17
Release:        3%{?dist}
Summary:        Helper functions for op tree manipulation
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/B-Utils/
Source0:        http://www.cpan.org/authors/id/J/JJ/JJORE/B-Utils-%{version}.tar.gz

BuildRequires:  perl(B)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::Depends) >= 0.302
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(subs)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(vars)
Requires:       perl(List::Util)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
Helper functions for op tree manipulation.

%prep
%setup -q -n B-Utils-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check


%files
%defattr(-,root,root,-)
%doc Changes LICENSE README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/B*
%{_mandir}/man3/*

%changelog
* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.17-3
- 为 Magic 3.0 重建

* Sat Jan 28 2012 Liu Di <liudidi@gmail.com> - 0.17-2
- 为 Magic 3.0 重建

* Thu Jan 05 2012 Iain Arnell <iarnell@gmail.com> 0.17-1
- update to latest upstream version

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.15-2
- Perl mass rebuild

* Wed Apr 20 2011 Iain Arnell <iarnell@gmail.com> 0.15-1
- update to latest upstream version

* Sun Mar 20 2011 Iain Arnell <iarnell@gmail.com> 0.14-1
- update to latest upstream version

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb 04 2011 Iain Arnell <iarnell@gmail.com> 0.13-1
- update to latest upstream version
- clean up spec for modern rpmbuild
- tweak buildrequires

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.11-3
- 661697 rebuild for fixing problems with vendorach/lib

* Thu Apr 29 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.11-2
- Mass rebuild with perl-5.12.0

* Thu Jan 14 2010 Iain Arnell <iarnell@gmail.com> 0.11-1
- update to latest upstream version

* Mon Jan 04 2010 Iain Arnell <iarnell@gmail.com> 0.10-1
- update to latest upstream version

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.08-2
- rebuild against perl 5.10.1

* Wed Sep 02 2009 Iain Arnell <iarnell@gmail.com> 0.08-1
- update to latest upstream
- use perl_default_filter 

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 08 2008 Iain Arnell <iarnell@gmail.com> 0.07-2
- BR Test::Signature

* Fri Dec 05 2008 Iain Arnell 0.07-1
- Specfile autogenerated by cpanspec 1.77.
