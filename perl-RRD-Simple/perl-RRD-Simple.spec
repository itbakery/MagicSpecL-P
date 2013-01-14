# Need to tweak provides/requires filters differently if we have rpm 4.9 onwards
%global rpm49 %(rpm --version | perl -pi -e 's/^.* (\\d+)\\.(\\d+)\\.(\\d+).*/sprintf("%d.%03d%03d",$1,$2,$3) ge 4.009 ? 1 : 0/e')

Name:		perl-RRD-Simple
Version:	1.44
Release:	13%{?dist}
Summary:	Simple interface to create and store data in RRD files
Group:		Development/Libraries
License:	ASL 2.0
URL:		http://search.cpan.org/dist/RRD-Simple
Source0:	http://search.cpan.org/CPAN/authors/id/N/NI/NICOLAW/RRD-Simple-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(id -nu)
BuildArch:	noarch
BuildRequires:	perl(Carp)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(POSIX)
BuildRequires:	perl(RRDs)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Pod::Coverage)

# https://rt.cpan.org/Public/Bug/Display.html?id=46193
BuildConflicts:	perl(Test::Deep)
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
RRD::Simple provides a simple interface to RRDTool's RRDs module. This module
does not currently offer the fetch method that is available in the RRDs
module. It does, however, create RRD files with a sensible set of default RRA
Round Robin Archive) definitions, and can dynamically add new data source
names to an existing RRD file.

This module is ideal for quick and simple storage of data within an RRD file
if you do not need to, nor want to, bother defining custom RRA definitions.

%prep
%setup -q -n RRD-Simple-%{version}

# Don't want provides/requires from %%{_docdir}
%global docfilt perl -p -e 's|%{_docdir}/%{name}-%{version}\\S+||'
# RRD::Simple version should be from distribution version, not svn revision
%global verfilt perl -pi -e 's/(perl\\(RRD::Simple\\) =) \\d+/\\1 %{version}/'
# Apply provides/requires filters
%if %{rpm49}
%global provfilt /bin/sh -c "%{docfilt} | %{__perllib_provides} | %{verfilt}"
%define __perllib_provides %{provfilt}
%global reqfilt /bin/sh -c "%{docfilt} | %{__perllib_requires}"
%define __perllib_requires %{reqfilt}
%else
%global provfilt /bin/sh -c "%{docfilt} | %{__perl_provides} | %{verfilt}"
%define __perl_provides %{provfilt}
%global reqfilt /bin/sh -c "%{docfilt} | %{__perl_requires}"
%define __perl_requires %{reqfilt}
%endif

%build
# Prevent call-home query/timeout; not strictly necessary
AUTOMATED_TESTING=1 perl Build.PL installdirs=vendor
./Build

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -depth -type d -exec rmdir {} ';' 2>/dev/null
%{_fixperms} %{buildroot}

%check
LC_ALL=C ./Build test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc Changes LICENSE NOTICE README examples/ t/
%dir %{perl_vendorlib}/RRD/
%dir %{perl_vendorlib}/RRD/Simple/
%{perl_vendorlib}/RRD/Simple.pm
%doc %{perl_vendorlib}/RRD/Simple/Examples.pod
%{_mandir}/man3/RRD::Simple.3pm*
%{_mandir}/man3/RRD::Simple::Examples.3pm*

%changelog
* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.44-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 27 2012 Petr Pisar <ppisar@redhat.com> - 1.44-12
- Perl 5.16 rebuild

* Thu Jan 12 2012 Paul Howarth <paul@city-fan.org> - 1.44-11
- Fix provides/requires filters to work with rpm 4.9+ too
- Add buildreqs for perl core modules, which may be dual-lived
- Nobody else likes macros for commands
- Don't package INSTALL file

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.44-10
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.44-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 16 2010 Paul Howarth <paul@city-fan.org> - 1.44-8
- Rebuild with rrdtool 1.4.4 in Rawhide (#631131)

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.44-7
- Mass rebuild with perl-5.12.0

* Thu Mar 11 2010 Paul Howarth <paul@city-fan.org> - 1.44-6
- Drop POD patch, only needed with Test::Pod 1.40

* Wed Mar  3 2010 Paul Howarth <paul@city-fan.org> - 1.44-5
- Change buildreq perl(Test::Deep) to a build conflict until upstream fixes
  failing t/32exported_function_interface.t (#464964, CPAN RT#46193)
- Fix broken POD (CPAN RT#50868)
- Cosmetic clean-up of spec
- Mark RRD::Simple::Examples POD as %%doc
- Run test suite in "C" locale for spec compatibility with old distributions
- Simplify provides/requires filter
- Fix versioned provide for perl(RRD::Simple)

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.44-4
- Rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.44-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.44-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Aug 03 2008 Chris Weyl <cweyl@alumni.drew.edu> - 1.44-1
- Update to 1.44

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.43-3
- Rebuild for new perl

* Fri Jan 11 2008 Ralf Corsépius <rc040203@freenet.de> - 1.43-2
- BR: perl(Test::More) (BZ 419631)
- BR: perl(Test::Pod), perl(Test::Pod::Coverage)

* Wed Mar 21 2007 Chris Weyl <cweyl@alumni.drew.edu> - 1.43-1
- Update to 1.43

* Tue Feb 13 2007 Chris Weyl <cweyl@alumni.drew.edu> - 1.41-1
- Update to 1.41
- Use Build.PL directly

* Thu Aug 31 2006 Chris Weyl <cweyl@alumni.drew.edu> - 1.40-2
- Bump for mass rebuild

* Fri Aug 25 2006 Chris Weyl <cweyl@alumni.drew.edu> - 1.40-1
- Update to 1.40
- Minor spec cleanups

* Tue Jun 27 2006 Chris Weyl <cweyl@alumni.drew.edu> - 1.39-1
- Bump release for extras build

* Tue Jun 27 2006 Chris Weyl <cweyl@alumni.drew.edu> - 1.39-0
- Initial spec file for F-E
