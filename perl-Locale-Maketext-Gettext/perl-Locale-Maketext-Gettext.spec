Name:           perl-Locale-Maketext-Gettext
Version:        1.27
Release:        9%{?dist}
Summary:        Joins the gettext and Maketext frameworks
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Locale-Maketext-Gettext/
Source0:        http://www.cpan.org/authors/id/I/IM/IMACAT/Locale-Maketext-Gettext-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Locale::Maketext::Gettext joins the GNU gettext and Maketext frameworks. It
is a subclass of Locale::Maketext(3) that follows the way GNU gettext
works. It works seamlessly, both in the sense of GNU gettext and Maketext.
As a result, you enjoy both their advantages, and get rid of both their
problems, too.

%prep
%setup -q -n Locale-Maketext-Gettext-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
rm -rf $RPM_BUILD_ROOT

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
rm -f debugsources.list debugfiles.list debuglinks.list
./Build test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Artistic BUGS Changes COPYING README THANKS TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*
%{_bindir}/maketext
%{_mandir}/man1/*

%changelog
* Mon Dec 10 2012 Liu Di <liudidi@gmail.com> - 1.27-9
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 1.27-8
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.27-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.27-6
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.27-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.27-4
- 661697 rebuild for fixing problems with vendorach/lib

* Mon May 03 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.27-3
- Mass rebuild with perl-5.12.0

* Mon Sep 21 2009 Rüdiger Landmann <rlandman@redhat.com> 1.27-2
- added BuildRequires:  perl(Test::More) and BuildRequires:  perl(Test::Pod)
* Mon Sep 07 2009 Rüdiger Landmann <rlandman@redhat.com> 1.27-1
- Specfile autogenerated by cpanspec 1.78.
