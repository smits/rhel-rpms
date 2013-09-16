# Created by pyp2rpm-1.0.1
%global pypi_name setuptools

Name:           python27-%{pypi_name}
Version:        1.1.5
Release:        2%{?dist}
Summary:        Easily download, build, install, upgrade, and uninstall Python packages

License:        Python and ZPLv%(TODO: version)s
URL:            https://pypi.python.org/pypi/setuptools
Source0:        https://pypi.python.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
 
BuildRequires:  python27-devel


%description
===============================
Installing and Using Setuptools
===============================

.. contents:: **Table of Contents**
-------------------------
Installation Instructions
-------------------------
Upgrading from Distribute
=========================

Currently, Distribute
disallows installing Setuptools 0.7+ over Distribute.
You must first uninstall
any active version of ...


%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
CFLAGS="$RPM_OPT_FLAGS" python2.7 setup.py build


%install
python2.7 setup.py install --skip-build --root %{buildroot}
# Lets not overwrite the default one in CentOS/RHEL
rm -f $RPM_BUILD_ROOT/usr/bin/easy_install


%files
%doc README.txt
/usr/lib/python2.7/site-packages/*
/usr/bin/easy_install-2.7
/usr/lib/python2.7/site-packages/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Fri Sep 13 2013 CODAC Core System Developer - 1.1.5-2
- rebuilt

* Thu Sep 12 2013 CODAC Core System Developer - 1.1.4-1
- Initial package.
