Name:           perl-MIME-EncWords
Version:        1.012.4
Release:        3%{?dist}
Summary:        Deal with RFC 2047 encoded words (improved)
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/MIME-EncWords/
Source0:        http://search.cpan.org/CPAN/authors/id/N/NE/NEZUMI/MIME-EncWords-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl >= 0:5.005
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(MIME::Charset) >= 1.006.2
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))


%description
MIME::EncWords is aimed to be another implementation of MIME::Words so that it
will achive more exact conformance with RFC 2047 (former RFC 1522)
specifications. Additionally, it contains some improvements. Following synopsis
and descriptions are inherited from its inspirer, then added descriptions on
improvements (**) or changes and clarifications (*).


%prep
%setup -q -n MIME-EncWords-%{version}

cat << \EOF > %{name}-prov
#!/bin/sh
%{__perl_provides} $* |\
sed -e '/perl(MIME::EncWords)$/d'
EOF

%global __perl_provides %{_builddir}/MIME-EncWords-%{version}/%{name}-prov
chmod +x %{__perl_provides}


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
%doc ARTISTIC Changes GPL README
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 1.012.4-3
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.012.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct 28 2011 Xavier Bachelot <xavier@bachelot.org> 1.012.4-1
- Update to 1.012.4.

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.012.3-2
- Perl mass rebuild

* Sat Jun 04 2011 Xavier Bachelot <xavier@bachelot.org> 1.012.3-1
- Update to 1.012.3.

* Wed Jun 01 2011 Xavier Bachelot <xavier@bachelot.org> 1.012.2-1
- Update to 1.012.2.

* Mon May 30 2011 Xavier Bachelot <xavier@bachelot.org> 1.012.1-1
- Update to 1.012.1.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.012-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.012-2
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Dec 17 2010 Xavier Bachelot <xavier@bachelot.org> 1.012-1
- Update to 1.012.
- Update Source0 URL.
- Add BuildRequires for better test coverage.

* Mon May 03 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.010.101-5
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.010.101-4
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.010.101-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon May 04 2009 Xavier Bachelot <xavier@bachelot.org> 1.010.101-2
- Better Description; tag.
- Filter duplicate Provides:.
- Remove unneeded Requires:.

* Fri Apr 24 2009 Xavier Bachelot <xavier@bachelot.org> 1.010.101-1
- Specfile autogenerated by cpanspec 1.77.
