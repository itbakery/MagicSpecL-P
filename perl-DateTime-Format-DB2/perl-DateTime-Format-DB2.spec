Name:           perl-DateTime-Format-DB2
Version:        0.05
Release:        12%{?dist}
Summary:        Parse and format DB2 dates and times
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/DateTime-Format-DB2/
Source0:        http://www.cpan.org/authors/id/J/JR/JROBINSON/DateTime-Format-DB2-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Format::Builder)
BuildRequires:  perl(ExtUtils::MakeMaker)
# tests
BuildRequires:  perl(Test::More)

# not picked up automatically 
Requires:       perl(DateTime::Format::Builder)

%description
This module understands the formats used by DB2 for its DATE, TIME, and
TIMESTAMP data types. It can be used to parse these formats in order to
create DateTime objects, and it can take a DateTime object and produce a
string representing it in the DB2 format.

%prep
%setup -q -n DateTime-Format-DB2-%{version}

chmod -c -x t/*

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
%doc Changes t/
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.05-12
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.05-11
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.05-9
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.05-7
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.05-6
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.05-5
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jul 22 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.05-2
- bump

* Wed Jul 16 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.05-1
- Specfile autogenerated by cpanspec 1.74.
