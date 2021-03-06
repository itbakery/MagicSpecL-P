%define with_java 0
%define separate_xpce 1

Name:       pl
Version:    6.2.2
Release:    2%{?dist}

Summary:    SWI-Prolog - Edinburgh compatible Prolog compiler

Group:      Development/Languages
#library/dialect/iso/iso_predicates.pl  GPLv2+ with SWI-Prolog extra clause
#                                       or Artistic 2.0
#packages/clib/uri.c            LGPLv2+
#packages/sgml/Test/test.pl     LGPLv2
#library/qsave.pl               GPLv2+
#library/COPYING                GPLv2 with SWI-Prolog extra clause
#library/unicode/blocks.pl      UCD
#packages/http/examples/calc.pl Public Domain
#External: JavaConfig.java      GPLv3+
License:    (GPLv2+ or Artistic 2.0) and LGPLv2+ and LGPLv2 and GPLv2 and GPLv2+ and UCD and Public Domain and GPLv3+
URL:        http://www.swi-prolog.org/
Source:     %{url}download/stable/src/%{name}-%{version}.tar.gz
Source1:    %{url}download/stable/doc/SWI-Prolog-%{version}.pdf
Source2:    %{url}download/xpce/doc/userguide/userguide.html.tgz
Source3:    JavaConfig.java
Patch1:     %{name}-6.2.2-jpl-configure.patch
Patch2:     %{name}-5.10.5-man-files.patch
Patch3:     %{name}-6.0.2-jni.patch
Patch4:     %{name}-6.2.0-pc.patch

# Base
BuildRequires:  gmp-devel
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
# XPCE
BuildRequires:  libICE-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libSM-devel
BuildRequires:  libX11-devel
BuildRequires:  libXft-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXpm-devel
BuildRequires:  libXt-devel
# Freetype support in XPCE
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  libXaw-devel
BuildRequires:  libXext-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXrender-devel
# ODBC
BuildRequires:  unixODBC-devel
# SSL
BuildRequires:  openssl-devel
# jpl
%if %{with_java}
BuildRequires:  jpackage-utils
BuildRequires:  java-devel
%endif
# zlib
BuildRequires:  zlib-devel
# helpers for export_dynamic patch
BuildRequires:  autoconf

%description
ISO/Edinburgh-style Prolog compiler including modules, auto-load,
libraries, Garbage-collector, stack-expandor, C/C++-interface,
GNU-readline interface, very fast compiler.  Including packages clib
(Unix process control and sockets), cpp (C++ interface), sgml (reading
XML/SGML), sgml/RDF (reading RDF into triples) and XPCE (Graphics UI
toolkit, integrated editor (Emacs-clone) and source-level debugger).


%package devel
Summary: Development files for SWI Prolog
Group: Development/Languages
Requires: %{name} = %{version}-%{release}
Requires: readline-devel, pkgconfig

%description devel
Development files for SWI Prolog.


%package doc
Summary: Documentation for SWI Prolog
Group: Documentation
# This must be archicture dependend because some files live in %%{_libdir}
# because they can are used by built-in documentation system.
Requires: %{name} = %{version}-%{release}

%description doc
%{summary}.


%package odbc
Summary: SWI-Prolog ODBC interface
Group: Development/Languages
Requires: %{name} = %{version}-%{release}

%description odbc
The value of RDMS for Prolog is often over-estimated, as Prolog itself can
manage substantial amounts of data. Nevertheless a Prolog/RDMS interface
provides advantages if data is already provided in an RDMS, data must be
shared with other applications, there are strong persistency requirements
or there is too much data to fit in memory.                                  
                                                                            
The popularity of ODBC makes it possible to design a single
foreign-language module that provides RDMS access for a wide variety of
databases on a wide variety of platforms. The SWI-Prolog RDMS interface is
closely modeled after the ODBC API. This API is rather low-level, but
defaults and dynamic typing provided by Prolog give the user quite simple
access to RDMS, while the interface provides the best possible performance
given the RDMS independency constraint.   


%package static
Summary: Static library for SWI Prolog
Group: Development/Languages
Requires: %{name} = %{version}-%{release}
Requires: readline-devel

%description static
Static library for SWI Prolog.


%if %{separate_xpce}
%package xpce
Summary: A toolkit for developing graphical applications in Prolog
Group: Development/Languages
Requires: %{name} = %{version}-%{release}

%description xpce
XPCE is a toolkit for developing graphical applications in Prolog and other
interactive and dynamically typed languages. XPCE follows a rather unique
approach of for developing GUI applications, as follows:

- Add object layer to Prolog
- High level of abstraction
- Exploit rapid Prolog development cycle
- Platform independent programs
%endif


%if %{with_java}
%package jpl
Summary: A bidirectional Prolog/Java interface for SWI Prolog
Group: Development/Languages
Requires: %{name} = %{version}-%{release}
Requires: java
Requires: jpackage-utils

%description jpl
JPL is a library using the SWI-Prolog foreign interface and the Java Native
Interface providing a bidirectional interface between Java and Prolog
that can be used to embed Prolog in Java as well as for embedding Java
in Prolog. In both setups it provides a re-entrant bidirectional interface.
%endif


%prep
%global docdir doc-install
%setup -q
%patch1 -p1 -b .libjvm
%patch2 -p1 -b .man-files
%patch3 -p1 -b .jni
%patch4 -p1 -b .pc
(
   cd src
   autoconf
)
(
   mkdir %{docdir}
   cp -p %{SOURCE1} %{docdir}
)
(
   mkdir %{docdir}-xpce
   cd %{docdir}-xpce
   tar -xzf %{SOURCE2}
   mv UserGuide xpce-UserGuide
)
(
    cp %{SOURCE3} .
)

# Adjustments to take into account the new location of JNI stuff
sed --in-place=.jni2 -e 's#LIBDIR#%{_libdir}#g' packages/jpl/jpl.pl
sed --in-place=.jni2 -e 's#LIBDIR#%{_libdir}#g' packages/jpl/src/java/jpl/fli/Prolog.java
sed --in-place=.jni2 -e 's#LIBDIR#"%{_libdir}/swipl-jpl"#g' packages/jpl/src/java/jpl/JPL.java


%build
%if %{with_java}
LC_CTYPE=en_US.UTF-8 javac JavaConfig.java
JAVA_HOME=$(java JavaConfig --home)
JAVA_LIBS=$(java JavaConfig --libs-only-L)
%else
# Processed by packages/configure
export DISABLE_PKGS="jpl"
%endif

# Build interpreter needed for SWI packages compilation
%configure --enable-shared LDFLAGS="-Wl,--enable-new-dtags"
make COFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"

# Build SWI packages
pushd packages
%configure LDFLAGS="-Wl,--enable-new-dtags"
make COFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing" JAVALIBS="${JAVA_LIBS} -ljava -lverify -ljvm"
popd


%install
# See <http://www.swi-prolog.org/build/guidelines.html> for file layout
make install DESTDIR=$RPM_BUILD_ROOT
# Library must be executable to get its debuginfo
chmod 0755 $RPM_BUILD_ROOT%{_libdir}/swipl-%{version}/lib/*/libswipl.so.*
# Script with shebang should be executable
chmod 0755 \
$RPM_BUILD_ROOT%{_libdir}/swipl-%{version}/library/dialect/sicstus/swipl-lfr.pl

pushd packages
make install DESTDIR=$RPM_BUILD_ROOT
# Do not chmod earlier, the run.sh's are executed
chmod -x jpl/examples/java/*/run.sh
popd

%if %{with_java}
# Move the JPL JNI stuff to where the Java packaging guidelines 
# say it should be
pushd $RPM_BUILD_ROOT%{_libdir}
mkdir -p swipl-jpl
mv swipl-%{version}/lib/*/libjpl.so swipl-jpl/
mv swipl-%{version}/lib/jpl.jar swipl-jpl/
# Original JAR locations is referenced by internal libraries and examples
ln -s ../../swipl-jpl/jpl.jar swipl-%{version}/lib/jpl.jar
popd
%endif

# Clean up the other stuff that shouldn't be packaged
find packages/jpl/examples -name "*.class" | xargs rm -f
find packages/jpl/examples -name ".cvsignore" | xargs rm -f
magic_rpm_clean.sh

%files
%doc ReleaseNotes/relnotes-5.10 README COPYING VERSION
%doc customize/dotplrc
%{_mandir}/man1/*
%dir %{_libdir}/swipl-%{version}
%{_libdir}/swipl-%{version}/*
%{_bindir}/*

# Exclude the files that are in the sub-packages
%if %{with_java}
# JPL
%exclude %{_libdir}/swipl-%{version}/lib/jpl.jar
%exclude %{_libdir}/swipl-%{version}/library/jpl.pl
%endif
# Devel
%exclude %{_libdir}/swipl-%{version}/lib/*/libswipl.so
%exclude %{_libdir}/swipl-%{version}/include
# Doc
%exclude %{_libdir}/swipl-%{version}/doc
# ODBC
%exclude %{_libdir}/swipl-%{version}/lib/*-linux/odbc4pl.so
%exclude %{_libdir}/swipl-%{version}/library/odbc.pl
# Static
%exclude %{_libdir}/swipl-%{version}/lib/*/libswipl.a
%if %{separate_xpce}
# XPCE
%exclude %{_bindir}/xpce*
%exclude %{_libdir}/swipl-%{version}/customize/dotxpcerc
%exclude %{_libdir}/swipl-%{version}/lib/*-linux/pl2xpce.so
%exclude %{_libdir}/swipl-%{version}/library/http/xpce_httpd.pl
%exclude %{_libdir}/swipl-%{version}/Makefile
%exclude %{_libdir}/swipl-%{version}/swipl.rc
%exclude %{_libdir}/swipl-%{version}/xpce
%exclude %{_mandir}/man1/xpce-client.1*
%endif

%if %{separate_xpce}
%files xpce
%doc customize/dotxpcerc packages/xpce/INFO
%{_bindir}/xpce*
%{_libdir}/swipl-%{version}/customize/dotxpcerc
%{_libdir}/swipl-%{version}/lib/*-linux/pl2xpce.so
%{_libdir}/swipl-%{version}/library/http/xpce_httpd.pl
%{_libdir}/swipl-%{version}/Makefile
%{_libdir}/swipl-%{version}/swipl.rc
%{_libdir}/swipl-%{version}/xpce
%{_mandir}/man1/xpce-client.1*
%endif

%files devel
%{_libdir}/swipl-%{version}/include
%{_libdir}/swipl-%{version}/lib/*/libswipl.so
%{_libdir}/pkgconfig/swipl.pc

%files doc
%{_libdir}/swipl-%{version}/doc
%doc %{docdir}/*
%doc %{docdir}-xpce/*

%files odbc
%{_libdir}/swipl-%{version}/lib/*-linux/odbc4pl.so
%{_libdir}/swipl-%{version}/library/odbc.pl
%doc packages/odbc/{demo,ChangeLog,odbc.html,README}

%files static
%{_libdir}/swipl-%{version}/lib/*/libswipl.a

%if %{with_java}
%files jpl
%doc packages/jpl/docs/*
%doc packages/jpl/examples
%{_libdir}/swipl-%{version}/lib/jpl.jar
%{_libdir}/swipl-%{version}/library/jpl.pl
%{_libdir}/swipl-jpl
%endif


%changelog
* Sat Dec 08 2012 Liu Di <liudidi@gmail.com> - 6.2.2-2
- 为 Magic 3.0 重建

* Tue Oct 02 2012 Petr Pisar <ppisar@redhat.com> - 6.2.2-1
- 6.2.2 bump

* Mon Sep 10 2012 Petr Pisar <ppisar@redhat.com> - 6.2.1-1
- 6.2.1 bump

* Thu Aug 23 2012 Petr Pisar <ppisar@redhat.com> - 6.2.0-1
- 6.2.0 bump

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar 22 2012 Petr Pisar <ppisar@redhat.com> - 6.0.2-3
- Remove JDK version constrain by hacking JDK paths (bug #740897)

* Fri Mar 09 2012 Petr Pisar <ppisar@redhat.com> - 6.0.2-2
- Own jpl.jar file by jpl sub-package only

* Mon Mar 05 2012 Petr Pisar <ppisar@redhat.com> - 6.0.2-1
- 6.0.2 bump
- Artistic licensed code dual-lincensed under GPLv2+ or Artistic 2.0 now
- Keep executables as symlinks because interpreter uses the symlink value to
  locate standard library
- xpce is run as swipl now
- Move documentation into separate sub-package
- Move XPCE into separate sub-package
- Move ODBC interface into separate sub-package
- Fix JPL interface (bug #590499)

* Thu Mar 01 2012 Petr Pisar <ppisar@redhat.com> - 6.0.1-1
- 6.0.1 bump
- Clean spec file

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.10.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.10.5-6
- Rebuilt for glibc bug#747377

* Wed Oct 26 2011 Marcela Mašláňová <mmaslano@redhat.com> - 5.10.5-5
- rebuild with new gmp

* Tue Sep 27 2011 Petr Pisar <ppisar@redhat.com> - 5.10.5-4
- Unify java path search (bug #740897)

* Fri Sep 23 2011 Petr Pisar <ppisar@redhat.com> - 5.10.5-3
- Correct Java paths on ARM (thanks to David A. Marlin)

* Wed Aug 24 2011 Petr Pisar <ppisar@redhat.com> - 5.10.5-2
- Fix segfault in PutImagePixels32() while displaying malformed GIF
  (bug #732952)

* Mon Aug 22 2011 Petr Pisar <ppisar@redhat.com> - 5.10.5-1
- 5.10.5 bump
- Adjust patches and remove merged ones

* Fri Aug 19 2011 Petr Pisar <ppisar@redhat.com> - 5.10.2-4
- Fix CVE-2011-2896 (David Koblas' GIF decoder LZW decoder buffer overflow)
  (bug #727800)
- Fix other GIF decoder bug
  (http://www.swi-prolog.org/bugzilla/show_bug.cgi?id=7#c4)

* Thu Feb 10 2011 Petr Pisar <ppisar@redhat.com> - 5.10.2-3
- Pass -export-dynamic to linker properly

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Petr Pisar <ppisar@redhat.com> - 5.10.2-1
- 5.10.2 bump
- Use DT_RUNPATH instead of pl-5.7.11-rpath.patch
- Adjust jpl-configure.patch to 5.10.2
- Adjust man-files.patch to 5.10.2
- Adjust jni.patch to 5.10.2
- Adjust pc.patch to 5.10.2
- Use make install method for installation
- Adjust license tag to 5.10.2 version (LGPLv2+ added)
- Add executable permission to some files to be properly packaged
- Re-add XPCE user guide

* Wed Dec  8 2010 Petr Pisar <ppisar@redhar.com> - 5.7.11-6
- Inhibit XPCE by macro to silent rpmlint 
- Define implicit attributes for jpl files 
- Expand tabs to spaces to silent rpmlint 
- Remove executable bit from jpl documentation files 
- Fix spelling in package descriptions 
- Strip debuginfo from libpl.so by setting executable bit 
- Change license to reflect reality (yes, Artistic1) 
- Make java part optional

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 5.7.11-5
- rebuilt with new openssl

* Fri Aug 14 2009 Gerard Milmeister <gemi@bluewin.ch> - 5.7.11-4
- move include files to expected place

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.7.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul  7 2009 Mary Ellen Foster <mefoster at gmail.com> - 5.7.11-2
- Really fix issue with compiling "maildrop" packages

* Mon Jul  6 2009 Mary Ellen Foster <mefoster at gmail.com> - 5.7.11-1
- Move binaries into /usr/bin directly to fix multilib issues
- Update to latest upstream release
- Use officially-distributed PDF documentation instead of HTML
- Unify Java patches
- Remove strndup package; they fixed it upstream
- Fix compilation of "maildrop" packages
- Give the xpce documentation directory a clearer name
- Removed the FILES section of the man page because it also caused
  multilib conflicts (and was inaccurate anyway)

* Fri Jun 12 2009 Dennis Gilmore <dennis@ausil.us> 5.7.6-5
-dont use a static definition for strndup

* Mon Mar 02 2009 Dennis Gilmore <dennis@ausil.us> 5.7.6-4
- fix JAVA_HOME and JAVA_LIB for sparc arches

* Sun Mar 01 2009 Karsten Hopp <karsten@redhat.com> 5.7.6-3
- fix java LIBDIRS for mainframe, similar to alpha

* Wed Feb 25 2009 Mary Ellen Foster <mefoster at gmail.com> - 5.7.6-2
- Unify all changes:
  - Fix java LIBDIRS on alpha (Oliver Falk)

* Wed Feb 25 2009 Mary Ellen Foster <mefoster at gmail.com> - 5.7.6-1
- Update to version 5.7
  - Cleaned up virtual machine and compiler
  - Increased performance

* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com> - 5.6.60-3
- rebuild with new openssl

* Fri Sep 19 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 5.6.60-2
- forgot to remove ANNOUNCE from doc list

* Fri Sep 19 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 5.6.60-1
- update to 5.6.60
- use openjdk (FIXME: there may be a way to make this more generic)

* Wed Jul  2 2008 Mary Ellen Foster <mefoster at gmail.com> - 5.6.57-2
- Build using any Java
- Include patch from SWI for Turkish locale (thanks to Keri Harris)

* Wed Jun 25 2008 Mary Ellen Foster <mefoster at gmail.com> - 5.6.57-1
- Another update, after vacation

* Mon May 19 2008 Mary Ellen Foster <mefoster at gmail.com> - 5.6.55-1
- Update to 5.6.55 (wow, fast updates!)
- Un-split xpce for now
- Conditionally build jpl (on Fedora 9 with openjdk, and on 
  Fedora 8 non-ppc with icedtea)

* Wed May 07 2008 Mary Ellen Foster <mefoster at gmail.com> - 5.6.54-1
- Update to 5.6.54 and prepare to actually push this
- Try splitting xpce into own package

* Tue Apr 15 2008 Mary Ellen Foster <mefoster at gmail.com> - 5.6.53-1
- Update to 5.6.53 -- fixes ppc64 problems, yay!

* Wed Apr 09 2008 Mary Ellen Foster <mefoster at gmail.com> - 5.6.52-2
- Put JPL stuff where the new Java packaging guidelines say it should be
  and make all of the necessary adjustments in other files
- Split out "-devel" and "-static" packages per guidelines

* Mon Mar 31 2008 Mary Ellen Foster <mefoster at gmail.com> - 5.6.52-1
- Switch jpl requirement from IcedTea to OpenJDK and enable it everywhere
- Upgrade to 5.6.52
- Patch jpl configure script to find Java libraries on ppc{64}
- NB: Still broken on ppc64, still trying to figure out why

* Mon Feb 25 2008 Mary Ellen Foster <mefoster at gmail.com> - 5.6.51-1
- Upgrade to 5.6.51

* Fri Feb 22 2008 Mary Ellen Foster <mefoster at gmail.com> - 5.6.50-1
- Update to 5.6.50
- Enable JPL (as a sub-package) -- NB: it only builds with icedtea for now,
  so we disable that sub-package on ppc64 and ppc for the moment

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 5.6.47-9
- Autorebuild for GCC 4.3

* Thu Dec  6 2007 Gerard Milmeister <gemi@bluewin.ch> - 5.6.47-8
- compile with -fno-strict-aliasing

* Wed Dec  5 2007 Gerard Milmeister <gemi@bluewin.ch> - 5.6.47-5
- disable jpl for now

* Wed Dec  5 2007 Gerard Milmeister <gemi@bluewin.ch> - 5.6.47-4
- enable shared library building

* Wed Dec  5 2007 Gerard Milmeister <gemi@bluewin.ch> - 5.6.47-1
- new release 5.6.47

* Fri Jun  8 2007 Gerard Milmeister <gemi@bluewin.ch> - 5.6.35-1
- new version 5.6.35
- add requires readline-devel

* Mon Apr 23 2007 Gerard Milmeister <gemi@bluewin.ch> - 5.6.34-1
- new version 5.6.34

* Fri Feb 23 2007 Gerard Milmeister <gemi@bluewin.ch> - 5.6.28-1
- new version 5.6.28

* Fri Dec  1 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.6.24-1
- new version 5.6.24

* Sun Oct  1 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.6.20-1
- new version 5.6.20

* Sat Sep  2 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.6.18-1
- updated to 5.6.18

* Mon Aug 28 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.6.16-3
- Rebuild for FE6

* Tue Jul 11 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.6.16-1
- new version 5.6.16

* Mon May  1 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.6.12-3
- added buildreq for libXinerama-devel

* Mon May  1 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.6.12-2
- added patch to compile with xft

* Sun Apr 30 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.6.12-1
- new version 5.6.12

* Wed Mar  8 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.6.7-1
- new version 5.6.7

* Sat Jan 28 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.6.3-1
- new version 5.6.3

* Mon Jan  2 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.6.0-1
- new version 5.6.0

* Wed Jun 22 2005 Gerard Milmeister <gemi@bluewin.ch> - 5.4.7-1
- new version 5.4.7

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 5.4.6-9
- rebuild on all arches

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Wed Feb 23 2005 David Woodhouse <dwmw2@infradead.org> - 5.4.6-7
- Fix visibility abuse. This may well fix x86_64 too, so re-enable that.

* Mon Feb 21 2005 Gerard Milmeister <gemi@bluewin.ch> - 5.4.6-6
- Exclude x86_64 for now (bugzilla 149038)

* Sun Feb 20 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 5.4.6-5
- Added patch1 for a few multilib Makefile/configure fixes.
- Use %%makeinstall and set libdir in install section.

* Sat Feb 12 2005 Warren Togami <wtogami@redhat.com> - 5.4.6-4
- remove duplicate RPATH patch
- remove Epoch
- remove redundant unixODBC from BR

* Sat Feb 12 2005 Gerard Milmeister <gemi@bluewin.ch> - 5.4.6-2
- Added BuildRequires: unixODBC, unixODBC-devel
- Removed rpath from shared libs: pl-rpath.patch

* Sat Feb 12 2005 Gerard Milmeister <gemi@bluewin.ch> - 5.4.6-1
- New Version 5.4.6

* Thu Jan 13 2005 Gerard Milmeister <gemi@bluewin.ch> - 5.4.5-0.fdr.1
- New Version 5.4.5
