Name:           perl-Crypt-SMIME
Version:        0.09
Release:        11%{?dist}
Summary:        S/MIME message signing, verification, encryption and decryption
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Crypt-SMIME/
Source0:        http://www.cpan.org/modules/by-module/Crypt/Crypt-SMIME-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  openssl-devel
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

#Add a test sub package.
%{?perl_default_subpackage_tests}

%description
This module provides a class for handling S/MIME messages. It can sign,
verify, encrypt and decrypt messages. It requires libcrypto
(http://www.openssl.org) to work.

%prep
%setup -q -n Crypt-SMIME-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Crypt*
%{_mandir}/man3/*

%changelog
* Sun Dec 09 2012 Liu Di <liudidi@gmail.com> - 0.09-11
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.09-10
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.09-8
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.09-6
- 661697 rebuild for fixing problems with vendorach/lib

* Sun Dec 12 2010 Iain Arnell <iarnell@gmail.com> 0.09-5
- doesn't require perl(Test::Exception) or perl(Test::More)

* Tue Jun 22 2010 Petr Pisar <ppisar@redhat.com> 0.09-4
- Rebuild against perl-5.12

* Tue May 4 2010 Steve Traylen <steve.traylen@cern.ch> 0.09-3
- First release on Fedora/EPEL.

* Mon May 3 2010 Steve Traylen <steve.traylen@cern.ch> 0.09-2
- Additon of openssl-devel build requires.

* Mon Apr 26 2010 Steve Traylen <steve.traylen@cern.ch> 0.09-1
- Specfile autogenerated by cpanspec 1.78.
- Install with DESTDIR
- Create -test subpackage if macro is define.
- Remove SMIME.mlpod from docs.
