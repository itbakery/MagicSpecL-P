Name:           perl-File-PathList
Version:        1.04
Release:        6%{?dist}
Summary:        Find a file within a set of paths (like @INC or Java classpaths)
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/File-PathList/
Source0:        http://www.cpan.org/authors/id/A/AD/ADAMK/File-PathList-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(File::Spec) >= 0.80
BuildRequires:  perl(File::Spec::Unix)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Params::Util) >= 0.24
# Tests only:
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Test::More) >= 0.47
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(File::Spec) >= 0.80
Requires:       perl(Params::Util) >= 0.24

# Remove underspecified dependencies
# RPM 4.8 style:
%filter_from_requires /^perl(File::Spec)\s*$/d
%filter_from_requires /^perl(Params::Util)\s*$/d
%filter_setup
# RPM 4.9 style:
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(File::Spec\\)\\s*$
%global __requires_exclude %__requires_exclude|^perl\\(Params::Util\\)\\s*$


%description
Many systems that map generic relative paths to absolute paths do so with a
set of base paths. For example, perl itself when loading classes first turn
a "Class::Name" into a path like "Class/Name.pm", and then looks through each
element of @INC to find the actual file. To aid in portability, all relative
paths are provided as UNIX-style relative paths, and converted to the
localized version in the process of looking up the path.

%prep
%setup -q -n File-PathList-%{version}

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
%defattr(-,root,root,-)
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Dec 09 2012 Liu Di <liudidi@gmail.com> - 1.04-6
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 1.04-5
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul 25 2011 Petr Pisar <ppisar@redhat.com> - 1.04-3
- RPM 4.9 dependency filtering added

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.04-2
- Perl mass rebuild

* Thu Mar 24 2011 Petr Pisar <ppisar@redhat.com> 1.04-1
- Specfile autogenerated by cpanspec 1.78.
- Remove BuildRoot stuff
- Enhance description
