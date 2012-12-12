Summary: Internationalization library for Perl, compatible with gettext
Name: perl-libintl
Version: 1.20
Release: 8%{?dist}
License: LGPLv2+
Group: Development/Libraries
URL: http://search.cpan.org/dist/libintl-perl/
Source: http://search.cpan.org/CPAN/authors/id/G/GU/GUIDO/libintl-perl-%{version}.tar.gz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Provides: perl-libintl-perl = %{version}-%{release}
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: gdbm-devel, db4-devel

%description
The package libintl-perl is an internationalization library for Perl that
aims to be compatible with the Uniforum message translations system as
implemented for example in GNU gettext.


%prep
%setup -q -n libintl-perl-%{version}
find -type f -exec chmod -x {} \;
find lib/Locale gettext_xs \( -name '*.pm' -o -name '*.pod' \) \
    -exec sed -i -e '/^#! \/bin\/false/d' {} \;

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f \( -name .packlist -o \
			-name '*.bs' -size 0 \) -exec rm -f {} ';'
find %{buildroot} -depth -type d -empty -exec rmdir {} ';'
chmod -R u+w %{buildroot}/*


%check
%{__make} test


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc ChangeLog COPYING* NEWS README THANKS TODO
%{perl_vendorlib}/Locale/
%{perl_vendorarch}/auto/Locale/
%{_mandir}/man?/*


%changelog
* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 1.20-8
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 1.20-7
- 为 Magic 3.0 重建

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.20-5
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.20-3
- 661697 rebuild for fixing problems with vendorach/lib

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.20-2
- Mass rebuild with perl-5.12.0

* Fri Jan 15 2010 Stepan Kasal <skasal@redhat.com> - 1.20-1
- new upstream version
- better buildroot

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.16-11
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.16-8
- Rebuild for perl 5.10 (again)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.16-7
- Autorebuild for GCC 4.3

* Tue Feb  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.16-6
- rebuild for new perl

* Wed Aug 22 2007 Matthias Saou <http://freshrpms.net/> 1.16-5
- Rebuild for new BuildID feature.

* Mon Aug  6 2007 Matthias Saou <http://freshrpms.net/> 1.16-4
- Update License field.
- Add perl(ExtUtils::MakeMaker) build requirement.

* Mon Aug 28 2006 Matthias Saou <http://freshrpms.net/> 1.16-3
- FC6 rebuild.
- Change spec file back to my own liking...

* Sat Feb 11 2006 Ralf Corsépius <rc040203@freenet.de>  1.16-2
- Rework spec (PR 180767).

* Thu Feb  9 2006 Matthias Saou <http://freshrpms.net/> 1.16-1
- Update to 1.16.

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Tue Nov  9 2004 Matthias Saou <http://freshrpms.net/> 1.11-2
- Fix : Added perl(Locale::gettext_xs) provides.

* Thu Nov  4 2004 Matthias Saou <http://freshrpms.net/> 1.11-1
- Initial RPM release.
