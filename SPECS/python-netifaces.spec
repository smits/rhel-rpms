%define realname netifaces
%define realver  0.8
%define srcext   tar.gz

# Common info
Name:          python-%{realname}
Version:       %{realver}
Release:       3.1
License:       MIT
Group:         Development/Libraries/Python
URL:           http://alastairs-place.net/projects/netifaces/
Summary:       Portable access to network interfaces from Python

# Build-time parameters
BuildRequires: python-devel
BuildRequires: python-distribute

BuildRoot:     %{_tmppath}/%{name}-root
Source:        http://alastairs-place.net/projects/netifaces/%{realname}-%{realver}%{?extraver}.%{srcext}

%description
netifaces provides a (hopefully portable-ish) way for Python programmers to
get access to a list of the network interfaces on the local machine, and to
obtain the addresses of those network interfaces.

The package has been tested on Mac OS X, Windows XP, Windows Vista, Linux
and Solaris.

It should work on other UNIX-like systems provided they implement
either getifaddrs() or support the SIOCGIFxxx socket options, although the
data provided by the socket options is normally less complete.

# Preparation step (unpackung and patching if necessary)
%prep
%setup -q -n %{realname}-%{realver}%{?extraver}

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}
%{__rm} -rf %{buildroot}%{python_sitearch}/%{realname}-%{realver}%{?extraver}-*.egg-info

%clean
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{python_sitearch}/*

%changelog
