Name:           perl-HTTP-BrowserDetect
Summary:        Determine the Web browser, version, and platform from an HTTP user agent string
Version:        1.21
Release:        6%{?dist}
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/HTTP-BrowserDetect/
Source0:        http://www.cpan.org/authors/id/O/OA/OALDERS/HTTP-BrowserDetect-%{version}.tar.gz 
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(Data::Dump)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(YAML)
BuildRequires:  perl(Module::Build)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
The HTTP::BrowserDetect object does a number of tests on an HTTP user agent
string. The results of these tests are available via methods of the object.

This module is based upon the JavaScript browser detection code available
at http://www.mozilla.org/docs/web-developer/sniffer/browser_type.html.

%prep
%setup -q -n HTTP-BrowserDetect-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
rm -rf $RPM_BUILD_ROOT

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes LICENSE README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 1.21-6
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 1.21-5
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 29 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.21-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 27 2010 Steven Pritchard <steve@kspei.com> 1.21-1
- Update to 1.21.
- BR Module::Build and build with that.
- Add LICENSE and TODO to docs.
- Drop BR for Exporter, FindBin (both core modules), and YAML::Tiny, and
  add BR YAML.

* Fri Dec 17 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.10-3
- 661697 rebuild for fixing problems with vendorach/lib

* Wed May 19 2010 Chris Weyl <cweyl@alumni.drew.edu> 1.10-2
- bump

* Wed May 19 2010 Chris Weyl <cweyl@alumni.drew.edu> 1.10-1
- PERL_INSTALL_DIR => DESTDIR
- update by Fedora::App::MaintainerTools 0.006
- updating to latest GA CPAN version (1.10)
- added a new br on perl(Data::Dump) (version 0)
- added a new br on perl(Exporter) (version 0)
- added a new br on perl(FindBin) (version 0)
- added a new br on perl(Test::More) (version 0)
- added a new br on perl(YAML::Tiny) (version 0)

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.99-6
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.99-5
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.99-2
- rebuild for new perl

* Fri May 18 2007 Steven Pritchard <steve@kspei.com> 0.99-1
- Update to 0.99.
- Update Source0 URL.
- Improve Summary and description.

* Tue Apr 17 2007 Steven Pritchard <steve@kspei.com> 0.98-4
- Use fixperms macro instead of our own chmod incantation.
- BR ExtUtils::MakeMaker.

* Tue Sep 05 2006 Steven Pritchard <steve@kspei.com> 0.98-3
- Fix find option order.
- Use canonical Source0 URL.

* Fri Mar 10 2006 Steven Pritchard <steve@kspei.com> 0.98-2
- Improve Summary.

* Thu Aug 18 2005 Steven Pritchard <steve@kspei.com> 0.98-1
- Specfile autogenerated.
