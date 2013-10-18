# Created by pyp2rpm-1.0.1
%global pypi_name rosdistro

Name:           python-%{pypi_name}
Version:        0.2.14
Release:        1%{?dist}
Summary:        A tool to work with rosdistro files

License:        BSD and MIT
URL:            http://www.ros.org/wiki/rosdistro
Source0:        https://pypi.python.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python-devel
 
Requires:       python-catkin-pkg
Requires:       python-distribute
Requires:       python-rospkg
Requires:       python-pyyaml

%description
A tool to work with rosdistro files


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
%{_bindir}/rosdistro_build_cache
%{_bindir}/rosdistro_reformat
%{python_sitelib}/%{pypi_name}
%{python_sitelib}/%{pypi_name}-%{version}-py2.6.egg-info

%changelog
* Thu Sep 12 2013 CODAC Core System Developer - 0.2.14-1
- Initial package.
