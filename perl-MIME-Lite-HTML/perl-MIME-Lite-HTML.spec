Name:           perl-MIME-Lite-HTML
Version:        1.24
Release:        4%{?dist}
Summary:        Provide routine to transform a HTML page in a MIME-Lite mail
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/MIME-Lite-HTML/
Source0:        http://www.cpan.org/modules/by-module/MIME/MIME-Lite-HTML-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTML::LinkExtor)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(MIME::Lite)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI::URL)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))


%description
This module is a Perl mail client interface for sending message that
support HTML format and build them for you.. This module provides routine to
transform an HTML page in a MIME::Lite mail. So you need this module to use
MIME-Lite-HTML possibilities.


%prep
%setup -q -n MIME-Lite-HTML-%{version}
chmod a-x README Changes HTML.pm
iconv -f iso8859-1 -t utf-8 Changes > Changes.utf8 && \
touch -r Changes Changes.utf8 && \
mv -f Changes.utf8 Changes


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



%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes COPYING README
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Mon Dec 10 2012 Liu Di <liudidi@gmail.com> - 1.24-4
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 1.24-3
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Oct 10 2011 Xavier Bachelot <xavier@bachelot.org> 1.24-1
- Update to 1.24.

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 1.23-3
- Perl mass rebuild

* Thu May 19 2011 Xavier Bachelot <xavier@bachelot.org> 1.23-2
- Clean up redundant Requires:.

* Mon May 02 2011 Xavier Bachelot <xavier@bachelot.org> 1.23-1
- Specfile autogenerated by cpanspec 1.78.
