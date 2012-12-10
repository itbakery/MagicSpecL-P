Name:           perl-Test-TinyMocker
Version:        0.03
Release:        5%{?dist}
Summary:        A very simple tool to mock external modules
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Test-TinyMocker/
Source0:        http://www.cpan.org/authors/id/S/SU/SUKRIA/Test-TinyMocker-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(base)  
BuildRequires:  perl(Carp)  
BuildRequires:  perl(Exporter)  
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Pod::Coverage)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
This module allows you to override methods with arbitrary code blocks. This lets
you simulate some kind of behavior for your tests.

%prep
%setup -q -n Test-TinyMocker-%{version}

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
%doc AUTHORS Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Dec 10 2012 Liu Di <liudidi@gmail.com> - 0.03-5
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 0.03-3
- Perl 5.16 rebuild

* Wed Mar 28 2012 Iain Arnell <iarnell@gmail.com> 0.03-2
- remove explicit Test::More dependency
- remove ignore.txt from docs

* Sat Feb 11 2012 Iain Arnell <iarnell@gmail.com> 0.03-1
- Specfile autogenerated by cpanspec 1.79.
