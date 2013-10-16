Summary:	Scripts to automatically set up peripherals when plugged in 
Name:		dynamic
Version:	0.26.17
Release:	10
License:	GPLv2
Group:		System/Configuration/Other
Url:		http://www.mandrivalinux.com/
Source0:	%{name}-%{version}.tar.bz2
BuildArch:	noarch
Requires:	mount
Requires:	psmisc
Requires:	usbutils

%description
Scripts to automatically set up peripherals when plugged in (mainly
USB devices). This means adding desktop icons (KDE, GMOME) to access
scanners, digital cameras, storage devices, ... adding print queues
for printers, and so on.

%prep
%setup -q

%install
%makeinstall

# no longer provides any launcher
rm -rf %{buildroot}%{_sysconfdir}/dynamic/launchers/*

#all system scripts are obsolete
rm -rf %{buildroot}%{_sysconfdir}/dynamic/scripts/{camera,lp,rawdevice,rio500,scanner,visor,webcam,part}.script

# hooks are obsolete
rm -rf %{buildroot}%{_sysconfdir}/dynamic/hooks/*

# kill udev rules
rm -rf %{buildroot}%{_sysconfdir}/udev

%files
%doc ChangeLog AUTHORS
%dir %{_sysconfdir}/dynamic
%dir %{_sysconfdir}/dynamic/scripts
%dir %{_sysconfdir}/dynamic/user-scripts
%dir %{_sysconfdir}/dynamic/hooks
%{_sysconfdir}/dynamic/scripts/*.script
%{_sysconfdir}/dynamic/user-scripts/*.script
%{_datadir}/dynamic

