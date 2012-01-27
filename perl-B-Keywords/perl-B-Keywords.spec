Name:           perl-B-Keywords
Version:        1.11
Release:        1%{?dist}
Summary:        Lists of reserved barewords and symbol names
Summary(zh_CN.UTF-8): 列出保留字和符号名称

Group:          Development/Libraries
Group(zh_CN.UTF-8):	开发/库
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/B-Keywords/
Source0:        http://www.cpan.org/authors/id/J/JJ/JJORE/B-Keywords-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(YAML)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)

%description
%{summary}.

%description -l zh_CN.UTF-8
列出保留字和符号名称

%prep
%setup -q -n B-Keywords-%{version}


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
%doc Changes LICENSE
%{perl_vendorlib}/B/
%{_mandir}/man3/*.3pm*


%changelog

