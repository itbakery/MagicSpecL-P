Name:           lua
Version:        5.1.4
Release:        4%{?dist}
Summary:        Powerful light-weight programming language
Summary(zh_CN.UTF-8): 强大的轻量级编程语言
Group:          Development/Languages
Group(zh_CN.UTF-8):	开发/语言
License:        MIT
URL:            http://www.lua.org/
Source0:        http://www.lua.org/ftp/lua-%{version}.tar.gz
Patch0:         lua-5.1.4-autotoolize.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  readline-devel ncurses-devel
Provides:       lua = 5.1

%description
Lua is a powerful light-weight programming language designed for
extending applications. Lua is also frequently used as a
general-purpose, stand-alone language. Lua is free software.
Lua combines simple procedural syntax with powerful data description
constructs based on associative arrays and extensible semantics. Lua
is dynamically typed, interpreted from bytecodes, and has automatic
memory management with garbage collection, making it ideal for
configuration, scripting, and rapid prototyping.

%description -l zh_CN.UTF-8
Lua 是一个强大的轻量级编程语言，设计成用于扩展应用程序。
Lua 也常被当作一个通用目的的、独立的语言使用。Lua 是自由
软件。Lua 将简单的程序语法与基于关联数组和可扩展语意的
强大的数据描述结构捆绑在一起。Lua 是类型动态的、字节码
解析的、带有垃圾回收的自动内存管理的，其目标是用于配置、
编写脚本、以及快速原型设计。

%package devel
Summary:        Development files for %{name}
Summary(zh_CN.UTF-8):	%{name} 的开发包。
Group:          System Environment/Libraries
Group(zh_CN.UTF-8):	系统环境/库
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description devel
This package contains development files for %{name}.

%description devel -l zh_CN.UTF-8
%{name} 的开发包。

%package static
Summary:        Static library for %{name}
Summary(zh_CN.UTF-8):	%{name} 的静态库
Group:          System Environment/Libraries
Group(zh_CN.UTF-8):   系统环境/库
Requires:       %{name} = %{version}-%{release}

%description static
This package contains the static version of liblua for %{name}.

%description static -l zh_CN.UTF-8
%{name} 的静态库。


%prep
%setup -q
%patch0 -p1 -E -z .autoxxx
# fix perms on auto files
chmod u+x autogen.sh config.guess config.sub configure depcomp install-sh missing


%build
%configure --with-readline
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
# hack so that only /usr/bin/lua gets linked with readline as it is the
# only one which needs this and otherwise we get License troubles
make %{?_smp_mflags} LIBS="-ldl" luac_LDADD="liblua.la -lm -ldl"
# also remove readline from lua.pc
sed -i 's/-lreadline -lncurses //g' etc/lua.pc


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_libdir}/*.la
mkdir -p $RPM_BUILD_ROOT%{_libdir}/lua/5.1
mkdir -p $RPM_BUILD_ROOT%{_datadir}/lua/5.1


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYRIGHT HISTORY README doc/*.html doc/*.css doc/*.gif doc/*.png
%{_bindir}/lua*
%{_libdir}/liblua-*.so
%{_mandir}/man1/lua*.1*
%dir %{_libdir}/lua
%dir %{_libdir}/lua/5.1
%dir %{_datadir}/lua
%dir %{_datadir}/lua/5.1


%files devel
%defattr(-,root,root,-)
%{_includedir}/l*.h
%{_includedir}/l*.hpp
%{_libdir}/liblua.so
%{_libdir}/pkgconfig/*.pc

%files static
%defattr(-,root,root,-)
%{_libdir}/*.a

%changelog
* Sat Jan 14 2012 Liu Di <liudidi@gmail.com> - 5.1.4-4
- 为 Magic 3.0 重建


