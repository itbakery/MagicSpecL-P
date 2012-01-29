Name:           perl-Kwiki-Diff
Version:        0.03
Release:        18%{?dist}
Summary:        Display differences between the current wiki page and older revisions
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Kwiki-Diff/
Source0:        http://www.cpan.org/authors/id/I/IA/IAN/Kwiki-Diff-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(Algorithm::Diff) >= 1.18
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::All)
BuildRequires:  perl(Kwiki) >= 0.34
BuildRequires:  perl(Kwiki::Revisions) >= 0.12
BuildRequires:  perl(Spiffy) >= 0.22
BuildRequires:  perl(Test::More)
# For improved tests
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
BuildRequires:  perl(Test::Pod) >= 1.14
Requires:       perl(Algorithm::Diff) >= 1.18
Requires:       perl(Kwiki) >= 0.34
Requires:       perl(Kwiki::Revisions) >= 0.12
Requires:       perl(Spiffy) >= 0.22
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Kwiki Diff plugin.

%prep
%setup -q -n Kwiki-Diff-%{version}

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
rm -f debug*.list


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.03-18
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 22 2011 Petr Sabata <contyk@redhat.com> - 0.03-16
- BuildRequire IO::All

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 0.03-15
- Perl mass rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.03-14
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.03-12
- 661697 rebuild for fixing problems with vendorach/lib

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.03-11
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.03-10
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.03-6
Rebuild for new perl

* Fri Jan 04 2008 Ralf Corsépius <rc040203@freenet.de> 0.03-5
- Update License-tag.
- BR: perl(Test::Pod::Coverage), perl(Test::Pod).
- BR: perl(Test::More) (BZ 419631).

* Tue Apr 17 2007 Steven Pritchard <steve@kspei.com> 0.03-4
- Use fixperms macro instead of our own chmod incantation.
- BR ExtUtils::MakeMaker.

* Tue Sep 05 2006 Steven Pritchard <steve@kspei.com> 0.03-3
- Minor spec cleanup.

* Sat Feb 25 2006 Steven Pritchard <steve@kspei.com> 0.03-2
- Fix License tag.
- Don't generate COPYING and Artistic so we can re-enable "".
- Remove debug*.list so "" doesn't fail.

* Thu Dec 29 2005 Steven Pritchard <steve@kspei.com> 0.03-1
- Specfile autogenerated.
