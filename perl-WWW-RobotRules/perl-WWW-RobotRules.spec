Name:           perl-WWW-RobotRules
Version:        6.02
Release:        6%{?dist}
Summary:        Database of robots.txt-derived permissions
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/WWW-RobotRules/
Source0:        http://www.cpan.org/authors/id/G/GA/GAAS/WWW-RobotRules-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(AnyDBM_File)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(URI) >= 1.10
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(URI) >= 1.10
Conflicts:      perl-libwww-perl < 6

# Remove underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(URI\\)$
# Do not provide private imlementation of abstract class methods
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}perl\\(WWW::RobotRules::InCore\\)

%description
This module parses /robots.txt files as specified in "A Standard for Robot
Exclusion", at <http://www.robotstxt.org/wc/norobots.html>. Webmasters can
use the /robots.txt file to forbid conforming robots from accessing parts
of their web site.

%prep
%setup -q -n WWW-RobotRules-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check


%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 6.02-6
- 为 Magic 3.0 重建

* Mon Sep 03 2012 Petr Pisar <ppisar@redhat.com> - 6.02-5
- Drop useless build-requires LWP::RobotUA and URI::URL (bug #853147)

* Mon Aug 27 2012 Jitka Plesnikova <jplesnik@redhat.com> - 6.02-4
- Specify all dependencies.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.02-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 6.02-2
- Perl 5.16 rebuild

* Mon Feb 20 2012 Petr Pisar <ppisar@redhat.com> - 6.02-1
- 6.02 bump

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.01-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jul 24 2011 Iain Arnell <iarnell@gmail.com> 6.01-3
- update filtering for rpm 4.9

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 6.01-2
- Perl mass rebuild

* Thu Mar 17 2011 Petr Pisar <ppisar@redhat.com> 6.01-1
- Specfile autogenerated by cpanspec 1.78.
- Remove BuildRoot stuff
- Conflicts with perl-libwww-perl-5* and older
