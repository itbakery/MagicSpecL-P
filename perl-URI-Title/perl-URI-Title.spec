Name:           perl-URI-Title
Version:        1.86
Release:        3%{?dist}
Summary:        Get the titles of things on the web in a sensible way
# Mentioned in URI::Title POD
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/URI-Title/
Source0:        http://www.cpan.org/authors/id/T/TO/TOMI/URI-Title-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::Type) >= 0.22
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(Image::Size)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Module::Pluggable) >= 1.2
BuildRequires:  perl(MP3::Info)
BuildRequires:  perl(Test::More)
Requires:       perl(File::Type) >= 0.22
Requires:       perl(Module::Pluggable) >= 1.2
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(File::Type\\)
%global __requires_exclude %__requires_exclude|^perl\\(Module::Pluggable\\)

%description
I keep having to find the title of things on the web.  This seems like a really
simple request, just get() the object, parse for a title tag, you're done.
Ha, I wish.  There are several problems with this approach:

What if the resource is on a very slow server?  Do we wait forever or what?
What if the resource is a 900 gig file?  You don't want to download that.
What if the page title isn't in a title tag, but is buried in the HTML
somewhere?
What if the resource is an MP3 file, or a word document or something?
...

So, let's solve these issues once.

%prep
%setup -q -n URI-Title-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes title.pl
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.86-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 15 2012 Petr Pisar <ppisar@redhat.com> - 1.86-2
- Perl 5.16 rebuild

* Mon Jun 04 2012 Petr Šabata <contyk@redhat.com> - 1.86-1
- 1.86 bump
- Drop command macros

* Fri Jan 20 2012 Petr Šabata <contyk@redhat.com> - 1.85-1
- Specfile autogenerated by cpanspec 1.78.
