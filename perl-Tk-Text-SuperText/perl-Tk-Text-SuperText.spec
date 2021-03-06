Name:           perl-Tk-Text-SuperText
Version:        0.9.4
Release:        9%{?dist}
Summary:        Improved text widget for perl/tk
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Tk-Text-SuperText/
Source0:        http://www.cpan.org/authors/id/A/AL/ALEXIOB/Tk-Text-SuperText-%{version}.tar.gz
Patch0:         perl-Tk-Text-SuperText-0.9.4-hashref.patch
Patch1:         perl-Tk-Text-SuperText-0.9.4-test.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Tk)
BuildRequires:  perl(Tk::Derived)
BuildRequires:  perl(Tk::Text)
BuildRequires:  perl(App::Prove)
# Parts of X Window System needed for tests to run:
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  xorg-x11-xinit
BuildRequires:  font(:lang=en)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Tk::Text::SuperText implements many new features over the standard Tk::Text
widget while supporting all it's standard features. Its used simply as the
Tk::Text widget.


%prep
%setup -q -n Tk-Text-SuperText-%{version}
%patch0 -p1 -b .hashref
%patch1 -p1 -b .test


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
xinit %{_bindir}/make -s test -- %{_bindir}/Xvfb :666 |tee testing.TAP
# xinit throws away the return value from make
# Let's validate its TAP output ourselves
prove --exec cat testing.TAP


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.9.4-9
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.9.4-7
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.9.4-5
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Nov 05 2010 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> 0.9.4-3
- Cosmetic fixes

* Wed Nov 03 2010 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> 0.9.4-2
- Formatting/wording fixes (Peter Pisar)
- Actually run the test suite (Peter Pisar)

* Tue Jun 09 2009 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> 0.9.4-1
- Specfile autogenerated by cpanspec 1.78.
- Fix up license
- Fix test warnings
