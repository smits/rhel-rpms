Name:           ros-groovy-core
Version:        1.9.48
Release:        1%{?dist}
Summary:        ROS Bare Bones

Group:          devel
License:        BSD
URL:            www.ros.org
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Source0:        ros-groovy-core.tar.gz

BuildRequires:  python27
BuildRequires:  python27-devel
BuildRequires:  python27-setuptools
BuildRequires:  python27-rosinstall-generator
BuildRequires:  python27-wstool
BuildRequires:  python27-rosdep
BuildRequires:  python27-rosinstall
BuildRequires:  python27-rospkg
BuildRequires:  python27-catkin-pkg
BuildRequires:  python27-empy
BuildRequires:  python27-netifaces
BuildRequires:  boost-devel
BuildRequires:  libstdc++
BuildRequires:  glibc
BuildRequires:  tinyxml
BuildRequires:  bzip2
BuildRequires:  pkgconfig
BuildRequires:  gtest
BuildRequires:  coreutils
BuildRequires:  python27-dateutil


Requires:  python27
Requires:  boost
Requires:  boost-date-time
Requires:  boost-filesystem
Requires:  boost-program-options
Requires:  boost-system
Requires:  boost-regex
Requires:  boost-signals
Requires:  boost-thread
Requires:  libstdc++
Requires:  glibc
Requires:  tinyxml
Requires:  bzip2
Requires:  pkgconfig
Requires:  gtest
Requires:  boost
Requires:  coreutils
Requires:  python27-rosdep
Requires:  python27-wstool
Requires:  python27-rosinstall
Requires:  python27-rospkg
Requires:  python27-catkin-pkg
Requires:  python27-empy
Requires:  python27-netifaces
Requires:  python27-dateutil

%description
ROS (Robot Operating System) provides libraries and tools to help software developers create robot applications. It provides hardware abstraction, device drivers, libraries, visualizers, message-passing, package management, and more. ROS is licensed under an open source, BSD license. This package only contains the Bare Bones: ROS package, build, and communication libraries. No GUI tools.

%prep
%setup -q -c -n %{name}-%{version}
#fix shebang lines
find ./src -type f | xargs sed -i '/^#!/{s/python^{[0-9].[0-9]}/python2.7/}'


%build
unset ROS_DISTRO
unset ROS_PACKAGE_PATH
unset ROS_ROOT
src/catkin/bin/catkin_make_isolated --install-space /opt/ros/groovy

%install
unset ROS_DISTRO
unset ROS_PACKAGE_PATH
unset ROS_ROOT
#cleanup cmakecache
find ./build_isolated -type f -name CMakeCache.txt | xargs rm
DESTDIR=$RPM_BUILD_ROOT src/catkin/bin/catkin_make_isolated --force-cmake --install --install-space /opt/ros/groovy
#cleanup paths
#find $RPM_BUILD_ROOT -type f -name *.h -name *.txt -name *.sh -name *.py | xargs sed -i "s|$RPM_BUILD_ROOT||"
sed -i "s|$RPM_BUILD_ROOT||" $RPM_BUILD_ROOT/opt/ros/groovy/_setup_util.py 
export QA_SKIP_BUILD_ROOT=1

%clean
rm -rf $RPM_BUILD_ROOT

%files
#%defattr(-,root,root,-)
%doc
/opt/ros/groovy/*
/opt/ros/groovy/.*

%changelog
* Thu Sep 12 2013 Ruben Smits <ruben@intermodalics.eu> - 1.9.48-1
- Initial RPM release


