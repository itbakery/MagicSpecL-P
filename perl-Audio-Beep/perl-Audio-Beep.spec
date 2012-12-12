Name:		perl-Audio-Beep
Version:	0.11
Release:	8%{?dist}
Summary:	Audio::Beep Perl module
License:	GPL+ or Artistic
Group:		Development/Libraries
URL:		http://search.cpan.org/dist/Audio-Beep/
Source0:	http://www.cpan.org/authors/id/G/GI/GIULIENK/Audio-Beep-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Test::More)
Requires:	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:	beep
BuildArch:	noarch

%{?perl_default_filter}

%description
Audio::Beep - Perl module to use your computer beeper in fancy ways

%prep
%setup -q -n Audio-Beep-%{version}
chmod -x music/*.pl
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
%doc Changes README music
%{perl_vendorlib}/Audio*
%{_mandir}/man3/*

%changelog
* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.11-8
- 为 Magic 3.0 重建

* Sat Jan 28 2012 Liu Di <liudidi@gmail.com> - 0.11-7
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.11-5
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.11-3
- 661697 rebuild for fixing problems with vendorach/lib

* Thu Apr 29 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.11-2
- Mass rebuild with perl-5.12.0

* Mon Mar 15 2010 Jan Klepek 0.11-1
- Specfile autogenerated by cpanspec 1.78.
