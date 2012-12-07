%global shortver	3
%global mediumver	%{shortver}.4

Summary: Numerical linear algebra package libraries
Name: lapack
Version: %{mediumver}.0
Release: 2%{?dist}
License: BSD
Group: Development/Libraries
URL: http://www.netlib.org/lapack/
Source0: http://www.netlib.org/lapack/lapack-%{version}.tgz
Source1: http://www.netlib.org/lapack/manpages.tgz
Source2: Makefile.blas
Source3: Makefile.lapack
Source4: http://www.netlib.org/lapack/lapackqref.ps
Source5: http://www.netlib.org/blas/blasqr.ps
Patch3: lapack-3.4.0-make.inc.patch
Patch4: lapack-3.4.0-lapacke-shared.patch
BuildRequires: gcc-gfortran

%description
LAPACK (Linear Algebra PACKage) is a standard library for numerical
linear algebra. LAPACK provides routines for solving systems of
simultaneous linear equations, least-squares solutions of linear
systems of equations, eigenvalue problems, and singular value
problems. Associated matrix factorizations (LU, Cholesky, QR, SVD,
Schur, and generalized Schur) and related computations (i.e.,
reordering of Schur factorizations and estimating condition numbers)
are also included. LAPACK can handle dense and banded matrices, but
not general sparse matrices. Similar functionality is provided for
real and complex matrices in both single and double precision. LAPACK
is coded in Fortran90 and built with gcc.

%package devel
Summary: LAPACK development libraries
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: blas-devel%{?_isa} = %{version}-%{release}

%description devel
LAPACK development libraries (shared).

%package static
Summary: LAPACK static libraries
Group: Development/Libraries
Requires: lapack-devel%{?_isa} = %{version}-%{release}

%description static
LAPACK static libraries.

%package -n blas
Summary: The Basic Linear Algebra Subprograms library
Group: Development/Libraries

%description -n blas
BLAS (Basic Linear Algebra Subprograms) is a standard library which
provides a number of basic algorithms for numerical algebra. 

%package -n blas-devel
Summary: BLAS development libraries
Group: Development/Libraries
Requires: blas%{?_isa} = %{version}-%{release}
Requires: gcc-gfortran

%description -n blas-devel
BLAS development libraries (shared).

%package -n blas-static
Summary: BLAS static libraries
Group: Development/Libraries
Requires: blas-devel%{?_isa} = %{version}-%{release}

%description -n blas-static
BLAS static libraries.

%prep
%setup -q 
%setup -q -D -T -a1
%patch3 -p1 -b .fedora
%patch4 -p1 -b .shared

mkdir manpages
mv man/ manpages/

cp -f INSTALL/make.inc.gfortran make.inc
cp -f %{SOURCE2} BLAS/SRC/Makefile
cp -f %{SOURCE3} SRC/Makefile

sed -i "s|@SHORTVER@|%{shortver}|g" BLAS/SRC/Makefile
sed -i "s|@SHORTVER@|%{shortver}|g" SRC/Makefile
sed -i "s|@SHORTVER@|%{shortver}|g" lapacke/Makefile
sed -i "s|@LONGVER@|%{version}|g" BLAS/SRC/Makefile
sed -i "s|@LONGVER@|%{version}|g" SRC/Makefile
sed -i "s|@LONGVER@|%{version}|g" lapacke/Makefile

%build
RPM_OPT_O_FLAGS=$(echo $RPM_OPT_FLAGS | sed 's|-O2|-O0|')
export FC=gfortran

# Build BLAS
pushd BLAS/SRC
FFLAGS="$RPM_OPT_O_FLAGS" make dcabs1.o
FFLAGS="$RPM_OPT_FLAGS" CFLAGS="$RPM_OPT_FLAGS" make static
cp libblas.a ${RPM_BUILD_DIR}/%{name}-%{version}/
make clean
FFLAGS="$RPM_OPT_O_FLAGS -fPIC" make dcabs1.o
FFLAGS="$RPM_OPT_FLAGS -fPIC" CFLAGS="$RPM_OPT_FLAGS -fPIC" make shared
cp libblas.so.%{version} ${RPM_BUILD_DIR}/%{name}-%{version}/
popd

ln -s libblas.so.%{version} libblas.so

# Build the static dlamch, dsecnd, lsame, second, slamch bits
pushd INSTALL
make NOOPT="$RPM_OPT_O_FLAGS" OPTS="$RPM_OPT_FLAGS"
popd

# Build the static lapack library
pushd SRC
make FFLAGS="$RPM_OPT_FLAGS" CFLAGS="$RPM_OPT_FLAGS" static
cp liblapack.a ${RPM_BUILD_DIR}/%{name}-%{version}/
popd

# Build the static with pic dlamch, dsecnd, lsame, second, slamch bits
pushd INSTALL
make clean
make NOOPT="$RPM_OPT_O_FLAGS -fPIC" OPTS="$RPM_OPT_FLAGS -fPIC"
popd

# Build the static with pic lapack library
pushd SRC
make clean
make FFLAGS="$RPM_OPT_FLAGS -fPIC" CFLAGS="$RPM_OPT_FLAGS -fPIC" static
cp liblapack.a ${RPM_BUILD_DIR}/%{name}-%{version}/liblapack_pic.a
popd

# Build the shared dlamch, dsecnd, lsame, second, slamch bits
pushd INSTALL
make clean
make NOOPT="$RPM_OPT_O_FLAGS -fPIC" OPTS="$RPM_OPT_FLAGS -fPIC"
popd

# Build the shared lapack library
pushd SRC
make clean
make FFLAGS="$RPM_OPT_FLAGS -fPIC" CFLAGS="$RPM_OPT_FLAGS -fPIC" shared
cp liblapack.so.%{version} ${RPM_BUILD_DIR}/%{name}-%{version}/
popd

ln -s liblapack.so.%{version} liblapack.so

# Build the lapacke libraries
pushd lapacke
make clean
make CFLAGS="$RPM_OPT_FLAGS" lapacke
cp liblapacke.a ${RPM_BUILD_DIR}/%{name}-%{version}/
make clean
make CFLAGS="$RPM_OPT_FLAGS -fPIC" shlib
cp liblapacke.so.%{version} ${RPM_BUILD_DIR}/%{name}-%{version}/
popd

cp -p %{SOURCE4} lapackqref.ps
cp -p %{SOURCE5} blasqr.ps

%install
mkdir -p ${RPM_BUILD_ROOT}%{_libdir}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man3
chmod 755 ${RPM_BUILD_ROOT}%{_mandir}/man3

for f in liblapack.so.%{version} libblas.so.%{version} liblapacke.so.%{version} libblas.a liblapack.a liblapack_pic.a liblapacke.a; do
  cp -f $f ${RPM_BUILD_ROOT}%{_libdir}/$f
done

# Blas manpages
pushd manpages/
mkdir -p blas/man/man3
cd man/man3/
mv caxpy.f.3 CAXPY.3 ccopy.f.3 CCOPY.3 cdotc.f.3 CDOTC.3 cdotu.f.3 CDOTU.3 cgbmv.f.3 CGBMV.3 \
cgemm.f.3 CGEMM.3 cgemv.f.3 CGEMV.3 cgerc.f.3 CGERC.3 cgeru.f.3 CGERU.3 chbmv.f.3 CHBMV.3 \
chemm.f.3 CHEMM.3 chemv.f.3 CHEMV.3 cher.f.3 CHER.3 cher2.f.3 CHER2.3 cher2k.f.3 CHER2K.3 \
cherk.f.3 CHERK.3 chpmv.f.3 CHPMV.3 chpr.f.3 CHPR.3 chpr2.f.3 CHPR2.3 crotg.f.3 CROTG.3 \
cscal.f.3 CSCAL.3 csrot.f.3 CSROT.3 csscal.f.3 CSSCAL.3 cswap.f.3 CSWAP.3 csymm.f.3 \
CSYMM.3 csyr2k.f.3 CSYR2K.3 csyrk.f.3 CSYRK.3 ctbmv.f.3 CTBMV.3 ctbsv.f.3 CTBSV.3 ctpmv.f.3 \
CTPMV.3 ctpsv.f.3 CTPSV.3 ctrmm.f.3 CTRMM.3 ctrmv.f.3 CTRMV.3 ctrsm.f.3 CTRSM.3 ctrsv.f.3 \
CTRSV.3 dasum.f.3 DASUM.3 daxpy.f.3 DAXPY.3 dcabs1.f.3 DCABS1.3 dcopy.f.3 DCOPY.3 ddot.f.3 \
DDOT.3 dgbmv.f.3 DGBMV.3 dgemm.f.3 DGEMM.3 dgemv.f.3 DGEMV.3 dger.f.3 DGER.3 dnrm2.f.3 \
DNRM2.3 drot.f.3 DROT.3 drotg.f.3 DROTG.3 drotm.f.3 DROTM.3 drotmg.f.3 DROTMG.3 dsbmv.f.3 \
DSBMV.3 dscal.f.3 DSCAL.3 dsdot.f.3 DSDOT.3 dspmv.f.3 DSPMV.3 dspr.f.3 DSPR.3 dspr2.f.3 \
DSPR2.3 dswap.f.3 DSWAP.3 dsymm.f.3 DSYMM.3 dsymv.f.3 DSYMV.3 dsyr.f.3 DSYR.3 dsyr2.f.3 \
DSYR2.3 dsyr2k.f.3 DSYR2K.3 dsyrk.f.3 DSYRK.3 dtbmv.f.3 DTBMV.3 dtbsv.f.3 DTBSV.3 dtpmv.f.3 \
DTPMV.3 dtpsv.f.3 DTPSV.3 dtrmm.f.3 DTRMM.3 dtrmv.f.3 DTRMV.3 dtrsm.f.3 DTRSM.3 dtrsv.f.3 \
DTRSV.3 dzasum.f.3 DZASUM.3 dznrm2.f.3 DZNRM2.3 icamax.f.3 ICAMAX.3 idamax.f.3 IDAMAX.3 \
isamax.f.3 ISAMAX.3 izamax.f.3 IZAMAX.3 LSAME.3 sasum.f.3 SASUM.3 saxpy.f.3 SAXPY.3 \
scabs1.f.3 SCABS1.3 scasum.f.3 SCASUM.3 scnrm2.f.3 SCNRM2.3 scopy.f.3 SCOPY.3 sdot.f.3 SDOT.3 \
sdsdot.f.3 SDSDOT.3 sgbmv.f.3 SGBMV.3 sgemm.f.3 SGEMM.3 sgemv.f.3 SGEMV.3 sger.f.3 SGER.3 \
snrm2.f.3 SNRM2.3 srot.f.3 SROT.3 srotg.f.3 SROTG.3 srotm.f.3 SROTM.3 srotmg.f.3 SROTMG.3 \
ssbmv.f.3 SSBMV.3 sscal.f.3 SSCAL.3 sspmv.f.3 SSPMV.3 sspr.f.3 SSPR.3 sspr2.f.3 SSPR2.3 \
sswap.f.3 SSWAP.3 ssymm.f.3 SSYMM.3 ssymv.f.3 SSYMV.3 ssyr.f.3 SSYR.3 ssyr2.f.3 SSYR2.3 \
ssyr2k.f.3 SSYR2K.3 ssyrk.f.3 SSYRK.3 stbmv.f.3 STBMV.3 stbsv.f.3 STBSV.3 stpmv.f.3 STPMV.3 \
stpsv.f.3 STPSV.3 strmm.f.3 STRMM.3 strmv.f.3 STRMV.3 strsm.f.3 STRSM.3 strsv.f.3 STRSV.3 \
XERBLA.3 XERBLA_ARRAY.3 zaxpy.f.3 ZAXPY.3 zcopy.f.3 ZCOPY.3 \
zdotc.f.3 ZDOTC.3 zdotu.f.3 ZDOTU.3 zdrot.f.3 ZDROT.3 zdscal.f.3 ZDSCAL.3 zgbmv.f.3 ZGBMV.3 \
zgemm.f.3 ZGEMM.3 zgemv.f.3 ZGEMV.3 zgerc.f.3 ZGERC.3 zgeru.f.3 ZGERU.3 zhbmv.f.3 ZHBMV.3 \
zhemm.f.3 ZHEMM.3 zhemv.f.3 ZHEMV.3 zher.f.3 ZHER.3 zher2.f.3 ZHER2.3 zher2k.f.3 ZHER2K.3 \
zherk.f.3 ZHERK.3 zhpmv.f.3 ZHPMV.3 zhpr.f.3 ZHPR.3 zhpr2.f.3 ZHPR2.3 zrotg.f.3 ZROTG.3 \
zscal.f.3 ZSCAL.3 zswap.f.3 ZSWAP.3 zsymm.f.3 ZSYMM.3 zsyr2k.f.3 ZSYR2K.3 zsyrk.f.3 ZSYRK.3 \
ztbmv.f.3 ZTBMV.3 ztbsv.f.3 ZTBSV.3 ztpmv.f.3 ZTPMV.3 ztpsv.f.3 ZTPSV.3 ztrmm.f.3 ZTRMM.3 \
ztrmv.f.3 ZTRMV.3 ztrsm.f.3 ZTRSM.3 ztrsv.f.3 ZTRSV.3 ../../blas/man/man3
cd ../..
popd

find manpages/blas/man/man3 -type f -printf "%{_mandir}/man3/%f*\n" > blasmans

find manpages/man/man3 -type f -printf "%{_mandir}/man3/%f*\n" > lapackmans

cp -f manpages/blas/man/man3/* ${RPM_BUILD_ROOT}%{_mandir}/man3
cp -f manpages/man/man3/* ${RPM_BUILD_ROOT}%{_mandir}/man3

# Lapacke headers
mkdir -p %{buildroot}%{_includedir}/lapacke/
cp -a lapacke/include/*.h %{buildroot}%{_includedir}/lapacke/

cd ${RPM_BUILD_ROOT}%{_libdir}
ln -sf liblapack.so.%{version} liblapack.so
ln -sf liblapack.so.%{version} liblapack.so.%{shortver}
ln -sf liblapack.so.%{version} liblapack.so.%{mediumver}
ln -sf libblas.so.%{version} libblas.so
ln -sf libblas.so.%{version} libblas.so.%{shortver}
ln -sf libblas.so.%{version} libblas.so.%{mediumver}
ln -sf liblapacke.so.%{version} liblapacke.so
ln -sf liblapacke.so.%{version} liblapacke.so.%{shortver}
ln -sf liblapacke.so.%{version} liblapacke.so.%{mediumver}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post -n blas -p /sbin/ldconfig

%postun -n blas -p /sbin/ldconfig

%files -f lapackmans
%doc README LICENSE lapackqref.ps
%dir %{_mandir}/man3/
%{_libdir}/liblapack.so.*
%{_libdir}/liblapacke.so.*

%files devel
%{_includedir}/lapacke/
%{_libdir}/liblapack.so
%{_libdir}/liblapacke.so

%files static
%{_libdir}/liblapack*.a

%files -n blas -f blasmans
%doc blasqr.ps LICENSE
%dir %{_mandir}/man3/
%{_libdir}/libblas.so.*

%files -n blas-devel
%{_libdir}/libblas.so

%files -n blas-static
%{_libdir}/libblas*.a

%changelog
* Fri Dec 07 2012 Liu Di <liudidi@gmail.com> - 3.4.0-2
- 为 Magic 3.0 重建

* Mon Nov 28 2011 Tom Callaway <spot@fedoraproject.org> - 3.4.0-1
- update to 3.4.0
- build and include lapacke

* Thu Jun 02 2011 Tom Callaway <spot@fedoraproject.org> - 3.3.1-1
- update to 3.3.1
- create /usr/share/man/manl/ as 0755 and own it in lapack and blas (bz634369)
- spec file cleanup

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 17 2010 Dan Horák <dan[at]danny.cz> - 3.2.2-2
- fix a typo in Makefile.lapack causing #615618

* Wed Jul  7 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 3.2.2-1
- update to 3.2.2
- properly include license text
- static subpackages depend on -devel (they're not useful without it)
- clean up makefiles
- pass on version into makefiles, rather than manually hacking on each update

* Wed Dec  9 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 3.2.1-4
- Move static libs to static subpackages (resolves bz 545143)

* Fri Sep  4 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 3.2.1-3
- use RPM_OPT_O_FLAGS (-O0) everywhere necessary, drop RPM_OPT_SIZE_FLAGS (-Os) (bz 520518)

* Thu Aug 20 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 3.2.1-2
- don't enable xblas yet

* Fri Aug 14 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 3.2.1-1
- update to 3.2.1, spec file cleanups

* Mon Aug 10 2009 Ville Skyttä <ville.skytta@iki.fi> - 3.1.1-7
- Convert specfile to UTF-8.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jul  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> 3.1.1-4
- fix missing dependencies (bz 442915)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 3.1.1-3
- Autorebuild for GCC 4.3

* Thu Aug 23 2007 Tom "spot" Callaway <tcallawa@redhat.com> 3.1.1-2
- fix license (BSD)
- rebuild for BuildID

* Fri May 25 2007 Tom "spot" Callaway <tcallawa@redhat.com> 3.1.1-1
- bump to 3.1.1

* Fri Jan  5 2007 Tom "spot" Callaway <tcallawa@redhat.com> 3.1.0-4
- fix bugzillas 219740,219741

* Wed Dec 20 2006 Tom "spot" Callaway <tcallawa@redhat.com> 3.1.0-3
- make clean everywhere

* Wed Dec 20 2006 Tom "spot" Callaway <tcallawa@redhat.com> 3.1.0-2
- fix the Makefiles

* Tue Nov 14 2006 Tom "spot" Callaway <tcallawa@redhat.com> 3.1.0-1
- bump to 3.1.0

* Thu Sep 14 2006 Tom "spot" Callaway <tcallawa@redhat.com> 3.0-38
- bump for fc-6

* Tue Feb 28 2006 Tom "spot" Callaway <tcallawa@redhat.com> 3.0-37
- bump for FC5

* Mon Dec 19 2005 Tom "spot" Callaway <tcallawa@redhat.com> 3.0-36
- bump for gcc4.1

* Tue Nov 15 2005 Tom "spot" Callaway <tcallawa@redhat.com> 3.0-35
- try not to patch files that do not exist

* Tue Nov 15 2005 Tom "spot" Callaway <tcallawa@redhat.com> 3.0-34
- finish fixing bz 143340

* Thu Oct  6 2005 Tom "spot" Callaway <tcallawa@redhat.com> 3.0-33
- fix bz 169558

* Wed Sep 28 2005 Tom "spot" Callaway <tcallawa@redhat.com> 3.0-32
- move to latest upstream 3.0 tarballs
- add 8 missing BLAS functions from upstream blas tarball (bz 143340)

* Thu Sep 22 2005 Tom "spot" Callaway <tcallawa@redhat.com> 3.0-31
- actually install liblapack_pic.a

* Wed Sep 14 2005 Tom "spot" Callaway <tcallawa@redhat.com> 3.0-30
- make -devel packages
- make liblapack_pic.a package
- use dist tag

* Thu Apr 14 2005 Tom "spot" Callaway <tcallawa@redhat.com> 3.0-29
- package moves to Fedora Extras, gcc4

* Tue Dec 21 2004 Ivana Varekova <varekova@redhat.com>
- fix bug #143420 problem with compiler optimalizations

* Tue Nov 30 2004 Ivana Varekova <varekova@redhat.com>
- fix bug #138683 problem with compilation

* Thu Nov 11 2004 Ivana Varekova <varekova@redhat.com>
- fix build problem bug #138447

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Dec 31 2003 Jeff Johnson <jbj@jbj.org> 3.0-23
- link -lg2c explicitly into liblapack and libblas (#109079).

* Wed Aug 20 2003 Jeremy Katz <katzj@redhat.com> 3.0-22
- nuke -man subpackages (#97506)

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Sun Nov 10 2002 Jeff Johnson <jbj@redhat.com> 3.0-19
- rebuild with x86_64.

* Thu Jul 18 2002 Trond Eivind Glomsrod <teg@redhat.com> 3.0-18
- Remove an empty man page (#63569)

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed May  1 2002 Trond Eivind Glomsrod <teg@redhat.com> 3.0-15
- Rebuild

* Thu Feb 21 2002 Trond Eivind Glomsrod <teg@redhat.com> 3.0-14
- Rebuild

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Aug 13 2001 Trond Eivind Glomsrod <teg@redhat.com> 3.0-12
- The man-pages for xerbla and lsame were in blas-man and lapack-man (#51605)

* Fri Jun  8 2001 Trond Eivind Glomsrod <teg@redhat.com>
- Reenable optimization for IA64

* Fri May 25 2001 Trond Eivind Glomsrod <teg@redhat.com>
- Add all patches from the LAPACK site as of 2001-05-25
- Use this workaround for IA64 instead
- Remove SPARC workaround
- Don't exclude IA64

* Thu Dec 07 2000 Trond Eivind Glomsrod <teg@redhat.com>
- rebuild for main distribution

* Mon Nov 20 2000 Trond Eivind Glomsrod <teg@redhat.com>
- add the LAPACK Quick Reference Guide to the docs
- add the BLAS Quick Reference Guide to the docs

* Tue Aug 01 2000 Trond Eivind Glomsrod <teg@redhat.com>
- fix lack of ldconfig in postuninstall script

* Mon Jul 24 2000 Prospector <prospector@redhat.com>
- rebuilt

* Mon Jul 10 2000 Trond Eivind Glomsrod <teg@redhat.com>
- updated with the latest updates (new tarfile..) from netlib 

* Thu Jun 15 2000 Trond Eivind Glomsrod <teg@redhat.com>
- use %%{_mandir}
- added some flags to work around SPARC compiler bug

* Wed Jan 19 2000 Tim Powers <timp@redhat.com>
- bzipped sources to conserve space

* Tue Jan  4 2000 Jeff Johnson <jbj@redhat.com>
- build for PowerTools 6.2.

* Sat Dec 25 1999 Joachim Frieben <jfrieben@hotmail.com>
- updated to version v3.0 + update as of Tue Nov 30 1999

* Sat Oct 23 1999 Joachim Frieben <jfrieben@hotmail.com>
- updated Red Hat makefiles to v3.0

* Mon Aug 2 1999 Tim Powers <timp@redhat.com>
- updated to v3.0
- built for 6.1

* Mon Apr 12 1999 Michael Maher <mike@redhat.com>
- built package for 6.0

* Sat Oct 24 1998 Jeff Johnson <jbj@redhat.com>
- new description/summary text.

* Fri Jul 17 1998 Jeff Johnson <jbj@redhat.com>
- repackage for powertools.

* Sun Feb 15 1998 Trond Eivind Glomsrod <teg@pvv.ntnu.no>
 [lapack-2.0-9]
 - No code updates, just built with a customized rpm -
   this should make dependencies right.

* Sat Feb 07 1998 Trond Eivind Glomsrod <teg@pvv.ntnu.no>
 [lapack-2.0-8]
 - Total rewrite of the spec file
 - Added my own makefiles - libs should build better,
   static libs should work (and be faster than they
	would be if they had worked earlier ;)
 - No patch necessary anymore.
 - Renamed lapack-blas and lapack-blas-man to
   blas and blas-man. "Obsoletes:" tag added.
   (oh - and as always: Dedicated to the girl I
   love, Eline Skirnisdottir)

* Sat Dec 06 1997 Trond Eivind Glomsrod <teg@pvv.ntnu.no>
 [lapack-2.0-7]
  - added a dependency to glibc, so people don't try with libc5

* Thu Nov 20 1997 Trond Eivind Glomsrod <teg@pvv.ntnu.no>
  [lapack-2.0-6]
  - removed etime.c
  - compiled with egcs, and for glibc 2.0

* Sun Oct 12 1997 Trond Eivind Glomsrod <teg@pvv.ntnu.no>
  [lapack-2.0-5]
  - added a changelog
  - cleaned up building of shared libs
  - now uses a BuildRoot
  - cleaned up the specfile
