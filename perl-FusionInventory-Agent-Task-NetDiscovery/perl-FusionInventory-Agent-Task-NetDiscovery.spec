Name:           perl-FusionInventory-Agent-Task-NetDiscovery
Version:        1.5
Release:        5%{?dist}
Summary:        Network discovery support for FusionInventory Agent
License:        GPLv2+
Group:          Development/Libraries

URL:            http://forge.fusioninventory.org/projects/fusioninventory-agent-task-netdiscovery
Source0:        http://search.cpan.org/CPAN/authors/id/F/FU/FUSINV/FusionInventory-Agent-Task-NetDiscovery-%{version}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker) perl(Module::Install)
# For tests
BuildRequires:  perl(FusionInventory::Agent) >= 2.0
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XML::TreePP)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(FusionInventory::Agent) >= 2.0
Requires:       perl(XML::SAX)
# Optional (but recommended) dependencies
Requires:       perl(Parallel::ForkManager)
Requires:       perl(Net::SNMP)
Requires:       perl(Net::NBName)
Requires:       nmap

%{?perl_default_filter}


%description
This module scans your networks to get information from devices with
SNMP protocol.


%prep
%setup -q -n FusionInventory-Agent-Task-NetDiscovery-%{version}


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
%doc AUTHORS Changes LICENSE README THANKS
%{perl_vendorlib}/FusionInventory/Agent/Task/NetDiscovery*
%{_mandir}/man3/FusionInventory*


%changelog
* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 1.5-5
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 1.5-4
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat May 28 2011 Remi Collet <Fedora@famillecollet.com> 1.5-2
- add dependency on perl(XML::SAX)

* Mon May  9 2011 Remi Collet <Fedora@famillecollet.com> 1.5-1
- update to 1.5
  http://cpansearch.perl.org/src/FUSINV/FusionInventory-Agent-Task-NetDiscovery-1.5/Changes

* Wed Mar 30 2011 Remi Collet <Fedora@famillecollet.com> 1.4-1
- update to 1.4

* Wed Mar 30 2011 Remi Collet <Fedora@famillecollet.com> 1.3-1
- update to 1.3

* Mon Aug 16 2010 Remi Collet <Fedora@famillecollet.com> 1.2-1
- update to 1.2

* Mon May 17 2010 Remi Collet <Fedora@famillecollet.com> 1.1-1
- Specfile autogenerated by cpanspec 1.78.
- spec cleanup

