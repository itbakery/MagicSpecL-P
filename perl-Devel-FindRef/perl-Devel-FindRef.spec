Name:           perl-Devel-FindRef
Version:        1.42
Release:        14%{?dist}
Summary:        Where is that reference to my variable hiding?
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Devel-FindRef/
Source0:        http://www.cpan.org/authors/id/M/ML/MLEHMANN/Devel-FindRef-%{version}2.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(common::sense)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Tracking down reference problems (e.g. you expect some object to be
destroyed, but there are still references to it that keep it alive) can be
very hard. Fortunately, perl keeps track of all its values, so tracking
references "backwards" is usually possible.

%prep
%setup -q -n Devel-FindRef-%{version}2


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes COPYING README
%{perl_vendorarch}/auto/Devel
%{perl_vendorarch}/Devel
%{_mandir}/man3/Devel*.3*

%changelog
* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.42-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jun 19 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.42-13
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.42-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.42-11
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.42-10
- Mass rebuild with perl-5.12.0

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.42-9
- Mass rebuild with perl-5.12.0

* Sun Dec 20 2009 Nicolas Chauvet <kwizart@fedoraproject.org> - 1.42-8
- Add BR perl(common::sense)

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.42-7
- rebuild against perl 5.10.1

* Mon Aug 31 2009 Nicolas Chauvet <kwizart@fedoraproject.org> - 1.42-5
- Update internal version to 1.422

* Tue Aug  4 2009 Stepan Kasal <skasal@redhat.com> 1.42-3
- back out the previous rebuild

* Fri Jul 31 2009 Stepan Kasal <skasal@redhat.com> 1.42-2
- rebuild against perl build without -DDEBUGGING

* Mon Jul 27 2009 Nicolas Chauvet (kwizart) 1.42-1
- Specfile autogenerated by cpanspec 1.78.
