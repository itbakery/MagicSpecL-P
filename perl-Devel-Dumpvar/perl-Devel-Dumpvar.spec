Name:           perl-Devel-Dumpvar
Version:        1.06
Release:        7%{?dist}
Summary:        Pure-OO reimplementation of dumpvar.pl
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Devel-Dumpvar/
Source0:        http://www.cpan.org/authors/id/A/AD/ADAMK/Devel-Dumpvar-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Scalar::Util) >= 1.18
BuildRequires:  perl(Test::More) >= 0.42
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Most perl dumping modules are focused on serializing data structures into
a format that can be rebuilt into the original data structure. They do
this with a variety of different focuses, such as human readability, the
ability to execute the dumped code directly, or to minimize the size of
the dumped data.

%prep
%setup -q -n Devel-Dumpvar-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Dec 09 2012 Liu Di <liudidi@gmail.com> - 1.06-7
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 1.06-6
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.06-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.06-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.06-2
- 661697 rebuild for fixing problems with vendorach/lib

* Tue Sep 14 2010 Petr Pisar <ppisar@redhat.com> - 1.06-1
- 1.06 bump

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.04-7
- Mass rebuild with perl-5.12.0

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.04-6
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.04-5
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 13 2009 Marcela Mašláňová <mmaslano@redhat.com> 0.04-2
- removed useless requirement

* Mon Jan 12 2009 Marcela Mašláňová <mmaslano@redhat.com> 0.04-1
- Specfile autogenerated by cpanspec 1.77.
