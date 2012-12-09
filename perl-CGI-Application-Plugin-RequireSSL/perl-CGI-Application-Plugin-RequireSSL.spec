Name:           perl-CGI-Application-Plugin-RequireSSL
Version:        0.04
Release:        6%{?dist}
Summary:        Force SSL in specified pages or modules
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/CGI-Application-Plugin-RequireSSL/
Source0:        http://www.cpan.org/authors/id/D/DH/DHORNE/CGI-Application-Plugin-RequireSSL-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(CGI)
BuildRequires:  perl(CGI::Application)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
CGI::Application::Plugin::RequireSSL allows individual run modes or whole
modules to be protected by SSL. If a standard HTTP request is received, you
can specify whether an error is raised or if the request should be
redirected to the HTTPS equivalent URL.

%prep
%setup -q -n CGI-Application-Plugin-RequireSSL-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check



%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Dec 09 2012 Liu Di <liudidi@gmail.com> - 0.04-6
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.04-5
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.04-4
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.04-2
- Perl mass rebuild

* Thu Nov 25 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 0.04-1
- Specfile autogenerated by cpanspec 1.78.
