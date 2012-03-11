Name:           perl-Task-Weaken
Version:        1.04
Release:        2%{?dist}
Summary:        Ensure that a platform has weaken support
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Task-Weaken/
Source0:        http://www.cpan.org/authors/id/A/AD/ADAMK/Task-Weaken-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec) >= 0.80
BuildRequires:  perl(Scalar::Util) >= 1.14
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

Requires:       perl(Scalar::Util) >= 1.14

%description
One recurring problem in modules that use Scalar::Util's weaken function is
that it is not present in the pure-perl variant.

This restores the functionality testing to a dependency you do once in
your Makefile.PL, rather than something you have to write extra tests
for each time you write a module.

%prep
%setup -q -n Task-Weaken-%{version}

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
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct 09 2011 Iain Arnell <iarnell@gmail.com> 1.04-1
- update to latest upstream version
- explicity require perl(Scalar::Util)

* Thu Jun 16 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.02-11
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.02-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.02-9
- 661697 rebuild for fixing problems with vendorach/lib

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.02-8
- Mass rebuild with perl-5.12.0

* Tue Feb  9 2010 Stepan Kasal <skasal@redhat.com> - 1.02-7
- fix the license tag

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.02-6
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.02-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.02-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jun 07 2008 Caolán McNamara <caolanm@redhat.com> 1.02-3
- rebuild for dependancies

* Fri Mar 28 2008 Simon Wilkinson <simon@sxw.org.uk> 1.02-2
- Fix license tag

* Thu Mar 27 2008 Simon Wilkinson <simon@sxw.org.uk> 1.02-1
- Specfile autogenerated by cpanspec 1.73.
