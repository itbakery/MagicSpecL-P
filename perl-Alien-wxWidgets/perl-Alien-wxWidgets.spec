Name:           perl-Alien-wxWidgets
Version:        0.51
Release:        8%{?dist}
Summary:        Building, finding and using wxWidgets binaries

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Alien-wxWidgets/
Source0:        http://search.cpan.org/CPAN/authors/id/M/MB/MBARBON/Alien-wxWidgets-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  wxGTK-devel
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# No binaries in this package
%define debug_package %{nil}

%description
"Alien::wxWidgets" can be used to detect and get configuration
settings from an installed wxWidgets.


%prep
%setup -q -n Alien-wxWidgets-%{version}


%build
%{__perl} Build.PL installdirs=vendor < /dev/null
./Build


%install
rm -rf $RPM_BUILD_ROOT
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
chmod -R u+w $RPM_BUILD_ROOT/*


%check
./Build test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes
%{perl_vendorarch}/Alien/
%{_mandir}/man3/*.3pm*


%changelog
* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.51-8
- 为 Magic 3.0 重建

* Fri Jan 27 2012 Liu Di <liudidi@gmail.com> - 0.51-7
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.51-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.51-5
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.51-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 14 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.51-3
- 661697 rebuild for fixing problems with vendorach/lib

* Wed Jul 14 2010 Dan Horák <dan@danny.cz> - 0.51-2
- rebuilt against wxGTK-2.8.11-2

* Mon May 17 2010 Petr Pisar <ppisar@redhat.com> - 0.51-1
- Version bump
- Remove perl-Alien-wxWidgets-SONAME.patch

* Thu Apr 29 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.44-4
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.44-3
- rebuild against perl 5.10.1

* Mon Aug 24 2009 Stepan Kasal <skasal@redhat.com> - 0.44-2
- fix the soname patch

* Thu Aug 20 2009 Stepan Kasal <skasal@redhat.com> - 0.44-1
- new upstream version
- add patch to remember the canonical sonames of libraries, so that
  perl-Wx runs without wxGTK-devel

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.42-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.42-1
- 0.42

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.32-4
- Rebuild for perl 5.10 (again)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.32-3
- Autorebuild for GCC 4.3

* Tue Feb  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.32-2
- rebuild for new perl

* Wed Nov 28 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 0.32-1
- Update to 0.32

* Sat Mar 31 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.31-1
- Update to 0.31.

* Fri Mar 23 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.30-1
- Update to 0.30.

* Sun Mar 18 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.29-1
- Update to 0.29.

* Wed Dec 20 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.27-1
- Update to 0.27.

* Sat Dec 16 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.26-1
- Update to 0.26.

* Sat Dec 16 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.25-2
- Rebuild (wxGTK 2.8.0).

* Sat Nov 11 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.25-1
- Update to 0.25.

* Sat Oct 21 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.24-1
- Update to 0.24.

* Thu Oct 19 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.23-1
- Update to 0.23.

* Tue Oct  3 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.22-1
- Update to 0.22.
- Avoid creation of the debuginfo package (#209180).
- Dropped patch Alien-wxWidgets-0.21-Any_wx_config.pm.patch
  (http://rt.cpan.org/Public/Bug/Display.html?id=21854).

* Sun Oct  1 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.21-3
- Patch to add /usr/lib64 to the library search path.

* Thu Sep 28 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.21-2
- This is a binary RPM (see bug #208007 comment #2).

* Sun Sep 24 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.21-1
- First build.
