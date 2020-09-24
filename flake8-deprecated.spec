#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : flake8-deprecated
Version  : 1.3
Release  : 11
URL      : https://files.pythonhosted.org/packages/28/28/d39539c84cfb432d7431255ed16f93125342ced4a137d653b50b621fae36/flake8-deprecated-1.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/28/28/d39539c84cfb432d7431255ed16f93125342ced4a137d653b50b621fae36/flake8-deprecated-1.3.tar.gz
Summary  : Warns about deprecated method calls.
Group    : Development/Tools
License  : GPL-2.0
Requires: flake8-deprecated-license = %{version}-%{release}
Requires: flake8-deprecated-python = %{version}-%{release}
Requires: flake8-deprecated-python3 = %{version}-%{release}
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
Requires: flake8-deprecated-python3 = %{version}-%{release}

%description python
python components for the flake8-deprecated package.


%package python3
Summary: python3 components for the flake8-deprecated package.
Group: Default
Requires: python3-core
Provides: pypi(flake8_deprecated)
Requires: pypi(flake8)

%description python3
python3 components for the flake8-deprecated package.


%prep
%setup -q -n flake8-deprecated-1.3
cd %{_builddir}/flake8-deprecated-1.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583534381
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/flake8-deprecated
cp %{_builddir}/flake8-deprecated-1.3/LICENSE %{buildroot}/usr/share/package-licenses/flake8-deprecated/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/flake8-deprecated-1.3/LICENSE.rst %{buildroot}/usr/share/package-licenses/flake8-deprecated/0c6f5260da599c2ea1bbe3b8b16e171332a14503
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/flake8-deprecated/0c6f5260da599c2ea1bbe3b8b16e171332a14503
/usr/share/package-licenses/flake8-deprecated/4cc77b90af91e615a64ae04893fdffa7939db84c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
