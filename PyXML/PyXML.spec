Summary: XML libraries for python.
Summary(zh_CN.GB18030): python µÄ XML ¿â
Name: PyXML
Version: 0.8.4
Release: 12%{?dist}
Source: http://prdownloads.sourceforge.net/pyxml/PyXML-%{version}.tar.gz
Patch0: PyXML-0.7.1-intern.patch
Patch1: PyXML-0.8.4-cvs20041111-python2.4-backport.patch
Patch2: PyXML-memmove.patch
License: MIT and Python and ZPLv1.0 and BSD
Group: Development/Libraries
Group(zh_CN.GB18030): ¿ª·¢/¿â
Requires: python
URL: http://pyxml.sourceforge.net/
BuildRequires: python python-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot

BuildRequires: python-setuptools-devel

%description
An XML package for Python.  The distribution contains a
validating XML parser, an implementation of the SAX and DOM
programming interfaces and an interface to the Expat parser.

%description -l zh_CN.GB18030
Python µÄ XML °ü¡£Õâ¸ö·¢ĞĞ°üÀ¨ÁËÒ»¸öºÏ·¨µÄ XML ½âÎöÆ÷£¬
SAX ºÍ DOM ÊµÏÖµÄ³ÌĞò½Ó¿ÚºÍ Expat ½âÎöÆ÷µÄ½Ó¿Ú¡£

%prep
%setup -q

%patch0 -p1 -b .intern
%patch1 -p1 -b .python2.4-backport
%patch2 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} -c 'import setuptools; execfile("setup.py")' build  --with-xslt

%install
rm -fr $RPM_BUILD_ROOT
python -c 'import setuptools; execfile("setup.py")' install --skip-build --root=$RPM_BUILD_ROOT --with-xslt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc LICENCE ANNOUNCE CREDITS README README.dom README.pyexpat README.sgmlop TODO doc/*
%{_bindir}/xmlproc_parse
%{_bindir}/xmlproc_val
%{_libdir}/python?.?/site-packages/*egg-info
%{_libdir}/python?.?/site-packages/_xmlplus

%changelog
* Mon Jan 23 2012 Liu Di <liudidi@gmail.com> - 0.8.4-12
- ä¸º Magic 3.0 é‡å»º


