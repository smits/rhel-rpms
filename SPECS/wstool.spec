# Created by pyp2rpm-1.0.1
%global pypi_name wstool

Name:           python27-%{pypi_name}
Version:        0.0.3
Release:        1%{?dist}
Summary:        workspace multi-SCM commands

License:        BSD
URL:            http://www.ros.org/wiki/wstool
Source0:        https://pypi.python.org/packages/source/w/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python27-devel
 
Requires:       python27-vcstools
Requires:       python27-pyyaml
Requires:       python27-rosinstall

%description
A tool for managing a workspace of multiple heterogenous SCM repositories


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
%{_bindir}/wstool
/usr/lib/python2.7/site-packages/%{pypi_name}
/usr/lib/python2.7/site-packages/%{pypi_name}-%{version}-py2.7.egg-info

%changelog
* Thu Sep 12 2013 CODAC Core System Developer - 0.0.3-1
- Initial package.
