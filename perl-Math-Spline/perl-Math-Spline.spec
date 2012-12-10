Name:           perl-Math-Spline
Version:        0.01
Release:        13%{?dist}
Summary:        Cubic Spline Interpolation of data
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Math-Spline/
Source0:        http://www.cpan.org/modules/by-module/Math/Math-Spline-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This package provides cubic spline interpolation of numeric data. The data
is passed as references to two arrays containing the x and y ordinates. It
may be used as an exporter of the numerical functions or, more easily as a
class module.

%prep
%setup -q -n Math-Spline-%{version}

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
%doc README Release
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Dec 10 2012 Liu Di <liudidi@gmail.com> - 0.01-13
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.01-12
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.01-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.01-10
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.01-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.01-8
- 661697 rebuild for fixing problems with vendorach/lib

* Mon May 03 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.01-7
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.01-6
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.01-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.01-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 08 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.01-3
- rebuild for new perl

* Tue Sep 04 2007 Alex Lancaster <alexl@users.sourceforge.net> 0.01-2
- Clarified license terms: GPL+ or Artistic

* Fri Mar 23 2007 Alex Lancaster <alexl@users.sourceforge.net> 0.01-1
- Add perl(ExtUtils::MakeMaker) BR.
- Specfile autogenerated by cpanspec 1.69.1.
