Name:           ros-hydro-core
Version:        1.9.50
Release:        2%{?dist}
Summary:        ROS Bare Bones

Group:          devel
License:        BSD
URL:            www.ros.org
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Source0:        ros-hydro-core.tar.bz2
Patch0:		ros-hydro-core.patch

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
BuildRequires:  tinyxml-devel
BuildRequires:  bzip2
BuildRequires:  pkgconfig
BuildRequires:  gtest-devel
BuildRequires:  log4cxx-devel
BuildRequires:  coreutils
BuildRequires:  python27-dateutil
BuildRequires:  cmake

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
Requires:  log4cxx
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
find ./src -type f | xargs sed -i '/^#!/{s/python$/python2.7/}'
%patch0 -p1

%build
#unset ROS_DISTRO
#unset ROS_PACKAGE_PATH
#unset ROS_ROOT
#src/catkin/bin/catkin_make_isolated --install-space /opt/ros/hydro

%install
unset ROS_DISTRO
unset ROS_PACKAGE_PATH
unset ROS_ROOT
#cleanup cmakecache
#find ./build_isolated -type f -name CMakeCache.txt | xargs rm
DESTDIR=$RPM_BUILD_ROOT src/catkin/bin/catkin_make_isolated --force-cmake --install --install-space /opt/ros/hydro
#cleanup paths
find $RPM_BUILD_ROOT -type f -name '*.hpp' -o -name '*.cmake' -o -name '*.h' -o -name '*.txt' -o -name '*.sh' -o -name '*.py' | xargs sed -i "s|$RPM_BUILD_ROOT||"
sed -i "s|$RPM_BUILD_ROOT||" $RPM_BUILD_ROOT/opt/ros/hydro/_setup_util.py 
mkdir -p %buildroot/etc/profile.d
ln -s /opt/ros/hydro/setup.sh %buildroot/etc/profile.d/ros.sh
export QA_SKIP_BUILD_ROOT=1

%clean
rm -rf $RPM_BUILD_ROOT

%files
#%defattr(-,root,root,-)
%doc
/opt/ros/hydro
/etc/profile.d/ros.sh

%changelog
* Mon Oct 28 2013 Ruben Smits <ruben@intermodalics.eu> - 1.9.50-2
- add ros setup to the standard shell setup

* Tue Oct 15 2013 Ruben Smits <ruben@intermodalics.eu> - 1.9.50-1
- rebuilt

* Thu Sep 12 2013 Ruben Smits <ruben@intermodalics.eu> - 1.9.48-1
- Initial RPM release


