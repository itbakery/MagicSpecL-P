Name:           perl-Module-Find
Version:        0.10
Release:        2%{?dist}
Summary:        Find and use installed modules in a (sub)category
Summary(zh_CN.UTF-8): 在(子)类别中查找和使用安装的模块

Group:          Development/Libraries
Group(zh_CN.UTF-8):	开发/库
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Module-Find/
Source0:        http://www.cpan.org/authors/id/C/CR/CRENZ/Module-Find-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Module::Find lets you find and use modules in categories. This can be very
useful for auto-detecting driver or plugin modules. You can differentiate
between looking in the category itself or in all subcategories.

%description -l zh_CN.UTF-8
在(子)类别中查找和使用安装的模块。

%prep
%setup -q -n Module-Find-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
%{_fixperms} $RPM_BUILD_ROOT/*


%check
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes README examples/
%{perl_vendorlib}/Module/
%{_mandir}/man3/*.3pm*


%changelog

