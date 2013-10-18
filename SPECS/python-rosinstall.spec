# Created by pyp2rpm-1.0.1
%global pypi_name rosinstall

Name:           python-%{pypi_name}
Version:        0.6.29
Release:        1%{?dist}
Summary:        The installer for ROS

License:        BSD
URL:            http://www.ros.org/wiki/rosinstall
Source0:        https://pypi.python.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python-devel
 
Requires:       python-vcstools >= 0.1.30
Requires:       python-pyyaml
Requires:       python-rosdistro
Requires:       python-catkin-pkg

%description
The installer for ROS


%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
find . -type f | xargs sed -i '/^#!/{s/python2.7/python/}'


%build
python setup.py build


%install
python setup.py install --skip-build --root %{buildroot}


%files
%doc README.rst
%{_bindir}/rosinstall
%{_bindir}/roslocate
%{_bindir}/rosws
%{_bindir}/rosco
%{python_sitedir}/%{pypi_name}
%{python_sitedir}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Thu Sep 12 2013 CODAC Core System Developer - 0.6.29-1
- Initial package.
