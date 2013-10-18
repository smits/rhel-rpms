# Created by pyp2rpm-1.0.1
%global pypi_name distribute

Name:           python27-%{pypi_name}
Version:        0.7.3
Release:        1%{?dist}
Summary:        distribute legacy wrapper

License:        Python and ZPLv%(TODO: version)s
URL:            http://packages.python.org/distribute
Source0:        https://pypi.python.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.zip
BuildArch:      noarch
 
BuildRequires:  python27-devel
 
Requires:       python27-setuptools >= 0.7

%description
Distribute - legacy package

This package is a simple compatibility layer that
installs Setuptools 0.7+.


%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
python2.7 setup.py build


%install
python2.7 setup.py install --skip-build --root %{buildroot}


%files
%doc 
/usr/lib/python2.7/site-packages/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Thu Sep 12 2013 CODAC Core System Developer - 0.7.3-1
- Initial package.
