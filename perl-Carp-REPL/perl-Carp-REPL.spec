Name:           perl-Carp-REPL
Version:        0.15
Release:        7%{?dist}
Summary:        Read-eval-print-loop on die and/or warn
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Carp-REPL/
Source0:        http://www.cpan.org/authors/id/S/SA/SARTAK/Carp-REPL-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Data::Dump::Streamer)
BuildRequires:  perl(Devel::LexAlias)
BuildRequires:  perl(Devel::REPL)
BuildRequires:  perl(Devel::StackTrace::WithLexicals)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Lexical::Persistence)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(Test::Expect)
BuildRequires:  perl(Test::More)
Requires:       perl(Devel::REPL)
Requires:       perl(Lexical::Persistence)
Requires:       perl(namespace::clean)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# Test::Expect and/or Devel::REPL is failing under mock 1.1.8 in koji
# all is fine locally with mock 1.1.14, though
%bcond_with expect_tests

%{?perl_default_filter}

%description
Carp-REPL is a debugging aid for Perl programs. When a program dies (or warns),
you get a REPL instead of dying or continuing blindly.

%prep
%setup -q -n Carp-REPL-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
# Test::Expect and/or Devel::REPL is failing under mock 1.1.8 in koji
# all is fine locally with mock 1.1.14, though
%if ! %{with expect_tests}
grep -lZ 'Test::Expect' t/*.t |xargs -0 rm -f
%endif


%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.15-7
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.15-6
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.15-5
- 为 Magic 3.0 重建

* Sat Jan 28 2012 Liu Di <liudidi@gmail.com> - 0.15-4
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 04 2011 Iain Arnell <iarnell@gmail.com> 0.15-2
- Test::Expect and/or Devel::REPL fail under mock 1.1.8 in koji
  use --with expect-tests to enable locally

* Fri Sep 30 2011 Iain Arnell <iarnell@gmail.com> 0.15-1
- Specfile autogenerated by cpanspec 1.78.
