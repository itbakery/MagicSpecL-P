Name:           perl-Test-File-ShareDir
Version:        0.3.1
Release:        2%{?dist}
Summary:        Create a Fake ShareDir for your modules for testing
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Test-File-ShareDir/
Source0:        http://www.cpan.org/authors/id/K/KE/KENTNL/Test-File-ShareDir-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Copy::Recursive)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::ShareDir) >= 1.00
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Path::Class::Dir)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
Requires:       perl(Carp)
Requires:       perl(File::Copy::Recursive)
Requires:       perl(File::Temp)
Requires:       perl(Path::Class::Dir)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
Create a fake ShareDir for your modules for testing.

%prep
%setup -q -n Test-File-ShareDir-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0

%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.3.1-2
- 为 Magic 3.0 重建

* Sun Jul 29 2012 Iain Arnell <iarnell@gmail.com> 0.3.1-1
- Specfile autogenerated by cpanspec 1.79.
