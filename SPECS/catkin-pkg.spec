# Created by pyp2rpm-1.0.1
%global pypi_name catkin_pkg

Name:           python27-catkin-pkg
Version:        0.1.19
Release:        1%{?dist}
Summary:        catkin package library

License:        BSD
URL:            http://www.ros.org/wiki/catkin_pkg
Source0:        https://pypi.python.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 

BuildRequires:  python27
BuildRequires:  python27-devel

Requires:	python27
 
%description
Library for retrieving information about catkin packages.


%prep
%setup -q -n %{pypi_name}-%{version}
find . -type f | xargs sed -i '/^#!/{s/python/python2.7/}'



%build
python2.7 setup.py build


%install
python2.7 setup.py install --skip-build --root %{buildroot}


%files
%doc 
%{_bindir}/catkin_create_pkg
%{_bindir}/catkin_generate_changelog
%{_bindir}/catkin_tag_changelog
%{_bindir}/catkin_test_changelog
/usr/lib/python2.7/site-packages/%{pypi_name}
/usr/lib/python2.7/site-packages/%{pypi_name}-%{version}-py2.7.egg-info

%changelog
* Thu Sep 12 2013 CODAC Core System Developer - 0.1.19-1
- Initial package.
