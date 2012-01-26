#%define opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)
%define with_java 0

Name:           ppl
Version:        0.11.2
Release:        2%{?dist}

Summary:        The Parma Polyhedra Library: a library of numerical abstractions
Group:          Development/Libraries
License:        GPLv3+
URL:            http://www.cs.unipr.it/ppl/
Source0:        ftp://ftp.cs.unipr.it/pub/ppl/releases/%{version}/%{name}-%{version}.tar.bz2
Source1:        ppl.hh
Source2:        ppl_c.h
Source3:        pwl.hh
Patch0:         ppl-0.11.2-Makefile.patch
#Patch1:
#Icon:
#Requires:
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  gmp-devel >= 4.1.3, m4 >= 1.4.8
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
#Prefix:        /usr

%description
The Parma Polyhedra Library (PPL) is a library for the manipulation of
(not necessarily closed) convex polyhedra and other numerical
abstractions.  The applications of convex polyhedra include program
analysis, optimized compilation, integer and combinatorial
optimization and statistical data-editing.  The Parma Polyhedra
Library comes with several user friendly interfaces, is fully dynamic
(available virtual memory is the only limitation to the dimension of
anything), written in accordance to all the applicable standards,
exception-safe, rather efficient, thoroughly documented, and free
software.  This package provides all what is necessary to run
applications using the PPL through its C and C++ interfaces.

%package devel
Summary:        Development tools for the Parma Polyhedra Library C and C++ interfaces
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}, gmp-devel >= 4.1.3
%description devel
The header files, Autoconf macro and minimal documentation for
developing applications using the Parma Polyhedra Library through
its C and C++ interfaces.

%package static
Summary:        Static archives for the Parma Polyhedra Library C and C++ interfaces
Group:          Development/Libraries
Requires:       %{name}-devel = %{version}-%{release}
%description static
The static archives for the Parma Polyhedra Library C and C++ interfaces.

%package utils
Summary:        Utilities using the Parma Polyhedra Library
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
BuildRequires:  glpk-devel >= 4.13
%description utils
This package contains the mixed integer linear programming solver ppl_lpsol.
the program ppl_lcdd for vertex/facet enumeration of convex polyhedra,
and the parametric integer programming solver ppl_pips.

%ifnarch ia64 ppc64 s390 s390x sparc64 sparcv9
%package gprolog
# The `gprolog' package is not available on ppc64:
# the GNU Prolog interface must thus be disabled for that architecture.
Summary:        The GNU Prolog interface of the Parma Polyhedra Library
Group:          Development/Libraries
BuildRequires:  gprolog >= 1.2.19
Requires:       %{name} = %{version}-%{release}, %{name}-pwl = %{version}-%{release}, gprolog >= 1.2.19
%description gprolog
This package adds GNU Prolog support to the Parma Polyhedra Library (PPL).
Install this package if you want to use the library in GNU Prolog programs.
%endif

%ifnarch ia64 ppc64 s390 s390x sparc64 sparcv9
%package gprolog-static
Summary:        The static archive for the GNU Prolog interface of the Parma Polyhedra Library
Group:          Development/Libraries
Requires:       %{name}-gprolog = %{version}-%{release}
%description gprolog-static
This package contains the static archive for the GNU Prolog interface
of the Parma Polyhedra Library.
%endif

%package swiprolog
Summary:        The SWI-Prolog interface of the Parma Polyhedra Library
Group:          Development/Libraries
BuildRequires:  pl >= 5.10.2-3, pl-devel >= 5.10.2-3
Requires:       %{name} = %{version}-%{release}, %{name}-pwl = %{version}-%{release}, pl >= 5.10.2-3
%description swiprolog
This package adds SWI-Prolog support to the Parma Polyhedra Library.
Install this package if you want to use the library in SWI-Prolog programs.

%package swiprolog-static
Summary:        The static archive for the SWI-Prolog interface of the Parma Polyhedra Library
Group:          Development/Libraries
BuildRequires:  pl >= 5.10.2-3, pl-devel >= 5.10.2-3, pl-static >= 5.10.2-3
Requires:       %{name}-swiprolog = %{version}-%{release}
%description swiprolog-static
This package contains the static archive for the SWI-Prolog interface
of the Parma Polyhedra Library.

%ifnarch sparc64 sparcv9
%package yap
Summary:        The YAP Prolog interface of the Parma Polyhedra Library
Group:          Development/Libraries
BuildRequires:  yap-devel >= 5.1.1
Requires:       %{name} = %{version}-%{release}, %{name}-pwl = %{version}-%{release}, yap >= 5.1.1
Obsoletes:      ppl-yap-static
%description yap
This package adds YAP Prolog support to the Parma Polyhedra Library (PPL).
Install this package if you want to use the library in YAP Prolog programs.
%endif

#%package ocaml
#Summary:        The OCaml interface of the Parma Polyhedra Library
#Group:          Development/Libraries
#BuildRequires:  ocaml >= 3.09
#Requires:       %{name} = %{version}-%{release}
#%description ocaml
#This package adds Objective Caml (OCaml) support to the Parma
#Polyhedra Library.  Install this package if you want to use the
#library in OCaml programs.

#%package ocaml-devel
#Summary:        The OCaml interface of the Parma Polyhedra Library
#Group:          Development/Libraries
#Requires:       %{name}-ocaml = %{version}-%{release}
#%description ocaml-devel
#This package contains libraries and signature files for developing
#applications using the OCaml interface of the Parma Polyhedra Library.

%if %{with_java}
%package java
Summary:        The Java interface of the Parma Polyhedra Library
Group:          Development/Libraries
BuildRequires:  java-devel >= 1:1.6.0
BuildRequires:  jpackage-utils
Requires:       java >= 1:1.6.0
Requires:       jpackage-utils
Requires:       %{name} = %{version}-%{release}
%description java
This package adds Java support to the Parma Polyhedra Library.
Install this package if you want to use the library in Java programs.

%package java-javadoc
Summary:        Javadocs for %{name}-java
Group:          Documentation
Requires:       %{name}-java = %{version}-%{release}
Requires:       jpackage-utils
%description java-javadoc
This package contains the API documentation for Java interface
of the Parma Polyhedra Library.
%endif

%package docs
Summary:        Documentation for the Parma Polyhedra Library
Group:          Documentation
Requires:       %{name} = %{version}-%{release}
%description docs
This package contains all the documentations required by programmers
using the Parma Polyhedra Library (PPL).
Install this package if you want to program with the PPL.

%package pwl
Summary:        The Parma Watchdog Library: a C++ library for watchdog timers
Group:          Development/Libraries
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
%description pwl
The Parma Watchdog Library (PWL) provides support for multiple,
concurrent watchdog timers on systems providing setitimer(2).  This
package provides all what is necessary to run applications using the
PWL.  The PWL is currently distributed with the Parma Polyhedra
Library, but is totally independent from it.

%package pwl-devel
Summary:        Development tools for the Parma Watchdog Library
Group:          Development/Libraries
Requires:       %{name}-pwl = %{version}-%{release}
%description pwl-devel
The header files, documentation and static libraries for developing
applications using the Parma Watchdog Library.

%package pwl-static
Summary:        Static archive for the Parma Watchdog Library
Group:          Development/Libraries
Requires:       %{name}-pwl-devel = %{version}-%{release}
%description pwl-static
This package contains the static archive for the Parma Watchdog Library.

%package pwl-docs
Summary:        Documentation for the Parma Watchdog Library
Group:          Documentation
Requires:       %{name}-pwl = %{version}-%{release}
%description pwl-docs
This package contains all the documentations required by programmers
using the Parma Watchdog Library (PWL).
Install this package if you want to program with the PWL.


%prep
%setup -q
%patch0 -p1
#%patch1 -p1

%build
CPPFLAGS="-I%{_includedir}/glpk"
%ifnarch ia64 ppc64 s390 s390x sparc64 sparcv9
CPPFLAGS="$CPPFLAGS -I%{_libdir}/gprolog-`gprolog --version 2>&1 | head -1 | sed -e "s/.* \([^ ]*\)$/\1/g"`/include"
%endif
%ifnarch sparc64 sparcv9
CPPFLAGS="$CPPFLAGS -I`swipl -dump-runtime-variables | grep PLBASE= | sed 's/PLBASE="\(.*\)";/\1/'`/include"
CPPFLAGS="$CPPFLAGS -I%{_includedir}/Yap"
%endif
%configure --docdir=%{_datadir}/doc/%{name}-%{version} --enable-shared --disable-rpath --enable-interfaces="c++ c \
           gnu_prolog swi_prolog yap_prolog \
           %if %{with_java}
            java\
	   %endif
	   " CPPFLAGS="$CPPFLAGS"
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' Watchdog/libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' Watchdog/libtool
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} INSTALL="%{__install} -p" install
rm -f %{buildroot}%{_libdir}/*.la %{buildroot}%{_libdir}/%{name}/*.la

# In order to avoid multiarch conflicts when installed for multiple
# architectures (e.g., i386 and x86_64), we rename the header files
# of the ppl-devel and ppl-pwl-devel packages.  They are substituted with
# ad-hoc switchers that select the appropriate header file depending on
# the architecture for which the compiler is compiling.

# Since our header files only depend on the sizeof things, we smash
# ix86 onto i386 and arm* onto arm.  For the SuperH RISC engine family,
# we smash sh3 and sh4 onto sh.
normalized_arch=%{_arch}
%ifarch %{ix86}
normalized_arch=i386
%endif
%ifarch %{arm}
normalized_arch=arm
%endif
%ifarch sh3 sh4
normalized_arch=sh
%endif

mv %{buildroot}/%{_includedir}/ppl.hh %{buildroot}/%{_includedir}/ppl-${normalized_arch}.hh
install -m644 %{SOURCE1} %{buildroot}/%{_includedir}/ppl.hh
mv %{buildroot}/%{_includedir}/ppl_c.h %{buildroot}/%{_includedir}/ppl_c-${normalized_arch}.h
install -m644 %{SOURCE2} %{buildroot}/%{_includedir}/ppl_c.h
mv %{buildroot}/%{_includedir}/pwl.hh %{buildroot}/%{_includedir}/pwl-${normalized_arch}.hh
install -m644 %{SOURCE3} %{buildroot}/%{_includedir}/pwl.hh

%if %{with_java}
# Install the Javadocs for ppl-java.
mkdir -p %{buildroot}%{_javadocdir}
mv \
%{buildroot}/%{_datadir}/doc/%{name}-%{version}/ppl-user-java-interface-%{version}-html \
%{buildroot}%{_javadocdir}/%{name}-java
%endif

%files
%defattr(-,root,root,-)
%doc %{_datadir}/doc/%{name}-%{version}/BUGS
%doc %{_datadir}/doc/%{name}-%{version}/COPYING
%doc %{_datadir}/doc/%{name}-%{version}/CREDITS
%doc %{_datadir}/doc/%{name}-%{version}/NEWS
%doc %{_datadir}/doc/%{name}-%{version}/README
%doc %{_datadir}/doc/%{name}-%{version}/README.configure
%doc %{_datadir}/doc/%{name}-%{version}/TODO
%doc %{_datadir}/doc/%{name}-%{version}/gpl.txt
%{_libdir}/libppl.so.*
%{_libdir}/libppl_c.so.*
%{_bindir}/ppl-config
%{_mandir}/man1/ppl-config.1.gz
%dir %{_libdir}/%{name}
%dir %{_datadir}/doc/%{name}-%{version}

%files devel
%defattr(-,root,root,-)
%{_includedir}/ppl*.hh
%{_includedir}/ppl_c*.h
%{_libdir}/libppl.so
%{_libdir}/libppl_c.so
%{_mandir}/man3/libppl.3.gz
%{_mandir}/man3/libppl_c.3.gz
%{_datadir}/aclocal/ppl.m4
%{_datadir}/aclocal/ppl_c.m4

%files static
%defattr(-,root,root,-)
%{_libdir}/libppl.a
%{_libdir}/libppl_c.a

%files utils
%defattr(-,root,root,-)
%{_bindir}/ppl_lcdd
%{_bindir}/ppl_lpsol
%{_bindir}/ppl_pips
%{_mandir}/man1/ppl_lcdd.1.gz
%{_mandir}/man1/ppl_lpsol.1.gz
%{_mandir}/man1/ppl_pips.1.gz

%ifnarch ia64 ppc64 s390 s390x sparc64 sparcv9
%files gprolog
%defattr(-,root,root,-)
%doc interfaces/Prolog/GNU/README.gprolog
%{_bindir}/ppl_gprolog
%{_libdir}/%{name}/ppl_gprolog.pl
%{_libdir}/%{name}/libppl_gprolog.so
%endif

%ifnarch ia64 ppc64 s390 s390x sparc64 sparcv9
%files gprolog-static
%defattr(-,root,root,-)
%{_libdir}/%{name}/libppl_gprolog.a
%endif

%files swiprolog
%defattr(-,root,root,-)
%doc interfaces/Prolog/SWI/README.swiprolog
%{_bindir}/ppl_pl
%{_libdir}/%{name}/libppl_swiprolog.so
%{_libdir}/%{name}/ppl_swiprolog.pl

%files swiprolog-static
%defattr(-,root,root,-)
%{_libdir}/%{name}/libppl_swiprolog.a

%ifnarch sparc64 sparcv9
%files yap
%defattr(-,root,root,-)
%doc interfaces/Prolog/YAP/README.yap
%{_libdir}/%{name}/ppl_yap.pl
%{_libdir}/%{name}/ppl_yap.so
%endif

#%files ocaml
#%defattr(-,root,root,-)
#%doc interfaces/OCaml/README.ocaml
#%{_libdir}/%{name}/ppl_ocaml.cma
#%{_libdir}/%{name}/ppl_ocaml.cmi
#%{_libdir}/%{name}/ppl_ocaml_globals.cmi

#%files ocaml-devel
#%defattr(-,root,root,-)
#%{_libdir}/%{name}/libppl_ocaml.a
#%{_libdir}/%{name}/ppl_ocaml.mli

%if %{with_java}
%files java
%defattr(-,root,root,-)
%doc interfaces/Java/README.java
%{_libdir}/%{name}/libppl_java.so
%{_libdir}/%{name}/ppl_java.jar

%files java-javadoc
%defattr(-,root,root,-)
%{_javadocdir}/%{name}-java
%endif

%files docs
%defattr(-,root,root,-)
%doc %{_datadir}/doc/%{name}-%{version}/ChangeLog*
%doc %{_datadir}/doc/%{name}-%{version}/README.doc
%doc %{_datadir}/doc/%{name}-%{version}/fdl.*
%doc %{_datadir}/doc/%{name}-%{version}/gpl.pdf
%doc %{_datadir}/doc/%{name}-%{version}/gpl.ps.gz
%doc %{_datadir}/doc/%{name}-%{version}/ppl-user-%{version}-html/
%doc %{_datadir}/doc/%{name}-%{version}/ppl-user-c-interface-%{version}-html/
#%doc %{_datadir}/doc/%{name}-%{version}/ppl-user-ocaml-interface-%{version}-html/
%doc %{_datadir}/doc/%{name}-%{version}/ppl-user-prolog-interface-%{version}-html/
%doc %{_datadir}/doc/%{name}-%{version}/ppl-user-%{version}.pdf
%doc %{_datadir}/doc/%{name}-%{version}/ppl-user-c-interface-%{version}.pdf
%if %{with_java}
%doc %{_datadir}/doc/%{name}-%{version}/ppl-user-java-interface-%{version}.pdf
%endif
#%doc %{_datadir}/doc/%{name}-%{version}/ppl-user-ocaml-interface-%{version}.pdf
%doc %{_datadir}/doc/%{name}-%{version}/ppl-user-prolog-interface-%{version}.pdf
%doc %{_datadir}/doc/%{name}-%{version}/ppl-user-%{version}.ps.gz
%doc %{_datadir}/doc/%{name}-%{version}/ppl-user-c-interface-%{version}.ps.gz
%if %{with_java}
%doc %{_datadir}/doc/%{name}-%{version}/ppl-user-java-interface-%{version}.ps.gz
%endif
#%doc %{_datadir}/doc/%{name}-%{version}/ppl-user-ocaml-interface-%{version}.ps.gz
%doc %{_datadir}/doc/%{name}-%{version}/ppl-user-prolog-interface-%{version}.ps.gz

%files pwl
%defattr(-,root,root,-)
%doc %{_datadir}/doc/%{name}-%{version}/pwl/BUGS
%doc %{_datadir}/doc/%{name}-%{version}/pwl/COPYING
%doc %{_datadir}/doc/%{name}-%{version}/pwl/CREDITS
%doc %{_datadir}/doc/%{name}-%{version}/pwl/NEWS
%doc %{_datadir}/doc/%{name}-%{version}/pwl/README
%doc %{_datadir}/doc/%{name}-%{version}/pwl/gpl.txt
%{_libdir}/libpwl.so.*
%dir %{_datadir}/doc/%{name}-%{version}/pwl

%files pwl-devel
%defattr(-,root,root,-)
%doc Watchdog/doc/README.doc
%{_includedir}/pwl*.hh
%{_libdir}/libpwl.so

%files pwl-static
%defattr(-,root,root,-)
%{_libdir}/libpwl.a

%files pwl-docs
%defattr(-,root,root,-)
%doc %{_datadir}/doc/%{name}-%{version}/pwl/ChangeLog*
%doc %{_datadir}/doc/%{name}-%{version}/pwl/README.doc
%doc %{_datadir}/doc/%{name}-%{version}/pwl/fdl.*
%doc %{_datadir}/doc/%{name}-%{version}/pwl/gpl.ps.gz
%doc %{_datadir}/doc/%{name}-%{version}/pwl/gpl.pdf
%doc %{_datadir}/doc/%{name}-%{version}/pwl/pwl-user-0.8-html/
%doc %{_datadir}/doc/%{name}-%{version}/pwl/pwl-user-0.8.pdf
%doc %{_datadir}/doc/%{name}-%{version}/pwl/pwl-user-0.8.ps.gz

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%post pwl -p /sbin/ldconfig
%postun pwl -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%changelog
* Thu Jan 26 2012 Liu Di <liudidi@gmail.com> - 0.11.2-2
- 为 Magic 3.0 重建

