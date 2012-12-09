Name:           perl-Convert-Bencode_XS
Version:        0.06
Release:        6%{?dist}
Summary:        Faster conversions to/from Bencode format
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Convert-Bencode_XS/
Source0:        http://www.cpan.org/authors/id/I/IW/IWADE/Convert-Bencode_XS-%{version}.tar.gz
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
This module provides two functions, bencode and bdecode, which encode and
decode bencoded strings respectively.

%prep
%setup -q -n Convert-Bencode_XS-%{version}

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
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Convert*
%{_mandir}/man3/*

%changelog
* Sun Dec 09 2012 Liu Di <liudidi@gmail.com> - 0.06-6
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.06-5
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.06-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 15 2011 Iain Arnell <iarnell@gmail.com> 0.06-1
- Specfile autogenerated by cpanspec 1.78.
