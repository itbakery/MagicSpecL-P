Name:           perl-Classic-Perl
Version:        0.04
Release:        3%{?dist}
Summary:        Selectively reinstate deleted Perl features
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Classic-Perl/
Source0:        http://www.cpan.org/authors/id/S/SP/SPROUT/Classic-Perl-%{version}.tar.gz
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(XSLoader)

%{?perl_default_filter}

%description
Classic::Perl restores some Perl features that have been deleted in the
latest versions. By 'classic' we mean as of perl 5.8.x.

%prep
%setup -q -n Classic-Perl-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Classic*
%{_mandir}/man3/*

%changelog
* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.04-3
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 26 2011 Petr Pisar <ppisar@redhat.com> - 0.04-1
- 0.04 bump

* Tue Sep 20 2011 Petr Pisar <ppisar@redhat.com> - 0.03-1
- 0.03 bump

* Mon Aug 22 2011 Petr Pisar <ppisar@redhat.com> 0.02-0.1.a
- Specfile autogenerated by cpanspec 1.78.
- Move `alpha' version substring to release tag.
- Remove BuildRoot and defattr spec code.
