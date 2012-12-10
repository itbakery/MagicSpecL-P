Name:           perl-Catalyst-ActionRole-ACL
Version:        0.06
Release:        6%{?dist}
Summary:        User role-based authorization action class
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Catalyst-ActionRole-ACL/
Source0:        http://www.cpan.org/authors/id/B/BO/BOBTFISH/Catalyst-ActionRole-ACL-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Catalyst::Controller::ActionRole)
BuildRequires:  perl(Catalyst::Runtime)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Moose)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Test::More)
Requires:       perl(Catalyst::Controller::ActionRole)
Requires:       perl(Catalyst::Runtime)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
Provides a Catalyst reusable action role for user role-based authorization.
ACLs are applied via the assignment of attributes to application action
subroutines.

%prep
%setup -q -n Catalyst-ActionRole-ACL-%{version}

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
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Dec 10 2012 Liu Di <liudidi@gmail.com> - 0.06-6
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.06-5
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.06-4
- 为 Magic 3.0 重建

* Sat Jan 28 2012 Liu Di <liudidi@gmail.com> - 0.06-3
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep 30 2011 Iain Arnell <iarnell@gmail.com> 0.06-1
- Specfile autogenerated by cpanspec 1.78.
