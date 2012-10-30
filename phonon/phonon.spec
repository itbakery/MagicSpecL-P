%define build_type release

# path define for backends
%define PLUGIN_INSTALL_DIR /usr/lib/kde4
%define SERVICES_INSTALL_DIR /usr/share/kde4/services
%define ICON_INSTALL_DIR /usr/share/icons

Name: phonon
Summary: KDE4 Multimedia Framework
Summary(zh_CN.UTF-8): KDE4 多媒体框架
Version: 4.6.0
Release: 6%{?dist}
URL: http://websvn.kde.org/branches/phonon/4.2/
License: LGPL v2+
Group: System/Libraries
Group(zh_CN.UTF-8): 系统环境/库

Source0: %{name}-%{version}.tar.xz
Source1: http://gstreamer.freedesktop.org/data/images/artwork/gstreamer-logo.svg

# svn export svn://anonsvn.kde.org/home/kde/trunk/playground/multimedia/phonon-backends/mplayer
Source2: phonon-mplayer.tar.bz2

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot-%(%{__id_u} -n)

BuildRequires: cmake >= 2.6.2
BuildRequires: qt4-devel >= 4.4.3
BuildRequires: automoc4 >= 0.9.86
BuildRequires: glib2-devel
BuildRequires: libxml2-devel
BuildRequires: ImageMagick

# 修正 phonon_gstreamer 本地媒体对象文件名编码问题
# patch written by nihui, Feb.1st, 2009
Patch21: phonon-4.3.80-gstreamer_localfile_path.patch
# phonon_gstreamer 添加 ape 格式媒体支持
# patch written by nihui, Feb.1st, 2009
Patch22: phonon-4.3.80-gstreamer-ape_mediatype.patch
# 总是列出 alsa 和 oss 音频输出设备
# patch written by nihui, Jul.31, 2009
Patch23: phonon-4.3.1-xine-always_list_default_devices.patch
# phonon_mplayer 添加 ape 格式媒体支持
# patch written by nihui, Jan.3rd, 2010
Patch24: phonon-4.3.80-phonon-mplayer.patch
Patch25: phonon-4.3.80-mplayer-ape_mediatype.patch
# 修正 phonon_mplayer 中文语言输出解析的问题
# patch written by nihui, Jan.15th, 2010
Patch26: phonon-4.3.80-mplayer-cn_regexp.patch
# 修正 phonon_mplayer 启动时音量过响的问题
# patch written by nihui, Apr.11st, 2010
Patch27: phonon-4.4.0-mplayer-using_sysvolume.patch




# revert broken upstream patch
Patch7000: 18b0efac45247f35b7f8aa5a54d2b269035713e6.patch


%description
Phonon is the KDE4 Multimedia Framework.

%description -l zh_CN.UTF-8
Phonon 是 KDE4 多媒体框架。

#--------------------------------------------------------------------
#后端独立出去
%if 0
%package -n phonon-gstreamer
Summary: GStreamer backend to Phonon
Summary(zh_CN.UTF-8): Phonon 的 GStreamer 后端
Group: System/Libraries
Group(zh_CN.UTF-8): 系统/库
BuildRequires: gstreamer-devel
BuildRequires: gstreamer-plugins-base-devel
Requires: gstreamer-plugins-good
Provides: phonon-backend

%description -n phonon-gstreamer
GStreamer backend to Phonon.

%description -n phonon-gstreamer -l zh_CN.UTF-8
Phonon 的 GStreamer 后端。

#--------------------------------------------------------------------
%package -n phonon-xine
Summary: Xine backend to Phonon
Summary(zh_CN.UTF-8): Phonon 的 Xine 后端
Group: System/Libraries
Group(zh_CN.UTF-8): 系统/库
BuildRequires: xine-lib-devel
Requires: xine-lib
Provides: phonon-backend

%description -n phonon-xine
Xine backend to Phonon.

%description -n phonon-xine -l zh_CN.UTF-8
Phonon 的 Xine 后端。

#--------------------------------------------------------------------
%package -n phonon-mplayer
Summary: MPlayer backend to Phonon
Summary(zh_CN.UTF-8): Phonon 的 MPlayer 后端
Group: System/Libraries
Group(zh_CN.UTF-8): 系统/库
BuildRequires: mplayer
Requires: mplayer
Provides: phonon-backend

%description -n phonon-mplayer
MPlayer backend to Phonon.

%description -n phonon-mplayer -l zh_CN.UTF-8
Phonon 的 MPlayer 后端。
%endif

#--------------------------------------------------------------------
%package devel
Group: Development/Libraries
Group(zh_CN.UTF-8): 开发/库
Summary: Header files and documentation for compiling KDE applications
Summary(zh_CN.UTF-8): 编译 KDE 应用程序所需的头文件和文档
Requires: %{name} = %{version}

%description devel
This package includes the header files you will need to compile applications
for KDE. Also included is the KDE API documentation in HTML format for easy
browsing.

%description devel -l zh_CN.UTF-8
本软件包包含了需要编译 KDE 应用程序所需的头文件和文档。同时也包含了方便浏览
的 HTML 格式的 KDE API 文档。

#--------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}

#%patch21 -p1
#%patch22 -p1
#%patch23 -p0

# phonon-mplayer
#tar -xf %{SOURCE2} -C .
#%patch24 -p1
#%patch25 -p1
#%patch26 -p1
#%patch27 -p0


#%patch7000 -p1 -R

%build
mkdir build
cd build
export CFLAGS=$RPM_OPT_FLAGS
%cmake_kde4 -DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DCMAKE_BUILD_TYPE=%{build_type} \
	-DCMAKE_CXX_FLAGS_DEBUG:STRING="$RPM_OPT_FLAGS" \
	-DLIB_INSTALL_DIR=%{_libdir} \
	-DPLUGIN_INSTALL_DIR=%{PLUGIN_INSTALL_DIR} \
	-DSERVICES_INSTALL_DIR=%{SERVICES_INSTALL_DIR} \
	-DICON_INSTALL_DIR=%{ICON_INSTALL_DIR} \
	-DCONFIG_INSTALL_DIR=%{_sysconfdir} ..

make %{?_smp_mflags}

%install
cd build
%{__rm} -rf %{buildroot}
%{__make} DESTDIR=%{buildroot} install

# qt4 phonon hack  --- nihui
mkdir -p %{buildroot}%{qt4_libdir}
mkdir -p %{buildroot}%{qt4_includedir}
pushd %{buildroot}%{_libdir}
for i in *.so* ; do
        ln -sf %{_libdir}/$i %{buildroot}%{qt4_libdir}
done
popd
pushd %{buildroot}%{_includedir}
for i in phonon ; do
        ln -sf %{_includedir}/$i %{buildroot}%{qt4_includedir}
done
popd

# set #include <Phonon/XXXX> for backward compability in Qt 4.4+   --- nihui
#mkdir -p %{buildroot}%{qt4_includedir}/Phonon
cp -r %{buildroot}%{_includedir}/KDE/Phonon %{buildroot}%{qt4_includedir}
pushd %{buildroot}%{qt4_includedir}/Phonon
for i in `ls -l | awk '/^-/{print $NF}'` ; do
	sed -i 's/\"\.\.\/\.\.\/phonon\//\"\.\.\/phonon\//g' $i
done
popd
pushd %{buildroot}%{qt4_includedir}/Phonon/Experimental
for i in * ; do
        sed -i 's/\"\.\.\/\.\.\/phonon\//\"\.\.\/phonon\//g' $i
done
popd


%if 0
# move the oxygen-only phonon-xine icons to hicolor
test -d %{buildroot}%ICON_INSTALL_DIR/hicolor && exit 0
mv %{buildroot}%ICON_INSTALL_DIR/oxygen %{buildroot}%ICON_INSTALL_DIR/hicolor

# install gstreamer icons
install -D -m 0644 %{SOURCE1} %{buildroot}%ICON_INSTALL_DIR/hicolor/scalable/apps/phonon-gstreamer.svg
for i in 16 22 32 48 64 128; do
  mkdir -p %{buildroot}%ICON_INSTALL_DIR/hicolor/${i}x${i}/apps
  convert -background None -geometry ${i}x${i}  %{SOURCE1} %{buildroot}%ICON_INSTALL_DIR/hicolor/${i}x${i}/apps/phonon-gstreamer.png
done

# install mplayer icons
# no 64x64 and 128x128 icons, and svgz icon
for i in 16 22 32 48; do
    mkdir -p %{buildroot}%ICON_INSTALL_DIR/hicolor/${i}x${i}/apps
    cp -r ../mplayer/icons/${i}x${i}/phonon-mplayer.png %{buildroot}%ICON_INSTALL_DIR/hicolor/${i}x${i}/apps/phonon-mplayer.png
done
%endif

magic_rpm_clean.sh

%clean
%{__rm} -rf %{buildroot} %{_builddir}/%{buildsubdir}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_libdir}/libphononexperimental.so.*
%{_datadir}/dbus-1/interfaces/org.kde.Phonon.AudioOutput.xml
%{_libdir}/libphonon.so.*
%{qt4_libdir}/*.so.*

%if 0
%files -n phonon-gstreamer
%defattr(-,root,root)
%PLUGIN_INSTALL_DIR/plugins/phonon_backend/phonon_gstreamer.so
%SERVICES_INSTALL_DIR/phononbackends/gstreamer.desktop
%ICON_INSTALL_DIR/hicolor/*/apps/phonon-gstreamer.*

%files -n phonon-xine
%defattr(-,root,root)
%PLUGIN_INSTALL_DIR/plugins/phonon_backend/phonon_xine.so
%SERVICES_INSTALL_DIR/phononbackends/xine.desktop
%ICON_INSTALL_DIR/hicolor/*/apps/phonon-xine.*

%files -n phonon-mplayer
%defattr(-,root,root)
%PLUGIN_INSTALL_DIR/plugins/phonon_backend/phonon_mplayer.so
%SERVICES_INSTALL_DIR/phononbackends/mplayer.desktop
%ICON_INSTALL_DIR/hicolor/*/apps/phonon-mplayer.*
%endif

%files devel
%defattr(-,root,root,-)
%{_includedir}/phonon
%{_includedir}/KDE
%{_libdir}/libphonon.so
%{_libdir}/libphononexperimental.so
%{_libdir}/pkgconfig/phonon.pc
%{_libdir}/cmake/phonon/*
%{qt4_libdir}/*.so
%{_datadir}/qt4/mkspecs/modules/qt_phonon.pri
%{qt4_includedir}/*
%{_datadir}/phonon/buildsystem/*
%{qt4_pluginsdir}/designer/libphononwidgets.so

%changelog
* Fri Jan 15 2010 Ni Hui <shuizhuyuanluo@126.com> - 4.3.80-2mgc
- 修正 mplayer 中文语言输出解析的问题(patch 26 written by nihui)
- 乙丑  十二月初一

* Sun Jan 3 2010 Ni Hui <shuizhuyuanluo@126.com> - 4.3.80-1mgc
- 更新至 4.3.80
- 添加 phonon-mplayer
- gstreamer 和 mplayer 后端的 ape 格式支持
- 己丑  十一月十九

* Fri Jul 31 2009 Ni Hui <shuizhuyuanluo@126.com> - 4.3.1-2mgc
- 总是列出 alsa 和 oss 音频输出设备(patch 23 written by nihui)
- 己丑  六月初十

* Sun Mar 15 2009 Ni Hui <shuizhuyuanluo@126.com> - 4.3.1-0.3mgc
- xine mrl 上游补丁(替代 patch 20)
- 还原 gstreamer 本地媒体编码
- 图标目录改为 hicolor，添加 gstreamer 徽标 
- 己丑  二月十九

* Sat Mar 7 2009 Ni Hui <shuizhuyuanluo@126.com> - 4.3.1-0.2mgc
- gstreamer 上游补丁两个，代替原中文文件名媒体修正
- 己丑  二月十一

* Sun Mar 1 2009 Ni Hui <shuizhuyuanluo@126.com> - 4.3.1-0.1mgc
- 更新至 4.3.1
- 禁用 patch 1000(need review...)
- 己丑  二月初五

* Sun Feb 1 2009 Ni Hui <shuizhuyuanluo@126.com> - 4.3.0-0.3mgc
- 修正 phonon_gstreamer 本地媒体对象文件名编码问题(patch 21 written by nihui, unused)
- phonon_gstreamer 添加 ape 格式媒体支持(patch 22 written by nihui)
- 己丑  正月初七

* Fri Jan 23 2009 Ni Hui <shuizhuyuanluo@126.com> - 4.3.0-0.2mgc
- 重建
- 戊子  十二月廿八

* Thu Jan 22 2009 Ni Hui <shuizhuyuanluo@126.com> - 4.3.0-0.1mgc
- 更新至 4.3.0
- 戊子  十二月廿七

* Tue Jan 13 2009 Ni Hui <shuizhuyuanluo@126.com> - 4.2.96-0.1mgc
- 更新至 4.2.96
- relwithdeb 编译模式
- 戊子  十二月十八

* Fri Nov 28 2008 Ni Hui <shuizhuyuanluo@126.com> - 4.2.80-0.1mgc
- 更新至 4.2.80
- 戊子  十一月初一

* Sat Nov 22 2008 Ni Hui <shuizhuyuanluo@126.com> - 4.2.71-0.1mgc
- 更新至 4.2.71
- 拆出 phonon-xine
- 戊子  十月廿五  [小雪]

* Fri Aug 29 2008 Ni Hui <shuizhuyuanluo@126.com> - 4.2.0-0.2mgc
- 重建
- 戊子  七月廿九

* Thu Jul 24 2008 Liu Di <liudidi@gmail.com> - 4.2.0-0.1mgc
- 更新到 4.2.0 正式版

* Mon Jun 30 2008 Ni Hui <shuizhuyuanluo@126.com> - 4.1.83-0.2mgc
- 更改 gstreamer 后端安装路径
- 戊子  五月廿七

* Sat Jun 21 2008 Ni Hui <shuizhuyuanluo@126.com> - 4.1.83-0.1mgc
- 更新至 4.1.83
- 戊子  五月十八  [夏至]

* Wed Jun 4 2008 Ni Hui <shuizhuyuanluo@126.com> - 4.2-0.svn815960.1mgc
- 首次生成 rpm 包
- 更新至 4.2-svn815960(KDE4 branches phonon)
- 戊子  五月初一
