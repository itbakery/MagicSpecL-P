Name:           perl-Glib
Version:        1.242
Release:        1%{?dist}
Summary:        Perl interface to GLib
Summary(zh_CN): GLib 的 perl 接口

Group:          Development/Libraries
Group(zh_CN):	开发/库
License:        LGPLv2+
URL:            http://search.cpan.org/dist/Glib/
Source0:        http://www.cpan.org/authors/id/T/TS/TSCH/Glib-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  perl >= 2:5.8.0
BuildRequires:  glib2-devel
BuildRequires:  perl(ExtUtils::Depends), perl(ExtUtils::PkgConfig)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module provides perl access to Glib and GLib's GObject libraries.
GLib is a portability and utility library; GObject provides a generic
type system with inheritance and a powerful signal system.  Together
these libraries are used as the foundation for many of the libraries
that make up the Gnome environment, and are used in many unrelated
projects.

%description -l zh_CN
GLib 的 perl 接口。

%prep
%setup -q -n Glib-%{version}

# Provides: exclude perl(MY)
cat <<__EOF__ > %{name}-perl.prov
#!/bin/sh
/usr/lib/rpm/perl.prov \$* | grep -v '^perl(MY)$'
__EOF__
%define __perl_provides %{_builddir}/Glib-%{version}/%{name}-perl.prov
chmod +x %{__perl_provides}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
%ifnarch ppc ppc64
make test
%endif

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS LICENSE NEWS README TODO
%{perl_vendorarch}/auto/Glib/
%{perl_vendorarch}/Glib*
%{_mandir}/man3/*.3pm*


%changelog

