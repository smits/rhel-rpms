Summary: common_msgs contains messages that are widely used by other ROS packages.
Name: ros-hydro-common-msgs
Version: 1.10.2
Release: 0%{?dist} 
License: BSD
Group: Development/Tools 
URL: http://wiki.ros.org/common_msgs
Source0:%name-%version.tar.bz2

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ros-hydro-core
Requires:      ros-hydro-core
Provides:      ros-hydro-common-msgs = %{version}-%{release} 

%description
common_msgs contains messages that are widely used by other
ROS packages. These includes messages for actions (actionlib_msgs),
diagnostics (diagnostic_msgs), geometric primitives (geometry_msgs),
robot navigation (nav_msgs), and common sensors (sensor_msgs), such as
laser range finders, cameras, point clouds.  

%prep
%setup -q -c
source /opt/ros/hydro/setup.bash

%build
catkin_make -DCMAKE_INSTALL_PREFIX=/opt/ros/hydro

%install
source /opt/ros/hydro/setup.bash
DESTDIR=%buildroot catkin_make install -DCMAKE_INSTALL_PREFIX=/opt/ros/hydro

%clean
rm -rf $RPM_BUILD_ROOT


%files
/opt/ros/hydro

%changelog
* Tue Oct 15 2013 Ruben Smits <ruben@intemodalics.eu> - 1.10.2-0
- Initial built

