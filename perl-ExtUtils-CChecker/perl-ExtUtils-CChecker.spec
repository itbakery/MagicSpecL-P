Name:           perl-ExtUtils-CChecker
Version:        0.04
Release:        6%{?dist}
Summary:        Configure-time utilities for using C headers, libraries, or OS features
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/ExtUtils-CChecker/
Source0:        http://www.cpan.org/authors/id/P/PE/PEVANS/ExtUtils-CChecker-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.00
Requires:       perl(ExtUtils::CBuilder)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Often Perl modules are written to wrap functionality found in existing C
headers, libraries, or to use OS-specific features. It is useful in the
Build.PL or Makefile.PL file to check for the existence of these
requirements before attempting to actually build the module.

%prep
%setup -q -n ExtUtils-CChecker-%{version}

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
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.04-6
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.04-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.04-2
- 661697 rebuild for fixing problems with vendorach/lib

* Sun Aug 22 2010 Nicolas Chauvet <kwizart@gmail.com> - 0.04-1
- Update to 0.04

* Tue Jun 22 2010 Nicolas Chauvet <kwizart@gmail.com> - 0.03-2
- rebuilt for perl 

* Mon Apr 19 2010 Nicolas Chauvet <kwizart@fedoraproject.org> - 0.03-1
- Specfile autogenerated by cpanspec 1.78.
