Summary: common_msgs contains messages that are widely used by other ROS packages.
Name: ros-hydro-orocos-kdl
Version: 1.1.102
Release: 1%{?dist} 
License: BSD
Group: Development/Tools 
URL: http://wiki.ros.org/common_msgs
Source0:%name.tar.bz2

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ros-hydro-core
BuildRequires: eigen3

Requires:      ros-hydro-core
Requires:      eigen3-devel
Provides:      ros-hydro-orocos-kdl = %{version}-%{release} 

%description
This package contains a recent version of the Kinematics and Dynamics
Library (KDL), distributed by the Orocos Project. 

%prep
%setup -q -c
source /opt/ros/hydro/setup.bash

%build

%install
source /opt/ros/hydro/setup.bash
DESTDIR=%buildroot catkin_make_isolated --install-space /opt/ros/hydro --install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%define _unpackaged_files_terminate_build 0
/opt/ros/hydro/lib
/opt/ros/hydro/share
/opt/ros/hydro/include

%changelog
* Fri Oct 18 2013 Ruben Smits <ruben@intermodalics.eu> - 1.1.102-1
- added eigen3-devel requirement

* Tue Oct 15 2013 Ruben Smits <ruben@intermodalics.eu> - 1.1.102-0
- Initial built

