Name:		netxen-firmware
Summary:	QLogic Linux Intelligent Ethernet (3000 and 3100 Series) Adapter Firmware
Version:	4.0.534
Release:	4%{?dist}
License:	Redistributable, no modification permitted
Group:		System Environment/Kernel
Source0:	ftp://ftp.qlogic.com/outgoing/linux/firmware/netxen_nic/phanfw.bin
Source1:	ftp://ftp.qlogic.com/outgoing/linux/firmware/netxen_nic/LICENCE.phanfw
URL:		ftp://ftp.qlogic.com/outgoing/linux/firmware/netxen_nic/
BuildArch:	noarch
Requires:	udev

%description
QLogic Linux Intelligent Ethernet (3000 and 3100 Series) Adapter Firmware.

%prep
%setup -n %{name} -c -T
cp %{SOURCE0} .
cp %{SOURCE1} .

%build
# Firmware, do nothing.

%install
mkdir -p %{buildroot}/lib/firmware/
install -m0644 phanfw.bin %{buildroot}/lib/firmware/

%files
%defattr(-,root,root,-)
%doc LICENCE.phanfw
/lib/firmware/phanfw.bin

%changelog
* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.534-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 23 2010 Tom Callaway <spot@fedoraproject.org> - 4.0.534-3
- new LICENCE.phanfw
- add Requires: udev

* Mon Dec 13 2010 Tom Callaway <spot@fedoraproject.org> - 4.0.534-2
- update urls

* Mon Dec  6 2010 Tom Callaway <spot@fedoraproject.org> - 4.0.534-1
- initial package
