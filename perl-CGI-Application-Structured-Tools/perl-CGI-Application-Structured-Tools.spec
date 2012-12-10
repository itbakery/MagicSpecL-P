Name:           perl-CGI-Application-Structured-Tools
Version:        0.013
Release:        7%{?dist}
Summary:        Tools to generate and maintain CGI::Application::Structured based web apps
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/CGI-Application-Structured-Tools/
Source0:        http://www.cpan.org/authors/id/V/VA/VANAMBURG/CGI-Application-Structured-Tools-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(CGI::Application::Structured)
BuildRequires:  perl(DBIx::Class::Schema::Loader)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(HTML::Template)
BuildRequires:  perl(Module::Signature)
BuildRequires:  perl(Module::Starter)
BuildRequires:  perl(Module::Starter::Plugin::Template)
BuildRequires:  perl(Module::Starter::Simple)
BuildRequires:  perl(Pod::Coverage)
BuildRequires:  perl(Probe::Perl)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::WWW::Mechanize::CGIApp)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# RPM 4.8 style:
%filter_from_requires /main_module>)/d; /perl(<tmpl_var)/d; /perl(<tmpl_var/d
%{?perl_default_filter}
# RPM 4.9 style:
%global __requires_exclude %{?__requires_exclude|%__requires_exclude"|}main_module>\\)
%global __requires_exclude %__requires_exclude|perl\\(<tmpl_var\\)
%global __requires_exclude %__requires_exclude|perl\\(<tmpl_var

%description
A simple, medium-weight, MVC, DB web micro-framework built on
CGI::Application. The framework combines tested, well known plugins, templates
and helper scripts to provide a rapid development environment.

%prep
%setup -q -n CGI-Application-Structured-Tools-%{version}

cat << \EOF > %{name}-req
#!/bin/sh
%{__perl_requires} $* |\
sed -e '/perl(<tmpl_var)/d'
EOF

%global __perl_requires %{_builddir}/CGI-Application-Structured-Tools-%{version}/%{name}-req
chmod +x %{__perl_requires}

cd lib/CGI/Application/Structured/Tools/templates
for i in create_dbic_schema.pl create_controller.pl \
         boilerplate.t perl-critic.t pod.t pod-coverage.t \
         test-app.t 00-signature.t 01-load.t; do
    chmod 755 $i;
    sed -i 's#!perl#!\/usr\/bin\/perl#' $i;
done

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
%doc Changes LICENSE README Todo
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_bindir}/cas-starter.pl

%changelog
* Mon Dec 10 2012 Liu Di <liudidi@gmail.com> - 0.013-7
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.013-6
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.013-5
- 为 Magic 3.0 重建

* Wed Jul 27 2011 Petr Pisar <ppisar@redhat.com> - 0.013-4
- RPM 4.9 filtering added

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 0.013-3
- Perl mass rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.013-2
- Perl mass rebuild

* Wed Apr 06 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.013-1
- Update to 0.013
- Add perl(Probe::Perl) as a BuildRequires.

* Tue Feb 15 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.007-5
- Improve filtering.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.007-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.007-3
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.007-2
- Mass rebuild with perl-5.12.0

* Thu Oct 15 2009 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 0.007-1
- Specfile autogenerated by cpanspec 1.78.
