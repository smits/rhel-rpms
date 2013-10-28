# Created by pyp2rpm-1.0.1
%global pypi_name rosdep

Name:           python-%{pypi_name}
Version:        0.10.21
Release:        1%{?dist}
Summary:        rosdep package manager abstrction tool for ROS

License:        BSD
URL:            http://www.ros.org/wiki/rosdep
Source0:        https://pypi.python.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python-devel
BuildRequires:  python-nose >= 1.0
 
Requires:       python-catkin-pkg
Requires:       python-rospkg
Requires:       python-rosdistro >= 0.2.1
Requires:       python-pyyaml >= 3.1

%description
Command-line tool for installing system dependencies on a variety of platforms.


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
%doc 
%{_bindir}/rosdep
%{_bindir}/rosdep-source
%{python_sitelib}/%{pypi_name}2
%{python_sitelib}/%{pypi_name}-%{version}-py2.6.egg-info

%changelog
* Thu Sep 12 2013 CODAC Core System Developer - 0.10.21-1
- Initial package.