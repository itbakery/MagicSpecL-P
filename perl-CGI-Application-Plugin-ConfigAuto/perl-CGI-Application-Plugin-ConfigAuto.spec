Name:           perl-CGI-Application-Plugin-ConfigAuto
Version:        1.33
Release:        5%{?dist}
Summary:        Easy configuration file management for CGI::Application
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/CGI-Application-Plugin-ConfigAuto/
Source0:        http://www.cpan.org/authors/id/M/MA/MARKSTOS/CGI-Application-Plugin-ConfigAuto-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(CGI)
BuildRequires:  perl(CGI::Application)
BuildRequires:  perl(Config::Auto)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
CGI::Application::Plugin::ConfigAuto adds easy access to configuration file
variables to your CGI::Application modules. Lazy loading is used to prevent
the configuration file from being parsed if no configuration variables are
accessed during the request.

%prep
%setup -q -n CGI-Application-Plugin-ConfigAuto-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
rm -rf $RPM_BUILD_ROOT

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.33-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 19 2012 Petr Pisar <ppisar@redhat.com> - 1.33-4
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.33-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 29 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.33-2
- Perl mass rebuild

* Wed Mar 02 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 1.33-1
- Update to 1.33

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.32-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.32-4
- 661697 rebuild for fixing problems with vendorach/lib

* Sat Dec 11 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 1.32-1
- Add perl(CGI) to BuildRequires (#660762)

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.32-2
- Mass rebuild with perl-5.12.0

* Sat Feb 27 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 1.32-1
- Update to 1.32
- Add perl default filter

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.31-2
- rebuild against perl 5.10.1

* Thu Jul 30 2009 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 1.31-1
- Upate to 1.31

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Dec 22 2008 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 1.30-1
- Specfile autogenerated by cpanspec 1.77.