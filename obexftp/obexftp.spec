%define python_sitelib %(%{__python} -c "from distutils import sysconfig; print sysconfig.get_python_lib()")
%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')
%define ruby_sitearch %(ruby -rrbconfig -e 'puts Config::CONFIG["sitearchdir"]')

%define pre rc9

Name: obexftp
Summary: Tool to access devices via the OBEX protocol
Summary(zh_CN.GB18030):	Õ®π˝ OBEX –≠“È∑√Œ …Ë±∏
Group: Applications/File
Group(zh_CN.GB18030): ”¶”√≥Ã–Ú/Œƒµµ
Version: 0.23
Release: 2%{?dist}
License: GPLv2+
URL: http://openobex.triq.net/
Source: http://triq.net/obexftp/%{name}-%{version}.tar.bz2
Patch0: %{name}-norpath.patch
Patch1: %{name}-perl.patch
Patch2: %{name}-r9.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(id -u -n)
BuildRequires: bluez-libs-devel
BuildRequires: gettext-devel
BuildRequires: libtool
BuildRequires: openobex-devel >= 1.2
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: python-devel
BuildRequires: ruby
BuildRequires: ruby-devel
BuildRequires: tcl-devel

%description
The overall goal of this project is to make mobile devices featuring the OBEX
protocol and adhering to the OBEX FTP standard accessible by an open source
implementation. The common usage for ObexFTP is to access your mobile phones
memory to store and retrieve e.g. your phonebook, logos, ringtones, music,
pictures and alike.

%description -l zh_CN.GB18030
Õ®π˝ OBEX –≠“È∑√Œ …Ë±∏

%package -n python-%{name}
Summary: Python library to access devices via the OBEX protocol
Summary(zh_CN.GB18030): %{name} µƒ Python ø‚
Group: Development/Libraries
Group(zh_CN.GB18030): ø™∑¢/ø‚
Requires: %{name} = %{version}-%{release}

%description -n python-%{name}
The overall goal of this project is to make mobile devices featuring the OBEX
protocol and adhering to the OBEX FTP standard accessible by an open source
implementation. The common usage for ObexFTP is to access your mobile phones
memory to store and retrieve e.g. your phonebook, logos, ringtones, music,
pictures and alike.

%description -n python-%{name} -l zh_CN.GB18030
%{name} µƒ Python ø‚

%package -n perl-%{name}
Summary: Perl library to access devices via the OBEX protocol
Summary(zh_CN.GB18030): %{name} µƒ Perl ø‚
Group: Development/Libraries
Group(zh_CN.GB18030): ø™∑¢/ø‚
Requires: %{name} = %{version}-%{release}
Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description -n perl-%{name}
The overall goal of this project is to make mobile devices featuring the OBEX
protocol and adhering to the OBEX FTP standard accessible by an open source
implementation. The common usage for ObexFTP is to access your mobile phones
memory to store and retrieve e.g. your phonebook, logos, ringtones, music,
pictures and alike.

%description -n perl-%{name} -l zh_CN.GB18030
%{name} µƒ Perl ø‚

%package -n ruby-%{name}
Summary: Ruby library to access devices via the OBEX protocol
Summary(zh_CN.GB18030): %{name} µƒ Ruby ø‚
Group: Development/Libraries
Group(zh_CN.GB18030): ø™∑¢/ø‚
Requires: ruby(abi) = 1.8
Requires: %{name} = %{version}-%{release}

%description -n ruby-%{name}
The overall goal of this project is to make mobile devices featuring the OBEX
protocol and adhering to the OBEX FTP standard accessible by an open source
implementation. The common usage for ObexFTP is to access your mobile phones
memory to store and retrieve e.g. your phonebook, logos, ringtones, music,
pictures and alike.

%description -n ruby-%{name} -l zh_CN.GB18030
%{name} µƒ Ruby ø‚

%package devel
Summary: Header files and libraries for %{name}
Summary(zh_CN.GB18030): %{name} µƒø™∑¢Œƒº˛
Group: Development/Libraries
Group(zh_CN.GB18030): ø™∑¢/ø‚
Requires: %{name} = %{version}-%{release}
Requires: openobex-devel >= 1.2
Requires: pkgconfig

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%description devel -l zh_CN.GB18030
%{name} µƒø™∑¢Œƒº˛

%prep
%setup -q
%patch0 -p1 -b .norpath
%patch1 -p1 -b .p
%patch2 -p1

%build
#mkdir m4
libtoolize --force --copy && aclocal && automake && autoconf
%configure --disable-static --disable-dependency-tracking --disable-rpath
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} DESTDIR=%{buildroot} install
chmod 755 %{buildroot}%{perl_vendorarch}/*/OBEXFTP/OBEXFTP.so

%{__rm} %{buildroot}%{_libdir}/*.la
%{__rm} %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/*/OBEXFTP/{.packlist,OBEXFTP.bs}

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, -)
%doc AUTHORS COPYING ChangeLog NEWS README THANKS TODO
%{_mandir}/man1/obexftp.1*
%{_mandir}/man1/obexftpd.1*
%{_bindir}/obexftp
%{_bindir}/obexftpd
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, -)
%{_includedir}/bfb/
%{_includedir}/multicobex/
%{_includedir}/obexftp/
%{_libdir}/*.so
%{_libdir}/pkgconfig/obexftp.pc

%files -n python-%{name}
%defattr(-, root, root, -)
%dir %{python_sitearch}/obexftp
%{python_sitearch}/obexftp/_obexftp.so*
%{python_sitearch}/obexftp/__init__.py*
%{python_sitearch}/*.egg-info

%files -n perl-%{name}
%defattr(-, root, root, -)
%{perl_vendorarch}/OBEXFTP.pm
%dir %{perl_vendorarch}/*/OBEXFTP
%{perl_vendorarch}/*/OBEXFTP/OBEXFTP.so

%files -n ruby-%{name}
%defattr(-, root, root, -)
%{ruby_sitearch}/obexftp.so

%changelog
* Thu Jan 19 2012 Liu Di <liudidi@gmail.com> - 0.23-2
- ‰∏∫ Magic 3.0 ÈáçÂª∫

* Fri Sep 05 2008 Liu Di <liudidi@gmail.com> - 0.22-1mgc
- …˝º∂µΩ 0.22 ’˝ Ω∞Ê
- ‘⁄ bluez 4.2 …œ÷ÿΩ®

* Tue Jun 10 2008 Liu Di <liudidi@gmail.com> - 0.22-0.9.rc9
- Œ™ Magic ÷ÿΩ®
