%define		kdeframever	5.83
%define		qtver		5.9.0
%define		kfname		kcalendarcore
Summary:	kcalendarcore
Name:		kf5-%{kfname}
Version:	5.83.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	64aa0fdc8f79981406292ec97cd8377c
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Test-devel >= 5.9.0
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	libical-devel >= 2.0
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Obsoletes:	ka5-kcalcore < 20.12.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library provides access to and handling of calendar data. It
supports the standard formats iCalendar and vCalendar and the group
scheduling standard iTIP.

A calendar contains information like incidences (events, to-dos,
journals), alarms, time zones, and other useful information. This API
provides access to that calendar information via well known calendar
formats iCalendar (or iCal) and the oolder vCalendar.

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	ka5-kcalcore-devel < 20.12.3

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%ghost %{_libdir}/libKF5CalendarCore.so.5
%attr(755,root,root) %{_libdir}/libKF5CalendarCore.so.5.*.*
%{_datadir}/qlogging-categories5/kcalendarcore.categories
%{_datadir}/qlogging-categories5/kcalendarcore.renamecategories

%files devel
%defattr(644,root,root,755)
%{_libdir}/cmake/KF5CalendarCore
%{_libdir}/libKF5CalendarCore.so
%{_libdir}/qt5/mkspecs/modules/qt_KCalendarCore.pri
%{_includedir}/KF5/kcalcore_version.h
%{_includedir}/KF5/KCalendarCore
%{_includedir}/KF5/kcalendarcore_version.h
