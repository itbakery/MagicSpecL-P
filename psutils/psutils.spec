Summary: PostScript Utilities
Summary(zh_CN.UTF-8): 与 PostScript 文档一起使用的工具。
Name: psutils
Version: 1.17
Release: 30%{?dist}
License: distributable
Group: Applications/Publishing
Group(zh_CN.UTF-8): 应用程序/出版
Source: ftp://ftp.dcs.ed.ac.uk/pub/ajcd/psutils-p17.tar.gz
Patch0: psutils-p17-Makefile.patch
Patch1: psutils-p17-misc.patch
Patch2: psutils-p17-paper.patch
Patch3: psutils-p17-strip.patch
Patch4: psutils-manpage.patch
Patch5: psutils-psmerge.patch
BuildRoot: %{_tmppath}/psutils-root

%description
This archive contains some utilities for manipulating PostScript documents.
Page selection and rearrangement are supported, including arrangement into
signatures for booklet printing, and page merging for n-up printing.

%description -l zh_CN.UTF-8
该软件包包括用来处理 PostScript 文档的工具。支持的功能包括：页码的选择和重
排，把页码排为签名用于手册打印和页码合并。

%prep
%setup -q -n psutils
%patch0 -p1 -b .makefile
%patch1 -p1 -b .misc
%patch2 -p1 -b .paper
%patch3 -p1 -b .strip
%patch4 -p1 -b .manpage
%patch5 -p1 -b .new

%build
make -f Makefile.unix RPM_OPT_FLAGS="$RPM_OPT_FLAGS"
 
%install
rm -rf $RPM_BUILD_ROOT

make -f Makefile.unix \
        MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
        DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644, root, root, 0755)
%doc README LICENSE
%attr(0755, root, root) /usr/bin/*
%{_mandir}/*/*
/usr/lib/psutils

%changelog
* Wed Jan 25 2012 Liu Di <liudidi@gmail.com> - 1.17-30
- 为 Magic 3.0 重建

* Tue Oct 10 2006 Liu Di <liudidi@gmail.com> - 1.17-26mgc
- rebuild for Magic

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.17-26.1
- rebuild

* Mon Jun 12 2006 Jitka Kudrnacova <jkudrnac@redhat.com> - 1.17-26
- new implementation of psmerge by Peter Williams

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.17-25.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.17-25.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Mar 16 2005 Tim Waugh <twaugh@redhat.com> 1.17-25
- Rebuild for new GCC.

* Mon Jan 10 2005 Tim Waugh <twaugh@redhat.com> 1.17-24
- Manpage correction for psresize (bug #144582).

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jun 17 2003 Tim Waugh <twaugh@redhat.com> 1.17-21
- Rebuilt.

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Dec 11 2002 Tim Powers <timp@redhat.com> 1.17-18
- rebuild on all arches

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Jun 20 2002 Than Ngo <than@redhat.com> 1.17-16
- Don't forcibly strip binaries

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Jul 19 2001 Than Ngo <than@redhat.com> 1.17-13
- add patch from enrico.scholz@informatik.tu-chemnitz.de

* Fri Jul 13 2001 Than Ngo <than@redhat.com> 1.17-12
- media size as letter (Bug #48831)
- Copyright->License
- don't hardcode manpath

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Fri Dec  8 2000 Tim Powers <timp@redhat.com>
- built for dist-7.1

* Mon Jul 24 2000 Prospector <prospector@redhat.com>
- rebuilt

* Mon Jul 10 2000 Tim Powers <timp@redhat.com>
- rebuilt

* Mon Jul 03 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Fri May 26 2000 Tim Powers <timp@redhat.com>
- man pages in /usr/share/man (FHS compliant location)
- grabbed spec from contrib
- initial build for Powertools

* Wed May 12 1999 Peter Soos <sp@osb.hu>
- Corrected the file and directory attributes to rebuild the package
  under RedHat Linux 6.0

* Fri Dec 25 1998 Peter Soos <sp@osb.hu>
- Corrected the file and directory attributes

* Tue Jun 23 1998 Peter Soos <sp@osb.hu>
- Using %attr for ability to rebuild the package as an ordinary user.

* Wed Jun 04 1997 Timo Karjalainen <timok@iki.fi>
- Reverted back to un-gzipped man-pages (Redhat style)
- Added patch to compile everything cleanly
- Some minor changes to specfile

* Thu Mar 27 1997 Tomasz K硂czko <kloczek@rudy.mif.pg.gda.pl>
  - new version:
    Patchlevel 17 had some minor bugfixes and improvements
    - Trailer information now put before %%EOF comments if no %%Trailer
    - psselect can now add blank pages.
    - Piped input works in Linux
    - spec file rewrited for using Buildroot,
    - man pages gziped.
