Name:           perl-Array-Diff
Version:        0.07
Release:        9%{?dist}
# Because 0.07 compares newer than 0.05002 in Perl world
# but not in RPM world :-(
Epoch:          1
Summary:        Diff two arrays
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Array-Diff/
Source0:        http://www.cpan.org/authors/id/T/TY/TYPESTER/Array-Diff-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(Algorithm::Diff)
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(Module::Install)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module do diff two arrays, and return added and deleted arrays. It's
simple usage of Algorithm::Diff.

%prep
%setup -q -n Array-Diff-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes LICENSE README
%dir %{perl_vendorlib}/Array
%{perl_vendorlib}/Array/Diff.pm
%{_mandir}/man3/*3pm*

%changelog
* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 1:0.07-9
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 1:0.07-8
- 为 Magic 3.0 重建

* Sat Jan 28 2012 Liu Di <liudidi@gmail.com> - 1:0.07-7
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.07-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 1:0.07-5
- Perl mass rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 1:0.07-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 25 2011 Daniel P. Berrange <berrange@redhat.com> - 1:0.07-2
- Bump epoch to ensure 0.07 is considered newer than 0.05002 (rhbz #672463)

* Fri Dec 17 2010 Daniel P. Berrange <berrange@redhat.com> - 0.07-1
- Update to 0.07 release

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.05002-6
- 661697 rebuild for fixing problems with vendorach/lib

* Thu Apr 29 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.05002-5
- Mass rebuild with perl-5.12.0

* Tue Jan 12 2010 Daniel P. Berrange <berrange@redhat.com> - 0.05002-4
- Fix source URL

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.05002-3
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 Daniel P. Berrange <berrange@redhat.com> - 0.05002-1
- Update to new 0.05002 release

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.04-3
- rebuild for new perl

* Fri Dec 21 2007 Daniel P. Berrange <berrange@redhat.com> 0.04-2.fc9
- Added Test::Pod and Test::Pod::Coverage build requires

* Fri Dec 21 2007 Daniel P. Berrange <berrange@redhat.com> 0.04-1.fc9
- Specfile autogenerated by cpanspec 1.73.
