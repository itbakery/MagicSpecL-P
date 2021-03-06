Name:           perl-Net-IP-Match-Regexp
Version:        1.01
Release:        4%{?dist}
Summary:        Efficiently match IP addresses against ranges
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Net-IP-Match-Regexp/
Source0:        http://www.cpan.org/modules/by-module/Net/Net-IP-Match-Regexp-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module allows you to check an IP address against one or more IP
ranges. It employs Perl's highly optimized regular expression engine to do
the hard work, so it is very fast. It is optimized for speed by doing the
match against a regexp which implicitly checks the broadest IP ranges
first. An advantage is that the regexp can be computed and stored in
advance (in source code, in a database table, etc) and reused, saving much
time if the IP ranges don't change too often. The match can optionally
report a value (e.g. a network name) instead of just a boolean, which makes
module useful for mapping IP ranges to names or codes or anything else.

%prep
%setup -q -n Net-IP-Match-Regexp-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
rm -rf $RPM_BUILD_ROOT

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc CHANGES LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 1.01-4
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1.01-2
- Perl 5.16 rebuild

* Mon Feb 13 2012 ktdreyer@ktdreyer.com 1.01-1
- Specfile autogenerated by cpanspec 1.78.
