%define real_name HTML-Parser

Name:           perl-%{real_name}
Summary:        Perl module for parsing HTML
Version:        3.69
Release:        9%{?dist}
License:        GPL+ or Artistic
Group:          Development/Libraries
Source0:        http://search.cpan.org/CPAN/authors/id/G/GA/GAAS/HTML-Parser-%{version}.tar.gz 
URL:            http://search.cpan.org/dist/HTML-Parser/
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTML::Tagset) >= 3
%if %{undefined perl_bootstrap}
# This creates cycle with perl-HTTP-Message.
BuildRequires:  perl(HTTP::Headers)
%endif
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI)
BuildRequires:  perl(XSLoader)
Requires:       perl(HTML::Tagset) >= 3
Requires:       perl(HTTP::Headers)
Requires:       perl(URI)
Requires:       perl(XSLoader)

%{?perl_default_filter}
%{?perl_default_subpackage_tests}

%description
The HTML-Parser module for perl to parse and extract information from
HTML documents, including the HTML::Entities, HTML::HeadParser,
HTML::LinkExtor, HTML::PullParser, and HTML::TokeParser modules.

%prep
%setup -q -n %{real_name}-%{version}
chmod -c a-x eg/*

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
file=%{buildroot}%{_mandir}/man3/HTML::Entities.3pm
iconv -f iso-8859-1 -t utf-8 <"$file" > "${file}_"
mv -f "${file}_" "$file"
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w %{buildroot}/*

%check


%files
%doc Changes README TODO eg/
%{perl_vendorarch}/HTML/
%{perl_vendorarch}/auto/HTML/
%{_mandir}/man3/*.3pm*


%changelog
* Sun Dec 09 2012 Liu Di <liudidi@gmail.com> - 3.69-9
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.69-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Petr Pisar <ppisar@redhat.com> - 3.69-7
- Perl 5.16 re-rebuild of bootstrapped packages

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 3.69-6
- Perl 5.16 rebuild

* Mon Apr 16 2012 Petr Pisar <ppisar@redhat.com> - 3.69-5
- Exclude HTTP::Headers build-dependency at Perl bootstrap (bug #810223)

* Mon Apr 16 2012 Petr Pisar <ppisar@redhat.com> - 3.69-4
- Revert "Exclude HTTP::Headers dependency at Perl bootstrap"

* Wed Jan 18 2012 Petr Pisar <ppisar@redhat.com> - 3.69-3
- Exclude HTTP::Headers dependency at Perl bootstrap

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.69-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 17 2011 Petr Sabata <contyk@redhat.com> - 3.69-1
- 3.69 bump
- Drop Buildroot and defattr, cleanup

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 3.68-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.68-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 17 2010 Marcela Maslanova <mmaslano@redhat.com> - 3.68-2
- 661697 rebuild for fixing problems with vendorach/lib

* Tue Sep 07 2010 Petr Sabata <psabata@redhat.com> - 3.68-1
- Update to the latest upstream release, v3.68

* Wed Sep 01 2010 Petr Sabata <psabata@redhat.com> - 3.67-1
- Update to the latest upstream release, v3.67

* Mon Jul 12 2010 Marcela Mašláňová <mmaslano@redhat.com> 3.66-1
- update

* Fri Jul 09 2010 Marcela Mašláňová <mmaslano@redhat.com> 3.65-1
- and re-add real-name macro back, maintainertool can't handle it

- update by Fedora::App::MaintainerTools 0.006
- updating to latest GA CPAN version (3.65)
- added a new br on perl(ExtUtils::MakeMaker) (version 0)
- altered br on perl(HTML::Tagset) (3.03, => 3)
- added a new br on perl(Test::More) (version 0)
- added a new br on perl(XSLoader) (version 0)
- altered req on perl(HTML::Tagset) (3.03 => 3)
- added a new req on perl(XSLoader) (version 0)

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 3.64-3
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 3.64-2
- rebuild against perl 5.10.1

* Mon Nov  2 2009 Stepan Kasal <skasal@redhat.com> - 3.64-1
- new upstream version

* Fri Oct 23 2009 Warren Togami <wtogami@redhat.com> - 3.63-2
- 3.63 CVE-2009-3627

* Thu Sep 17 2009 Warren Togami <wtogami@redhat.com> - 3.62-1
- 3.62

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.60-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 08 2009 Chris Weyl <cweyl@alumni.drew.edu> - 3.60-1
- update to latest for mojomojo
- filter bad provides (Parser.so)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.59-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec 16 2008 Marcela Mašláňová <mmaslano@redhat.com> - 3.59-1
- update to the latest version for Padre editor

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 3.56-5
- Rebuild for perl 5.10 (again)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 3.56-4
- Autorebuild for GCC 4.3

* Sun Jan 20 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 3.56-3
- rebuild for new perl

* Wed Aug 29 2007 Robin Norwood <rnorwood@redhat.com> - 3.56-2
- Fix license tag
- update BuildRequires

* Sat Feb  3 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.56-1
- Update to 3.56.
- Brought specfile closer to the Fedora's Perl template.
- Converted specfile to UTF-8 (changelog entries).
- Added examples and doc files.

* Mon Jul 17 2006 Jason Vas Dias <jvdias@redhat.com> - 3.55-1.fc6
- Upgrade to 3.55

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 3.54-1.fc6.1
- rebuild

* Mon Jun 05 2006 Jason Vas Dias <jvdias@redhat.com> - 3.54-1
- upgrade to 3.54

* Mon Mar 22 2006 Jason Vas Dias <jvdias@redhat.com> - 3.51-1
- upgrade to 3.51

* Mon Feb 20 2006 Jason Vas Dias <jvdias@redhat.com> - 3.50-1
- upgrade to 3.50

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 3.48-1.1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 3.48-1.1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Feb 03 2006 Jason Vas Dias <jvdias@redhat.com> - 3.48-1
- rebuild for new perl-5.8.8

* Mon Dec 19 2005 Jason Vas Dias<jvdias@redhat.com> - 3.48-1
- upgrade to 3.48

* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcc

* Sun Nov 06 2005 Florian La Roche <laroche@redhat.com>
- 3.46

* Fri Apr  1 2005 Michael Schwendt <mschwendt@users.sf.net> - 3.45-1
- Update to 3.45 plus heavy spec cleanup.

* Wed Mar 30 2005 Warren Togami <wtogami@redhat.com>
- remove brp-compress

* Thu Nov 25 2004 Miloslav Trmac <mitr@redhat.com> - 3.35-7
- Convert man page to UTF-8

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Mar 17 2004 Chip Turner <cturner@redhat.com> 3.35-2
- rebuild for fc1 update

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Chip Turner <cturner@redhat.com> 3.35-1
- update to 3.35

* Thu Jun 05 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Aug  6 2002 Chip Turner <cturner@redhat.com>
- automated release bump and build

* Tue Jun  4 2002 Chip Turner <cturner@redhat.com>
- properly claim directories owned by package so they are removed when package is removed

* Mon Jun  3 2002 Chip Turner <cturner@redhat.com>
- fix for Makefile.PL sometimes prompting for input

* Wed Mar 27 2002 Chip Turner <cturner@redhat.com>
- update to 3.26, move to vendor_perl

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Jul 18 2001 Crutcher Dunnavant <crutcher@redhat.com> 3.25-2
- imported from mandrake. tweaked man path.

* Tue Jul 03 2001 François Pons <fpons@mandrakesoft.com> 3.25-1mdk
- 3.25.

* Wed Jun 20 2001 Christian Belisle <cbelisle@mandrakesoft.com> 3.18-3mdk
- Fixed distribution tag.
- Updated Requires.
- Added an option to %%makeinstall.

* Sun Jun 17 2001 Geoffrey Lee <snailtalk@mandrakesoft.com> 3.18-2mdk
- Rebuild against the latest perl.

* Tue Feb 27 2001 François Pons <fpons@mandrakesoft.com> 3.18-1mdk
- 3.18.

* Tue Jan 30 2001 François Pons <fpons@mandrakesoft.com> 3.15-1mdk
- 3.15.

* Tue Dec 05 2000 François Pons <fpons@mandrakesoft.com> 3.14-1mdk
- 3.14.

* Thu Oct 12 2000 François Pons <fpons@mandrakesoft.com> 3.13-1mdk
- 3.13.

* Tue Aug 29 2000 François Pons <fpons@mandrakesoft.com> 3.11-1mdk
- 3.11.

* Thu Aug 03 2000 François Pons <fpons@mandrakesoft.com> 3.10-2mdk
- macroszifications.
- add doc.

* Tue Jul 18 2000 François Pons <fpons@mandrakesoft.com> 3.10-1mdk
- removed perllocal.pod from files.
- 3.10.

* Tue Jun 27 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 3.08-1mdk
- update to 3.08

* Wed May 17 2000 David BAUDENS <baudens@mandrakesoft.com> 3.05-4mdk
- Fix build for i486
- Use %%{_tmppath} for BuildRoot

* Fri Mar 31 2000 Pixel <pixel@mandrakesoft.com> 3.05-3mdk
- rebuild, new group, cleanup

* Tue Feb 29 2000 Jean-Michel Dault <jmdault@netrevolution.com> 3.0.5-1mdk
- upgrade to 3.05

* Mon Jan  3 2000 Jean-Michel Dault <jmdault@netrevolution.com>
- final cleanup for Mandrake 7

* Thu Dec 30 1999 Jean-Michel Dault <jmdault@netrevolution.com>
-updated to 3.02

* Sun Aug 29 1999 Jean-Michel Dault <jmdault@netrevolution.com>
- bzip2'd sources
- updated to 2.23

* Tue May 11 1999 root <root@alien.devel.redhat.com>
- Spec file was autogenerated. 
