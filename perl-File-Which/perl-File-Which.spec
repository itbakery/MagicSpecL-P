Name:           perl-File-Which
Version:        1.09
Release:        1%{?dist}
Summary:        Portable implementation of the 'which' utility
Summary(zh_CN.UTF-8): 可移植的 'which' 工具实现

Group:          Development/Libraries
Group(zh_CN.UTF-8):	开发/库
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/File-Which/
Source0:        http://www.cpan.org/authors/id/P/PE/PEREINAR/File-Which-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
File::Which is a portable implementation (in Perl) of 'which', and can
be used to get the absolute filename of an executable program
installed somewhere in your PATH, or just check for its existence. It
includes the command-line utility 'pwhich' which has the same function
as 'which'.

%description -l zh_CN.UTF-8
可移植的 'which' 工具实现

%prep
%setup -q -n File-Which-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes README
%{_bindir}/pwhich
%{perl_vendorlib}/File/
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3pm*


%changelog

