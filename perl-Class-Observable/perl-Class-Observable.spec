Name:           perl-Class-Observable
Version:        1.04
Release:        14%{?dist}
Summary:        Allow other classes and objects to respond to events in yours
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Class-Observable/
Source0:        http://www.cpan.org/modules/by-module/Class/Class-Observable-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildRequires:  perl(ExtUtils::MakeMaker), perl(Test::More), perl(Class::ISA)


%description
If you have ever used Java, you may have run across the
java.util.Observable class and the java.util.Observer interface. With them
you can decouple an object from the one or more objects that wish to be
notified whenever particular events occur.

%prep
%setup -q -n Class-Observable-%{version}

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
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Dec 09 2012 Liu Di <liudidi@gmail.com> - 1.04-14
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 1.04-13
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jun 19 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.04-11
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.04-9
- 661697 rebuild for fixing problems with vendorach/lib
- add missing BR Class::ISA

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.04-8
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 1.04-7
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.04-4
- rebuild for new perl

* Sun Jan 27 2008 Andreas Thienemann <andreas@bawue.net> 1.04-3
- Added Test::More to the BuildReqs

* Sat Mar 17 2007 Andreas Thienemann <andreas@bawue.net> 1.04-2
- Fixed BuildReq to pull in perl-devel in a portable way

* Thu Mar 15 2007 Andreas Thienemann <andreas@bawue.net> 1.04-1
- Specfile autogenerated by cpanspec 1.69.1.
- Cleaned up for FE
