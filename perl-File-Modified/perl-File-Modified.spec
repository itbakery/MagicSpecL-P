Name:           perl-File-Modified
Version:        0.07
Release:        15%{?dist}
Summary:        Checks intelligently if files have changed
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/File-Modified/
Source0:        http://www.cpan.org/authors/id/C/CO/CORION/File-Modified-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# make TODO tests fail properly :)
Patch0:         tests.patch

# core
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Digest::MD5)
# tests
BuildRequires:  perl(Digest::MD2)
BuildRequires:  perl(Digest::SHA1)
BuildRequires:  perl(Test::Exception)

%description
The Modified module is intended as a simple method for programs to detect
whether configuration files (or modules they rely on) have changed. There
are currently two methods of change detection implemented, mtime and MD5.
The MD5 method will fall back to use timestamps if the Digest::MD5 module
cannot be loaded.

%prep
%setup -q -n File-Modified-%{version}
%patch0

# source cleanup
find . -type f -exec chmod -c -x {} \;
sed -i 's/\r//' README bug.txt

# hey, you guys shouldn't be here!
# http://rt.cpan.org/Ticket/Display.html?id=26843
find . -type f -name .cvsignore -exec rm -v {} \;
sed -i '/^.*cvsignore$/d' MANIFEST

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
# we expect two tests to be skipped -- perl(Digest) is _always_ installed


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
# note: example/ deliberately left out -- useless
%doc bug.txt Changes MANIFEST.skip README t/
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Dec 09 2012 Liu Di <liudidi@gmail.com> - 0.07-15
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.07-14
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.07-12
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.07-10
- 661697 rebuild for fixing problems with vendorach/lib

* Sat May 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.07-9
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.07-8
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Mar 05 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.07-5
- rebuild for new perl

* Thu May 03 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.07-4
- bump

* Mon Apr 30 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.07-3
- comments, keep Makefile.PL from complaining about missing .cvsignore files

* Sun Apr 29 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.07-2
- patch tests to enable successful failure of one TODO test :)

* Tue Apr 10 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.07-1
- Specfile autogenerated by cpanspec 1.70.
