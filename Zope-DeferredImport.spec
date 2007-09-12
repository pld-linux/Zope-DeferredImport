Summary:	Deferr Python module import
Name:		Zope-DeferredImport
Version:	3.4.0
Release:	1
License:	ZPL 2.1
Group:		Libraries/Python
Source0:	http://download.zope.org/distribution/zope.deferredimport-%{version}.tar.gz
# Source0-md5:	fb1929c582c470fe1bfe90f0568f7b20
URL:		http://www.zope.org/
BuildRequires:	python
BuildRequires:	python-devel
%pyrequires_eq	python-modules
Requires:	Zope-Proxy
Requires:	Zope-Testing
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Deferr Python module import.

%prep
%setup -q -n zope.deferredimport-%{version}

%build
python ./setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python ./setup.py install \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT

%{py_postclean}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/zope/deferredimport
%{py_sitescriptdir}/zope*egg*
%{py_sitescriptdir}/zope*pth
