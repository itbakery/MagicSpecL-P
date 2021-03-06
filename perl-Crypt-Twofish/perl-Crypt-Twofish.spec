Name:           perl-Crypt-Twofish
Version:        2.14
Release:        9%{?dist}
Summary:        Twofish Encryption Algorithm
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Crypt-Twofish/
Source0:        http://www.cpan.org/authors/id/A/AM/AMS/Crypt-Twofish-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
Twofish is a 128-bit symmetric block cipher with a variable length (128,
192, or 256-bit) key, developed by Counterpane Labs. It is unpatented and
free for all uses, as described at http://www.counterpane.com/twofish.html.

%prep
%setup -q -n Crypt-Twofish-%{version}

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
* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 2.14-9
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 2.14-8
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.14-6
- Perl mass rebuild

* Tue Jun 14 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.14-5
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.14-3
- 661697 rebuild for fixing problems with vendorach/lib

* Thu May 20 2010 Iain Arnell <iarnell@gmail.com> 2.14-2
- Rebuild with perl-5.12.0

* Sun May 09 2010 Iain Arnell <iarnell@gmail.com> 2.14-1
- update to latest upstream
- use perl_default_filter and DESTDIR

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.13-4
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 2.13-3
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon May 11 2009 Iain Arnell 2.13-1
- Specfile autogenerated by cpanspec 1.77.
