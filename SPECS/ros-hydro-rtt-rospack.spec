Summary: rtt_rospack is a RTT service for the rospack functionality
Name: ros-hydro-rtt-rospack
Version: 2.6.0
Release: 0%{?dist} 
License: BSD
Group: Development/Tools 
URL: http://wiki.ros.org/rtt_rospack
Source0:rtt_rospack.tar.bz2

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ros-hydro-core
Requires:      ros-hydro-core, orocos-toolchain
Provides:      ros-hydro-rtt-rospack = %{version}-%{release} 

%define __find_requires %{nil}

%description
rtt_rospack is a RTT service for the rospack functionality

%prep
%setup -q -c -T
mkdir src
pushd src
tar -xf %SOURCE0
popd
source /opt/ros/hydro/setup.bash

%build
catkin_make -DCMAKE_INSTALL_PREFIX=/opt/ros/hydro

%install
source /opt/ros/hydro/setup.bash
DESTDIR=%buildroot catkin_make install -DCMAKE_INSTALL_PREFIX=/opt/ros/hydro

%clean
rm -rf $RPM_BUILD_ROOT

%files
%define _unpackaged_files_terminate_build 0
/opt/ros/hydro/lib
/opt/ros/hydro/share

%changelog
* Mon Oct 28 2013 Ruben Smits <ruben@intemodalics.eu> - 2.6.0-0
- Initial built

