# Created by pyp2rpm-1.0.1
%global pypi_name rosinstall

Name:           python27-%{pypi_name}
Version:        0.6.29
Release:        1%{?dist}
Summary:        The installer for ROS

License:        BSD
URL:            http://www.ros.org/wiki/rosinstall
Source0:        https://pypi.python.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python27-devel
 
Requires:       python27-vcstools >= 0.1.30
Requires:       python27-pyyaml
Requires:       python27-rosdistro
Requires:       python27-catkin-pkg

%description
The installer for ROS


%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
find . -type f | xargs sed -i '/^#!/{s/python/python2.7/}'


%build
python2.7 setup.py build


%install
python2.7 setup.py install --skip-build --root %{buildroot}


%files
%doc README.rst
%{_bindir}/rosinstall
%{_bindir}/roslocate
%{_bindir}/rosws
%{_bindir}/rosco
/usr/lib/python2.7/site-packages/%{pypi_name}
/usr/lib/python2.7/site-packages/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Thu Sep 12 2013 CODAC Core System Developer - 0.6.29-1
- Initial package.
