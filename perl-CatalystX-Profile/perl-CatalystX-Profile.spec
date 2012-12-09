Name:           perl-CatalystX-Profile
Version:        0.02
Release:        5%{?dist}
Summary:        Profile your Catalyst application with Devel::NYTProf
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/CatalystX-Profile/
Source0:        http://www.cpan.org/authors/id/J/JJ/JJNAPIORK/CatalystX-Profile-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Catalyst::Runtime) >= 5.80020
BuildRequires:  perl(CatalystX::InjectComponent) >= 0.024
BuildRequires:  perl(Devel::NYTProf) >= 3.01
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Moose) >= 0.93
BuildRequires:  perl(namespace::autoclean) >= 0.09
BuildRequires:  perl(Sub::Identify) >= 0.04
BuildRequires:  perl(Test::More)
Requires:       perl(Catalyst::Runtime) >= 5.80020
Requires:       perl(CatalystX::InjectComponent) >= 0.024
Requires:       perl(Devel::NYTProf) >= 3.01
Requires:       perl(Moose) >= 0.93
Requires:       perl(namespace::autoclean) >= 0.09
Requires:       perl(Sub::Identify) >= 0.04
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
This (really basic for now) plugin adds support for profiling your Catalyst
application, without profiling all the crap that happens during setup. This
noise can make finding the real profiling stuff trickier, so profiling is
disabled while this happens.

%prep
%setup -q -n CatalystX-Profile-%{version}

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
%doc LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Dec 09 2012 Liu Di <liudidi@gmail.com> - 0.02-5
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.02-4
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.02-3
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep 30 2011 Iain Arnell <iarnell@gmail.com> 0.02-1
- Specfile autogenerated by cpanspec 1.78.
