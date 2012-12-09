Name:           perl-Eval-LineNumbers
Version:        0.31
Release:        5%{?dist}
Summary:        Add line numbers to hereis blocks that contain perl source code
License:        Artistic 2.0 or LGPLv2+
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Eval-LineNumbers/
Source0:        http://www.cpan.org/authors/id/M/MU/MUIR/modules/Eval-LineNumbers-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module adds a line number to hereis text that is going to be
eval'ed so that error messages will point back to the right place.

%prep
%setup -q -n Eval-LineNumbers-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check


%files
%{perl_vendorlib}/Eval
%{_mandir}/man3/Eval::LineNumbers.3pm.gz

%changelog
* Sun Dec 09 2012 Liu Di <liudidi@gmail.com> - 0.31-5
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.31-4
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.31-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Aug 13 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.31-2
- Bump to build against perl 5.14.1

* Thu Jul 28 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 0.31-1
- Specfile autogenerated by cpanspec 1.78.
