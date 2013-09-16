# Created by pyp2rpm-1.0.1
%global pypi_name rosinstall_generator

Name:           python27-rosinstall-generator
Version:        0.1.2
Release:        1%{?dist}
Summary:        A tool to generator rosinstall files

License:        BSD and MIT
URL:            http://www.ros.org/wiki/rosinstall_generator
Source0:        https://pypi.python.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python27-devel
 
Requires:       python27-distribute
Requires:       python27-rosdistro >= 0.2.13
Requires:       python27-rospkg
Requires:       python27-pyyaml

%description
A tool to generator rosinstall files


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
%{_bindir}/rosinstall_generator
/usr/lib/python2.7/site-packages/%{pypi_name}
/usr/lib/python2.7/site-packages/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Thu Sep 12 2013 CODAC Core System Developer - 0.1.2-1
- Initial package.
