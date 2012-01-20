Name:           perl-Tree-DAG_Node
Version:        1.06
Release:        6%{?dist}
Summary:        Class for representing nodes in a tree
Summary(zh_CN.UTF-8): 表示树中结点的类

Group:          Development/Libraries
Group(zh_CN.UTF-8):	开发/库
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Tree-DAG_Node/
Source0:        http://search.cpan.org/CPAN/authors/id/C/CO/COGENT/Tree-DAG_Node-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This class encapsulates/makes/manipulates objects that represent nodes
in a tree structure. The tree structure is not an object itself, but
is emergent from the linkages you create between nodes.  This class
provides the methods for making linkages that can be used to build up
a tree, while preventing you from ever making any kinds of linkages
which are not allowed in a tree (such as having a node be its own
mother or ancestor, or having a node have two mothers).

%description -l zh_CN.UTF-8
表示树中结点的类

%prep
%setup -q -n Tree-DAG_Node-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc ChangeLog README
%{perl_vendorlib}/Tree/
%{_mandir}/man3/*.3pm*


%changelog
* Fri Jan 20 2012 Liu Di <liudidi@gmail.com> - 1.06-6
- 为 Magic 3.0 重建


