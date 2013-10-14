Summary: Orocos Toolchain for component-based sofware development
Name: orocos_toolchain
Version: 2.6.9
Release: 1%{?dist}
License: GPL+linking exception
Group: Development/Tools
URL: http://www.orocos.org/toolchain
Source0: orocos-toolchain.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel, readline-devel
BuildRequires: boost-devel
BuildRequires: lua-devel
BuildRequires: cmake, catkin
BuildRequires: ruby, ruby-devel
BuildRequires: ros-groovy-core
Requires:      boost, ncurses, readline, ruby, lua, ros-groovy-core, gccxml
Provides:      orocos-toolchain = %{version}-%{release} 

%define __find_provides %{nil}

%description
Orocos Toolchain including RTT, OCL, typelib and log4cxx

%prep
%setup -q -c
shopt -s extglob
mkdir src && mv !(src) src

source /opt/ros/groovy/setup.bash
wstool init src

%build
#source /opt/ros/groovy/setup.bash
#catkin_make_isolated --install-space /opt/ros/groovy

%install
source /opt/ros/groovy/setup.bash
#find ./build_isolated -type f -name CMakeCache.txt | xargs rm
mkdir -p ${RPM_BUILD_ROOT}/opt/ros/groovy
cp /opt/ros/groovy/env.sh ${RPM_BUILD_ROOT}/opt/ros/groovy
cp /opt/ros/groovy/setup.sh ${RPM_BUILD_ROOT}/opt/ros/groovy/setup.sh
cp /opt/ros/groovy/_setup_util.py ${RPM_BUILD_ROOT}/opt/ros/groovy/_setup_util.py
DESTDIR=${RPM_BUILD_ROOT} catkin_make_isolated --force-cmake --install --install-space /opt/ros/groovy
rm ${RPM_BUILD_ROOT}/opt/ros/groovy/env.sh
rm ${RPM_BUILD_ROOT}/opt/ros/groovy/setup.sh
rm ${RPM_BUILD_ROOT}/opt/ros/groovy/_setup_util.py
export QA_SKIP_BUILD_ROOT=1

%clean
rm -rf $RPM_BUILD_ROOT


%files
/opt/ros/groovy


%changelog
* Fri Oct 11 2013 Ruben Smits <ruben.smits@intermodalics.eu> - 2.6.9-1
- Updated to use groovy and the latest catkin branch

* Thu Aug 23 2012 Ruben Smits <ruben.smits@intermodalics.eu> - iter-1.1
- Updated env.sh and added to /etc/profile.d

* Tue Aug 21 2012 Ruben Smits <ruben.smits@intermodalics.eu> - iter-1
- Initial build.
