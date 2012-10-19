Name:           perl-Perl-Critic-Deprecated
Version:        1.108
Release:        6%{?dist}
Summary:        Perl::Critic policies which have been superseded by others
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Perl-Critic-Deprecated/
Source0:        http://www.cpan.org/authors/id/E/EL/ELLIOTJS/Perl-Critic-Deprecated-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Perl::Critic::Policy) >= 1.094
BuildRequires:  perl(Perl::Critic::TestUtils) >= 1.094
BuildRequires:  perl(Perl::Critic::Utils) >= 1.094
BuildRequires:  perl(PPI::Node)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Test::More)
# Tests only
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(Perl::Critic::TestUtils)
BuildRequires:  perl(Test::Pod::Coverage)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(Perl::Critic::Policy) >= 1.094
Requires:       perl(Perl::Critic::Utils) >= 1.094

# Filter underspecified dependecies
# RPM 4.8 style:
%filter_from_requires /^perl(Perl::Critic::Policy)$/d
%filter_from_requires /^perl(Perl::Critic::Utils)$/d
%filter_setup
# RPM 4.9 style:
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Perl::Critic::Policy\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Perl::Critic::Utils\\)$

%description
The included policies are:
  - Write "$my_variable = 42" instead of "$MyVariable = 42".
  - Write "sub my_function{}" instead of "sub MyFunction{}".

%prep
%setup -q -n Perl-Critic-Deprecated-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.108-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 20 2012 Petr Pisar <ppisar@redhat.com> - 1.108-5
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.108-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 26 2011 Petr Pisar <ppisar@redhat.com> - 1.108-3
- RPM 4.9 dependency filtering added

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 1.108-2
- Perl mass rebuild

* Wed Mar 02 2011 Petr Pisar <ppisar@redhat.com> 1.108-1
- Specfile autogenerated by cpanspec 1.78.
- Summary shortened
- Remove BuildRoot stuff
