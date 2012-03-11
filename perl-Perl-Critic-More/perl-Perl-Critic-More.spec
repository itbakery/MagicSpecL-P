Name:           perl-Perl-Critic-More
Version:        1.000
Release:        4%{?dist}
Summary:        Supplemental policies for Perl::Critic
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Perl-Critic-More/
Source0:        http://www.cpan.org/authors/id/E/EL/ELLIOTJS/Perl-Critic-More-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Perl::Critic) >= 1.082
BuildRequires:  perl(Perl::MinimumVersion) >= 0.14
BuildRequires:  perl(Readonly) >= 1.03
# Tests:
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Perl::Critic::Config)
BuildRequires:  perl(Perl::Critic::Policy)
BuildRequires:  perl(Perl::Critic::TestUtils)
BuildRequires:  perl(Perl::Critic::Utils)
BuildRequires:  perl(Perl::Critic::Violation)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(Perl::Critic) >= 1.082
Requires:       perl(Perl::MinimumVersion) >= 0.14
Requires:       perl(Readonly) >= 1.03

# Remove underspecified dependencies for RPM 4.8
%filter_from_requires /^perl(Readonly)\s*$/d
%filter_setup
# filter for RPM 4.9
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(Readonly\\)\\s*$

%description
This is a collection of Perl::Critic policies that are not included in the
Perl::Critic core for a variety of reasons.

%prep
%setup -q -n Perl-Critic-More-%{version}

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
%doc Changes LICENSE README TODO.pod
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.000-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 26 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.000-3
- add RPM4.9 macro filter

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 1.000-2
- Perl mass rebuild

* Thu Mar 24 2011 Petr Pisar <ppisar@redhat.com> 1.000-1
- Specfile autogenerated by cpanspec 1.78.
- Remove BuildRoot stuff
