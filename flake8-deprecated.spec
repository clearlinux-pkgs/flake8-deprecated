#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : flake8-deprecated
Version  : 1.3
Release  : 4
URL      : https://files.pythonhosted.org/packages/28/28/d39539c84cfb432d7431255ed16f93125342ced4a137d653b50b621fae36/flake8-deprecated-1.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/28/28/d39539c84cfb432d7431255ed16f93125342ced4a137d653b50b621fae36/flake8-deprecated-1.3.tar.gz
Summary  : Warns about deprecated method calls.
Group    : Development/Tools
License  : GPL-2.0
Requires: flake8-deprecated-python3
Requires: flake8-deprecated-license
Requires: flake8-deprecated-python
Requires: flake8
BuildRequires : buildreq-distutils3
BuildRequires : flake8
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
.. image:: https://travis-ci.org/gforcada/flake8-deprecated.svg?branch=master
:target: https://travis-ci.org/gforcada/flake8-deprecated

%package license
Summary: license components for the flake8-deprecated package.
Group: Default

%description license
license components for the flake8-deprecated package.


%package python
Summary: python components for the flake8-deprecated package.
Group: Default
Requires: flake8-deprecated-python3

%description python
python components for the flake8-deprecated package.


%package python3
Summary: python3 components for the flake8-deprecated package.
Group: Default
Requires: python3-core

%description python3
python3 components for the flake8-deprecated package.


%prep
%setup -q -n flake8-deprecated-1.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1533151592
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/flake8-deprecated
cp LICENSE %{buildroot}/usr/share/doc/flake8-deprecated/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/flake8-deprecated/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
