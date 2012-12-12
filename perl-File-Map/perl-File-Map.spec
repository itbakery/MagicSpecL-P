Name:           perl-File-Map
Version:        0.31
Release:        9%{?dist}
Summary:        Memory mapping made simple and safe
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/File-Map/
Source0:        http://www.cpan.org/authors/id/L/LE/LEONT/File-Map-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  perl >= 0:5.008
BuildRequires:  perl(Const::Fast)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::Pod) >= 1.22
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(Time::HiRes)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
File::Map maps files or anonymous memory into perl variables.


%prep
%setup -q -n File-Map-%{version}
chmod -x examples/fastsearch.pl


%build
%{__perl} Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build


%install
rm -rf $RPM_BUILD_ROOT

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*


%check
./Build test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes examples LICENSE README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/File*
%{_mandir}/man3/*


%changelog
* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.31-9
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.31-8
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.31-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.31-6
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.31-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Nov 05 2010 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> 0.31-4
- Fix a BR typo

* Wed Nov 03 2010 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> 0.31-3
- Drop el5 secific patches
- Add more BuildRequires (Petr Pisar)

* Mon Oct 11 2010 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> 0.31-2
- Fix build on el5

* Fri Oct 08 2010 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> 0.31-1
- Fix POD
- Specfile autogenerated by cpanspec 1.78.
