Name:           perl-Pod-Spell-CommonMistakes
Version:        1.000
Release:        4%{?dist}
Summary:        Catches common typos in POD
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Pod-Spell-CommonMistakes/
Source0:        http://www.cpan.org/authors/id/A/AP/APOCAL/Pod-Spell-CommonMistakes-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Module::Build)
# Run-Time:
BuildRequires:  perl(base)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(IO::Scalar) >= 2.110
BuildRequires:  perl(Pod::Spell) >= 1.01
# Tests:
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More) >= 0.88
# Optional test:
BuildRequires:  perl(Test::Script) >= 1.05
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module looks for any typos in your POD. It differs from Pod::Spell or
Test::Spelling because it uses a custom word list and doesn't use the system
spellchecker. The idea for this came from the
<http://wiki.debian.org/Teams/Lintian> code in Debian, thanks!

%prep
%setup -q -n Pod-Spell-CommonMistakes-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes CommitLog examples LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Dec 10 2012 Liu Di <liudidi@gmail.com> - 1.000-4
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.000-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 1.000-2
- Perl 5.16 rebuild

* Fri Apr 27 2012 Petr Pisar <ppisar@redhat.com> 1.000-1
- Specfile autogenerated by cpanspec 1.78.
