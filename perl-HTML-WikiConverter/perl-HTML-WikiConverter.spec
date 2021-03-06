Name:           perl-HTML-WikiConverter
Version:        0.68
Release:        10%{?dist}
Summary:        Perl module to convert HTML to wiki markup
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/HTML-WikiConverter/
Source0:        http://www.cpan.org/authors/id/D/DI/DIBERRI/HTML-WikiConverter-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(Class::Data::Inheritable) >= 0.02
BuildRequires:  perl(CSS) >= 1.07
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTML::Element)
BuildRequires:  perl(HTML::Entities) >= 1.27
BuildRequires:  perl(HTML::Tagset) >= 3.04
BuildRequires:  perl(HTML::Tree) >= 3.18
BuildRequires:  perl(Params::Validate) >= 0.77
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(URI) >= 1.35
BuildRequires:  perl(URI::Escape)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
HTML::WikiConverter is an HTML to wiki converter. It can convert HTML source
into a variety of wiki markups, called wiki "dialects". 

This package contains the perl modules; install the "html2wiki" package for the
application itself.

%package -n html2wiki
Summary:        Convert HTML to wiki markup
Group:          Applications/Publishing
Requires:       %{name} = %{version}-%{release}

%description -n html2wiki
A command line tool to convert pages in HTML to Wiki markup. Various wiki
dialects are supported.


%prep
%setup -q -n HTML-WikiConverter-%{version}
find webapp-install cgi/* -type f | xargs chmod 0644


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
%doc Changes LICENSE README webapp-install cgi
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files -n html2wiki
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.68-10
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.68-9
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.68-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.68-7
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.68-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 17 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.68-5
- 661697 rebuild for fixing problems with vendorach/lib

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.68-4
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.68-3
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.68-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May 05 2009 Iain Arnell 0.68-1
- Specfile autogenerated by cpanspec 1.77.
- Create sub-package for html2wiki
