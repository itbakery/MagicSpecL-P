%global subver 1

Name:           perl-AnyEvent
Version:        5.27
Release:        7%{?dist}
Summary:        Framework for multiple event loops

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/AnyEvent/
Source0:        http://search.cpan.org/CPAN/authors/id/M/ML/MLEHMANN/AnyEvent-%{version}%{?subver}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
# Needed for test
BuildRequires:  perl(Test::Simple)

# RPM 4.8 style
%{?filter_setup:
%filter_from_requires /perl(Tk)/d; /perl(EV)/d; /perl(Irssi)/d; /perl(Qt/d; /perl(AnyEvent::Impl::Qt/d
%filter_from_provides /perl(AnyEvent::Impl::Qt/d
%filter_setup
}
# RPM 4.9 style
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}perl(Tk)
%global __requires_exclude %__requires_exclude|perl(EV)
%global __requires_exclude %__requires_exclude|perl(Irssi)
%global __requires_exclude %__requires_exclude|perl(Qt
%global __requires_exclude %__requires_exclude|perl(AnyEvent::Impl::Qt
%global __provides_exclude %{?__provides_exclude:__provides_exclude|}perl(AnyEvent::Impl::Qt

Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
AnyEvent provides an identical interface to multiple event loops. This
allows module authors to utilise an event loop without forcing module users
to use the same event loop (as only a single event loop can coexist
peacefully at any one time).


%prep
%setup -q -n AnyEvent-%{version}%{?subver}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'


%check
# PERL_ANYEVENT_NET_TESTS shoudn't be set to avoid network tests
# on our builder.
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes COPYING README
%{perl_vendorlib}/AE.pm
%{perl_vendorlib}/AnyEvent*
%{_mandir}/man3/*.3*


%changelog
* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.27-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 22 2011 Petr Pisar <ppisar@redhat.com> - 5.27-6
- RPM 4.9 dependency filtering added

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 5.27-5
- Perl mass rebuild

* Thu Feb 10 2011 Nicolas Chauvet <kwizart@gmail.com> - 5.27-4
- Rewritten to new filtering rules
 http://fedoraproject.org/wiki/Packaging:AutoProvidesAndRequiresFiltering#Perl

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 14 2010 Marcela Maslanova <mmaslano@redhat.com> - 5.27-2
- 661697 rebuild for fixing problems with vendorach/lib

* Sun Aug 22 2010 Nicolas Chauvet <kwizart@gmail.com> - 5.27-1
- Update to 5.271 (rpm version : 5.27)

* Thu Apr 29 2010 Nicolas Chauvet <kwizart@fedoraproject.org> - 5.26-1
- Update to 5.261 (rpm version : 5.26)

* Thu Apr 29 2010 Marcela Maslanova <mmaslano@redhat.com> - 5.24-2
- Mass rebuild with perl-5.12.0

* Tue Jan 19 2010 Nicolas Chauvet <kwizart@fedoraproject.org> - 5.24-1
- Update to 5.24  (rpm version : 5.24)

* Mon Dec 7 2009 Nicolas Chauvet <kwizart@fedoraproject.org> - 5.22-1
- Update to 5.22  (rpm version : 5.22)

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 5.11-3
- rebuild against perl 5.10.1

* Mon Aug 31 2009 kwizart < kwizart at gmail.com > - 5.11-2
- Update to 5.112   (rpm version : 5.11 )

* Mon Jul 27 2009 kwizart < kwizart at gmail.com > - 4.870-1
- Update to 4.87   (rpm version : 4.870 )
- Add more filter requires to workaround rhbz#512553

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.820-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 15 2009 kwizart < kwizart at gmail.com > - 4.820-1
- Update to 4.82   (rpm version : 4.820 )

* Fri May 29 2009 kwizart < kwizart at gmail.com > - 4.410-1
- Update to 4.41   (rpm version : 4.41 )

* Wed Apr 22 2009 kwizart < kwizart at gmail.com > - 4.352-1
- Update to 4.352   (rpm version : same )

* Fri Apr  3 2009 kwizart < kwizart at gmail.com > - 4.350-1
- Update to 4.35   (rpm version : 4.350 )

* Thu Mar  5 2009 kwizart < kwizart at gmail.com > - 4.340-1
- Update to 4.34   (rpm version : 4.340 )

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.331-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan 12 2009 kwizart < kwizart at gmail.com > - 4.331-1
- Update to 4.331   (rpm version : same )

* Fri Oct 17 2008 kwizart < kwizart at gmail.com > - 4.300-1
- Update to 4.3   (rpm version : 4.300 )

* Tue Oct 14 2008 kwizart < kwizart at gmail.com > - 4.3-1
- Update to 4.3 

* Mon Aug  4 2008 kwizart < kwizart at gmail.com > - 4.231-1
- Update to 4.231 (rpm version : match )

* Fri Jul 18 2008 kwizart < kwizart at gmail.com > - 4.220-1
- Update to 4.22 (rpm version : 4.220 )

* Fri Jul 18 2008 kwizart < kwizart at gmail.com > - 4.21-1
- Update to 4.21

* Fri Jul  4 2008 kwizart < kwizart at gmail.com > - 4.161-1
- Update to 4.161

* Mon Jun 23 2008 kwizart < kwizart at gmail.com > - 4.152-1
- Update to 4.152

* Mon Jun  9 2008 kwizart < kwizart at gmail.com > - 4.151-1
- Update to 4.151

* Thu Jun  5 2008 kwizart < kwizart at gmail.com > - 4.13-1
- Update to 4.13

* Tue Jun  3 2008 kwizart < kwizart at gmail.com > - 4.12-1
- Update to 4.12

* Thu May 29 2008 kwizart < kwizart at gmail.com > - 4.1-1
- Update to 4.1

* Tue May 27 2008 kwizart < kwizart at gmail.com > - 3.5-1
- Update to 3.5

* Wed Apr 30 2008 kwizart < kwizart at gmail.com > - 3.3-1
- Initial package for Fedora

