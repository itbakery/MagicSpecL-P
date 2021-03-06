Name:           perl-autovivification
Version:        0.10
Release:        4%{?dist}
Summary:        Lexically disable autovivification
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/autovivification/
Source0:        http://search.cpan.org/CPAN/authors/id/V/VP/VPIT/autovivification-%{version}.tar.gz
BuildRequires:  perl >= 0:5.008003
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Kwalitee)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::Portability::Files)
BuildRequires:  perl(XSLoader)
Requires:       perl(XSLoader)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
When an undefined variable is dereferenced, it gets silently upgraded to an
array or hash reference (depending of the type of the dereferencing). This
behavior is called autovivification and usually does what you mean (e.g.
when you store a value) but it's sometimes unnatural or surprising because
your variables gets populated behind your back. This is especially true
when several levels of dereferencing are involved, in which case all levels
are vivified up to the last, or when it happens in intuitively read-only
constructs like exists.

%prep
%setup -q -n autovivification-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check


%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/autovivification*
%{_mandir}/man3/*

%changelog
* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.10-4
- 为 Magic 3.0 重建

* Sat Jan 28 2012 Liu Di <liudidi@gmail.com> - 0.10-3
- 为 Magic 3.0 重建

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Aug 28 2011 Iain Arnell <iarnell@gmail.com> 0.10-1
- update to latest upstream version

* Thu Aug 11 2011 Iain Arnell <iarnell@gmail.com> 0.09-1
- Specfile autogenerated by cpanspec 1.78.
