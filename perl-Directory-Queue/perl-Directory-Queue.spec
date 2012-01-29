Name:           perl-Directory-Queue
Version:        1.4
Release:        3%{?dist}
Summary:        Object oriented interface to a directory based queue
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Directory-Queue/
Source0:        http://search.cpan.org/CPAN/authors/id/L/LC/LCONS/Directory-Queue-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Time::HiRes)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))



%{?perl_default_subpackage_tests}

%description
The goal of this module is to offer a simple queue system using the
underlying file system for storage, security and to prevent race conditions
via atomic operations. It focuses on simplicity, robustness and
scalability.

%prep
%setup -q -n Directory-Queue-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 1.4-3
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 8 2011 Steve Traylen <steve.traylen@cern.ch> - 1.4-1
- Update 1.4 rhbz#760472.

* Tue Aug 30 2011 Steve Traylen <steve.traylen@cern.ch> - 1.2-1
- Update 1.2 rhbz#73941.

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.1-2
- Perl mass rebuild

* Mon May 2 2011 Steve Traylen <steve.traylen@cern.ch> 1.1-1
- New upstream 1.1.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.0-3
- 661697 rebuild for fixing problems with vendorach/lib

* Tue Aug 31 2010 Steve Traylen <steve.traylen@cern.ch> 1.0-2
- perl(Time::HiRes) needed explicity on el4 and el6? 
  Just buildrequire it everywhere.

* Tue Aug 31 2010 Steve Traylen <steve.traylen@cern.ch> 1.0-1
- New upstream 1.0.

* Sun Jun 27 2010 Steve Traylen <steve.traylen@cern.ch> 0.5-3
- Rebuilt due to cvs mistake.

* Sun Jun 27 2010 Steve Traylen <steve.traylen@cern.ch> 0.5-2
- Explicit perl(Time::HiRes) br on EL4 added.

* Mon Jun 21 2010 Steve Traylen <steve.traylen@cern.ch> 0.5-1
- Specfile autogenerated by cpanspec 1.78.
- Add tests rpm generation  macro.
- Change PERL_INSTALL_DIR for DESTDIR.
- Add br perl(Test::Pod::Coverage) and perl(Test::Pod)
- Remove r of perl(Test::More)

