Summary:	Macros to process XSL formatting objects
Summary(zh_CN.GB18030): ¥¶¿Ì XSL ∏Ò Ω∂‘œÛµƒ∫Í
Name:		passivetex
Version:	1.25
Release:  10%{?dist}
License:	LPPL
Group:		Applications/Publishing
Group(zh_CN.GB18030):	”¶”√≥Ã–Ú/≥ˆ∞Ê
Source0:	http://www.tei-c.org.uk/Software/passivetex/%{name}-%{version}.zip
Patch0:		passivetex-1.21-leader.patch
URL:		http://www.tei-c.org.uk/Software/passivetex/
BuildArch:	noarch
Requires: tex(latex)
Requires(post): tex(latex)
Requires:	xmltex >= 20020625-10
BuildRequires: tex(latex)
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
PassiveTeX is a library of TeX macros which can be used to process an
XML document which results from an XSL transformation to formatting
objects.

%description -l zh_CN.GB18030
¥¶¿Ì XSL ∏Ò Ω∂‘œÛµƒ∫Í°£

%prep
%setup -q -n %{name}
%patch0 -p1 -b .leader

%install
rm -rf $RPM_BUILD_ROOT
install -p -d $RPM_BUILD_ROOT%{_datadir}/texmf/tex/xmltex/passivetex
install -p *.sty *.xmt $RPM_BUILD_ROOT%{_datadir}/texmf/tex/xmltex/passivetex

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null || :
/usr/bin/env - PATH=$PATH:%{_bindir} fmtutil-sys --all > /dev/null 2>&1
exit 0

%postun
[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null || :
%{_bindir}/env - PATH=$PATH:%{_bindir} fmtutil-sys --all > /dev/null 2>&1
exit 0

%triggerin -- tetex-latex
%{_bindir}/env - PATH=$PATH:%{_bindir} fmtutil-sys --all > /dev/null 2>&1
exit 0

%files
%defattr(644,root,root,755)
%doc README.passivetex LICENSE
%{_datadir}/texmf/tex/xmltex/passivetex


%changelog
* Sat Jan 21 2012 Liu Di <liudidi@gmail.com> - 1.25-10
- ‰∏∫ Magic 3.0 ÈáçÂª∫


