%global checkout 06c8f81

Name:		linux-firmware
Version:	20120206
Release:	0.1.git%{checkout}%{?dist}
Summary:	Firmware files used by the Linux kernel

Group:		System Environment/Kernel
License:	GPL+ and GPLv2+ and MIT and Redistributable, no modification permitted
URL:		http://www.kernel.org/
Source0:	ftp://ftp.kernel.org/pub/linux/kernel/people/dwmw2/firmware/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch
Provides:	kernel-firmware = %{version} xorg-x11-drv-ati-firmware = 7.0
Obsoletes:	kernel-firmware < %{version} xorg-x11-drv-ati-firmware < 6.13.0-0.22
Obsoletes:	ueagle-atm4-firmware < 1.0-5
# The netxen firmware gets independently updated, so we'll use it instead of 
# whatever happens to be in the last checkout.
Requires:	netxen-firmware
Requires:	udev

%description
Kernel-firmware includes firmware files required for some devices to
operate.

%prep
%setup -q -n linux-firmware-%{checkout}

%build
# Remove firmware shipped in separate packages already
# Perhaps these should be built as subpackages of linux-firmware?
rm ql2???_fw.bin LICENCE.qla2xxx
rm iwlwifi-*.ucode LICENCE.iwlwifi_firmware
rm -rf ess korg sb16 yamaha
# We have _some_ ralink firmware in separate packages already.
rm rt73.bin rt2561.bin rt2561s.bin rt2661.bin
# And _some_ conexant firmware.
rm v4l-cx23418-apu.fw v4l-cx23418-cpu.fw v4l-cx23418-dig.fw v4l-cx25840.fw
# Netxen firmware
rm phanfw.bin LICENCE.phanfw

# Remove source files we don't need to install
rm -f usbdux/*dux */*.asm

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/lib/firmware
cp -r * $RPM_BUILD_ROOT/lib/firmware
rm $RPM_BUILD_ROOT/lib/firmware/{WHENCE,LICENCE.*,LICENSE.*}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc WHENCE LICENCE.* LICENSE.*
/lib/firmware/*

%changelog
* Tue Feb 07 2012 Josh Boyer <jwboyer@redhat.com>
- Update to latest upstream git snapshot.  Fixes rhbz 786937

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20110731-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Aug 04 2011 Tom Callaway <spot@fedoraproject.org> 20110731-2
- resolve conflict with netxen-firmware

* Wed Aug 03 2011 David Woodhouse <dwmw2@infradead.org> 20110731-1
- Latest firmware release with v1.3 ath9k firmware (#727702)

* Sun Jun 05 2011 Peter Lemenkov <lemenkov@gmail.com> 20110601-2
- Remove duplicated licensing files from /lib/firmware

* Wed Jun 01 2011 Dave Airlie <airlied@redhat.com> 20110601-1
- Latest firmware release with AMD llano support.

* Thu Mar 10 2011 Dave Airlie <airlied@redhat.com> 20110304-1
- update to latest upstream for radeon ni/cayman, drop nouveau fw we don't use it anymore

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20110125-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 25 2011 David Woodhouse <dwmw2@infradead.org> 20110125-1
- Update to linux-firmware-20110125 (new bnx2 firmware)

* Fri Jan 07 2011 Dave Airlie <airlied@redhat.com> 20101221-1
- rebase to upstream release + add new radeon NI firmwares.

* Thu Aug 12 2010 Hicham HAOUARI <hicham.haouari@gmail.com> 20100806-4
- Really obsolete ueagle-atm4-firmware

* Thu Aug 12 2010 Hicham HAOUARI <hicham.haouari@gmail.com> 20100806-3
- Obsolete ueagle-atm4-firmware

* Fri Aug 06 2010 David Woodhouse <dwmw2@infradead.org> 20100806-2
- Remove duplicate radeon firmwares; they're upstream now

* Fri Aug 06 2010 David Woodhouse <dwmw2@infradead.org> 20100806-1
- Update to linux-firmware-20100806 (more legacy firmwares from kernel source)

* Fri Apr 09 2010 Dave Airlie <airlied@redhat.com> 20100106-4
- Add further radeon firmwares

* Wed Feb 10 2010 Dave Airlie <airlied@redhat.com> 20100106-3
- add radeon RLC firmware - submitted upstream to dwmw2 already.

* Tue Feb 09 2010 Ben Skeggs <bskeggs@redhat.com> 20090106-2
- Add firmware needed for nouveau to operate correctly (this is Fedora
  only - do not upstream yet - we just moved it here from Fedora kernel)

* Wed Jan 06 2010 David Woodhouse <David.Woodhouse@intel.com> 20090106-1
- Update

* Fri Aug 21 2009 David Woodhouse <David.Woodhouse@intel.com> 20090821-1
- Update, fix typos, remove some files which conflict with other packages.

* Thu Mar 19 2009 David Woodhouse <David.Woodhouse@intel.com> 20090319-1
- First standalone kernel-firmware package.
