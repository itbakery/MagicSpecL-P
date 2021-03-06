
## lyx-fonts
%global fontname lyx
%if 1
%define fontpackages 1
BuildRequires: fontpackages-devel
%else
%define _fontdir %{_datadir}/fonts/%{fontname}
%endif

%define _without_included_boost --without-included-boost

Summary: WYSIWYM (What You See Is What You Mean) document processor
Name:	 lyx
Version: 2.0.5
Release: 4%{?dist}

License: GPLv2+
Group: 	 Applications/Publishing
Url: 	 http://www.lyx.org/
Source0: ftp://ftp.lyx.org/pub/lyx/stable/2.0.x/lyx-%{version}.tar.xz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source1: lyxrc.dist
Source10: lyx.desktop

## upstreamable patches
# submitted, but upstream rejected it.  we currently agree to disagree.
Patch50: lyx-2.0.1-xdg_open.patch
# Do we need to rebuild configuration files?
%global autotools 0

%if 0%{?autotools}
BuildRequires: automake libtool
%endif
BuildRequires: enchant-devel
%if 0%{?_without_included_boost:1}
BuildRequires: boost-devel
%endif
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: hunspell-devel
BuildRequires: python
BuildRequires: qt4-devel
BuildRequires: zlib-devel

# optional minimal qt4 dep
%{?_qt_version:Requires: qt4 >= %{_qt4_version}}

Obsoletes: %{name}-qt < 1.5.0
Provides:  %{name}-qt = %{version}-%{release}
Obsoletes: %{name}-xforms < 1.5.0

Requires: %{name}-common = %{version}-%{release}

Requires: %{fontname}-fonts = %{version}-%{release}

%if 0%{?fedora} > 8 || 0%{?rhel} > 5
%if 0%{?fedora} > 17
BuildRequires: texlive-texmf-fonts
%else
#BuildRequires: texlive-fonts
%endif
BuildRequires: tex(dvips) tex(latex)
Requires: dvipdfm
Requires: tex(dvips) tex(latex)
Requires: tex-simplecv
%else
BuildRequires: tetex-dvips tetex-latex tetex-fonts
Requires: tetex-dvips tetex-latex
%endif


%if 0%{?fedora} > 8 || 0%{?rhel} > 5
Requires(post): texlive
Requires(postun): texlive
%else
Requires(post): tetex-fonts
Requires(postun): tetex-fonts
%endif

Requires: ghostscript
## Soft dependencies
%if 0%{?fedora} > 3 && 0%{?fedora} < 9
# Document->Change Tracking feature
Requires: tetex-dvipost
Requires: tetex-preview
Requires: tetex-IEEEtran
%endif
# convert doc files to lyx (bug #193858)
Requires: wv
Requires: xdg-utils
# required for instant preview
# we use a file require because depending on the texlive version used
# the package can either be texlive-dviutils for texlive 2007 or
# texlive-dtl-bin for texlive >= 2010
Requires: /usr/bin/dv2dt
Requires: ImageMagick

%description
LyX is a modern approach to writing documents which breaks with the
obsolete "typewriter paradigm" of most other document preparation
systems.

It is designed for people who want professional quality output
with a minimum of time and effort, without becoming specialists in
typesetting.

The major innovation in LyX is WYSIWYM (What You See Is What You Mean).
That is, the author focuses on content, not on the details of formatting.
This allows for greater productivity, and leaves the final typesetting
to the backends (like LaTeX) that are specifically designed for the task.

With LyX, the author can concentrate on the contents of his writing,
and let the computer take care of the rest.

%package common
Summary:  Common files of %{name}
Group:    Applications/Publishing
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description common
{summary}.

%package fonts
Summary: Lyx/MathML fonts
Group:   Applications/Publishing
# The actual license says "The author of these fonts, Basil K. Malyshev, has
# kindly granted permission to use and modify these fonts."
# One of the font files (wasy10) is separately licensed GPL+.
License: Copyright only and GPL+
%{?fontpackages:Requires: fontpackages-filesystem}
Obsoletes: mathml-fonts < 1.0-50
Provides:  mathml-fonts = 1.0-50
Obsoletes: lyx-fonts-common < 1.6.5-3
Obsoletes: lyx-fonts-compat < 1.6.5-3
Obsoletes: lyx-cmex10-fonts < 1.6.5-3
Obsoletes: lyx-cmmi10-fonts < 1.6.5-3
Obsoletes: lyx-cmr10-fonts < 1.6.5-3
Obsoletes: lyx-cmsy10-fonts < 1.6.5-3
Obsoletes: lyx-esint10-fonts < 1.6.5-3
Obsoletes: lyx-eufm10-fonts < 1.6.5-3
Obsoletes: lyx-msam10-fonts < 1.6.5-3
Obsoletes: lyx-msbm10-fonts < 1.6.5-3
Obsoletes: lyx-wasy10-fonts < 1.6.5-3
Provides:  lyx-cmex10-fonts = %{version}-%{release}
Provides:  lyx-cmmi10-fonts = %{version}-%{release}
Provides:  lyx-cmr10-fonts = %{version}-%{release}
Provides:  lyx-cmsy10-fonts = %{version}-%{release}
BuildArch: noarch
%description  fonts
A collection of Math symbol fonts for %{name}.


%prep

%setup -q -n %{name}-%{version}

%patch50 -p1 -b .xdg_open

%if 0%{?autotools}
./autogen.sh
%endif


%build

%configure \
  --disable-dependency-tracking \
  --disable-rpath \
  --enable-build-type=release \
  --enable-optimization="%{optflags}" \
  --without-included-boost \
  --with-enchant \
  --with-hunspell

make %{?_smp_mflags}


%install
rm -rf %{buildroot}

make install DESTDIR=%{buildroot}

# misc/extras
install -p -m644 -D %{SOURCE1} %{buildroot}%{_datadir}/lyx/lyxrc.dist

# Set up the lyx-specific class files where TeX can see them
texmf=%{_datadir}/texmf
mkdir -p %{buildroot}${texmf}/tex/latex
mv %{buildroot}%{_datadir}/lyx/tex \
   %{buildroot}${texmf}/tex/latex/lyx

# .desktop
desktop-file-install --vendor="" \
  --dir="%{buildroot}%{_datadir}/applications" \
  %{SOURCE10}

# icon
install -p -D -m644 lib/images/lyx.png \
  %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/lyx.png

# ghost'd files
touch %{buildroot}%{_datadir}/lyx/lyxrc.defaults
touch %{buildroot}%{_datadir}/lyx/{packages,textclass}.lst

# fonts
install -m 0755 -d %{buildroot}%{_fontdir}
mv %{buildroot}%{_datadir}/lyx/fonts/*.ttf %{buildroot}%{_fontdir}/
rm -rf %{buildroot}%{_datadir}/lyx/fonts

%find_lang %{name}

# bash completion
install -p -D -m 0755 lib/scripts/bash_completion %{buildroot}%{_sysconfdir}/bash_completion.d/lyx

%check
# tests/test_filetools error bogus ( see http://bugzilla.redhat.com/723938 )
make -k check ||:


%post common
touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :

%postun common
if [ $1 -eq 0 ] ; then
  texhash >& /dev/null
  update-desktop-database -q &> /dev/null
  touch --no-create %{_datadir}/icons/hicolor &> /dev/null
  gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
fi

%posttrans common
texhash >& /dev/null
update-desktop-database -q &> /dev/null
gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :

## Catch installed/uninstalled helpers
##   not sure if this is really needed anymore, as it seems to be a per-user thing,
##   and besides, we use xdg-open now -- Rex
#triggerin common -- latex2html,wv
#if [ $2 -gt 1 ]; then
#cd %{_datadir}/lyx && ./configure.py --without-latex-config > /dev/null 2>&1 ||:
#fi
#
#triggerun common -- latex2html,wv
#if [ $2 -eq 0 ]; then
#cd %{_datadir}/lyx && ./configure.py --without-latex-config > /dev/null 2>&1 ||:
#fi


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc ANNOUNCE COPYING lib/CREDITS NEWS README
%{_bindir}/*

%files common -f %{name}.lang
%defattr(-,root,root,-)
%{_mandir}/man1/*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/lyx/
%config(noreplace) %{_datadir}/lyx/lyxrc.dist
%ghost %{_datadir}/lyx/lyxrc.defaults
%ghost %{_datadir}/lyx/*.lst
%{_datadir}/texmf/tex/latex/lyx/
%{_sysconfdir}/bash_completion.d

%if 0%{?fontpackages:1}
%_font_pkg
%{_fontdir}/*.ttf
%doc lib/fonts/BaKoMaFontLicense.txt
%doc lib/fonts/ReadmeBaKoMa4LyX.txt
%else
%files fonts
%defattr(-,root,root,-)
%dir %{_fontdir}/
%{_fontdir}/*.ttf
%doc lib/fonts/BaKoMaFontLicense.txt
%doc lib/fonts/ReadmeBaKoMa4LyX.txt

%posttrans fonts
fc-cache %{_fontdir} 2> /dev/null ||:
%endif


%changelog
* Sat Apr 20 2013 Liu Di <liudidi@gmail.com> - 2.0.5-4
- 为 Magic 3.0 重建

* Mon Nov 26 2012 José Matos <jamatos@fedoraproject.org> - 2.0.5-3
- Install bash completion (#802149)

* Sun Nov 25 2012 José Matos <jamatos@fedoraproject.org> - 2.0.5-2
- New texlive packaging for Fedora 18+

* Sun Nov 25 2012 José Matos <jamatos@fedoraproject.org> - 2.0.5-1
- New bugfix release

* Thu Aug 09 2012 Rex Dieter <rdieter@fedoraproject.org> 2.0.4-3
- rebuild (boost)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 30 2012 Rex Dieter <rdieter@fedoraproject.org> 2.0.4-1
- lyx-2.0.4
- Omitted backslash in code for floatingfootnote, after export to latex, and re-import (#811719)

* Mon Mar  5 2012 José Matos <jamatos@fedoraproject.org> - 2.0.3-1
- New bugfix release

* Wed Feb 29 2012 Rex Dieter <rdieter@fedoraproject.org> 2.0.2-4
- hack around gcc-4.7 ftbfs for now

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-3
- Rebuilt for c++ ABI breakage

* Sat Jan  7 2012 José Matos <jamatos@fedoraproject.org> - 2.0.2-2
- Require ImageMagick (#753626)

* Thu Dec  1 2011 José Matos <jamatos@fedoraproject.org> - 2.0.2-1
- New stable release.

* Tue Nov 22 2011 Rex Dieter <rdieter@fedoraproject.org> 2.0.1-3
- rebuild (boost)

* Mon Sep  5 2011 José Matos <jamatos@fedoraproject.org> - 2.0.1-2
- Update xdg_open patch for version 2.0.1

* Mon Sep  5 2011 José Matos <jamatos@fedoraproject.org> - 2.0.1-1
- Update to 2.0.1

* Thu Jul 21 2011 Rex Dieter <rdieter@fedoraproject.org> 2.0.0-5
- rebuild (boost)

* Wed Jun  1 2011 José Matos <jamatos@fedoraproject.org> - 2.0.0-4
- LaTeXConfig.lyx is no longer a ghost (#684428)

* Thu May 26 2011 Rex Dieter <rdieter@fedoraproject.org> 2.0.0-3
- fix hunspell support (use pkgconfig)

* Thu May 26 2011 Rex Dieter <rdieter@fedoraproject.org> 2.0.0-2
- rebuild (hunspell)

* Fri Apr 29 2011 José Matos <jamatos@fedoraproject.org> - 2.0.0-1
- Update to 2.0.0 final

* Mon Apr 11 2011 José Matos <jamatos@fedoraproject.org> - 2.0.0-0.21.rc3
- Update to rc3

* Thu Apr  7 2011 José Matos <jamatos@fedoraproject.org> - 2.0.0-0.20.rc2
- Rebuild for new boost (just applies to F16)

* Tue Mar 29 2011 José Matos <jamatos@fedoraproject.org> - 2.0.0-0.19.rc2
- New upstream release (rc2)

* Mon Mar 14 2011 José Matos <jamatos@fedoraproject.org> - 2.0.0-0.18.rc1
- Rebuild for boost upgrade

* Sat Mar 12 2011 José Matos <jamatos@fedoraproject.org> - 2.0.0-0.17.rc1
- Add thesaurus and hunspell paths to lyxrc.dist thus fixing
  http://www.lyx.org/trac/ticket/7253
- Simplified the content of lyxrc.dist leaving only the relevant
  options and updating the format to the current one

* Fri Mar 11 2011 José Matos <jamatos@fedoraproject.org> - 2.0.0-0.16.rc1
- Update for rc1 and add a dependency to ensure that math instant
  preview works by default
- Removed patch applied upstream for gcc 4.6 fixes
- Renamed patch for xdg_open to be in sync with current version (rc1)

* Fri Feb 11 2011 Orion Poplawski <orion@cora.nwra.com> 2.0.0-0.15.beta4
- Get gcc46 fixes from svn

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-0.14.beta4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb 07 2011 Rex Dieter <rdieter@fedoraproject.org> 2.0.0-0.13.beta4
- 2.0.0-beta4

* Mon Feb 07 2011 Thomas Spura <tomspur@fedoraproject.org> 2.0.0-0.12.beta3
- rebuild for new boost

* Tue Jan 11 2011 Rex Dieter <rdieter@fedoraproject.org> 2.0.0-0.11.beta3
- lyx-2.0.0-beta3

* Wed Dec 08 2010 Rex Dieter <rdieter@fedoraproject.org> 2.0.0-0.10.beta2
- lyx-2.0.0-beta2

* Wed Nov 10 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.0.0-0.9.beta1
- lyx-2.0.0-beta1 (#651488)

* Tue Nov 09 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.0.0-0.8.alpha6
- lyx-2.0.0-alpha6 (#651488)

* Wed Nov 03 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.0.0-0.7.alpha5
- drop %%triggers, *may* affect selinux labels (#632944)

* Thu Aug 05 2010 Orion Poplawski <orion@cora.nwra.com> - 2.0.0-0.6.alpha5
- Rebuild for newer boost

* Wed Jul 21 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.0.0-0.5.alpha5
- lyx-2.0.0-alpha5

* Thu Jun 17 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.0.0-0.4.alpha4
- lyx-2.0.0-alpha4

* Thu May 13 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.0.0-0.3.alpha3
- lyx-2.0.0-alpha3

* Sat Apr 17 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.0.0-0.2.alpha2
- lyx-2.0.0-alpha2

* Sat Apr 03 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.0.0-0.1.alpha1
- lyx-2.0.0-alpha1

* Sun Feb 14 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.6.5-5
- FTBFS lyx-1.6.5-4.fc13: ImplicitDSOLinking (#565009)

* Thu Jan 21 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.6.5-4
- -fonts: Provides: lyx-{cmex10,cmmi10,cmr10,cmsy10}-fonts

* Sat Jan 16 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.6.5-3
- rebiuld (boost)
- use simple font template

* Wed Dec  9 2009 José Matos <jamatos@fc.up.pt> - 1.6.5-2
- Add patch for autoconf 2.65 (F13+)

* Wed Dec  9 2009 José Matos <jamatos@fc.up.pt> - 1.6.5-1
- lyx-1.6.5

* Thu Nov 19 2009 José Matos <jamatos@fc.up.pt> - 1.6.4-3
- LyX supports autoconf 2.64 (should be upstream for 1.6.5)

* Thu Sep 17 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.6.4-2
- use enchant instead of aspell (#524046)

* Sat Aug 22 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.6.4-1
- lyx-1.6.4
- handle fonts manually (now EPEL-5 compatible)

* Mon Aug 03 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.6.3-3
- add lyx-*-fonts subpkgs (#452357, #514549)
- -common (noarch) subpkg
- trim %%changelog

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jun 04 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.6.3-1
- lyx-1.6.3

* Mon Mar 23 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.6.2-2
- scriptlet optimization

* Sun Mar 15 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.6.2-1
- lyx-1.6.2
- use --without-included-boost unconditionally

* Wed Mar 04 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.6.1-3
- --without-included-boost (f11+)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Dec 14 2008 Rex Dieter <rdieter@fedoraproject.org> - 1.6.1-1
- lyx-1.6.1

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.6.0-2
- Rebuild for Python 2.6

* Fri Nov 07 2008 Rex Dieter <rdieter@fedoraproject.org> - 1.6.0-1
- lyx-1.6.0(final)

* Tue Oct 28 2008 José Matos <jamatos@fc.up.pt> - 1.6.0-0.11.rc5
- lyx-1.6.0rc5

* Fri Oct 24 2008 Rex Dieter <rdieter@fedoraproject.org> - 1.6.0-0.10.rc4
- lyx-1.6.0rc4

* Tue Sep 30 2008 Rex Dieter <rdieter@fedoraproject.org> - 1.6.0-0.9.rc3
- lyx-1.6.0rc3

* Fri Sep 26 2008 Rex Dieter <rdieter@fedoraproject.org> - 1.6.0-0.8.rc3
- lyx-1.6.0rc3-svn26576

* Fri Sep 12 2008 Rex Dieter <rdieter@fedoraproject.org> - 1.6.0-0.7.rc2
- lyx-1.6.0rc2

* Wed Aug 06 2008 Rex Dieter <rdieter@fedoraproject.org> - 1.6.0-0.6.rc1
- lyx-1.6.0rc1

* Sun Aug 03 2008 Rex Dieter <rdieter@fedoraproject.org> - 1.6.0-0.5.beta4
- Requires: dvipdfm (f9+, #448647)
- add (optional) minimal qt4 dep
- make Req: tex-simplecv fedora only
- drop file deps (texhash)

* Wed Jul 16 2008 José Matos <jamatos[AT]fc.up.pt> - 1.6.0-0.4.beta4
- Changelog has been removed from the distribution

* Wed Jul 16 2008 José Matos <jamatos[AT]fc.up.pt> - 1.6.0-0.3.beta4
- icon has changed from xpm to png

* Wed Jul 16 2008 José Matos <jamatos[AT]fc.up.pt> - 1.6.0-0.2.beta4
- revert to use pre instead of devrel.
- require tex-simplecv (#428526)

* Wed Jul 16 2008 José Matos <jamatos[AT]fc.up.pt> - 1.6.0-0.1.beta4
- lyx-1.6.0beta4
- --enable-build-type=release disables extra debug information (no
    warnings, debug, assertions, concept-checks and stdlib-debug).

* Mon May 12 2008 Rex Dieter <rdieter@fedoraproject.org> 1.5.5-1
- lyx-1.5.5

* Mon Feb 25 2008 Rex Dieter <rdieter@fedoraproject.org> 1.5.4-1
- lyx-1.5.4 (#434689)
- reintroduce xdg-utils patch (reverted upstream).
- omit bakoma ttf fonts

* Mon Feb 11 2008 José Matos <jamatos[AT]fc.up.pt> - 1.5.3-2
- Rebuild for gcc 4.3

* Mon Dec 17 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.5.3-1
- lyx-1.5.3

* Tue Dec 04 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.5.2-2
- drop scriptlet optimization hack

* Mon Oct 08 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.5.2-1
- lyx-1.5.2

* Sat Aug 25 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.5.1-2
- respin (BuildID)

* Thu Aug 09 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.5.1-1
- lyx-1.5.1
- License: GPLv2+

* Wed Jul 25 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.5.0-1
- lyx-1.5.0(final)

* Sun Jul 15 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.5.0-0.10.rc2
- upstream patch for 'lyx --export latex' crasher (#248282)

* Thu Jun 28 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.5.0-0.9.rc2
- scriptlet optmization

* Thu Jun 28 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.5.0-0.8.rc2
- lyx-1.5.0rc2

* Fri Jun 01 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.5.0-0.7.rc1
- lyx-1.5.0rc1

* Fri May 18 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.5.0-0.6.beta3
- lyx-1.5.0beta3

* Sun Apr 22 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.5.0-0.5.beta2
- lyx-1.5.0beta2

* Mon Apr 02 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.5.0-0.4.beta1
- fix qt-4.3 crasher

* Tue Mar 27 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.5.0-0.3.beta1
- stop omitting -fexceptions

* Wed Mar 21 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.5.0-0.2.beta1
- +Requires: tetex-IEEEtran (#232840)

* Mon Mar 05 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.5.0-0.1.beta1
- lyx-1.5.0beta1
- tweak lyxrc.dist

* Thu Feb 15 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.4.4-2
- biffed sources, respin

* Wed Feb 14 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.4.4-1
- lyx-1.4.4
- .desktop's: -Category=Application
- mark -xforms as deprecated

* Sun Oct 01 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.4.3-3
- sync .desktop files with upstream
- use xdg-open as default helper, +Requires: xdg-utils

* Thu Sep 21 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.4.3-1
- lyx-1.4.3

* Thu Sep 07 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.4.2-5
- fc6 respin

* Thu Aug 17 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.4.2-4
- owowned files, incomplete package removal (bug #201197)

* Thu Jul 13 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.4.2-2
- 1.4.2

* Wed Jun 29 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.4.1-9
- Requires(hint): wv (bug #193858)
- fix dependancy -> dependency

* Thu Jun 15 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.4.1-8
- BR: gettext
- fc4: restore Requires(hint): tetex-preview

* Thu May 25 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.4.1-7.1
- fc4: drop Requires: tetex-preview, it's not ready yet.

* Wed May 24 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.4.1-7
- use serverpipe "~/.lyx/lyxpipe" instead, that was the old default
  and what pybibliographer expects.

* Tue May 23 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.4.1-6
- set defaults for (see %{_datadir}/lyx/lyxrc.defaults.custom)
  screen_font_roman "Serif"
  screen_font_sans "Sans"
  screen_font_typewriter "Monospace"
  screen_zoom 100
  serverpipe "~/.lyx/pipe"
  (bug #192253)

* Mon May 22 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.4.1-5
- Requires(hint): tetex-preview

* Tue May 16 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.4.1-4
- add generic app icon (rh #191944)

* Fri Apr 28 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.4.1-3
- Requires(hint): tetex-dvipost
  adds support for lyx's Document->Change Tracking

* Tue Apr 11 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.4.1-2
- 1.4.1

* Thu Mar 30 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.4.0-5
- %%trigger ImageMagick (#186319)

* Thu Mar 09 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.4.0-4
- fix stripping of -fexceptions from %%optflags

* Wed Mar 08 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.4.0-3
- include beamer.layout

* Wed Mar 08 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.4.0-2
- 1.4.0(final)
- drop boost bits
