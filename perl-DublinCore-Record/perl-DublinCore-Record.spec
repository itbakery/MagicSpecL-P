Name:           perl-DublinCore-Record
Version:        0.03
Release:        4%{?dist}
Summary:        Container for Dublin Core meta-data elements
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/DublinCore-Record/
Source0:        http://www.cpan.org/authors/id/B/BR/BRICAS/DublinCore-Record-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Class::Accessor)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)

%description
DublinCore::Record is an abstract class for manipulating DublinCore
meta-data. The Dublin Core is a small set of meta-data elements for
describing information resources. For more information on embedding
DublinCore in HTML see RFC 2731 http://www.ietf.org/rfc/rfc2731 or
http://www.dublincore.org/documents/dces/

%prep
%setup -q -n DublinCore-Record-%{version}

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
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.03-4
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 28 2011 Nicholas van Oudtshoorn <vanoudt@gmail.com> - 0.03-2
- Specfile updates to conform to guidelines
* Thu Apr 28 2011 Nicholas van Oudtshoorn <vanoudt@gmail.com> - 0.03-1
- Specfile autogenerated by cpanspec 1.78.
