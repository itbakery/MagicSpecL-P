Name:           perl-Catalyst-Plugin-Session-Store-Delegate
Version:        0.06
Release:        5%{?dist}
Summary:        Delegate session storage to an application model object
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Catalyst-Plugin-Session-Store-Delegate/
Source0:        http://www.cpan.org/authors/id/B/BO/BOBTFISH/Catalyst-Plugin-Session-Store-Delegate-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Catalyst::Plugin::Session) >= 0.27
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::Emulate::Class::Accessor::Fast)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::use::ok)
Requires:       perl(Catalyst::Plugin::Session) >= 0.27
Requires:       perl(MooseX::Emulate::Class::Accessor::Fast)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
This store plugins makes delegating session storage to a first class object
model easy.

%prep
%setup -q -n Catalyst-Plugin-Session-Store-Delegate-%{version}

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
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Dec 10 2012 Liu Di <liudidi@gmail.com> - 0.06-5
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.06-4
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.06-3
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep 30 2011 Iain Arnell <iarnell@gmail.com> 0.06-1
- Specfile autogenerated by cpanspec 1.78.
