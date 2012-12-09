Name:           perl-Devel-Caller
Version:        2.05
Release:        10%{?dist}
Summary:        Meatier versions of caller
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Devel-Caller/
Source0:        http://www.cpan.org/authors/id/R/RC/RCLAMP/Devel-Caller-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(PadWalker) >= 0.08
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# Don't provide Caller.so or perl(DB)
# RPM 4.8 style
%{?filter_setup:
%filter_from_provides /^perl(DB)/d
}
# RPM 4.9 style
%{?perl_default_filter}
%global __provides_exclude %{?__provides_exclude:__provides_exclude|}^perl\\(DB\\)

%description
Devel::Caller - Meatier versions of caller.

%prep
%setup -q -n Devel-Caller-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes
%{perl_vendorarch}/auto/Devel/
%{perl_vendorarch}/Devel/
%{_mandir}/man3/Devel::Caller.3pm*

%changelog
* Sun Dec 09 2012 Liu Di <liudidi@gmail.com> - 2.05-10
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 2.05-9
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.05-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul 25 2011 Iain Arnell <iarnell@gmail.com> 2.05-7
- provides_exclude needs to come after perl_default_filter

* Mon Jul 25 2011 Petr Pisar <ppisar@redhat.com> - 2.05-6
- RPM 4.9 dependency filtering added

* Sun Jun 19 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.05-5
- Perl mass rebuild

* Tue Apr 19 2011 Paul Howarth <paul@city-fan.org> - 2.05-4
- Filter bogus provides Caller.so and perl(DB)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.05-2
- Rebuild to fix problems with vendorarch/lib (#661697)

* Sat Jun 05 2010 Iain Arnell <iarnell@gmail.com> 2.05-1
- update to latest upstream (required for Devel::LexAlias)
- re-enable tests

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.03-8
- Mass rebuild with perl-5.12.0

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.03-7
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 2.03-6
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.03-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.03-3
- Rebuild for new perl

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.03-2
- Autorebuild for GCC 4.3

* Mon Jan 28 2008 Steven Pritchard <steve@kspei.com> 2.03-1
- Update to 2.03.

* Wed Jan 02 2008 Steven Pritchard <steve@kspei.com> 2.02-1
- Update to 2.02.
- Update License tag.
- Drop README.
- Switch to using ExtUtils::MakeMaker build instead of Module::Build.
- BR Test::More.

* Thu Feb 01 2007 Steven Pritchard <steve@kspei.com> 0.11-1
- Specfile autogenerated by cpanspec 1.69.1.
- "Fix" description.
- Remove explicit dependency on PadWalker.
