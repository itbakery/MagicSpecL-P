Summary: The GNU macro processor
Name: m4
Version: 1.4.16
Release: 2%{?dist}
License: GPLv3+
Group: Applications/Text
Source0: http://ftp.gnu.org/gnu/m4/m4-%{version}.tar.xz
Source1: http://ftp.gnu.org/gnu/m4/m4-%{version}.tar.xz.sig
URL: http://www.gnu.org/software/m4/
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires(post): /sbin/install-info
Requires(preun): /sbin/install-info

%description
A GNU implementation of the traditional UNIX macro processor.  M4 is
useful for writing text files which can be logically parsed, and is used
by many programs as part of their build process.  M4 has built-in
functions for including files, running shell commands, doing arithmetic,
etc.  The autoconf program needs m4 for generating configure scripts, but
not for running configure scripts.

Install m4 if you need a macro processor.

%prep
%setup -q
chmod 644 COPYING

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install INSTALL="%{__install} -p" DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%check
make %{?_smp_mflags} check

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog NEWS README THANKS TODO
%{_bindir}/m4
%{_infodir}/*
%{_mandir}/man1/m4.1*

%post
if [ -f %{_infodir}/m4.info ]; then # --excludedocs?
    /sbin/install-info %{_infodir}/m4.info %{_infodir}/dir || :
fi

%preun
if [ "$1" = 0 ]; then
    if [ -f %{_infodir}/m4.info ]; then # --excludedocs?
        /sbin/install-info --delete %{_infodir}/m4.info %{_infodir}/dir || :
    fi
fi

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sat Jan 14 2012 Liu Di <liudidi@gmail.com> - 1.4.16-2
- 为 Magic 3.0 重建

