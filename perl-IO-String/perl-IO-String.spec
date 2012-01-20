%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define pkg_name IO-String

Summary: IO::File interface for in-core strings
Name: perl-IO-String
Version: 1.08
Release: 1%{?dist}
Group: Development/Libraries
Group(zh_CN): 开发/库
License: Artistic
URL: http://search.cpan.org/dist/%{pkg_name}/
Source0: http://www.cpan.org/authors/id/G/GA/GAAS/%{pkg_name}-%{version}.tar.gz

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: perl(ExtUtils::MakeMaker)

%description
The "IO::String" module provides the "IO::File" interface for in-core strings.
An "IO::String" object can be attached to a string, and makes it possible to
use the normal file operations for reading or writing data, as well as for
seeking to various locations of the string. This is useful when you want to
use a library module that only provides an interface to file handles on data
that you have in a string variable.


%prep
%setup -q -n %{pkg_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%{!?_without_test:%{__make} test}

%install
%{__rm} -rf %{buildroot}

%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot} %{_builddir}/%{buildsubdir}

%files
%defattr(-,root,root,-)
%doc Changes README
%doc %{_mandir}/man3/*.3pm*
%{perl_vendorlib}

%changelog
* Sun Oct 14 2007 Ni Hui <shuizhuyuanluo@126.com> - 1.08-0.1mgc
- Initial package
