%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Inline

Summary: Perl module to write Perl subroutines in other programming languages
Summary(zh_CN): Perl 模块用于以其它编程语言写入 Perl 子程序
Name: perl-Inline
Version: 0.49
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
Group(zh_CN): 应用程序/CPAN
URL: http://search.cpan.org/dist/Inline/
Source: http://www.cpan.org/modules/by-module/Inline/Inline-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot-%(%{__id_u} -n)

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Parse::RecDescent)
Requires: perl
Requires: perl(Parse::RecDescent)

%description
Inline is a Perl module to write Perl subroutines
in other programming languages.

%description -l zh_CN
Inline 是一个 Perl 模块，用于以其它编程语言写入 Perl 子程序。

%prep
%setup -n %{real_name}-%{version}

%build
echo "y" | %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%{__make} test

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot} %{_builddir}/%{buildsubdir}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README
%doc %{_mandir}/man3/*.3pm*
%{perl_vendorlib}/Inline-API.pod
%{perl_vendorlib}/Inline-FAQ.pod
%{perl_vendorlib}/Inline-Support.pod
%{perl_vendorlib}/Inline.pm
%{perl_vendorlib}/Inline.pod
%{perl_vendorlib}/Inline/
%{perl_vendorlib}/auto/Inline/

%changelog
* Sun Oct 14 2007 Ni Hui <shuizhuyuanluo@126.com> - 0.44-0.1mgc
- Initial package
