Summary: common_msgs contains messages that are widely used by other ROS packages.
Name: ros-hydro-orocos-kdl
Version: 1.1.102
Release: 0%{?dist} 
License: BSD
Group: Development/Tools 
URL: http://wiki.ros.org/common_msgs
Source0:%name.tar.bz2

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ros-hydro-core
Requires:      ros-hydro-core
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
* Tue Oct 15 2013 Ruben Smits <ruben@intemodalics.eu> - 1.1.102-0
- Initial built

