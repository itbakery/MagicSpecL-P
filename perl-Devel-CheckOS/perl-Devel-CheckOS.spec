Name:           perl-Devel-CheckOS
Version:        1.64
Release:        7%{?dist}
Summary:        Check what OS we're running on
License:        GPLv2 or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Devel-CheckOS/
Source0:        http://www.cpan.org/authors/id/D/DC/DCANTRELL/Devel-CheckOS-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find::Rule) >= 0.28
BuildRequires:  perl(Test::More) >= 0.62
# Tests only:
BuildRequires:  perl(Data::Compare) >= 1.21
BuildRequires:  perl(File::Temp) >= 0.19
BuildRequires:  perl(Test::More) >= 0.62
BuildRequires:  perl(Test::Pod) >= 1.00
Requires:       perl(Data::Compare) >= 1.21
Requires:       perl(File::Find::Rule) >= 0.28
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# Remove unversioned requires
# RPM 4.8 style
%filter_from_requires /perl(Data::Compare)$/d /perl(File::Find::Rule)$/d
%filter_setup
# RPM 4.9 style
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}perl\\(Data::Compare\\)$
%global __requires_exclude %__requires_exclude|perl\\(File::Find::Rule\\)$

%description
Devel::CheckOS provides a more friendly interface to $^O, and also lets you
check for various OS "families" such as "Unix", which includes things like
Linux, Solaris, AIX etc.

%prep
%setup -q -n Devel-CheckOS-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

# delete wrong tests, which breaks succesful build
# this wasn't written whole
rm -rf t/50-script.t
# this is testing installation, which can't pass
rm -rf t/XX-autodetected-linux-as-Y.t

%check


%files
%defattr(-,root,root,-)
%doc ARTISTIC.txt CHANGES GPL2.txt README TODO
%{_bindir}/use-devel-assertos
%{perl_vendorlib}/*
%{_mandir}/man1/use-devel-assertos.1.gz
%{_mandir}/man3/*

%changelog
* Mon Dec 10 2012 Liu Di <liudidi@gmail.com> - 1.64-7
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 1.64-6
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.64-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul 25 2011 Petr Pisar <ppisar@redhat.com> - 1.64-4
- RPM 4.9 dependency filtering added

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 1.64-3
- Perl mass rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 1.64-2
- Perl mass rebuild

* Wed Apr 27 2011 Marcela Mašláňová <mmaslano@redhat.com> 1.64-1
- update to 1.64

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.63-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.63-2
- 661697 rebuild for fixing problems with vendorach/lib

* Tue Sep 14 2010 Petr Pisar <ppisar@redhat.com> - 1.63-1
- 1.63 bump
- Remove `dontask' patch as interactive code is not run anymore
- Add versioned Requires, filter unversioned ones out

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.50-7
- Mass rebuild with perl-5.12.0

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.50-6
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.50-5
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.50-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.50-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec 17 2008 Marcela Mašláňová <mmaslano@redhat.com> 1.50-2
- remove two tests, because they can't pass in rpmbuild.

* Tue Dec 16 2008 Marcela Mašláňová <mmaslano@redhat.com> 1.50-1
- Specfile autogenerated by cpanspec 1.77.
