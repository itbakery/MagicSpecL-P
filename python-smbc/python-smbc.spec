%{?filter_setup:
%filter_provides_in %{python_sitearch}/.*\.so$ 
%filter_setup
}

Summary:       Python bindings for libsmbclient API from Samba
Name:          python-smbc
Version:       1.0.11
Release:       2%{?dist}
URL:           http://cyberelk.net/tim/software/pysmbc/
Source:        http://pypi.python.org/packages/source/p/pysmbc/pysmbc-%{version}.tar.bz2
License:       GPLv2+
Group:         Development/Languages
BuildRequires: python2-devel
BuildRequires: python3-devel
BuildRequires: libsmbclient-devel >= 3.2
BuildRequires: epydoc

%description
This package provides Python bindings for the libsmbclient API
from Samba, known as pysmbc. It was written for use with
system-config-printer, but can be put to other uses as well.

%package -n python3-smbc
Summary:       Python3 bindings for libsmbclient API from Samba
Group:         Development/Languages

%description -n python3-smbc
This package provides Python bindings for the libsmbclient API
from Samba, known as pysmbc. It was written for use with
system-config-printer, but can be put to other uses as well.

This is a ported release for python 3.1

%package doc
Summary:       Documentation for python-smbc
Group:         Documentation

%description doc
Documentation for python-smbc.

%prep
%setup -q -n pysmbc-%{version}

rm -rf %{py3dir}
cp -a . %{py3dir}


%build
CFLAGS="%{optflags}" %{__python} setup.py build
rm -rf html
epydoc -o html --html build/lib*/smbc.so

pushd %{py3dir}
CFLAGS="%{optflags}" %{__python3} setup.py build
popd


%install
pushd %{py3dir}
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}
chmod 755 %{buildroot}%{python3_sitearch}/smbc*.so
popd

%{__python} setup.py install -O1 --skip-build --root %{buildroot}
chmod 755 %{buildroot}%{python_sitearch}/smbc.so


%files
%defattr(-,root,root,-)
%doc COPYING README NEWS
%{python_sitearch}/smbc.so
%{python_sitearch}/pysmbc*.egg-info

%files doc
%defattr(-,root,root,-)
%doc html

%files -n python3-smbc
%defattr(-,root,root,-)
%doc COPYING README NEWS
%{python3_sitearch}/smbc.cpython-3?mu.so
%{python3_sitearch}/pysmbc*.egg-info


%changelog
* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri May 20 2011 Tim Waugh <twaugh@redhat.com> - 1.0.11-1
- 1.0.11.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 29 2010 David Malcolm <dmalcolm@redhat.com> - 1.0.10-3
- rework python3 DSO name for PEP 3149, and rebuild for newer python3

* Wed Nov 17 2010 Jiri Popelka <jpopelka@redhat.com> - 1.0.10-2
- Fixed rpmlint errors/warnings (#648987)
- doc subpackage

* Mon Nov 01 2010 Jiri Popelka <jpopelka@redhat.com> - 1.0.10-1
- Initial RPM spec file
