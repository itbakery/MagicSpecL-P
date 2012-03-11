Name:           perl-Pod-Eventual
Version:        0.093330
Release:        8%{?dist}
Summary:        Read a POD document as a series of trivial events
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Pod-Eventual/
Source0:        http://www.cpan.org/authors/id/R/RJ/RJBS/Pod-Eventual-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Mixin::Linewise::Readers) >= 0.001
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
#BuildRequires:  perl(Test::Pod::Coverage)
# causes circular builddeps
#BuildRequires:  perl(Pod::Coverage::TrustPod)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
POD is a pretty simple format to write, but it can be a big pain to deal
with reading it and doing anything useful with it. Most existing POD
parsers care about semantics, like whether a =item occurred after an
=over but before a back, figuring out how to link a L<>, and other things
like that.

Pod::Eventual is much less ambitious and much more stupid. Fortunately, stupid
is often better. (That's what I keep telling myself, anyway.)

Pod::Eventual reads line-based input and produces events describing each POD
paragraph or directive it finds. Once complete events are immediately passed to
the handle_event method. This method should be implemented by Pod::Eventual
subclasses. If it isn't, Pod::Eventual's own handle_event will be called, and
will raise an exception.

%prep
%setup -q -n Pod-Eventual-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes LICENSE META.json README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.093330-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul 18 2011 Petr Sabata <contyk@redhat.com> - 0.093330-7
- Perl mass rebuild

* Wed Jul 13 2011 Iain Arnell <iarnell@gmail.com> 0.093330-6
- drop circular Pod::Coverage::TrustPod buildreq
- don't run "release" tests

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.093330-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.093330-4
- 661697 rebuild for fixing problems with vendorach/lib

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.093330-3
- Mass rebuild with perl-5.12.0

* Sat Feb 27 2010 Iain Arnell <iarnell@gmail.com> 0.093330-2
- BR perl(Pod::Coverage::TrustPod)

* Thu Jan 14 2010 Iain Arnell 0.093330-1
- Specfile autogenerated by cpanspec 1.78.
