Name:           perl-Devel-Trace
Version:        0.11
Release:        5%{?dist}
Summary:        Print out each line before it is executed (like sh -x)
License:        Public Domain
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Devel-Trace/
Source0:        http://www.cpan.org/authors/id/M/MJ/MJD/Devel-Trace-%{version}.tar.gz
Patch0:         perl-Devel-Trace-0.11-Uninteractive-tests.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))


%description
If you run your program with perl -d:Trace program, this module will print
a message to standard error just before each line is executed.

This is something like the shell's -x option.


%prep
%setup -q -n Devel-Trace-%{version}
%patch0 -p1

# doc file must not be executable:
#   -> http://fedoraproject.org/wiki/Packaging/Guidelines#Documentation
chmod -x sample


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf %{buildroot}

make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*


%check



%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc Changes README sample
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Sun Dec 09 2012 Liu Di <liudidi@gmail.com> - 0.11-5
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.11-4
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.11-2
- Perl mass rebuild

* Fri Apr 08 2011 Mathieu Bridon <bochecha@fedoraproject.org> 0.11-1
- Specfile autogenerated by cpanspec 1.78.
- Fixed the license (incorrectly guessed by cpanspec).
- Patched the tests to make the build non interactive.
- Removed dubious executable permission on a doc file.
