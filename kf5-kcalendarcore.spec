#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeframever	5.249.0
%define		qtver		5.15.2
%define		kfname		kcalendarcore
Summary:	kcalendarcore
Name:		kf5-%{kfname}
Version:	5.249.0
Release:	0.1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/unstable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	0d8ca6054e4fd3193f920781a6771e94
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel
BuildRequires:	Qt6Test-devel >= 5.9.0
BuildRequires:	cmake >= 3.16.0
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	libical-devel >= 2.0
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qtver}
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
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON

%ninja_build -C build

%if %{with tests}
%ninja_build -C build test
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%ghost %{_libdir}/libKF6CalendarCore.so.6
%attr(755,root,root) %{_libdir}/libKF6CalendarCore.so.5.*.*
%{_datadir}/qlogging-categories6/kcalendarcore.categories
%{_datadir}/qlogging-categories6/kcalendarcore.renamecategories

%files devel
%defattr(644,root,root,755)
%{_libdir}/cmake/KF6CalendarCore
%{_libdir}/libKF6CalendarCore.so
%{_includedir}/KF6/KCalendarCore
%{_pkgconfigdir}/KF6CalendarCore.pc
