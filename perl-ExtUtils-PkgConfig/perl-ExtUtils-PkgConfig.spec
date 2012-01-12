Name:           perl-ExtUtils-PkgConfig
Version:        1.12
Release:        3%{?dist}
Summary:        Simplistic interface to pkg-config
Summary(zh_CN):	pkg-config 的简单接口
Group:          Development/Libraries
Group(zh_CN):	开发/库
License:        LGPLv2+
URL:            http://search.cpan.org/dist/ExtUtils-PkgConfig/
Source0:        http://search.cpan.org/CPAN/authors/id/T/TS/TSCH/ExtUtils-PkgConfig-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  pkgconfig
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       pkgconfig

%description
The pkg-config program retrieves information about installed libraries,
usually for the purposes of compiling against and linking to them.

ExtUtils::PkgConfig is a very simplistic interface to this utility,
intended for use in the Makefile.PL of perl extensions which bind
libraries that pkg-config knows. It is really just boilerplate code
that you would've written yourself.

%description -l zh_CN
pkg-config 的简单接口。

%prep
%setup -q -n ExtUtils-PkgConfig-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/ExtUtils/
%{_mandir}/man3/*.3pm*


%changelog
* Thu Jan 12 2012 Liu Di <liudidi@gmail.com> - 1.12-3
- 为 Magic 3.0 重建


