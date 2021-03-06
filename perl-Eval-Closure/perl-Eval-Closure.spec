Name:           perl-Eval-Closure
Version:        0.08
Release:        4%{?dist}
Summary:        Safely and cleanly create closures via string eval
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Eval-Closure/
Source0:        http://www.cpan.org/authors/id/D/DO/DOY/Eval-Closure-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(PadWalker)
BuildRequires:  perl(Perl::Tidy)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Output)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Try::Tiny)
Requires:       perl(Perl::Tidy)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
String eval is often used for dynamic code generation. For instance, Moose uses
it heavily, to generate inlined versions of accessors and constructors, which
speeds code up at runtime by a significant amount. String eval is not without
its issues however - it's difficult to control the scope it's used in (which
determines which variables are in scope inside the eval), and it's easy to miss
compilation errors, since eval catches them and sticks them in $@ instead.

This module attempts to solve these problems. It provides an eval_closure
function, which evals a string in a clean environment, other than a fixed list
of specified variables. Compilation errors are rethrown automatically.

%prep
%setup -q -n Eval-Closure-%{version}

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
* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.08-4
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 0.08-2
- Perl 5.16 rebuild

* Fri Feb 10 2012 Iain Arnell <iarnell@gmail.com> 0.08-1
- update to latest upstream version

* Sat Feb 04 2012 Iain Arnell <iarnell@gmail.com> 0.07-1
- update to latest upstream version
- update description

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 29 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.06-2
- Perl mass rebuild

* Tue Jun 07 2011 Iain Arnell <iarnell@gmail.com> 0.06-1
- update to latest upstream version

* Wed May 04 2011 Iain Arnell <iarnell@gmail.com> 0.05-1
- update to latest upstream version

* Wed Apr 20 2011 Iain Arnell <iarnell@gmail.com> 0.04-1
- update to latest upstream version

* Thu Mar 03 2011 Iain Arnell <iarnell@gmail.com> 0.03-1
- update to latest upstream version

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 28 2011 Iain Arnell <iarnell@gmail.com> 0.02-1
- update to latest upstream version

* Sun Jan 23 2011 Iain Arnell <iarnell@gmail.com> 0.01-1
- Specfile autogenerated by cpanspec 1.78.
