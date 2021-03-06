Name:           perl-CGI-Application-Server
Version:        0.062
Release:        9%{?dist}
Summary:        Simple HTTP server for developing with CGI::Application
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/CGI-Application-Server/
Source0:        http://www.cpan.org/authors/id/R/RJ/RJBS/CGI-Application-Server-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  perl(CGI)
BuildRequires:  perl(CGI::Application)
BuildRequires:  perl(CGI::Application::Plugin::Redirect)
BuildRequires:  perl(CGI::Application::Dispatch)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Server::Simple)
BuildRequires:  perl(HTTP::Server::Simple::Static)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::HTTP::Server::Simple)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::WWW::Mechanize)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This is a simple HTTP server for for use during development with
CGI::Application. At this moment, it serves our needs in a very basic way.
The plan is to release early and release often, and add features when we
need them. That said, we welcome any and all patches, tests and feature
requests (the ones with which are accompanied by failing tests will get
priority).

%prep
%setup -q -n CGI-Application-Server-%{version}

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
%doc ChangeLog README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.062-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 02 2012 Petr Pisar <ppisar@redhat.com> - 0.062-8
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.062-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.062-6
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.062-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.062-4
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Dec 10 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.062-3
- Add BR: perl(CGI) (Fix FTBFS: BZ 661027).

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.062-2
- Mass rebuild with perl-5.12.0

* Thu Jan 21 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.062-1
- Update to 0.062

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.061-3
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.061-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 02 2009 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 0.061-1
- Update to 0.061

* Mon Dec 22 2008 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 0.060-1
- Specfile autogenerated by cpanspec 1.77.
