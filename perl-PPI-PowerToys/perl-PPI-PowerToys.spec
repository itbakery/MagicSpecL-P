Name:           perl-PPI-PowerToys
Version:        0.14
Release:        7%{?dist}
Summary:        Handy collection of small PPI-based utilities
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/PPI-PowerToys/
Source0:        http://www.cpan.org/authors/id/A/AD/ADAMK/PPI-PowerToys-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find::Rule) >= 0.30
BuildRequires:  perl(File::Find::Rule::Perl) >= 0.03
BuildRequires:  perl(File::Spec) >= 0.80
BuildRequires:  perl(Getopt::Long) >= 2.36
BuildRequires:  perl(PPI::Document) >= 1.201
BuildRequires:  perl(version) >= 0.74
# Tests only:
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(IPC::Run3) >= 0.034
BuildRequires:  perl(Probe::Perl) >= 0.01
BuildRequires:  perl(Test::More) >= 0.47
BuildRequires:  perl(Test::Script) >= 1.03
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# Remove underspecified dependecies in RPM 4.8 filter
%{?perl_default_filter:
%filter_from_requires /^perl(File::Find::Rule)\s*$/d
%filter_from_requires /^perl(File::Find::Rule::Perl)\s*$/d
%filter_from_requires /^perl(File::Spec)\s*$/d
%filter_from_requires /^perl(Getopt::Long)\s*$/d
%filter_from_requires /^perl(PPI::Document)\s*$/d
%filter_from_requires /^perl(version)\s*$/d
%perl_default_filter
}
# RPM 4.9 filter style
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(File::Find::Rule\\)\\s*$
%global __requires_exclude %__requires_exclude|perl\\(File::Find::Rule::Perl\\)\\s*$
%global __requires_exclude %__requires_exclude|perl\\(File::Spec\\)\\s*$
%global __requires_exclude %__requires_exclude|perl\\(Getopt::Long\\)\\s*$
%global __requires_exclude %__requires_exclude|perl\\(PPI::Document\\)\\s*$
%global __requires_exclude %__requires_exclude|perl\\(version\\)\\s*$

%description
The PPI PowerToys are a small collection of utilities for working with Perl
files, modules and distributions.

%prep
%setup -q -n PPI-PowerToys-%{version}

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
%doc Changes LICENSE README
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Dec 09 2012 Liu Di <liudidi@gmail.com> - 0.14-7
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 19 2012 Petr Pisar <ppisar@redhat.com> - 0.14-5
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul 25 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.14-3
- add new filter for rpm 4.9

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.14-2
- Perl mass rebuild

* Fri Jun 17 2011 Petr Pisar <ppisar@redhat.com> 0.14-1
- Specfile autogenerated by cpanspec 1.78.
- Remove BuildRoot and defattr
