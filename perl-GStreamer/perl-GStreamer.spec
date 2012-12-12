Name:           perl-GStreamer
Version:        0.16
Release:        3%{?dist}
Summary:        Perl bindings to the GStreamer framework
License:        LGPLv2+
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/GStreamer/
Source0:        http://www.cpan.org/authors/id/T/TS/TSCH/GStreamer-%{version}.tar.gz
BuildRequires:  gstreamer-devel
BuildRequires:  perl(ExtUtils::Depends) >= 0.205
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::PkgConfig) >= 1.07
BuildRequires:  perl(Glib::MakeHelper)
# Run-time
BuildRequires:  perl(constant)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Glib) >= 1.180
# Tests
BuildRequires:  gstreamer-plugins-base
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
GStreamer makes everybody dance like crazy.  It provides the means to play,
stream, and convert nearly any type of media -- be it audio or video.
GStreamer wraps the GStreamer library in a nice and Perlish way, freeing 
the programmer from any memory management and object casting hassles.


%prep
%setup -q -n GStreamer-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} %{buildroot}/*

%check
# note some 64-bit funkiness (but not failures):
# http://bugzilla.gnome.org/show_bug.cgi?id=352750
# http://bugzilla.gnome.org/show_bug.cgi?id=352753


%files
%doc ChangeLog.pre-git copyright.pod LICENSE NEWS README TODO examples/
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/GStreamer*
%{_mandir}/man3/*

%changelog
* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.16-3
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.16-2
- 为 Magic 3.0 重建

* Wed Jan 25 2012 Petr Pisar <ppisar@redhat.com> - 0.16-1
- 0.16 bump

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jun 19 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.15-9
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 17 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.15-7
- 661697 rebuild for fixing problems with vendorach/lib

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.15-6
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.15-5
- rebuild against perl 5.10.1

* Sat Aug 29 2009 Chris Weyl <cweyl@alumni.drew.edu> - 0.15-4
- Filter errant private provides

* Thu Jul 30 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.15-3
- Fix mass rebuild breakdown: Add BR: perl(Glib::MakeHelper).

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar 02 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.15-1
- update to 1.15
- trim doc
- update BR's

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.09-6
- Rebuild for new perl

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.09-5
- Autorebuild for GCC 4.3

* Tue Aug 21 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.09-4
- bump

* Mon Feb 19 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.09-3
- disable test suite for mock/plague building; they just won't play nice with
  each other.  pass --with-network-tests to rpmbuild for local testing.

* Sun Sep 03 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.09-2
- bump

* Wed Aug 23 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.09-1
- Specfile autogenerated by cpanspec 1.68.
- Initial spec file for F-E
