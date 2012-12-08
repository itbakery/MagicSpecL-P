Name:           perl-Astro-FITS-CFITSIO
Version:        1.07
Release:        3%{?dist}
Summary:        Perl extension for using the cfitsio library
# tarball m51 doesn't state license https://rt.cpan.org/Public/Bug/Display.html?id=66226
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Astro-FITS-CFITSIO/
Source0:        http://www.cpan.org/authors/id/P/PR/PRATZLAFF/Astro-FITS-CFITSIO-%{version}.tar.gz
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  cfitsio-devel
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Perl interface to William Pence's cfitsio subroutine library. For more
information on cfitsio, see http://heasarc.gsfc.nasa.gov/fitsio.

%prep
%setup -q -n Astro-FITS-CFITSIO-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS -I%{_includedir}/cfitsio"
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
#works locally
#make test

%files
%doc ChangeLog NOTES README TODO examples
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Astro*
%{_mandir}/man3/*

%changelog
* Sat Dec 08 2012 Liu Di <liudidi@gmail.com> - 1.07-3
- 为 Magic 3.0 重建

* Sat Jan 28 2012 Liu Di <liudidi@gmail.com> - 1.07-2
- 为 Magic 3.0 重建

* Fri Jan 6 2012 Orion Poplawski <orion@cora.nwra.com> - 1.07-1
- Update to 1.07, build with cfitsio 3.290

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.06-1
- update to 1.06, switch off tests (working only locally), clean spec
- link to license problem

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.05-11
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.05-9
- 661697 rebuild for fixing problems with vendorach/lib

* Thu Apr 29 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.05-8
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.05-7
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.05-4
Rebuild for new perl

* Sat Feb  9 2008 Orion Poplawski <orion@cora.nwra.com> 1.05-3
- Rebuild for gcc 3.4

* Thu Aug 23 2007 Orion Poplawski <orion@cora.nwra.com> 1.05-2
- Update license tag to GPL+ or Artistic
- Rebuild for BuildID

* Tue Jul 31 2007 Orion Poplawski 1.05-1
- Specfile autogenerated by cpanspec 1.73.
