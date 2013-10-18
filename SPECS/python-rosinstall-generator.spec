# Created by pyp2rpm-1.0.1
%global pypi_name rosinstall_generator

Name:           python-rosinstall-generator
Version:        0.1.2
Release:        1%{?dist}
Summary:        A tool to generator rosinstall files

License:        BSD and MIT
URL:            http://www.ros.org/wiki/rosinstall_generator
Source0:        https://pypi.python.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python-devel
 
Requires:       python-distribute
Requires:       python-rosdistro >= 0.2.13
Requires:       python-rospkg
Requires:       python-pyyaml

%description
A tool to generator rosinstall files


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
%{_bindir}/rosinstall_generator
%{python_sitelib}/%{pypi_name}
%{python_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Thu Sep 12 2013 CODAC Core System Developer - 0.1.2-1
- Initial package.
