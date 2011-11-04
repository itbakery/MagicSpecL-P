%define rc_ver RC2
Name:           lazarus
Version:        0.9.30.2
Release:        0.%{rc_ver}.%{?dist}
Summary:        Lazarus Component Library and IDE for Freepascal
Summary(zh_CN.UTF-8): Lazarus 组件库和 IDE

Group:          Development/Languages
Group(zh_CN.UTF-8):   开发/语言
# GNU Classpath style exception, see COPYING.modifiedLGPL
License:        GPLv2+ and MPLv1.1 and LGPLv2+ with exceptions
URL:            http://www.lazarus.freepascal.org/
Source0:        http://download.sourceforge.net/%{name}/%{name}-%{version}%{rc_ver}-src.tar.bz2
patch0:         Makefile_patch.diff
patch1:         Desktop_patch.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  fpc >= 2.2.2, binutils, gdk-pixbuf-devel, gtk+-devel, glibc-devel, desktop-file-utils, gtk2-devel, fpc-src >= 2.2.2
Requires:       fpc-src >= 2.2.2, fpc >= 2.2.2, binutils, gdk-pixbuf-devel, gtk+-devel, glibc-devel, gdb 

%description
Lazarus is a free and opensource RAD tool for freepascal using the lazarus
component library - LCL, which is also included in this package.

%description -l zh_CN.UTF-8
Lazarus 是一个自由开源的快速开发工具，使用来自 freepascal 的
Lazarus 的组件库 - LCL，它也包含在这个包里。
类似于 Windows 下的 Delphi。

%prep
%setup -c -q
%patch0 -p0
%patch1 -p0

%build
cd lazarus
# Remove the files for building debian-repositories
rm -rf debian
rm -rf tools/install/cross_unix/debian_crosswin32
rm tools/install/cross_unix/create_linux_cross_win32_deb.sh
rm tools/install/cross_unix/HowToCreate_fpc_crosswin32_deb.txt
# Remove scripts vulnerable to symlink-attacks (bug 460642)
rm tools/install/build_fpc_snaphot_rpm.sh
rm tools/install/check_fpc_dependencies.sh
rm tools/install/create_fpc_deb.sh
rm tools/install/create_fpc_export_tgz.sh
rm tools/install/create_fpc_rpm.sh
rm tools/install/create_fpc-src_rpm.sh
rm tools/install/create_fpc_tgz_from_local_dir.sh
rm tools/install/create_lazarus_export_tgz.sh 

export FPCDIR=%{_datadir}/fpcsrc/
fpcmake -Tall
make tools OPT='-gl'
make bigide OPT='-gl'
make lazbuilder OPT='-gl'
# Add the ability to create gtk2-applications
export LCL_PLATFORM=gtk2
make lcl ideintf packager/registration bigidecomponents OPT='-gl'
export LCL_PLATFORM=

%install
rm -rf %{buildroot}
make -C lazarus install INSTALL_PREFIX=%{buildroot}%{_prefix} _LIB=%{_lib}
make -C lazarus/install/man INSTALL_MANDIR=%{buildroot}%{_mandir}

install -D -p -m 0644 lazarus/install/lazarus-mime.xml $LazBuildDir%{buildroot}%{_datadir}/mime/packages/lazarus.xml
install -D -p -m 0644 lazarus/images/ide_icon48x48.png %{buildroot}%{_datadir}/pixmaps/lazarus.png
desktop-file-install \
        --vendor fedora \
        --dir %{buildroot}%{_datadir}/applications \
        lazarus/install/%{name}.desktop

ln -sf ../%{_lib}/%{name}/lazarus %{buildroot}%{_bindir}/lazarus-ide
ln -sf ../%{_lib}/%{name}/startlazarus %{buildroot}%{_bindir}/startlazarus
ln -sf ../%{_lib}/%{name}/lazbuild %{buildroot}%{_bindir}/lazbuild

install -D -p -m 0644 lazarus/tools/install/linux/editoroptions.xml %{buildroot}%{_sysconfdir}/lazarus/editoroptions.xml
sed 's#/usr/lib/lazarus/#%{_libdir}/%{name}#;s#/\$(FPCVER)##' lazarus/tools/install/linux/environmentoptions.xml > %{buildroot}%{_sysconfdir}/lazarus/environmentoptions.xml

chmod 755 %{buildroot}%{_libdir}/%{name}/components/lazreport/tools/localize.sh

%clean
rm -rf %{buildroot}

%post
update-mime-database %{_datadir}/mime &> /dev/null || :

%postun
update-mime-database %{_datadir}/mime &> /dev/null || :

%files
%defattr(-,root,root,-)
%{_libdir}/%{name}
%{_bindir}/%{name}-ide
%{_bindir}/startlazarus
%{_bindir}/lazbuild
%{_datadir}/pixmaps/lazarus.png
%{_datadir}/applications/fedora-%{name}.desktop
%{_datadir}/mime/packages/lazarus.xml
%doc lazarus/COPYING*
%doc lazarus/README.txt
%dir %{_sysconfdir}/lazarus
%config(noreplace) %{_sysconfdir}/lazarus/editoroptions.xml
%config(noreplace) %{_sysconfdir}/lazarus/environmentoptions.xml
%{_mandir}/*/*

%changelog
* Sun May 31 2009 Liu Di <liudidi@gmail.com> - 0.9.26.2-1
- 更新到 0.9.26.2

* Tue Jul 15 2008 Liu Di <liudidi@gmail.com> - 0.9.24-1mgc
- 更新到 0.9.24
