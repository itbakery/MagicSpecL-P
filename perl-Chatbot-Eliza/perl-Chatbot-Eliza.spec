Name:           perl-Chatbot-Eliza
Version:        1.04
Release:        15%{?dist}
Summary:        Implementation of the Eliza algorithm
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Chatbot-Eliza/
Source0:        http://www.cpan.org/authors/id/J/JN/JNOLAN/Chatbot-Eliza-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module implements the classic Eliza algorithm. The original Eliza
program was written by Joseph Weizenbaum and described in the
Communications of the ACM in 1966. Eliza is a mock Rogerian
psychotherapist. It prompts for user input, and uses a simple
transformation algorithm to change user input into a follow-up question.
The program is designed to give the appearance of understanding.

%prep
%setup -q -n Chatbot-Eliza-%{version}
# quiet rpmlint :)
chmod -x *
chmod +x Chatbot
for enc in deutsch.txt norsk.txt; do
    iconv -f latin1 -t utf8 ${enc} > ${enc}.utf && \
      mv ${enc}.utf ${enc}
done

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} %{buildroot}/*

%check


%files
%doc simple.cgi doctor.txt README simple twobots debug.cgi
%lang(de) %doc deutsch*
%lang(no) %doc norsk*
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 1.04-15
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 1.04-14
- 为 Magic 3.0 重建

* Mon Jan 16 2012 Petr Šabata <contyk@redhat.com> - 1.04-13
- A new build with UTF8 German and Norwegian translations

* Mon Jan 16 2012 Petr Šabata <contyk@redhat.com> - 1.04-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild
- Spec cleanup

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.04-11
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.04-9
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.04-8
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.04-7
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.04-4.1
Rebuild for new perl

* Mon Oct 15 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1.04-3.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Fri Oct 27 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.04-3
- bump

* Fri Oct 27 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.04-2
- change summary
- tag certain files in %%doc with %%lang

* Thu Oct 26 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.04-1
- Specfile autogenerated by cpanspec 1.69.1.
