Name:           perl-Devel-PatchPerl
Version:        0.62
Release:        3%{?dist}
Summary:        Patch perl source à la Devel::PPPort's buildperl.pl
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Devel-PatchPerl/
Source0:        http://www.cpan.org/authors/id/B/BI/BINGOS/Devel-PatchPerl-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::pushd) >= 1.00
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IPC::Cmd) >= 0.40
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Test::More)
Requires:       patch
Requires:       perl(File::pushd) >= 1.00
Requires:       perl(IPC::Cmd) >= 0.40
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
Devel::PatchPerl is a modularisation of the patching code contained in
Devel::PPPort's buildperl.pl.

%prep
%setup -q -n Devel-PatchPerl-%{version}

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
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.62-3
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.62-2
- 为 Magic 3.0 重建

* Fri Jan 06 2012 Iain Arnell <iarnell@gmail.com> 0.62-1
- update to latest upstream version

* Mon Oct 31 2011 Iain Arnell <iarnell@gmail.com> 0.60-2
- requires 'patch'

* Fri Oct 28 2011 Iain Arnell <iarnell@gmail.com> 0.60-1
- update to latest upstream version

* Sat Oct 22 2011 Iain Arnell <iarnell@gmail.com> 0.58-1
- update to latest upstream version

* Sat Sep 24 2011 Iain Arnell <iarnell@gmail.com> 0.52-1
- update to latest upstream version

* Sat Aug 13 2011 Iain Arnell <iarnell@gmail.com> 0.48-1
- update to latest upstream version

* Sun Jun 19 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.40-3
- Perl mass rebuild

* Sun Jun 19 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.40-2
- Perl mass rebuild

* Fri Jun 10 2011 Iain Arnell <iarnell@gmail.com> 0.40-1
- update to latest upstream version

* Fri May 27 2011 Iain Arnell <iarnell@gmail.com> 0.36-1
- update to latest upstream version

* Wed Apr 27 2011 Iain Arnell <iarnell@gmail.com> 0.30-1
- Specfile autogenerated by cpanspec 1.78.
