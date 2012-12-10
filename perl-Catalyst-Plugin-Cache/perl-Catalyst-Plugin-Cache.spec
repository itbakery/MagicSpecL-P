Name:           perl-Catalyst-Plugin-Cache
Version:        0.10
Release:        8%{?dist}
Summary:        Flexible caching support for Catalyst
License:        (GPL+ or Artistic) or MIT
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Catalyst-Plugin-Cache/
Source0:        http://www.cpan.org/authors/id/B/BO/BOBTFISH/Catalyst-Plugin-Cache-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(Catalyst) >= 5.7
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(Class::Data::Inheritable)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(Task::Weaken)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::WWW::Mechanize::Catalyst)
Requires:       perl(Class::Accessor::Fast)
Requires:       perl(Class::Data::Inheritable)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
This plugin gives you access to a variety of systems for caching data. It
allows you to use a very simple configuration API, while maintaining the
possibility of flexibility when you need it later.

%prep
%setup -q -n Catalyst-Plugin-Cache-%{version}

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
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Dec 10 2012 Liu Di <liudidi@gmail.com> - 0.10-8
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.10-7
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.10-6
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.10-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.10-2
- 661697 rebuild for fixing problems with vendorach/lib

* Fri May 28 2010 Iain Arnell <iarnell@gmail.com> 0.10-1
- update to latest upstream

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.09-2
- Mass rebuild with perl-5.12.0

* Tue Mar 09 2010 Iain Arnell <iarnell@gmail.com> 0.09-1
- update to latest upstream version
- br perl(Class::Data::Inheritable)
- use perl_default_filter and DESTDIR

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.08-4
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 03 2009 Iain Arnell <iarnell@gmail.com> 0.08-2
- add missing requires

* Sun May 03 2009 Iain Arnell <iarnell@gmail.com> 0.08-1
- Specfile autogenerated by cpanspec 1.77.
- remove explicit requires
