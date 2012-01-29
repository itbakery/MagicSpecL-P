Name:           perl-Devel-CheckLib
Version:        0.95
Release:        3%{?dist}
Summary:        Check that a library is available

License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Devel-CheckLib/
Source0:        http://www.cpan.org/modules/by-module/Devel/Devel-CheckLib-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::CaptureOutput) >= 1.0801
BuildRequires:  perl(Test::More) >= 0.62

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Devel::CheckLib is a perl module that checks whether a particular C library
and its headers are available.

%prep
%setup -q -n Devel-CheckLib-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc CHANGES README
%{_bindir}/*
%{perl_vendorlib}/Devel*
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3*

%changelog
* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.95-3
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.95-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct 23 2011 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.95-1
- Update to 0.95.

* Wed Oct 19 2011 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.94-1
- First build.
