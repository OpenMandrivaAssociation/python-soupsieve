# Created by pyp2rpm-3.3.2
%global pypi_name soupsieve
%global with_tests 0

Name:           python-%{pypi_name}
Version:	1.9.5
Release:	3
Summary:        A modern CSS selector implementation for Beautiful Soup
Group:          Development/Python
License:        MIT
URL:            https://github.com/facelessuser/soupsieve
Source0:	https://files.pythonhosted.org/packages/92/cf/57dfed8a00f4ba33af3a6615d693bb65a19a11e26ab13293f62359216417/soupsieve-1.9.5.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python2dist(backports.functools-lru-cache)
BuildRequires:  python2dist(setuptools)
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Soup Sieve is a CSS selector library designed to be used with Beautiful Soup 4.
It aims to provide selecting, matching, and filtering using modern CSS
selectors. Soup Sieve currently provides selectors from the CSS level 1
specifications up through the latest CSS level 4 drafts and beyond (though
some are not yet implemented).

Soup Sieve was written with the intent to replace Beautiful Soup's builtin
select feature, and as of Beautiful Soup version 4.7.0, it now is good.
Soup Sieve can also be imported in order to use its API directly for more
controlled, specialized parsing.

Soup Sieve has implemented most of the CSS selectors up through the latest CSS
draft specifications, though there are a number that don't make sense in a
non-browser environment. Selectors that cannot provide meaningful functionality
simply do not match anything.

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python2dist(backports.functools-lru-cache)
%description -n python2-%{pypi_name}
Soup Sieve is a CSS selector library designed to be used with Beautiful Soup 4.
It aims to provide selecting, matching, and filtering using modern CSS
selectors. Soup Sieve currently provides selectors from the CSS level 1
specifications up through the latest CSS level 4 drafts and beyond (though
some are not yet implemented).

Soup Sieve was written with the intent to replace Beautiful Soup's builtin
select feature, and as of Beautiful Soup version 4.7.0, it now is good.
Soup Sieve can also be imported in order to use its API directly for more
controlled, specialized parsing.

Soup Sieve has implemented most of the CSS selectors up through the latest CSS
draft specifications, though there are a number that don't make sense in a
non-browser environment. Selectors that cannot provide meaningful functionality
simply do not match anything.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build
%py3_build

%install
# Must do the default python version install last because
# the scripts in /usr/bin are overwritten with every setup.py install.
%py2_install
%py3_install

%if %with_tests
%check
%{__python2} setup.py test
%{__python3} setup.py test
%endif

%files -n python2-%{pypi_name}
%license LICENSE.md docs/src/markdown/about/license.md
%doc README.md
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files
%license LICENSE.md docs/src/markdown/about/license.md
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
