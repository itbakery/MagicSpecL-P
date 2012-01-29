Name:           perl-HTML-Tree
Version:        4.2
Release:        5%{?dist}
Epoch:          1
Summary:        HTML tree handling modules for Perl
Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/HTML-Tree/
Source0:        http://www.cpan.org/authors/id/J/JF/JFEARN/HTML-Tree-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(HTML::Parser) >= 3.46
BuildRequires:  perl(HTML::Tagset) >= 3.02
BuildRequires:  perl(Module::Build)
# For improved tests
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::More)

Requires:       perl(HTML::Parser) >= 3.46
Requires:       perl(HTML::Tagset) >= 3.02
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
# add because of possible problems with not mathing cpan,rpm version
Provides:       perl(HTML::Tree) = %{version}

%description
This distribution contains a suite of modules for representing,
creating, and extracting information from HTML syntax trees; there is
also relevant documentation.  These modules used to be part of the
libwww-perl distribution, but are now unbundled in order to facilitate
a separate development track.

%prep
%setup -q -n HTML-Tree-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README TODO
%{_bindir}/htmltree
%{perl_vendorlib}/HTML
%{_mandir}/man3/HTML::*3*

%changelog
* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 1:4.2-5
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 1:4.2-3
- Perl mass rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 1:4.2-2
- Perl mass rebuild

* Tue Jun 28 2011 Tom Callaway <spot@fedoraproject.org> - 1:4.2-1
- update to 4.2

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1:4.1-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec  1 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 1:4.1-1
- update to 4.1

* Mon Oct 18 2010 Marcela Mašláňová <mmaslano@redhat.com> - 1:3.40-1
- update, adjust specfile to use Build.PL

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 1:3.23-11
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1:3.23-10
- rebuild against perl 5.10.1

* Mon Sep 28 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1:3.23-9
- apply Jeff Fearn's fix for the missing close tag bug (bz 535587)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.23-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.23-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.23-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Nov 20 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1:3.23-5
- fix source url

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1:3.23-4
- Rebuild for perl 5.10 (again)

* Sun Jan 20 2008 Tom "spot" Callaway <tcallawa@redhat.com> 3.23-3
- rebuild for new perl

* Sun Aug 26 2007 Tom "spot" Callaway <tcallawa@redhat.com> 3.23-2
- license tag fix

* Wed Jan 17 2007 Tom "spot" Callaway <tcallawa@redhat.com> 3.23-1
- bump to 3.23

* Fri Sep 15 2006 Tom "spot" Callaway <tcallawa@redhat.com> 3.21-1
- bump to 3.21

* Tue Jul 11 2006 Tom "spot" Callaway <tcallawa@redhat.com> 3.20-2
- bump epoch to ensure clean upgrades

* Fri Jul  7 2006 Tom "spot" Callaway <tcallawa@redhat.com> 3.20-1
- bump to 3.20

* Mon Jan 16 2006 Ralf Corsépius <rc040203@freenet.de> - 3.1901-2
- BR: perl(Test::Pod).

* Mon Jan 16 2006 Ralf Corsépius <rc040203@freenet.de> - 3.1901-1
- Spec cleanup.
- Filter Provides: perl(main).
- Upstream update.

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Tue Jan  4 2005 Ville Skyttä <ville.skytta at iki.fi> - 0:3.18-2
- Don't install htmltree into %%{_bindir} but include it in docs.

* Sat Dec  4 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:3.18-0.fdr.1
- First build.
