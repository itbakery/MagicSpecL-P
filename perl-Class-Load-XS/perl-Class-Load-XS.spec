#TODO: BR: Test::Pod::No404s when available
#TODO: BR: Test::Pod::LinkCheck when available

Name:		perl-Class-Load-XS
Version:	0.03
Release:	3%{?dist}
Summary:	XS implementation of parts of Class::Load
Group:		Development/Libraries
License:	Artistic 2.0
URL:		http://search.cpan.org/dist/Class-Load-XS/
Source0:	http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/Class-Load-XS-%{version}.tar.gz
# ===================================================================
# Module build requirements
# ===================================================================
BuildRequires:	perl(Module::Build)
# ===================================================================
# Module requirements
# ===================================================================
BuildRequires:	perl(Class::Load) >= 0.11
# ===================================================================
# Regular test suite requirements
# ===================================================================
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Test::More)
# ===================================================================
# Author/Release test requirements
# ===================================================================
BuildRequires:	perl(Test::CPAN::Changes)
BuildRequires:	perl(Test::EOL)
BuildRequires:	perl(Test::NoTabs)
BuildRequires:	perl(Test::Pod)
# ===================================================================
# Runtime requirements
# ===================================================================
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:	perl(Class::Load) >= 0.11

%{?perl_default_filter}

%description
This module provides an XS implementation for portions of Class::Load.
See Class::Load for API details.

%prep
%setup -q -n Class-Load-XS-%{version}

%build
perl Build.PL installdirs=vendor optimize="%{optflags}"
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} ';' 2>/dev/null
%{_fixperms} %{buildroot}

%check
RELEASE_TESTING=1 ./Build test

%files
%doc Changes LICENSE README
%{perl_vendorarch}/auto/Class/
%{perl_vendorarch}/Class/
%{_mandir}/man3/Class::Load::XS.3pm*

%changelog
* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.03-3
- 为 Magic 3.0 重建

* Tue Jan 10 2012 Paul Howarth <paul@city-fan.org> - 0.03-2
- Rebuild for gcc 4.7 in Rawhide

* Fri Nov 18 2011 Paul Howarth <paul@city-fan.org> - 0.03-1
- Update to 0.03:
  - Explicitly include Test::Fatal as a test prerequisite (CPAN RT#72493)

* Wed Nov 16 2011 Paul Howarth <paul@city-fan.org> - 0.02-2
- Sanitize spec for Fedora submission

* Wed Nov 16 2011 Paul Howarth <paul@city-fan.org> - 0.02-1
- Initial RPM version
