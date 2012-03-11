Name:           perl-YAML
Version:        0.73
Release:        3%{?dist}
Summary:        YAML Ain't Markup Language (tm)
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/YAML/
Source0:        http://search.cpan.org/CPAN/authors/id/I/IN/INGY/YAML-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
%if !%{defined perl_bootstrap}
BuildRequires:  perl(Test::CPAN::Meta), perl(Test::MinimumVersion), perl(Test::Pod)
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
The YAML.pm module implements a YAML Loader and Dumper based on the
YAML 1.0 specification. http://www.yaml.org/spec/
YAML is a generic data serialization language that is optimized for
human readability. It can be used to express the data structures of
most modern programming languages, including Perl.
For information on the YAML syntax, please refer to the YAML
specification.

%prep
%setup -q -n YAML-%{version}

# Re-code docs as UTF-8
iconv -f iso-8859-1 -t utf8 < README > README.utf8
mv README.utf8 README

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor < /dev/null
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

# Removing Test::YAML (at least temporarily) due
# to security concerns and questionable value.
# https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=197539
rm -f $RPM_BUILD_ROOT%{perl_vendorlib}/Test/YAML* \
    $RPM_BUILD_ROOT%{_mandir}/man3/Test::YAML*.3*

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
%if !%{defined perl_bootstrap}
make test AUTOMATED_TESTING=1
%endif

%files
%doc Changes README LICENSE
%{perl_vendorlib}/YAML*
%{_mandir}/man3/YAML*.3*

%changelog
* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.73-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.73-2
- Perl mass rebuild
- add perl_bootstrap macro

* Sat May 14 2011 Iain Arnell <iarnell@gmail.com> 0.73-1
- update to latest upstream version
- clean up spec for modern rpmbuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.72-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 08 2010 Steven Pritchard <steve@kspei.com> 0.72-1
- Update to 0.72.

* Wed Aug 18 2010 Paul Howarth <paul@city-fan.org> - 0.71-1
- Update to 0.71 (use UTF-8 encoding in LoadFile/DumpFile: CPAN RT#25434)
- Enable AUTOMATED_TESTING
- BR: perl(Test::CPAN::Meta), perl(Test::MinimumVersion), perl(Test::Pod)
- This release by ADAMK -> update source URL
- Re-code docs as UTF-8

* Thu Apr 29 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.70-5
- Mass rebuild with perl-5.12.0

* Thu Feb 25 2010 Marcela Mašláňová <mmaslano@redhat.com> - 0.70-4
- add license

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.70-3
- rebuild against perl 5.10.1

* Wed Oct  7 2009 Marcela Mašláňová <mmaslano@redhat.com> - 0.70-2
- rebuild for push

* Tue Oct 6  2009 Marcela Mašláňová <mmaslano@redhat.com> - 0.70-1
- new upstream version

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.68-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.68-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec 10 2008 Steven Pritchard <steve@kspei.com> 0.68-1
- Update to 0.68.
- COMPATIBILITY went away.
- ysh moved to YAML::Shell.

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.66-3
- Rebuild for perl 5.10 (again)

* Fri Jan 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.66-2
- rebuild for new perl

* Tue Oct 16 2007 Steven Pritchard <steve@kspei.com> 0.66-1
- Update to 0.66.
- Update License tag.

* Wed Jun 27 2007 Steven Pritchard <steve@kspei.com> 0.65-1
- Update to 0.65.

* Tue Mar 13 2007 Steven Pritchard <steve@kspei.com> 0.62-3
- Use fixperms macro instead of our own chmod incantation.
- Drop Test::Base build dependency to avoid a BR loop (#215637).
- BR ExtUtils::MakeMaker.

* Sat Sep 16 2006 Steven Pritchard <steve@kspei.com> 0.62-2
- Fix find option order.

* Fri Jul 07 2006 Steven Pritchard <steve@kspei.com> 0.62-1
- Update to 0.62.
- Removed Test::YAML (bug #197539).

* Mon Jul 03 2006 Steven Pritchard <steve@kspei.com> 0.61-1
- Update to 0.61.

* Sat May 20 2006 Steven Pritchard <steve@kspei.com> 0.58-3
- Rebuild.

* Tue May 09 2006 Steven Pritchard <steve@kspei.com> 0.58-2
- Drop testmore patch.
- Catch Test::YAML module and man page in file list.

* Thu May 04 2006 Steven Pritchard <steve@kspei.com> 0.58-1
- Update to 0.58.
- Small spec cleanups.

* Thu Apr 14 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.39-2
- 0.39.

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Sat May 15 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:0.35-0.fdr.5
- Avoid creation of the perllocal.pod file (make pure_install).

* Sun Apr 25 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.35-0.fdr.4
- Require perl(:MODULE_COMPAT_*).
- Cosmetic tweaks (bug 1383).

* Sun Mar 14 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.35-0.fdr.3
- Reduce directory ownership bloat.

* Tue Nov 18 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.35-0.fdr.2
- Use INSTALLARCHLIB workaround in %%install.

* Wed Sep  3 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.35-0.fdr.1
- First build.
