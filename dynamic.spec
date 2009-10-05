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
%define release %mkrel 3

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
