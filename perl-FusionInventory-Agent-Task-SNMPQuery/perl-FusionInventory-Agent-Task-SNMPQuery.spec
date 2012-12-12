Name:           perl-FusionInventory-Agent-Task-SNMPQuery
Version:        1.3
Release:        4%{?dist}
Summary:        SNMP Query support for FusionInventory Agent
License:        GPLv2+
Group:          Development/Libraries

URL:            http://forge.fusioninventory.org/projects/fusioninventory-agent-task-snmpquery
Source0:        http://search.cpan.org/CPAN/authors/id/F/FU/FUSINV/FusionInventory-Agent-Task-SNMPQuery-%{version}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  perl(ExtUtils::MakeMaker) perl(Module::Install)
# For tests
BuildRequires:  perl(FusionInventory::Agent) >= 2.0
BuildRequires:  perl(Test::More)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(FusionInventory::Agent) >= 2.0
# Optional (but recommended) dependencies
Requires:       perl(Parallel::ForkManager)
Requires:       perl(Net::SNMP)

%{?perl_default_filter}


%description
SNMP Query support for FusionInventory Agent


%prep
%setup -q -n FusionInventory-Agent-Task-SNMPQuery-%{version}


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
%{perl_vendorlib}/FusionInventory/Agent/Task/SNMPQuery*


%changelog
* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 1.3-4
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 1.3-3
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Mar 30 2011 Remi Collet <Fedora@famillecollet.com> 1.3-1
- update to 1.3
  http://cpansearch.perl.org/src/FUSINV/FusionInventory-Agent-Task-SNMPQuery-1.3/Changes

* Mon Aug 16 2010 Remi Collet <Fedora@famillecollet.com> 1.2-1
- update to 1.2

* Tue May 18 2010 http://blog.famillecollet.com 1.1-1
- Specfile autogenerated by cpanspec 1.78.
- spec cleanup

