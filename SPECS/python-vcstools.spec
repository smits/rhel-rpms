# Created by pyp2rpm-1.0.1
%global pypi_name vcstools

Name:           python-%{pypi_name}
Version:        0.1.30
Release:        1%{?dist}
Summary:        VCS/SCM source control library for svn, git, hg, and bzr

License:        BSD
URL:            http://www.ros.org/wiki/vcstools
Source0:        https://pypi.python.org/packages/source/v/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python-devel
 
Requires:       python-pyyaml

%description
Library for managing source code trees from multiple version control systems.
Current supports svn, git, hg, and bzr.


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
%{python_sitelib}/%{pypi_name}
%{python_sitelib}/%{pypi_name}-%{version}-py2.6.egg-info

%changelog
* Thu Sep 12 2013 CODAC Core System Developer - 0.1.30-1
- Initial package.
