Name:           perl-HTML-BarGraph
Version:        0.5
Release:        8%{?dist}
Summary:        Generate multiset bar graphs using plain HTML
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/HTML-BarGraph/
Source0:        http://www.cpan.org/authors/id/P/PO/PODGURSV/HTML-BarGraph-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
HTML::BarGraph is a module that creates graphics for one or more data-sets,
using plain HTML and, optionally, one-pixel images, which are stretched
using the width and height attributes of the HTML img tag.

%prep
%setup -q -n HTML-BarGraph-%{version}
chmod -x BarGraph.pm

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT/%{_datadir}/%{name}
cp sample.html $RPM_BUILD_ROOT/%{_datadir}/%{name}
cp -r pixels $RPM_BUILD_ROOT/%{_datadir}/%{name}

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README sample.html
%{perl_vendorlib}/*
%{_mandir}/man3/*
%{_datadir}/%{name}

%changelog
* Sun Dec 09 2012 Liu Di <liudidi@gmail.com> - 0.5-8
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.5-7
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 15 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.5-5
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 17 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.5-3
- 661697 rebuild for fixing problems with vendorach/lib

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.5-2
- Mass rebuild with perl-5.12.0

* Fri Mar 26 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 0.5-1
- Specfile autogenerated by cpanspec 1.78.
