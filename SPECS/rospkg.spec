# Created by pyp2rpm-1.0.1
%global pypi_name rospkg

Name:           python27-%{pypi_name}
Version:        1.0.23
Release:        1%{?dist}
Summary:        ROS package library

License:        BSD
URL:            http://www.ros.org/wiki/rospkg
Source0:        https://pypi.python.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python27-devel


%description
Library for retrieving information about ROS packages and stacks.


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
%doc 
%{_bindir}/rosversion
/usr/lib/python2.7/site-packages/%{pypi_name}
/usr/lib/python2.7/site-packages/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Thu Sep 12 2013 CODAC Core System Developer - 1.0.23-1
- Initial package.
