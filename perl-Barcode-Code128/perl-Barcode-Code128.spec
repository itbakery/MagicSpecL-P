name:           perl-Barcode-Code128
Version:        2.01
Release:        9%{?dist}
Summary:        Generate CODE 128 bar codes
License:        Public Domain
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Barcode-Code128/
Source0:        http://www.cpan.org/authors/id/W/WR/WRW/Barcode-Code128-%{version}.tar.gz
Patch0:         perl-Barcode-Code128-testfix.patch
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(GD)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(GD)

%description
Barcode::Code128 generates bar codes using the CODE 128 symbology. It can
generate images in PNG or GIF format using the GD package, or it can
generate a text string representing the barcode that you can render using
some other technology if desired.

%prep
%setup -q -n Barcode-Code128-%{version}
%patch0
rm t/gif.t

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
%{_mandir}/man3/*

%changelog
* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 2.01-9
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 2.01-8
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 2.01-7
- 为 Magic 3.0 重建

* Sat Jan 28 2012 Liu Di <liudidi@gmail.com> - 2.01-6
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.01-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 2.01-4
- Perl mass rebuild

* Tue May 24 2011 Nicholas van Oudtshoorn <vanoudt@gmail.com> 2.01-3
- Simplified the spec file to conform to Fedora guidelines
* Tue May 24 2011 Nicholas van Oudtshoorn <vanoudt@gmail.com> 2.01-2
- Added build and run-time dependency on perl(GD)
* Thu Apr 28 2011 Nicholas van Oudtshoorn <vanoudt@gmail.com> 2.01-1
- Specfile autogenerated by cpanspec 1.78.
- Disable tests since they are broken

