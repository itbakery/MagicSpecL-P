Name:           perl-CPAN-Uploader
Version:        0.103000
Release:        6%{?dist}
Summary:        Upload things to the CPAN
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/CPAN-Uploader/
Source0:        http://www.cpan.org/authors/id/R/RJ/RJBS/CPAN-Uploader-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Getopt::Long::Descriptive) >= 0.084
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Term::ReadKey)
# tests
BuildRequires:  perl(Pod::Coverage::TrustPod)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)

Requires:       perl(Term::ReadKey)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
CPAN::Uploader is a module which automates the process of uploading a file to
CPAN using PAUSE, the Perl Authors Upload Server.

%prep
%setup -q -n CPAN-Uploader-%{version}

# don't conflict with cpan-upload
mv bin/cpan-upload bin/cpan-uploader
sed -i -e 's!bin/cpan-upload!bin/cpan-uploader!' Makefile.PL

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
RELEASE_TESTING=1 

%files
%defattr(-,root,root,-)
%doc Changes dist.ini LICENSE META.json README
%{perl_vendorlib}/*
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Sun Dec 09 2012 Liu Di <liudidi@gmail.com> - 0.103000-6
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.103000-5
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.103000-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 0.103000-3
- Perl mass rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 0.103000-2
- Perl mass rebuild

* Sat Apr 09 2011 Iain Arnell <iarnell@gmail.com> 0.103000-1
- update to latest upstream version
- clean up spec for modern rpmbuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.102150-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.102150-2
- 661697 rebuild for fixing problems with vendorach/lib

* Thu Aug 05 2010 Iain Arnell <iarnell@gmail.com> 0.102150-1
- update to latest upstream

* Fri Jun 18 2010 Iain Arnell <iarnell@gmail.com> 0.101670-1
- update to latest upstream

* Sat Jun 05 2010 Iain Arnell <iarnell@gmail.com> 0.101550-1
- update to latest upstream

* Fri May 28 2010 Iain Arnell <iarnell@gmail.com> 0.101260-2
- bump release for rebuild with perl-5.12.0

* Sun May 09 2010 Iain Arnell <iarnell@gmail.com> 0.101260-1
- update to latest upstream

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.100760-2
- Mass rebuild with perl-5.12.0

* Thu Apr 08 2010 Iain Arnell <iarnell@gmail.com> 0.100760-1
- Specfile autogenerated by cpanspec 1.78.
- use perl_default_filter and DESTDIR
- tweak requires
