Name:           perl-AnyEvent-DBus
Version:        0.31
Release:        9%{?dist}
Summary:        Adapt Net::DBus to AnyEvent
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/AnyEvent-DBus/
Source0:        http://www.cpan.org/authors/id/M/ML/MLEHMANN/AnyEvent-DBus-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(Net::DBus)
BuildRequires:  perl(common::sense)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))


%description
Loading this module will install the necessary magic to seamlessly integrate
Net::DBus into AnyEvent.


%prep
%setup -q -n AnyEvent-DBus-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf %{buildroot}

make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*


%check



%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc Changes COPYING META.json README
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.31-9
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.31-8
- 为 Magic 3.0 重建

* Sat Jan 28 2012 Liu Di <liudidi@gmail.com> - 0.31-7
- 为 Magic 3.0 重建

* Fri Jan 27 2012 Liu Di <liudidi@gmail.com> - 0.31-6
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.31-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 0.31-4
- Perl mass rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 0.31-3
- Perl mass rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.31-2
- Perl mass rebuild

* Tue Jan 25 2011 Mathieu Bridon <bochecha@fedoraproject.org> 0.31-1
- Specfile autogenerated by cpanspec 1.78.
- Fixed description and license.
- Added missing BRs
