Name:           perl-Moo
Version:        1.000004
Release:        2%{?dist}
Summary:        Minimalist Object Orientation (with Moose compatibility)
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Moo/
Source0:        http://search.cpan.org/CPAN/authors/id/M/MS/MSTROUT/Moo-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Class::Method::Modifiers) >= 1.04
BuildRequires:  perl(Devel::GlobalDestruction) >= 0.09
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Module::Runtime) >= 0.012
BuildRequires:  perl(Role::Tiny) >= 1.001003
BuildRequires:  perl(strictures) >= 1.001001
BuildRequires:  perl(Test::Fatal) >= 0.003
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(Class::Method::Modifiers) >= 1.04
Requires:       perl(Role::Tiny) >= 1.001003
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}perl\\(Moo::_
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}perl\\(Moo::_

%description
This module is an extremely light-weight, high-performance Moose
replacement. It also avoids depending on any XS modules to allow simple
deployments. The name Moo is based on the idea that it provides almost -but
not quite- two thirds of Moose.

%prep
%setup -q -n Moo-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check


%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Dec 10 2012 Liu Di <liudidi@gmail.com> - 1.000004-2
- 为 Magic 3.0 重建

* Fri Oct 19 2012 Iain Arnell <iarnell@gmail.com> 1.000004-1
- update to latest upstream version

* Sun Sep 09 2012 Iain Arnell <iarnell@gmail.com> 1.000003-1
- update to latest upstream version

* Sun Jul 29 2012 Iain Arnell <iarnell@gmail.com> 1.000001-1
- update to latest upstream version

* Thu Jul 26 2012 Iain Arnell <iarnell@gmail.com> 1.000000-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jul 20 2012 Iain Arnell <iarnell@gmail.com> 1.000000-1
- update to latest upstream version
- explicity require Role::Tiny >= 1.001003

* Tue Jul 17 2012 Iain Arnell <iarnell@gmail.com> 0.091014-1
- update to latest upstream version

* Sat Jun 23 2012 Petr Pisar <ppisar@redhat.com> - 0.091007-2
- Perl 5.16 rebuild

* Sat May 19 2012 Iain Arnell <iarnell@gmail.com> 0.091007-1
- update to latest upstream version

* Mon Apr 02 2012 Iain Arnell <iarnell@gmail.com> 0.009014-1
- update to latest upstream version

* Fri Jan 06 2012 Iain Arnell <iarnell@gmail.com> 0.009013-1
- update to latest upstream version

* Sun Nov 20 2011 Iain Arnell <iarnell@gmail.com> 0.009012-1
- update to latest upstream version
- filter private requires/provides

* Mon Oct 10 2011 Iain Arnell <iarnell@gmail.com> 0.009011-1
- update to latest upstream version

* Sun Oct 02 2011 Iain Arnell <iarnell@gmail.com> 0.009010-1
- Specfile autogenerated by cpanspec 1.79.
