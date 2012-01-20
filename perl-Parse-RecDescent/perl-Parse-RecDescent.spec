%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Parse-RecDescent

Summary: Generate Recursive-Descent Parsers
Summary(zh_CN): 生成递归系分析器
Name: perl-Parse-RecDescent
Version: 1.966_000
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
Group(zh_CN): 应用程序/CPAN
URL: http://search.cpan.org/dist/Parse-RecDescent/
Source: http://search.cpan.org/CPAN/authors/id/D/DC/DCONWAY/Parse-RecDescent-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
RecDescent incrementally generates top-down recursive-descent text
parsers from simple yacc-like grammar specifications.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%{__make} test

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot} %{_builddir}/%{buildsubdir}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Parse/RecDescent.p*

%changelog
* Sun Oct 14 2007 Ni Hui <shuizhuyuanluo@126.com> - 1.94-0.1mgc
- Initial package.
