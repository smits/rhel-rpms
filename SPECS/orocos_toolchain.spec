Summary: Orocos Toolchain for component-based sofware development
Name: orocos_toolchain
Version: 2.7.0
Release: 2%{?dist}
License: GPL+linking exception
Group: Development/Tools
URL: http://www.orocos.org/toolchain
Source0: orocos-toolchain-2.7.0.tar.bz2
Patch0: orocos_toolchain-2.7.0.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel, readline-devel
BuildRequires: boost-devel
BuildRequires: lua-devel
BuildRequires: cmake
BuildRequires: ruby, ruby-devel, rubygem-rake
BuildRequires: ros-hydro-core
Requires:      boost, ncurses, readline, ruby, lua, ros-hydro-core, gccxml
Provides:      orocos-toolchain = %{version}-%{release} 

%define __find_provides %{nil}
%define __find_requires %{nil}

%description
Orocos Toolchain including RTT, OCL, typelib and log4cxx

%prep
%setup -q -c
%patch0 -p1
source /opt/ros/hydro/setup.bash
#wstool init src

%build
#source /opt/ros/hydro/setup.bash
#catkin_make_isolated --install-space /opt/ros/hydro

%install
source /opt/ros/hydro/setup.bash
mkdir -p %buildroot/opt/ros/hydro
cp /opt/ros/hydro/env.sh %buildroot/opt/ros/hydro
cp /opt/ros/hydro/setup.sh %buildroot/opt/ros/hydro/setup.sh
cp /opt/ros/hydro/_setup_util.py %buildroot/opt/ros/hydro/_setup_util.py
#DESTDIR=%buildroot catkin_make_isolated --install --install-space /opt/ros/hydro --cmake-args -DCMAKE_PREFIX_PATH=%buildroot/opt/ros/hydro
DESTDIR=%buildroot catkin_make_isolated --install --install-space /opt/ros/hydro
rm %buildroot/opt/ros/hydro/env.sh
rm %buildroot/opt/ros/hydro/setup.sh
rm %buildroot/opt/ros/hydro/_setup_util.py
export QA_SKIP_BUILD_ROOT=1

%clean
rm -rf $RPM_BUILD_ROOT


%files
%attr(755,root, -) /opt/ros/hydro/bin/typegen 
%attr(755,root, -) /opt/ros/hydro/bin/orogen
%attr(755,root, -) /opt/ros/hydro/bin/orogen-unregister 
/opt/ros/hydro


%changelog
* Fri Oct 28 2013 Ruben Smits <ruben.smits@intermodalics.eu> - 2.7.0-2
- Updated to use hydro and the latest catkin branch

* Fri Oct 11 2013 Ruben Smits <ruben.smits@intermodalics.eu> - 2.7.0-1
- Updated to use hydro and the latest catkin branch

* Thu Aug 23 2012 Ruben Smits <ruben.smits@intermodalics.eu> - iter-1.1
- Updated env.sh and added to /etc/profile.d

* Tue Aug 21 2012 Ruben Smits <ruben.smits@intermodalics.eu> - iter-1
- Initial build.
