Name:           perl-Data-Hierarchy
Version:        0.34
Release:        13%{?dist}
Summary:        Handle data in a hierarchical structure
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Data-Hierarchy/
Source0:        http://www.cpan.org/modules/by-module/Data/Data-Hierarchy-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Exception)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Data::Hierarchy provides a simple interface for manipulating inheritable
data attached to a hierarchical environment (like filesystem).

%prep
%setup -q -n Data-Hierarchy-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type d -depth -exec rmdir {} 2>/dev/null \;
chmod -R u+rwX,go+rX,go-w %{buildroot}/*

%check


%files
%doc CHANGES README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.34-13
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.34-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.34-11
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.34-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.34-9
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.34-8
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.34-7
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.34-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.34-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.34-4
- rebuild for new perl

* Thu Aug 16 2007 Ian M. Burrell <ianburrell@gmail.com> - 0.34-3
- Fix BuildRequires

* Sat Dec 16 2006 Ian Burrell <ianburrell@gmail.com> - 0.34-2
- Add Test::Exception BuildRequires
- Remove Clone BuildRequires

* Sat Dec 16 2006 Ian Burrell <ianburrell@gmail.com> - 0.34-1
- Update to 0.34

* Tue Jun 27 2006 Ian Burrell <ianburrell@gmail.com> - 0.22-2
- Remove useless requires

* Tue Jun 27 2006 Ian M. Burrell <ianburrell@gmail.com> - 0.22-1
- Update to 0.22

* Thu Mar 30 2006 Ian Burrell <ianburrell@gmail.com> 0.21-1
- Specfile autogenerated by cpanspec 1.64.
