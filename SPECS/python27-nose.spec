# Created by pyp2rpm-1.0.1
%global pypi_name nose

Name:           python27-%{pypi_name}
Version:        1.3.0
Release:        1%{?dist}
Summary:        nose extends unittest to make testing easier

License:        LGPL
URL:            http://readthedocs.org/docs/nose/
Source0:        https://pypi.python.org/packages/source/n/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python27-devel


%description
nose extends the test loading and running features of unittest, making
    it
easier to write, find and run tests.

    By default, nose will run tests in
files or directories under the current
    working directory whose names
include "test" or "Test" at a word boundary
    (like "test_this" or
"functional_test" or "TestClass" but not
    "libtest"). Test output is similar
to that of unittest, ...


%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
find . -type f | xargs sed -i '/^#!/{s/python/python2.7/}'

# generate html docs 

#sphinx-build doc html
# remove the sphinx-build leftovers
#rm -rf html/.{doctrees,buildinfo}


%build
python2.7 setup.py build


%install
python2.7 setup.py install --skip-build --root %{buildroot}
mv %{buildroot}/usr/bin/nosetests %{buildroot}/usr/bin/nosetests2.7

%files
%doc README.txt 
/usr/man
/usr/lib/python2.7/site-packages/%{pypi_name}
/usr/lib/python2.7/site-packages/%{pypi_name}-%{version}-py?.?.egg-info
/usr/bin/nosetests2.7

%changelog
* Thu Sep 12 2013 CODAC Core System Developer - 1.3.0-1
- Initial package.
