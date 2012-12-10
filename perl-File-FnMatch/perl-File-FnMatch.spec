%global shortname File-FnMatch

Name:           perl-%{shortname}
Version:        0.02
Release:        13%{?dist}
Summary:        Simple file-name and pathname matching
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/%{shortname}/
Source0:        http://www.cpan.org/modules/by-module/File/%{shortname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
# RPM 4.8 style:
%{?filter_setup:
%filter_from_provides /FnMatch.so/d
}
# RPM 4.9 style:
%global __provides_exclude %{%?__provides_exclude:__provides_exclude|}FnMatch.so
%{?perl_default_filter}


%description
This module provides simple, shell-like pattern matching.

%prep
%setup -q -n %{shortname}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/File*
%{_mandir}/man3/*

%changelog
* Mon Dec 10 2012 Liu Di <liudidi@gmail.com> - 0.02-13
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.02-12
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.02-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul 25 2011 Petr Pisar <ppisar@redhat.com> - 0.02-10
- RPM 4.9 dependency filtering added

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.02-9
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.02-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.02-7
- 661697 rebuild for fixing problems with vendorach/lib

* Sat Sep 4 2010 Colin Coe <colin.coe@gmail.com> 0.02-6
- Fix 'private-shared-object-provides', take 3

* Fri Sep 3 2010 Colin Coe <colin.coe@gmail.com> 0.02-5
- Fix 'private-shared-object-provides', take 2

* Thu Sep 2 2010 Colin Coe <colin.coe@gmail.com> 0.02-4
- Bump for sanity

* Thu Sep 2 2010 Colin Coe <colin.coe@gmail.com> 0.02-3
- Fix 'private-shared-object-provides'
- Introduce shortname macro

* Thu Aug 26 2010 Colin Coe <colin.coe@gmail.com> 0.02-2
- Silence rpmlint warning

* Wed Aug 25 2010 Colin Coe <colin.coe@gmail.com> 0.02-1
- Specfile autogenerated by cpanspec 1.77.
