#---------------------------------------------------------------
# Project         : Mandriva Linux
# Module          : dynamic
# File            : dynamic.spec
# Version         : $Id: dynamic.spec 223977 2007-06-26 00:13:24Z adamw $
# Author          : Frederic Lepied and others
# Created On      : Wed Aug  8 11:32:16 2001
# License         : GPL
# Purpose         : spec file to build an rpm
#---------------------------------------------------------------

%define name dynamic
%define version 0.26.17
%define release %mkrel 8

Summary: Scripts to automatically set up peripherals when plugged in 
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: System/Configuration/Other
URL: http://www.mandrivalinux.com/
Requires: psmisc, mount, usbutils
# scannerdrake --dynamic
Conflicts: drakxtools <= 10.1-0.22mdk
Conflicts: kdemultimedia-kscd <= 1:3.3.2-13mdk
BuildArchitectures: noarch
BuildRoot: %{_tmppath}/%{name}-buildroot

%description
Scripts to automatically set up peripherals when plugged in (mainly
USB devices). This means adding desktop icons (KDE, GMOME) to access
scanners, digital cameras, storage devices, ... adding print queues
for printers, and so on.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

# no longer provides any launcher
rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/dynamic/launchers/*

#all system scripts are obsolete
rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/dynamic/scripts/{camera,lp,rawdevice,rio500,scanner,visor,webcam,part}.script

# hooks are obsolete
rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/dynamic/hooks/*

# kill udev rules
rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/udev

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog AUTHORS
%dir %{_sysconfdir}/dynamic
%dir %{_sysconfdir}/dynamic/scripts
%dir %{_sysconfdir}/dynamic/user-scripts
%dir %{_sysconfdir}/dynamic/hooks
%{_sysconfdir}/dynamic/scripts/*.script
%{_sysconfdir}/dynamic/user-scripts/*.script
%_datadir/dynamic

# DON'T ADD SOURCE OR PATCH, USE SVN DIRECTLY


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.26.17-6mdv2011.0
+ Revision: 663900
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 0.26.17-5mdv2011.0
+ Revision: 604837
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.26.17-4mdv2010.1
+ Revision: 522567
- rebuilt for 2010.1

* Mon Oct 05 2009 Frederic Crozat <fcrozat@mandriva.com> 0.26.17-3mdv2010.0
+ Revision: 454119
- Drop all system scripts and udev rules

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.26.17-2mdv2010.0
+ Revision: 413416
- rebuild

* Wed Mar 25 2009 Frederic Crozat <fcrozat@mandriva.com> 0.26.17-1mdv2009.1
+ Revision: 361042
- Release 0.26.17 :
 - disable icon on desktop by default now (Mdv bug #45887)

* Tue Mar 03 2009 Frederic Crozat <fcrozat@mandriva.com> 0.26.16-1mdv2009.1
+ Revision: 347986
- Release 0.26.16 :
 - create .desktop files with 755 rights

* Tue Sep 02 2008 Olivier Blin <oblin@mandriva.com> 0.26.15-1mdv2009.0
+ Revision: 279102
- 0.26.15
- add XFce support (from tpg, #39960)

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.26.14-2mdv2009.0
+ Revision: 220714
- rebuild

* Wed Jan 23 2008 Olivier Blin <oblin@mandriva.com> 0.26.14-1mdv2008.1
+ Revision: 157196
- 0.26.14
- add iPod script (from Goetz Waschk, #35999)

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 0.26.13-2mdv2008.1
+ Revision: 149685
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Sep 13 2007 Olivier Blin <oblin@mandriva.com> 0.26.13-1mdv2008.0
+ Revision: 85121
- 0.26.13 (fix udev rules)

* Mon Sep 10 2007 Olivier Blin <oblin@mandriva.com> 0.26.12-1mdv2008.0
+ Revision: 84241
- 0.26.12
- fork udev scripts not to hang udevd (#30530)

* Tue Jun 26 2007 Adam Williamson <awilliamson@mandriva.org> 0.26.11-1mdv2008.0
+ Revision: 44289
- new release 0.26.11; rebuild for 2008
- Import dynamic



* Thu Sep 07 2006 Frederic Crozat <fcrozat@mandriva.com> 0.26.10-1mdv2007.0
- Add more applications to user scripts

* Wed Aug 30 2006 Frederic Crozat <fcrozat@mandriva.com> 0.26.9-1mdv2007.0
- Add f-spot as default digicam importer for GNOME

* Thu Aug 24 2006 Olivier Blin <oblin@mandriva.com> 0.26.8-1mdv2007.0
- remove X11R6 path (#22959)

* Fri Apr 21 2006 Till Kamppeter <till@mandriva.com> 0.26.7-1mdk
- lp.script: Let re-enabling disabled CUPS queues being done by
  printerdrake.

* Thu Apr 20 2006 Till Kamppeter <till@mandriva.com> 0.26.6-1mdk
- lp.script: Make Plug-n-Print (auto queue setup on plugging USB printers)
  also working with CUPS 1.2.
- lp.script: Updated info in the header comments.
- Updated summary and description of the package.
- Introduced %%mkrel.

* Thu Feb 16 2006 Frederic Crozat <fcrozat@mandriva.com> 0.26.5-1mdk
- Update video_dvd script to call totem directly without changing its
  configuration

* Thu Dec 29 2005 Olivier Blin <oblin@mandriva.com> 0.26.4-1mdk
- fill undefined environment variables (ACTION and DEVNAME) with command
  line options (don't superseed environment with command line options,
  since some scripts are directly called by udev, with different options)
- kill devfs stuff
- fix 60-dynamic.rules permissions
- visor script (Frederic Crozat): don't create pilot symlink in /

* Mon Dec 26 2005 Olivier Blin <oblin@mandriva.com> 0.26.3-1mdk
- make command line options superseed environment (ACTION and DEVNAME variables)

* Thu Sep  1 2005 Olivier Blin <oblin@mandriva.com> 0.26.2-1mdk
- really handle command-line arguments in system scripts

* Thu Aug 18 2005 Frederic Lepied <flepied@mandriva.com> 0.26.1-1mdk
- fixed udev rule for pilots, removed udev rule for scanners
- fixed typo in functions.script

* Tue Aug 16 2005 Till Kamppeter <till@mandriva.com> 0.26-2mdk
- lp.script: Do not auto-enable print queues by default, as with
  new CUPS backend wrapper they do not get automatically disabled.
- lp.script: Do auto setup for printers also if CUPS is not installed
  (CUPS will be installed then if user agrees).

* Mon Aug  8 2005 Thierry Vignaud <tvignaud@mandriva.com> 0.26-1mdk
- convert from slow shell spawner dev.d scheme to fast event udev
  rules (no more fork bomb) (#15371)
- status: lp, visor & webcam were tested; scanner is definitively
  broken by kernel->userland switch

* Wed Jul 27 2005 Till Kamppeter <till@mandriva.com> 0.25-4mdk
- Mandrake --> Mandriva

* Wed Jul 27 2005 Till Kamppeter <till@mandrakesoft.com> 0.25-3mdk
- Updated lp.script for configurable queue re-enabling and auto queue
  setup 

* Thu Apr 07 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 0.25-2mdk 
- Update digicam.script to detect if kio_kamera is available

* Mon Feb 28 2005 Olivier Blin <oblin@mandrakesoft.com> 0.25-1mdk
- don't try to run part.script for removable devices
- from Laurent Montel, video_dvd.script:
  o add -p DVD to autoplay DVD (thanks to Nicolas Chipaux)
  o add missing argument "--device" (Buchan Milne, #12930)

* Thu Feb 17 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 0.24-1mdk 
- Improve digicam script for mass storage digicam (Fedora)
- Don't ship part.scripts, it is now handled by HAL and gnome-volume-manager

* Fri Feb 11 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 0.23-1mdk 
- Add digicam script
- from Laurent Montel, audio_cd.script:
  o user-scripts/audio_cd.script: Adapt to new kscd parameter (#12845)

* Mon Sep 13 2004 Frederic Lepied <flepied@mandrakesoft.com> 0.21-1mdk
- wait while file system is read only in scripts called from udev
- use lsusb to find device name

* Fri Sep 10 2004 Frederic Lepied <flepied@mandrakesoft.com> 0.20-1mdk
- fixed tvtuner detection in kernel 2.6 (bug #9263)
- use $devicename as a descriptive text and let $device be the name of
the special file for dynamic desktop entries.

* Tue Sep  7 2004 Frederic Lepied <flepied@mandrakesoft.com> 0.19-1mdk
- part.script: mount even in non supermount mode as we put the 'users' option

* Thu Aug 26 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.18-1mdk
- Fix visor script to link /dev/pilot based on productID or VISOR_SWAP
  value in /etc/sysconfig/usb (Mdk bug #3381)

* Wed Aug 25 2004 Frederic Lepied <flepied@mandrakesoft.com> 0.17-1mdk
- launch kscd with --device (bug #10747)

* Tue Aug 24 2004 Robert Vojta <robert.vojta@mandrakesoft.org> 0.16-2mdk
- added missing "" (#10899)

* Mon Aug 23 2004 Frederic Lepied <flepied@mandrakesoft.com> 0.16-1mdk
- if there is no queue for a printer, run the automatic queue setup of
printerdrake (Till)

* Thu Aug 19 2004 Frederic Lepied <flepied@mandrakesoft.com> 0.15-1mdk
- enable a disabled cups queue on an add event (Till)

* Thu Aug 19 2004 Frederic Lepied <flepied@mandrakesoft.com> 0.14-1mdk
- udev support
- try to find a better device name via sysfs

* Thu Aug  5 2004 Frederic Lepied <flepied@mandrakesoft.com> 0.13-1mdk
- video_dvd.script: corrected totem test
                    launch kaffeine
- lp.script: take the needed actions for cups and hpoj (Till)

* Thu Jul 29 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.12.8-1mdk
- Launch nautilus-cd-burner in browser mode 

* Tue Jun  1 2004 Frederic Lepied <flepied@mandrakesoft.com> 0.12.7-1mdk
- fix webcam detection under 2.6 kernels (Sir Pingus) [anthill #865, bugzilla #9263]

* Fri Apr 23 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.12.6-1mdk
- Allow several DVD drive to be used with totem

* Mon Mar 29 2004 Frederic Lepied <flepied@mandrakesoft.com> 0.12.5-1mdk
- scanner.script: only call scannerdrake on add event

* Fri Mar 12 2004 Frederic Lepied <flepied@mandrakesoft.com> 0.12.4-1mdk
- video_dvd.script: use dvd: as totem argument

* Tue Mar  2 2004 Frederic Lepied <flepied@mandrakesoft.com> 0.12.3-1mdk
- use pidof in GNOME test

* Sat Feb 28 2004 Frederic Lepied <flepied@mandrakesoft.com> 0.12.2-1mdk
- corrected GNOME detection in user-scripts (bug #8175)
- launch k3b only once

* Thu Feb 19 2004 Frederic Lepied <flepied@mandrakesoft.com> 0.12.1-1mdk
- use the right parameter to launch totem in video_dvd.script

* Tue Feb 10 2004 Frederic Lepied <flepied@mandrakesoft.com> 0.12-1mdk
- allow to override the default applications launched by magicdev
in ~/.dynamic and /etc/dynamic/user-scripts/config by setting the
audio_cd_launcher, blank_cd_launcher and video_dvd_launcher shell
variables.

* Tue Feb  3 2004 Frederic Lepied <flepied@mandrakesoft.com> 0.11.1-1mdk
- rebuild to fix audio_cd.script (launch kscd without argument)
- rawdevice.script fix (Andrey Borzenkov)

* Fri Jan 30 2004 Frederic Lepied <flepied@mandrakesoft.com> 0.11-1mdk
- add user-scripts to be launched by magicdev

* Tue Jul  1 2003 Frederic Lepied <flepied@mandrakesoft.com> 0.10-1mdk
- create desktop files with the _dynamic.desktop suffix

* Thu Mar  6 2003 Frederic Lepied <flepied@mandrakesoft.com> 0.9-1mdk
- let kde handle dynamic icons for removable devices by itself

* Wed Feb 19 2003 Frederic Lepied <flepied@mandrakesoft.com> 0.8.1-1mdk
- change device to group usb in scanner script

* Mon Feb 17 2003 Frederic Lepied <flepied@mandrakesoft.com> 0.8-1mdk
- prevent dynamic scripts from starting while / is mounted ro (bug #1563)

* Fri Aug 30 2002 Frederic Lepied <flepied@mandrakesoft.com> 0.7-1mdk
- activate part with drakupdate_fstab

* Mon Aug 19 2002 Pixel <pixel@mandrakesoft.com> 0.6-4mdk
- drop require kudzu (since that's harddrake which provides it and it doesn't provide updfstab)

* Mon Aug 19 2002 Frederic Lepied <flepied@mandrakesoft.com> 0.6-3mdk
- create files in 644 mode
- removed source1 and put it directly in tar ball

* Sat Aug 17 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.6-2mdk
- Source1 : add devfs support

* Tue Aug 13 2002 Frederic Lepied <flepied@mandrakesoft.com> 0.6-1mdk
- added support for camera
- added $basename support in templates (basename of the device name).

* Mon Jul 29 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 0.5-4mdk
- Fix menu entries for rio500 support
- gnome.hook: dynamic entries are now in /var/lib/gnome/desktop

* Sat Jul 20 2002 Pixel <pixel@mandrakesoft.com> 0.5-3mdk
- rawdevice.script: created, useful to bind a dynamic device to a rawdevice

* Mon Mar 11 2002 Frederic Lepied <flepied@mandrakesoft.com> 0.5-2mdk
- lp.script: change permission/owner/group of /dev/ptal-printd/* (Till).

* Mon Nov 19 2001 Frederic Lepied <flepied@mandrakesoft.com> 0.5-1mdk
- scanner.script: call scannerdrake

* Mon Oct 22 2001 Frederic Lepied <flepied@mandrakesoft.com> 0.4-8mdk
- lp.script: change permission/owner/group of /dev/oki4drv (Till).

* Fri Sep 21 2001 Frederic Lepied <flepied@mandrakesoft.com> 0.4-7mdk
- lp.script: fix permissions of printer devices according to what is installed.

* Fri Sep 21 2001 Frederic Lepied <flepied@mandrakesoft.com> 0.4-6mdk
- use DYNAMIC=no in /etc/sysconfig/system to disable completely
- check that / is rw in all scripts

* Mon Sep 17 2001 Frederic Lepied <flepied@mandrakesoft.com> 0.4-5mdk
- added a way to deactivate dynamic support by adding a DYNAMIC_$name=no
in /etc/sysconfig/system.
- fixed check of / ro to avoid catching errors=continue (Borsenkow Andrej).

* Sun Sep 16 2001 Frederic Lepied <flepied@mandrakesoft.com> 0.4-4mdk
- part.script: more robust by checking if / is rw and testing before
unmounting (Borsenkow Andrej).

* Sun Sep 16 2001 Frederic Lepied <flepied@mandrakesoft.com> 0.4-3mdk
- run part.script only when whe are not anymore in rc.sysinit.

* Sat Sep 15 2001 Frederic Lepied <flepied@mandrakesoft.com> 0.4-2mdk
- add part launcher for kde.
- visor script make the symlink to /dev/pilot

* Thu Sep 13 2001 Frederic Lepied <flepied@mandrakesoft.com> 0.4-1mdk
- added part.script

* Wed Sep 12 2001 Frederic Lepied <flepied@mandrakesoft.com> 0.3-3mdk
- lanchers are provided by packages themselves.

* Thu Sep  6 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 0.3-2mdk
- Add support for gnome

* Tue Aug 28 2001 Frederic Lepied <flepied@mandrakesoft.com> 0.3-1mdk
- removed unneeded messages when a desktop isn't installed.
- call pam_console_apply before running the desktop hooks.

* Sat Aug 25 2001 Frederic Lepied <flepied@mandrakesoft.com> 0.2-1mdk
- added kde hook for webcam (lmontel)

* Thu Aug  2 2001 Frederic Lepied <flepied@mandrakesoft.com> 0.1-1mdk
- first version

# dynamic.spec ends here
