Name:           perl-HTML-StripScripts
Version:        1.05
Release:        6%{?dist}
Summary:        Strip scripting constructs out of HTML
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/HTML-StripScripts/
Source0:        http://search.cpan.org/CPAN/authors/id/D/DR/DRTECH/HTML-StripScripts-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module strips scripting constructs out of HTML, leaving as much non-
scripting markup in place as possible. This allows web applications to
display HTML originating from an untrusted source without introducing XSS
(cross site scripting) vulnerabilities.

%prep
%setup -q -n HTML-StripScripts-%{version}

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


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 1.05-6
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.05-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 17 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.05-2
- 661697 rebuild for fixing problems with vendorach/lib

* Tue Dec 14 2010 Xavier Bachelot <xavier@bachelot.org> 1.05-1
- Update to 1.05.
- Update Source0 URL.

* Sun Dec 12 2010 Iain Arnell <iarnell@gmail.com> 1.04-5
- doesn't require perl(Test::More)

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.04-4
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.04-3
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Apr 25 2009 Xavier Bachelot <xavier@bachelot.org> 1.04-1
- Specfile autogenerated by cpanspec 1.77.
- Fix BR:s.
