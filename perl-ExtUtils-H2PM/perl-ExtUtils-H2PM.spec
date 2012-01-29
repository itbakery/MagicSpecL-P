Name:           perl-ExtUtils-H2PM
Version:        0.08
Release:        4%{?dist}
Summary:        Automatically generate perl modules to wrap C header files
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/ExtUtils-H2PM/
Source0:        http://www.cpan.org/authors/id/P/PE/PEVANS/ExtUtils-H2PM-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(ExtUtils::CBuilder)

%{?perl_default_filter}

%description
This module assists in generating wrappers around system functionality,
such as socket() types or ioctl() calls, where the only interesting
features required are the values of some constants or layouts of structures
normally only known to the C header files. Rather than writing an entire XS
module just to contain some constants and pack/unpack functions, this
module allows the author to generate, at module build time, a pure perl
module containing constant declarations and structure utility functions.
The module then requires no XS module to be loaded at run time.


%prep
%setup -q -n ExtUtils-H2PM-%{version}


%build
%{__perl} Build.PL installdirs=vendor
./Build


%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*


%check
./Build test


%files
%defattr(-,root,root,-)
%doc Changes LICENSE README
%{perl_vendorlib}/ExtUtils
%{_mandir}/man3/ExtUtils::H2PM*


%changelog
* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.08-4
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 19 2011 Mathieu Bridon <bochecha@fedoraproject.org> 0.08-2
- Remove the --optimize build option as per Remi's suggestion.

* Mon Sep 19 2011 Mathieu Bridon <bochecha@fedoraproject.org> 0.08-1
- Update to latest upstream release.
- Fixed a few things based on Remi's review feedback.

* Mon Sep 12 2011 Mathieu Bridon <bochecha@fedoraproject.org> 0.07-1
- Specfile autogenerated by cpanspec 1.78.
- Slightly tweaked the specfile (removed buildroot lines, made noarch)
