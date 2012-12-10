Name:           perl-Pod-Markdown
Version:        1.320
Release:        4%{?dist}
Summary:        Convert POD to Markdown
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Pod-Markdown/
Source0:        http://www.cpan.org/authors/id/R/RW/RWSTAUNER/Pod-Markdown-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl >= 0:5.008
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(parent)
BuildRequires:  perl(Pod::ParseLink) >= 1.10
BuildRequires:  perl(Pod::Parser)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Script) >= 1.05
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module subclasses Pod::Parser and converts POD to Markdown.

%prep
%setup -q -n Pod-Markdown-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check


%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man[13]/*
%{_bindir}/*

%changelog
* Mon Dec 10 2012 Liu Di <liudidi@gmail.com> - 1.320-4
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.320-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 27 2012 Petr Pisar <ppisar@redhat.com> - 1.320-2
- Perl 5.16 rebuild

* Tue Jun 26 2012 Jitka Plesnikova <jplesnik@redhat.com> 1.320-1
- Specfile autogenerated by cpanspec 1.78.
