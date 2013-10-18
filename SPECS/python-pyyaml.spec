# Created by pyp2rpm-1.0.1
%global pypi_name PyYAML

Name:           python-pyyaml
Version:        3.10
Release:        1%{?dist}
Summary:        YAML parser and emitter for Python

License:        MIT
URL:            http://pyyaml.org/wiki/PyYAML
Source0:        https://pypi.python.org/packages/source/P/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
 
BuildRequires:  python-devel


%description
YAML is a data serialization format designed for human readability
and
interaction with scripting languages.  PyYAML is a YAML parser
and emitter for
Python.

PyYAML features a complete YAML 1.1 parser, Unicode support, pickle
support, capable extension API, and sensible error messages.  PyYAML
supports
standard YAML tags and provides Python-specific tags that
allow to represent an
arbitrary ...


%prep
%setup -q -n %{pypi_name}-%{version}



%build
CFLAGS="$RPM_OPT_FLAGS" python setup.py build


%install
python setup.py install --skip-build --root %{buildroot}


%files
%doc LICENSE
%{python_sitearch}/%{pypi_name}-%{version}-py2.6.egg-info
%{python_sitearch}/yaml

%changelog
* Thu Sep 12 2013 CODAC Core System Developer - 3.10-1
- Initial package.
