Name:           rhcs-core-system
Version:        2.0.0
Release:        0%{?dist}
Summary:        Meta package providing all packages for the rhcs-core-system

Group:          devel
License:        Mixed
URL:            www.iter.org

Provides: rhcs-core-system = %version-%release

Requires: python27-catkin-pkg = 0.1.19-1.el6
Requires: python27-dateutil = 1.5-6.el6
Requires: python27-distribute = 0.7.3-1.el6
Requires: python27-empy = 3.3-5.1
Requires: python27-nose = 1.3.0-1.el6
Requires: python27-rosdep = 0.10.21-1.el6
Requires: python27-rosdistro = 0.2.14-1.el6
Requires: python27-rosinstall = 0.6.29-1.el6
Requires: python27-rosinstall-generator = 0.1.2-1.el6
Requires: python27-rospkg = 1.0.23-1.el6
Requires: python27-vcstools = 0.1.30-1.el6
Requires: python27-wstool = 0.0.3-1.el6
Requires: rubygem-flexmock = 0.8.6-2.3
Requires: rubygem-rake = 0.8.7-2.1.el6
Requires: lua = 5.1.4-4.1.el6
Requires: lua-devel = 5.1.4-4.1.el6
Requires: orocos_toolchain = 2.7.0-2.el6
Requires: python27 = 2.7.5-1.ius.el6
Requires: python27-libs = 2.7.5-1.ius.el6
Requires: python27-netifaces = 0.8-3.1
Requires: python27-pyyaml = 3.10-1.el6
Requires: python27-setuptools = 1.1.5-2.el6
Requires: python27-test = 2.7.5-1.ius.el6
Requires: python27-tools = 2.7.5-1.ius.el6
Requires: ros-hydro-common-msgs = 1.10.2-0.el6
Requires: ros-hydro-core = 1.9.50-1.el6
Requires: ros-hydro-orocos-kdl = 1.1.102-1.el6
Requires: ros-hydro-rtt-rospack = 2.6.0-0.el6
Requires: tkinter27 = 2.7.5-1.ius.el6


%description
Meta package providing all packages for the rhcs-core-system

%files

%changelog
* Mon Oct 28 2013 Ruben Smits <ruben@intermodalics.eu> - 2.0.0-0
- Initial RPM release


