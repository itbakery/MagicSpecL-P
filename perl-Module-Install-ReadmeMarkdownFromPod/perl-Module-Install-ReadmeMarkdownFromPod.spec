Name:           perl-Module-Install-ReadmeMarkdownFromPod
Version:        0.03
Release:        2%{?dist}
Summary:        Create README.mkdn from POD
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Module-Install-ReadmeMarkdownFromPod/
Source0:        http://www.cpan.org/authors/id/M/MA/MARCEL/Module-Install-ReadmeMarkdownFromPod-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl >= 1:5.6.0
# XXX: We cannot remove ./inc because it build-requires this module
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(CPAN) >= 1.89
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::Command)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::Manifest)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Pod::Parser)
BuildRequires:  perl(Pod::Text)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(URI::Escape)
Requires:       perl(Module::Install)
Requires:       perl(Module::Install::ReadmeFromPod)
Requires:       perl(Pod::Markdown)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Module::Install::ReadmeMarkdownFromPod is a Module::Install extension that
generates a README.mkdn file automatically from an indicated file
containing POD whenever the author runs Makefile.PL. This file is used by
GitHub to display nicely formatted information about a repository.

%prep
%setup -q -n Module-Install-ReadmeMarkdownFromPod-%{version}

# README is ISO-8859-1 encoded
iconv -f iso-8859-1 -t utf8 < README > README.utf8
mv README.utf8 README

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check


%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.03-2
- 为 Magic 3.0 重建

* Tue Jun 26 2012 Jitka Plesnikova <jplesnik@redhat.com> 0.03-1
- Specfile autogenerated by cpanspec 1.78.
