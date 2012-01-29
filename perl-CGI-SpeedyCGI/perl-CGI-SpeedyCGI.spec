%define pkgname CGI-SpeedyCGI

Summary:        Speed up perl scripts by running them persistently
Name:           perl-CGI-SpeedyCGI
Version:        2.22
Release:        13%{?dist}
License:        GPLv3+
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/%{pkgname}/
Source0:	http://www.cpan.org/modules/by-authors/id/H/HO/HORROCKS/%{pkgname}-%{version}.tar.gz
Source1:	speedycgi.conf
Patch0:		perl-CGI-SpeedyCGI-2.22-documentation.patch
Patch1:		perl-CGI-SpeedyCGI-2.22-empty_param.patch
Patch2:		perl-CGI-SpeedyCGI-2.22-strerror.patch
Patch3:		perl-CGI-SpeedyCGI-2.22-brigade_foreach.patch
Patch4:		perl-CGI-SpeedyCGI-2.22-exit_messages.patch
Patch5:		perl-CGI-SpeedyCGI-2.22-perl_510.patch
Patch6:		perl-CGI-SpeedyCGI-2.22-c99_inline.patch
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildRequires:  perl >= 5.8.0, perl(ExtUtils::MakeMaker), perl(ExtUtils::Embed)
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
SpeedyCGI is a way to run perl scripts persistently, which can make
them run much more quickly. After the script is initially run, instead
of exiting, the perl interpreter is kept running. During subsequent
runs, this interpreter is used to handle new executions instead of
starting a new perl interpreter each time. It is a very fast frontend
program, written in C, is executed for each request. 

%package -n mod_speedycgi
Summary:	SpeedyCGI module for the Apache HTTP Server
Group:		System Environment/Daemons
BuildRequires:	httpd-devel
Requires:	%{name}%{?_isa} = %{version}-%{release}, httpd >= 2.0.40
Requires:	httpd-mmn = %(cat %{_includedir}/httpd/.mmn || echo missing)

%description -n mod_speedycgi
The SpeedyCGI module for the Apache HTTP Server. It can be used to run
perl scripts for web application persistently to make them more quickly.

%prep
%setup -q -n %{pkgname}-%{version}
%patch0 -p1 -b .documentation
%patch1 -p1 -b .empty_param
%patch2 -p1 -b .strerror
%patch3 -p1 -b .brigade_foreach
%patch4 -p1 -b .exit_messages
%patch5 -p1 -b .perl_510
%patch6 -p1 -b .c99_inline

%build
sed -i 's@apxs -@%{_sbindir}/apxs -@g' Makefile.PL src/SpeedyMake.pl \
  mod_speedycgi/t/ModTest.pm mod_speedycgi/t/mod_perl.t
sed -i 's@APXS=apxs@APXS=%{_sbindir}/apxs@g' mod_speedycgi/Makefile.tmpl

echo yes | perl Makefile.PL INSTALLDIRS=vendor
make OPTIMIZE="$RPM_OPT_FLAGS" # doesn't understand %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT \( -name perllocal.pod -o -name .packlist \) -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -exec rm -f {} ';'
chmod -R u+w $RPM_BUILD_ROOT/*

mkdir -p $RPM_BUILD_ROOT{%{_libdir}/httpd/modules,%{_sysconfdir}/httpd/conf.d}
install -m 755 mod_speedycgi2/mod_speedycgi.so $RPM_BUILD_ROOT%{_libdir}/httpd/modules/
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes COPYING README docs/*
%{_bindir}/speedy*
%{perl_vendorlib}/CGI

%files -n mod_speedycgi
%defattr(-,root,root)
%{_libdir}/httpd/modules/mod_speedycgi.so
%config(noreplace) %{_sysconfdir}/httpd/conf.d/speedycgi.conf

%changelog
* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 2.22-13
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.22-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.22-11
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.22-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.22-9
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.22-8
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 2.22-7
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.22-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Robert Scheck <robert@fedoraproject.org> 2.22-5
- Rebuild against gcc 4.4 and rpm 4.6

* Thu Oct 30 2008 Robert Scheck <robert@fedoraproject.org> 2.22-4
- Fixed default configuration file reading loadmodule (#448320)

* Sun Oct 12 2008 Robert Scheck <robert@fedoraproject.org> 2.22-3
- Work around C99 inline issues caused by C99 inline support in
  newer GCC versions (#464963, thanks to Andreas Thienemann)

* Sun May 04 2008 Robert Scheck <robert@fedoraproject.org> 2.22-2
- Changes to match with Fedora Packaging Guidelines (#429609)

* Mon Jan 21 2008 Robert Scheck <robert@fedoraproject.org> 2.22-1
- Upgrade to 2.22
- Initial spec file for Fedora and Red Hat Enterprise Linux
