Name:       m17n-db
Summary:    Multilingualization datafiles for m17n-lib
Version:    1.6.3
Release:    3%{?dist}
Group:      System Environment/Libraries
License:    LGPLv2+
URL:        http://www.m17n.org/m17n-lib/index.html
Source0:    http://www.m17n.org/m17n-lib-download/%{name}-%{version}.tar.gz
BuildArch:  noarch
BuildRequires: gettext

# Fedora speicifc patches
Patch1:     number_pad_itrans-222634.patch
Patch2:     bn-itrans-t-182227.patch
Patch4:     kn-itrans_key-summary_228806.patch
Patch5:     ml-itrans-keysummary-435260.patch
# Upstream patches
Patch11:     si-wijesekera-altgr-key.patch

%description
This package contains multilingualization (m17n) datafiles for m17n-lib
which describe input maps, encoding maps, OpenType font data and
font layout text rendering for languages.

%package extras
Summary:  Extra m17n-db files
Group:    System Environment/Libraries
Requires: %{name} = %{version}-%{release}

%description extras
m17n-db extra files for input maps that are less used.

%package devel
Summary:  Development files for m17n-db
Group:    Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
m17n-db development files


%prep
%setup -q 
pushd MIM
%patch1 -p1 -b .1~
%patch2 -p1 -b .2~
%patch4 -p0 -b .4~
%patch5 -p0 -b .5~
%patch11 -p0 -b .11~
popd

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

# don't ship unijoy map for now
rm $RPM_BUILD_ROOT%{_datadir}/m17n/{bn-unijoy.mim,icons/bn-unijoy.png}

#removing ispell.mim for rh#587927
rm $RPM_BUILD_ROOT%{_datadir}/m17n/ispell.mim

# For installing the translation files
%find_lang %name

%files 
%doc AUTHORS COPYING README
%dir %{_datadir}/m17n
%dir %{_datadir}/m17n/icons
%{_datadir}/m17n/mdb.dir
%{_datadir}/m17n/*.tbl
%{_datadir}/m17n/*.mim
%exclude %{_datadir}/m17n/zh-*.mim
%exclude %{_datadir}/m17n/icons/zh*.png
%exclude %{_datadir}/m17n/ja-*.mim
%exclude %{_datadir}/m17n/icons/ja*.png
%{_datadir}/m17n/icons/*.png
%{_datadir}/m17n/*.flt

%files extras -f %{name}.lang
%{_datadir}/m17n/zh-*.mim
%{_datadir}/m17n/icons/zh*.png
%{_datadir}/m17n/ja*.mim
%{_datadir}/m17n/icons/ja*.png
%{_datadir}/m17n/*.fst
%{_datadir}/m17n/*.map
%{_datadir}/m17n/*.tab
%{_datadir}/m17n/*.lnm
%{_datadir}/m17n/LOCALE.*

%files devel
%{_bindir}/m17n-db
%{_datadir}/pkgconfig/m17n-db.pc

%changelog
* Fri Dec 07 2012 Liu Di <liudidi@gmail.com> - 1.6.3-3
- 为 Magic 3.0 重建

* Wed Dec 21 2011 Parag Nemade <pnemade AT redhat DOT com> - 1.6.3-2
- Resolves:rh#769239 - altgr change in wijesekara keyboard layout

* Tue Oct 11 2011 Parag Nemade <pnemade AT redhat DOT com> - 1.6.3-1
- update to 1.6.3

* Thu Mar 24 2011 Parag Nemade <pnemade AT redhat DOT com> - 1.6.2-3
- Resolves:rh#650802-[si] stick characters with cursor, while input with si-wijesekera.mim
- Resolves:rh#651289-zh-cangjie.mim: excessive space after committing Chinese word
- Drop obsoletes/provides added in f14

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Oct 06 2010 Parag Nemade <pnemade AT redhat.com> - 1.6.2-1
- update to new upstream release 1.6.2
- Drop kn-itrans-ZWNJ-221965.patch

* Fri Jul 23 2010 Parag Nemade <pnemade AT redhat.com> - 1.6.1-3
- Fix the upgrade path from F13 to F14

* Thu Jul  8 2010 Jens Petersen <petersen@redhat.com>
- use excludes to simplify .mim and icon filelists

* Wed Jul 07 2010 Parag Nemade <pnemade@redhat.com> - 1.6.1-2
- Resolves: rh#587927:- evince attempts to use libmimx-ispell.so

* Tue Apr 27 2010 Parag Nemade <pnemade AT redhat.com> - 1.6.1-1
- update to new upstream release 1.6.1

* Wed Apr 07 2010 Parag Nemade <pnemade AT redhat.com> - 1.6.0-2
- drop Provides:m17n-db-devel for m17n-db

* Wed Apr 07 2010 Parag Nemade <pnemade AT redhat.com> - 1.6.0-1
- update to new upstream release 1.6.0

* Wed Dec 23 2009 Jens Petersen <petersen@redhat.com> - 1.5.5-3
- separate .flt files to flt subpackage for m17n-lib-flt

* Fri Dec 18 2009 Jens Petersen <petersen@redhat.com> - 1.5.5-2
- add common-cjk option to mk_pkg for zh and ko
- use mk_pkg for zh, el, ka, ug
- bring back ja-anthy and en-ispell
- cleanup trailing whitespace

* Wed Jul 29 2009 Parag Nemade <pnemade@redhat.com> -1.5.5-1
- update to new upstream release 1.5.5

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr 08 2009 Parag Nemade <pnemade@redhat.com> -1.5.4-2
- Resolves: rh#494810-[indic][m17n-db][m17n-contrib] ibus .engine files no longer needed for new ibus

* Tue Mar 03 2009 Parag Nemade <pnemade@redhat.com> -1.5.4-1
- Update to new upstream release 1.5.4

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Oct 21 2008 Parag Nemade <pnemade@redhat.com> -1.5.3-1.fc10
- Update to new upstream release 1.5.3

* Mon Oct 20 2008 Jens Petersen <petersen@redhat.com> - 1.5.2-4.fc10
- add obsoletes for ibus-m17n subpackages
- fix m17n-gen-ibus-engine to check for lang 't'

* Wed Oct 15 2008 Jens Petersen <petersen@redhat.com> - 1.5.2-3.fc10
- create .engine files for ibus-m17n with m17n-gen-ibus-engine (#466410)

* Fri Aug 29 2008 Parag Nemade <pnemade@redhat.com> -1.5.2-2
- Recreated patch si-wijesekera-keymap-rename_key-summary.patch

* Thu Jul 03 2008 Parag Nemade <pnemade@redhat.com> -1.5.2-1
- Update to new upstream release 1.5.2

* Fri Apr 04 2008 Parag Nemade <pnemade@redhat.com> -1.5.1-3.fc9
- Resolves:rh#440567

* Wed Apr 02 2008 Parag Nemade <pnemade@redhat.com> -1.5.1-2.fc9
- Resolves:rh#435260

* Thu Feb 07 2008 Parag Nemade <pnemade@redhat.com> -1.5.1-1.fc9
- Update to new upstream release 1.5.1
- Added BR: gettext

* Fri Dec 28 2007 Parag Nemade <pnemade@redhat.com> -1.5.0-1.fc9
- Update to new upstream release 1.5.0

* Fri Sep 07 2007 Parag Nemade <pnemade@redhat.com> - 1.4.0-6.fc8
- Removed incorrect version of hi-typewriter.mim

* Mon Aug 20 2007 Parag Nemade <pnemade@redhat.com> - 1.4.0-5.fc8
- Added Obsoletes to m17n-db-gregorian
- Added Obsoletes to m17n-db-uyghur
- Added Provides to m17n-db-gregorian, m17n-db-gregorian, m17n-db-chinese

* Mon Aug 13 2007 Parag Nemade <pnemade@redhat.com>
- update License tag

* Wed Jul 25 2007 Parag Nemade <pnemade@redhat.com> - 1.4.0-4
- Added m17n-db as Requires for mk_pkg() macro generating packages.
- Added m17b-db and m17n-contrib-lang as Requires
  for mk_pkg_uses_contrib() macro generating packages.

* Wed Jul 25 2007 Jens Petersen <petersen@redhat.com> - 1.4.0-3
- cleanup summaries and descriptions
- make just main package own m17n and icons dir
- replace %%makeinstall with make install

* Tue Jul 24 2007 Parag Nemade <pnemade@redhat.com> - 1.4.0-2.1
- Fix directory ownership issue

* Mon Jul 23 2007 Parag Nemade <pnemade@redhat.com> - 1.4.0-2
- SPEC clean up. Remove m17n-contrib

* Thu Jul 19 2007 Parag Nemade <pnemade@redhat.com> - 1.4.0-1
- Updated to new upstream release 1.4.0

* Wed Jul 18 2007 Jens Petersen <petersen@redhat.com>
- install .pc file under %%{_datadir}/pkgconfig
  and include it in a new devel subpackage

* Mon Jun 18 2007 Jens Petersen <petersen@redhat.com> - 1.3.4-10
- name Uyghur subpackage consistently

* Wed May 16 2007 Jens Petersen <petersen@redhat.com> - 1.3.4-9
- update ta-typewriter.mim with bug fixes (I Felix, #236169)

* Thu Mar 15 2007 Mayank Jain <majain@redhat.com> 1.3.4-8
- Added key summary to kn-itrans,inscript keymaps - resolves 228806

* Thu Feb 15 2007 Mayank Jain <majain@redhat.com>
- Added ZWNJ (U+200d) needed in kn-* keymaps, resolved - 221965
- Added kn-itrans-ZWNJ-221965.patch

* Thu Feb 15 2007 Mayank Jain <majain@redhat.com>
- Added itrans layout for Marahi, resolved - 225561

* Thu Feb 8 2007 Mayank Jain <majain@redhat.com>
- Added phonetic keymaps for Marathi & Oriya, resolved - 225559 and 225562

* Tue Jan 17 2007 Mayank Jain <majain@redhat.com>
- Added Patch 4 as number_pad_itrans-222634.patch for adding number pad support in itrans keymaps
- Added number pad support in all indic keymaps except tamil as they used english numerals.
- Resolves bug : 222634

* Tue Jan 16 2007 Mayank Jain <majain@redhat.com>
- Added Patch 3 as sk-kbd-222804.patch to fix bug 222804

* Tue Jan 11 2007 Mayank Jain <majain@redhat.com>
- Moved all translations to m17n-db-datafiles package

* Tue Jan 8 2007 Mayank Jain <majain@redhat.com>
- Resolves: Bug 221794 - Rebased to new release m17n-db-1.3.4
- Removed patch: si-wijesekera_surrounding_to_preedit.patch
- Added directive to delete si-wijesekera from the upstream tarball as it used surrounding text
- Commented directive to copy bopo-kbd.mim
- Commented directive using variable.mim and command.mim - added global.mim in place of them
- Added sections for new Uyghur.
- Added copy directive for Mizuochi (grc-*) keymap for classical greek
- Added directives to install translations for japanese translations.
- Added patch to rename si-wijesekera-preedit to si-wijesekera and add key summary as Patch2

* Tue Jan 2 2007 Mayank Jain <majain@redhat.com>
- Resolves: Bug 221122: [hi_IN-remington] vowels in hi-remington are not typed correctly

* Thu Dec 7 2006 Mayank Jain <majain@redhat.com>
- Resolves: bug 218255 - Fixed ta-typewriter keymap.

* Tue Dec 1 2006 Mayank Jain <majain@redhat.com>
- Fixed typo in si-wijesekera key summary (in the patch)

* Tue Nov 28 2006 Mayank Jain <majain@redhat.com>
- Reverted back to upstream's tarball for m17n-db
- Added si-wijesekera-with-preedit as a patch to m17n-db tarball
- Updated license header in hi-remington, as-inscript, or-inscript, ta-typewriter
- Resolved - 217318, 217319

* Mon Nov 27 2006 Mayank Jain <majain@redhat.com>
- Added halant to (t) in bn-itrans.mim in m17n-indic tarball, resolves bug 217139
- Edited our own bn-itrans-t-182227.patch to resolve bug 217139

* Mon Nov 20 2006 Mayank Jain <majain@redhat.com>
- Retained mapping of (.) to (.) in as-inscript as per bug 215486
- Fixed an error in ta-tamil99 key summary.

* Mon Nov 14 2006 Mayank Jain <majain@redhat.com>
- Fixed Bug 177371: mapping of X and x in kn-kgp
- Fixed Bug 215486: Mapped 0x0964 to shift(.) instead of . in as-inscript
- Fixed Bug 215489: Mapped 0x0964 to shift(.) instead of . in bn-inscript

* Mon Nov 13 2006 Mayank Jain <majain@redhat.com>
- Added ZWNJ to ml-inscript, fixes 214971

* Mon Nov 9 2006 Mayank Jain <majain@redhat.com>
- Fixed an errounous fix of ZWNJ to hi-inscript/phonetic

* Mon Nov 6 2006 Mayank Jain <majain@redhat.com>
- Fixed Bug 213633: Need changes in Assamese Inscript layout

* Mon Nov 2 2006 Mayank Jain <majain@redhat.com>
- Added ZWNJ to hi-inscript/phonetic

* Mon Nov 1 2006 Mayank Jain <majain@redhat.com>
- Added 09CE mapped to z in as-inscript (213372)

* Mon Nov 1 2006 Mayank Jain <majain@redhat.com>
- Imported m17n-db-indic-0.4.29.tar.gz from RHEL-5 package, changes happened from .28 version are
- Added few more key combinations for ta-typewriter keymap - bug 209088
- Added ZWJ for hi-inscript and hi-phonetic keymaps - bug 211576
- Corrected kn-kgp and kn-inscript keymaps for keymapping of X - bug 209963

* Mon Oct 17 2006 Mayank Jain <majain@redhat.com>
- Added si-wijesekera keymap with preedit, replaces si-wijesekera with surrounding text support
- Fixed kn-kgp keymap

* Mon Oct 16 2006 Mayank Jain <majain@redhat.com>
- Cleaned the spec file, versioning errors & removed use of epoch from the spec file
- Added ta-typewriter keymap & icon, fixes bug 209088

* Mon Oct 16 2006 Mayank Jain <majain@redhat.com>
- Switched the version number for m17n-db back to 1.3.3
- Added "Epoch : 1" in the spec file to override the 1.3.4 build.

* Mon Oct 9 2006 Mayank Jain <majain@redhat.com>
- Added key summary for si-wijesekera keymap

* Wed Oct 4 2006 Mayank Jain <majain@redhat.com>
- Removed errernous entries from ta-tamil99 keymap

* Tue Sep 12 2006 Mayank Jain <majain@redhat.com>
- Added key summary to te-inscript keymap

* Thu Sep 7 2006 Mayank Jain <majain@redhat.com>
- Updated keymaps for typo errors, updated copyright header in all keymaps with "This file is part of the m17n contrib; a sub-part of the m17n library"
- Added key summary for ta-tamil99 keymap
- updated key summary for bn-itrans.mim

* Wed Sep 6 2006 Mayank Jain <majain@redhat.com>
- Updated or-inscript.mim for bug 204726

* Wed Sep 6 2006 Mayank Jain <majain@redhat.com>
- Updated bn-probhat & as-phonetic keymaps with *=>ৎ
- Corrected date type in changelog

* Tue Sep 5 2006 Mayank Jain <majain@redhat.com>
- Updated as-phonetic with key summary

* Mon Sep 4 2006 Mayank Jain <majain@redhat.com>
- Added key summaries to pa-inscript/jhelum
- Fixed 204755

* Tue Aug 31 2006 Mayank Jain <majain@redhat.com>
- Added ur-phonetic icon
- Updated spec file to incorporate the icon

* Tue Aug 31 2006 Mayank Jain <majain@redhat.com>
- Updated bn-{inscript,probhat,itrans} for RH bug #204275
- Added ur-phonetic.mim file for RH bug #177372
- Updated m17n-db.spec file to incorporate Urdu keymap.

* Tue Aug 8 2006 Mayank Jain <majain@redhat.com>
- Updated bn-probhat.mim for RH bz #200890 ...weird... that previous update didnt showed up!
- https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=200890#c4

* Tue Aug 1 2006 Mayank Jain <majain@redhat.com>
- Corrected bn-probhat.mim file, RH bz #200890, added U+09CE

* Tue Aug 1 2006 Mayank Jain <majain@redhat.com>
- Corrected ml-inscript.mim file, RH bz #200876

* Tue Jul 25 2006 Jens Petersen <petersen@redhat.com> - 1.3.3-14
- move bopomofo to chinese subpackage

* Mon Jul 17 2006 Mayank Jain <majain@redhat.com> - 1.3.3-13
- Removed ta-typewriter.mim keymap as its not working
- Added ml-inscript.png
- Added hi-inscript.png
- added hi-remington.png

* Thu Jul 13 2006 Mayank Jain <majain@redhat.com>
- Added ta-typewriter.mim keymap

* Thu Jul 6 2006 Mayank Jain <majain@redhat.com>
- Added key summaries in various keymaps

* Thu Jun 29 2006 Mayank Jain <majain@redhat.com>
- Added hi-remington keymap - <rranjan@redhat.com>
- Added hi-remington.png - <aalam@redhat.com>

* Thu Jun 8 2006 Mayank Jain <majain@redhat.com>
- Added hi-typewriter keymap.

* Wed Jun 7 2006 Mayank Jain <majain@redhat.com>
- Added or-*.png icons.

* Mon Jun 5 2006 Mayank Jain <majain@redhat.com>
- Added as-*.png icons.

* Fri Jun 2 2006 Mayank Jain <majain@redhat.com>
- Added or-inscript keymap to the tarball
- Commented out as-*.png and or-*.png from the directives as respective .png files are missing from tarball.

* Fri Jun 2 2006 Mayank Jain <majain@redhat.com>
- Added modified as-phonetic.mim keymap, modified by <runab@redhat.com> for RH bz #193849

* Mon May 29 2006 Mayank Jain <majain@redhat.com>
- Added icon for marathi inscript - thanks to <aalam@redhat.com>

* Wed May 17 2006 Mayank Jain <majain@redhat.com>
- Added following keymaps
  - as-inscript.mim
  - as-phonetic.mim
  - mr-inscript.mim
  - ta-tamil99.mim

* Wed Mar 22 2006 Jens Petersen <petersen@redhat.com>
- fix language names in Indic .mim file headers (Naoto Takahashi)
- add make-dist script to m17n-db-indic

* Thu Mar  9 2006 Jens Petersen <petersen@redhat.com> - 1.3.3-2
- Bengali input maps fixes (runab)
  - map Probhat '*' key to an alternate sequence since glyph missing (#179821)
  - more itrans cleanup (#182227)
- add icon for Tamil99 (aalam)

* Thu Mar  2 2006 Jens Petersen <petersen@redhat.com> - 1.3.3-1
- update to 1.3.3 bugfix release
- fixes to Bengali, Hindi, and Punjabi maps (runab, aalam)
- Tamil phonetic map now works
- new Tamil99 Government Standard map (I Felix)

* Tue Feb 14 2006 Jens Petersen <petersen@redhat.com> - 1.3.2-2
- add Indian input maps ported from scim-tables
- add Nepali subpackage

* Fri Feb 10 2006 Jens Petersen <petersen@redhat.com> - 1.3.2-1
- update to 1.3.2 bugfix release
- do not include ja-anthy.mim input map

* Thu Feb  2 2006 Jens Petersen <petersen@redhat.com> - 1.3.1-1
- update to 1.3.1 release
  - add new icons to language subpackages
  - new common-cjk subpackage for CJK common files
  - new Swedish subpackage
  - exclude new pkgconfig file

* Fri Dec 16 2005 Jens Petersen <petersen@redhat.com> - 1.2.0-2
- import to Fedora Core

* Wed Nov  9 2005 Jens Petersen <petersen@redhat.com> - 1.2.0-1
- separate output datafiles to datafiles subpackage.

* Wed Oct  5 2005 Jens Petersen <petersen@redhat.com>
- initial packaging for Fedora Extras

* Sat Sep 24 2005 Jens Petersen <petersen@redhat.com>
- split .mim input tables into separate subpackages per language

* Sat Jan 15 2005 UTUMI Hirosi <utuhiro78@yahoo.co.jp>
- modify spec for fedora
