# Package is noarch from perl 5.13.7
%global noarch_package %(perl -e 'print (($] >= 5.013007) ? 1 : 0);')

Name:		perl-Devel-GlobalDestruction
Version:	0.04
Release:	2%{?dist}
License:	GPL+ or Artistic
Group:		Development/Libraries
Summary:	Expose PL_dirty, the flag that marks global destruction
Url:		http://search.cpan.org/dist/Devel-GlobalDestruction
Source:		http://search.cpan.org/CPAN/authors/id/F/FL/FLORA/Devel-GlobalDestruction-%{version}.tar.gz
%if %{noarch_package}
BuildArch:	noarch
%endif
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(id -nu)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl(XSLoader)
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

# Don't "provide" private Perl libs
%{?perl_default_filter}

%description
Perl's global destruction is a little tricky to deal with with respect to
finalizers because it's not ordered and objects can sometimes disappear.

Writing defensive destructors is hard and annoying, and usually if global
destruction is happening you only need the destructors that free up non
process local resources to actually execute.

For these constructors you can avoid the mess by simply bailing out if
global destruction is in effect.

%prep
%setup -q -n Devel-GlobalDestruction-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} ';' 2>/dev/null
%{_fixperms} %{buildroot}

%check


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc Changes t/
%if %{noarch_package}
%{perl_vendorlib}/Devel/
%else
%{perl_vendorarch}/auto/Devel/
%{perl_vendorarch}/Devel/
%endif
%{_mandir}/man3/Devel::GlobalDestruction.3pm*

%changelog
* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.04-2
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Paul Howarth <paul@city-fan.org> - 0.04-1
- Update to 0.04
  - To detect a perl with ${^GLOBAL_PHASE}, check for the feature itself
    instead of a specific perl version
  - Update the documentation to reflect the use of ${^GLOBAL_PHASE} if available
  - Stop depending on Scope::Guard for the tests
  - Upgrade ppport.h from version 3.13 to 3.19
- Drop no-longer-necessary buildreq perl(Scope::Guard)
- Use DESTDIR rather than PERL_INSTALL_ROOT
- BR: perl(XSLoader)

* Wed Jan 11 2012 Paul Howarth <paul@city-fan.org> - 0.03-3
- Fedora 17 mass rebuild

* Wed Jun 29 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.03-2
- Perl mass rebuild

* Fri Jun 24 2011 Paul Howarth <paul@city-fan.org> - 0.03-1
- Update to 0.03
  - Drop the XS code on perl versions recent enough to have ${^GLOBAL_PHASE}
    (5.13.7 onwards)
  - Require at least Perl 5.6
    - Use XSLoader without a fallback to DynaLoader
    - Use our instead of use vars
- This release by FLORA -> update source URL
- Package is noarch from perl 5.13.7
- Package Changes file
- Use %%{?perl_default_filter}

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.02-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.02-11
- Rebuild to fix problems with vendorarch/lib (#661697)

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.02-10
- Mass rebuild with perl-5.12.0

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.02-9
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.02-8
- rebuild against perl 5.10.1

* Sun Aug 23 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.02-7
- bump

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.02-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 23 2009 Chris Weyl <cweyl@alumni.drew.edu> - 0.02-5
- Stripping bad provides of private Perl extension libs

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.02-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Nov 03 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.02-3
- bump

* Sat Nov 01 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.02-2
- tweak summary

* Sun Oct 26 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.02-1
- clean up for review submission

* Sun Oct 19 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.02-0.1
- initial RPM packaging
- generated with cpan2dist (CPANPLUS::Dist::RPM version 0.0.5)

