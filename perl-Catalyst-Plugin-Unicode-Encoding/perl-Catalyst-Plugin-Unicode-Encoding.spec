Name:           perl-Catalyst-Plugin-Unicode-Encoding
Version:        1.3
Release:        3%{?dist}
Summary:        Unicode aware Catalyst
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Catalyst-Plugin-Unicode-Encoding/
Source0:        http://www.cpan.org/authors/id/B/BO/BOBTFISH/Catalyst-Plugin-Unicode-Encoding-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Catalyst) >= 5.80
BuildRequires:  perl(Class::Data::Inheritable)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(LWP) >= 5.837
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(URI) >= 1.36
# tests
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::WWW::Mechanize::Catalyst)
Requires:       perl(Catalyst) >= 5.80
Requires:       perl(LWP) >= 5.837
Requires:       perl(URI) >= 1.36
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
On request, decodes all params from encoding into a sequence of logical
characters. On response, encodes body into encoding.

%prep
%setup -q -n Catalyst-Plugin-Unicode-Encoding-%{version}

sed -i -e '/auto_install/d' Makefile.PL

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
TEST_POD=1 

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 1.3-3
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 1.3-2
- 为 Magic 3.0 重建

* Fri Jan 20 2012 Iain Arnell <iarnell@gmail.com> 1.3-1
- update to latest upstream version

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Sep 24 2011 Iain Arnell <iarnell@gmail.com> 1.2-1
- update to latest upstream version
- clean up spec for modern rpmbuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 1.1-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.1-2
- 661697 rebuild for fixing problems with vendorach/lib

* Sun Jul 11 2010 Iain Arnell <iarnell@gmail.com> 1.1-1
- update to latest upstream
- disable Module::AutoInstall

* Wed Jun 30 2010 Iain Arnell <iarnell@gmail.com> 1.0-1
- Specfile autogenerated by cpanspec 1.78.
