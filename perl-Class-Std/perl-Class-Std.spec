Name:           perl-Class-Std
Version:        0.0.8
Release:        13%{?dist}
Summary:        Support for creating standard "inside-out" classes
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Class-Std/
Source0:        http://www.cpan.org/modules/by-module/Class/Class-Std-v%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(Module::Build), perl(version), perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Pod::Coverage)
Requires:       perl(version)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module provides tools that help to implement the "inside out object"
class structure in a convenient and standard way.

%prep
%setup -q -n Class-Std-v%{version}

# Fix UTF-8
iconv -f ISO_8859-1 -t UTF-8 -o tmp.man lib/Class/Std.pm &&
mv -f tmp.man lib/Class/Std.pm

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
rm -rf %{buildroot}

./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
./Build test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Dec 10 2012 Liu Di <liudidi@gmail.com> - 0.0.8-13
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.0.8-12
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.0.8-10
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.0.8-8
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.0.8-7
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.0.8-6
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.0.8-3
Rebuild for new perl

* Sun Jan 20 2008 Andreas Thienemann <andreas@bawue.net> - 0.0.8-2
- Added changed BuildReqs to handle changed Perl packaging in fedora (bz
- Detailed License to specify "GPL2 or later" clause
- Thx to Ralf Corsépius for the heads up

* Thu Mar 15 2007 Andreas Thienemann <andreas@bawue.net> - 0.0.8-1
- Specfile autogenerated by cpanspec 1.69.1.
- Adapted for FE
