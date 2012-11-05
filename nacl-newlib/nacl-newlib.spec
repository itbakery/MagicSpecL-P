%global gitver 67e3510

Name:		nacl-newlib
Summary:	C library intended for use on embedded systems
Version:	1.20.0
Release:	2.git%{gitver}%{?dist}
# Generated from git
# git clone http://git.chromium.org/native_client/nacl-newlib.git
# (Checkout ID taken from chromium-17.0.963.46/native_client/tools/REVISIONS)
# cd nacl-newlib
# git checkout 67e351079b71e78eaad782a19ffa9f3ff2c1d78d
# cd ..
# For newlib version, grep PACKAGE_VERSION newlib/libm/configure
# mv nacl-newlib nacl-newlib-1.20.0-git67e3510
# tar cfj nacl-newlib-1.20.0-git67e3510.tar.bz2 nacl-newlib-1.20.0-git67e3510
License:	BSD and MIT and LGPLv2+
Source0:	nacl-newlib-%{version}-git%{gitver}.tar.bz2
# We need to copy some missing header files from chromium
# mkdir ~/nacl-headers-21.0.1180.81
# cd chromium-21.0.1180.81/native_client/
# ./src/trusted/service_runtime/export_header.py src/trusted/service_runtime/include ~/nacl-headers-19.0.1084.56/
# cd ~/nacl-headers-21.0.1180.81
# tar cfj ~/nacl-headers-21.0.1180.81.tar.bz2 .
Source1:	nacl-headers-21.0.1180.81.tar.bz2
# Taken from chromium-21.0.1180.81/native_client/tools/newlib-libc-script
Source2:	newlib-libc-script
# Taken from chromium-21.0.1180.81/native_client/src/untrusted/pthread/pthread.h
Source3:	pthread.h

URL:		http://sourceware.org/newlib/
BuildRequires:	nacl-binutils nacl-gcc
ExclusiveArch:	i686 x86_64

%description
Newlib is a C library intended for use on embedded systems. It is a 
conglomeration of several library parts, all under free software licenses
that make them easily usable on embedded products. This is the nacl fork.

%prep
%setup -q -n %{name}-%{version}-git%{?gitver}
pushd newlib/libc/sys/nacl
tar xf %{SOURCE1}
popd
cp -a %{SOURCE2} .

%build
export NEWLIB_CFLAGS="-O2 -D_I386MACH_ALLOW_HW_INTERRUPTS -DSIGNAL_PROVIDED -mtls-use-call"
%configure \
	--disable-libgloss \
	--enable-newlib-iconv \
	--enable-newlib-io-long-long \
	--enable-newlib-io-long-double \
	--enable-newlib-io-c99-formats \
	--enable-newlib-mb \
	libc_cv_initfinit_array=yes \
	CFLAGS="-O2" \
	CFLAGS_FOR_TARGET="$NEWLIB_CFLAGS" \
	CXXFLAGS_FOR_TARGET="$NEWLIB_CFLAGS" \
	--target=x86_64-nacl

make

%install
make DESTDIR=%{buildroot} install

# Conflicts with binutils
rm -rf %{buildroot}%{_infodir}/

# The default pthread.h doesn't work right?
rm -rf %{buildroot}%{_prefix}/x86_64-nacl/include/pthread.h
cp %{SOURCE3} %{buildroot}%{_prefix}/x86_64-nacl/include/

# We have to hack up libc.a to get things working.

# 32bit
mv %{buildroot}%{_prefix}/x86_64-nacl/lib/32/libc.a %{buildroot}%{_prefix}/x86_64-nacl/lib/32/libcrt_common.a
sed "s/@OBJFORMAT@/elf32-nacl/" newlib-libc-script > %{buildroot}%{_prefix}/x86_64-nacl/lib/32/libc.a

# 64bit (default)
mv %{buildroot}%{_prefix}/x86_64-nacl/lib/libc.a %{buildroot}%{_prefix}/x86_64-nacl/lib/libcrt_common.a
sed "s/@OBJFORMAT@/elf64-nacl/" newlib-libc-script > %{buildroot}%{_prefix}/x86_64-nacl/lib/libc.a
magic_rpm_clean.sh

%files
%{_datadir}/iconv_data/
%{_prefix}/x86_64-nacl/include/
%{_prefix}/x86_64-nacl/lib/

%changelog
* Tue Aug 28 2012 Tom Callaway <spot@fedoraproject.org> 1.20.0-2.git67e3510
- update for chromium 21

* Tue Jun 12 2012 Tom Callaway <spot@fedoraproject.org> 1.20.0-1.git096a72b
- update for chromium 19

* Mon Feb 13 2012 Tom Callaway <spot@fedoraproject.org> 1.18.0-2.git590577e
- update for chromium 17

* Thu Oct 27 2011 Tom Callaway <spot@fedoraproject.org> 1.18.0-1.gitf5185a57
- initial package
