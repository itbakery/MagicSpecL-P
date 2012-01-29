Name:           perl-IO-AIO
Version:        3.71
Release:        5%{?dist}
Summary:        Asynchronous Input/Output
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/IO-AIO/
Source0:        http://search.cpan.org/CPAN/authors/id/M/ML/MLEHMANN/IO-AIO-%{version}.tar.gz
BuildRequires:  perl(common::sense)
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
This module implements asynchronous I/O using whatever means your operating
system supports.

%prep
%setup -q -n IO-AIO-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}

# Remove script we don't want packaged
rm %{buildroot}%{_bindir}/treescan

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} \; 2>/dev/null
%{_fixperms} %{buildroot}

%check


%files
%defattr(-,root,root,-)
%doc Changes COPYING README
%{perl_vendorarch}/auto/IO/
%{perl_vendorarch}/IO/
%{_mandir}/man3/IO::AIO.3pm*

%changelog
* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 3.71-5
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.71-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jun 19 2011 Marcela Mašláňová <mmaslano@redhat.com> - 3.71-3
- Perl mass rebuild

* Thu Mar 10 2011 Paul Howarth <paul@city-fan.org> - 3.71-2
- Spec cleanup
- Use %%{?perl_default_filter} instead of our own custom provides filter

* Wed Feb  9 2011 Ruben Kerkhof <ruben@rubenkerkhof.com> - 3.71-1
- Upstream released new version

* Tue Feb  8 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.65-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 17 2010 Marcela Maslanova <mmaslano@redhat.com> - 3.65-2
- Rebuild to fix problems with vendorarch/lib (#661697)

* Thu Jun 24 2010 Ruben Kerkhof <ruben@rubenkerkhof.com> 3.65-1
- Upstream released new version

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 3.17-5
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 3.17-4
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 18 2008 Nicolas Chauvet <kwizart@gmail.com> 3.17-1
- Update to 3.17

* Sun Nov 09 2008 Ruben Kerkhof <ruben@rubenkerkhof.com> 3.16-1
- Upstream release new version

* Mon Mar 03 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.51-2
- rebuild for new perl (again)

* Sat Feb 09 2008 Ruben Kerkhof <ruben@rubenkerkhof,com> 2.51-1
- Sync with upstream

* Thu Feb  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.33-2
- rebuild for new perl

* Sun May 13 2007 Ruben Kerkhof <ruben@rubenkerkhof.com> 2.33-1
- Initial import
