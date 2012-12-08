Name:		perl-aliased
Version:	0.30
Release:	11%{?dist}
Summary:	Use shorter versions of class names
License:	GPL+ or Artistic
Group:		Development/Libraries
URL:		http://search.cpan.org/dist/aliased/
Source0:	http://search.cpan.org/CPAN/authors/id/O/OV/OVID/aliased-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(id -nu)
BuildArch:	noarch
BuildRequires:	perl(Exporter)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Pod::Coverage)
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
aliased is simple in concept but is a rather handy module. It loads the
class you specify and exports into your namespace a subroutine that returns
the class name. You can explicitly alias the class to another name or, if
you prefer, you can do so implicitly. In the latter case, the name of the
subroutine is the last part of the class name.

%prep
%setup -q -n aliased-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -depth -type d -exec rmdir {} \; 2>/dev/null
%{_fixperms} %{buildroot}

%check
./Build test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/aliased.pm
%{_mandir}/man3/aliased.3pm*

%changelog
* Sat Dec 08 2012 Liu Di <liudidi@gmail.com> - 0.30-11
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.30-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 0.30-9
- Perl 5.16 rebuild

* Mon Jan 16 2012 Paul Howarth <paul@city-fan.org> - 0.30-8
- Spec clean-up:
  - BR: perl(Exporter)
  - Make %%files list more explicit
  - Don't use macros for commands
  - Use tabs

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.30-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.30-6
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.30-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 14 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.30-4
- Rebuild to fix problems with vendorarch/lib (#661697)

* Thu Apr 29 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.30-3
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.30-2
- rebuild against perl 5.10.1

* Sat Aug 22 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.30-1
- auto-update to 0.30 (by cpan-spec-update 0.01)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed May 28 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.22-1
- update to 0.22

* Wed Mar  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.21-2
- rebuild for new perl

* Fri Mar 30 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.21-1
- update to 0.21

* Thu Oct 12 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.20-2
- bump

* Mon Oct 09 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.20-1
- Specfile autogenerated by cpanspec 1.69.
