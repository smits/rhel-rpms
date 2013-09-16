Summary: Orocos Toolchain for component-based sofware development
Name: orocos_toolchain
Version: iter
Release: 1.1%{?dist}
License: GPL+linking exception
Group: Development/Tools
URL: http://www.orocos.org/toolchain
Source0: %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel, readline-devel
BuildRequires: boost-devel
BuildRequires: lua-devel
BuildRequires: cmake, catkin
BuildRequires: ruby
BuildRequires: ros-fuerte-rospack-devel
Requires:      boost, ncurses, readline, ruby, lua, ros-fuerte-rospack, gccxml
Provides:      orocos-toolchain = %{version}-%{release} 

%description
Orocos Toolchain including RTT, OCL, typelib and log4cxx

%package	 devel
Summary:	 Development files for Orocos Toolchain
Group:		 Development/Tools
Requires:	 orocos-toolchain = %{version}-%{release}

%description devel
Development files for Orocos Toolchain

%prep
%setup -q -c

%build
cd orocos_toolchain
source /etc/catkin/profile.d/10.ros.all
export ROS_PACKAGE_PATH="%{_builddir}/%{name}-%{version}:$ROS_PACKAGE_PATH"

pushd utilmm
make
popd

pushd utilrb
make
popd

pushd typelib
make
popd

pushd rtt
mkdir -p build;cd build
cmake .. -DDEFAULT_PLUGIN_PATH=/usr/lib/orocos -DENABLE_CORBA=OFF
make;make install
popd

pushd rtt_typelib
make
popd

pushd orogen
make
popd

pushd log4cpp
make
popd

pushd ocl
mkdir -p build;cd build
cmake .. -DDEFAULT_COMPONENT_PATH=/usr/lib/orocos -DBUILD_TESTING=OFF
make
popd


%install
cd orocos_toolchain
source /etc/catkin/profile.d/10.ros.all
export ROS_PACKAGE_PATH="%{_builddir}:$ROS_PACKAGE_PATH"

mkdir -p %{buildroot}%{_datadir}/ros-stacks/%{name}/
cp -a stack.xml env.mk env.sh rosdep.yaml .gems %{buildroot}%{_datadir}/ros-stacks/%{name}/
mkdir -p %{buildroot}/etc/profile.d/
ln -s %{_datadir}/ros-stacks/%{name}/env.sh %{buildroot}/etc/profile.d/orocosenv.sh

pushd utilmm
mkdir -p %{buildroot}%{_datadir}/ros-stacks/%{name}/utilmm
cp -a Changes.txt LICENSE.* manifest.xml README.txt %{buildroot}%{_datadir}/ros-stacks/%{name}/utilmm
cd build
cmake -DCMAKE_INSTALL_PREFIX=/usr ..
DESTDIR=%{buildroot} make install
popd

pushd utilrb
mkdir -p %{buildroot}%{_datadir}/ros-stacks/%{name}/utilrb
cp -a History.txt License.txt manifest.xml Manifest.txt README.txt %{buildroot}%{_datadir}/ros-stacks/%{name}/utilrb
cp -rL lib %{buildroot}%{_datadir}/ros-stacks/%{name}/utilrb
popd

pushd typelib
mkdir -p %{buildroot}%{_datadir}/ros-stacks/%{name}/typelib
cp -a CHANGES LICENSE.* manifest.xml README.txt TODO %{buildroot}%{_datadir}/ros-stacks/%{name}/typelib
cd build
cmake -DCMAKE_INSTALL_PREFIX=/usr ..
DESTDIR=%{buildroot} make install
popd

pushd rtt
mkdir -p %{buildroot}%{_datadir}/ros-stacks/%{name}/rtt
cp -a AUTHORS ChangeLog COPYING manifest.xml NEWS NO-WARRANTY README %{buildroot}%{_datadir}/ros-stacks/%{name}/rtt
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=/usr
DESTDIR=%{buildroot} make install
popd

pushd rtt_typelib
echo $ROS_PACKAGE_PATH
mkdir -p %{buildroot}%{_datadir}/ros-stacks/%{name}/rtt_typelib
cp -a manifest.xml %{buildroot}%{_datadir}/ros-stacks/%{name}/rtt_typelib
cd build
cmake -DCMAKE_INSTALL_PREFIX=/usr ..
DESTDIR=%{buildroot} make install
popd

pushd orogen
mkdir -p %{buildroot}%{_datadir}/ros-stacks/%{name}/orogen
cp -a History.txt LICENSE.txt Manifest.txt manifest.xml README.txt lib bin %{buildroot}%{_datadir}/ros-stacks/%{name}/orogen
popd

pushd log4cpp
mkdir -p %{buildroot}%{_datadir}/ros-stacks/%{name}/log4cpp
cp -a AUTHORS ChangeLog COPYING INSTALL NEWS README THANKS TODO manifest.xml %{buildroot}%{_datadir}/ros-stacks/%{name}/log4cpp
cd build
cmake -DCMAKE_INSTALL_PREFIX=/usr ..
DESTDIR=%{buildroot} make install
popd

pushd ocl
mkdir -p %{buildroot}%{_datadir}/ros-stacks/%{name}/ocl
cp -a manifest.xml COPYING INSTALL NEWS README scripts/pkg %{buildroot}%{_datadir}/ros-stacks/%{name}/ocl
mkdir -p %{buildroot}%{_bindir}
cp -a scripts/pkg/orocreate-pkg %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/orocos-ocl/
cp -a scripts/pkg/templates %{buildroot}%{_datadir}/orocos-ocl/
mkdir -p %{buildroot}%{_datadir}/ros-stacks/%{name}/ocl/scripts/pkg
ln -s %{_bindir}/orocreate-pkg %{buildroot}%{_datadir}/ros-stacks/%{name}/ocl/scripts/pkg/orocreate-pkg
ln -s %{_datadir}/orocos-ocl/templates %{buildroot}%{_datadir}/ros-stacks/%{name}/ocl/scripts/pkg

cd build
cmake -DCMAKE_INSTALL_PREFIX=/usr ..
DESTDIR=%{buildroot} make install
popd

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc /usr/share/doc/liborocos-rtt
/etc/profile.d/orocosenv.sh
/usr/lib/liblog4cpp.so.6.0
/usr/lib/liblog4cpp.so.6.0.0
/usr/lib/libtypeLib.so.1
/usr/lib/libtypeLib.so.1.1
/usr/lib/typelib/*.so
/usr/lib/ruby/*/*/typelib_ruby.so
/usr/lib/ruby/*/*.rb
/usr/lib/libutilmm.so.1
/usr/lib/libutilmm.so.1.1
%{_datadir}/ros-stacks/%{name}
%exclude %{_datadir}/ros-stacks/%{name}/ocl/scripts
%{_bindir}/deployer*
%{_bindir}/rttlua*
%{_bindir}/rttscript*
/usr/lib/cmake/orocos-rtt/cmake_uninstall.cmake.in
/usr/lib/liborocos-ocl-deployment-gnulinux.so.2.5.0
/usr/lib/liborocos-ocl-log4cpp-gnulinux.so.2.5.0
/usr/lib/liborocos-ocl-taskbrowser-gnulinux.so.2.5.0
/usr/lib/liborocos-rtt-gnulinux.so.2.5
/usr/lib/liborocos-rtt-gnulinux.so.2.5.0
/usr/lib/liborocos-rtt-mqueue-gnulinux.so.2.5
/usr/lib/liborocos-rtt-mqueue-gnulinux.so.2.5.0
/usr/lib/librtt-typelib-gnulinux.so
/usr/lib/orocos/gnulinux/plugins/*.so.2.5.0
/usr/lib/orocos/gnulinux/types/*.so.2.5.0
/usr/lib/orocos/gnulinux/ocl/*.so.2.5.0
/usr/lib/orocos/gnulinux/ocl/plugins/*.so.2.5.0
/usr/lib/orocos/gnulinux/ocl/types/*.so.2.5.0
%{_datadir}/lua




%files devel
%{_bindir}/orocreate-pkg
%{_datadir}/ros-stacks/%{name}/ocl/scripts
%{_datadir}/orocos-ocl
/usr/lib/pkgconfig/*.pc
%{_includedir}/log4cpp
/usr/lib/liblog4cpp.so
%{_includedir}/typelib
/usr/lib/libtypeLib.so
/usr/lib/ruby/*/*/typelib_ruby.hh
%{_includedir}/utilmm
/usr/lib/libutilmm.so
%{_includedir}/rtt
%{_includedir}/orocos/ocl
/usr/lib/cmake/orocos-rtt/*.cmake
/usr/lib/liborocos-ocl-deployment-gnulinux.so
/usr/lib/liborocos-rtt-mqueue-gnulinux.so
/usr/lib/liborocos-rtt-gnulinux.so
/usr/lib/liborocos-ocl-taskbrowser-gnulinux.so
/usr/lib/liborocos-ocl-log4cpp-gnulinux.so
/usr/lib/orocos/gnulinux/plugins/*.so
/usr/lib/orocos/gnulinux/types/*.so
/usr/lib/orocos/gnulinux/ocl/*.so
/usr/lib/orocos/gnulinux/ocl/plugins/*.so
/usr/lib/orocos/gnulinux/ocl/types/*.so


%changelog
* Thu Aug 23 2012 Ruben Smits <ruben.smits@intermodalics.eu> - iter-1.1
- Updated env.sh and added to /etc/profile.d

* Tue Aug 21 2012 Ruben Smits <ruben.smits@intermodalics.eu> - iter-1
- Initial build.

