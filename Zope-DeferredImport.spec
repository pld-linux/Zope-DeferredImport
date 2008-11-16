Summary:	Defer Python module import
Summary(pl.UTF-8):	Opóźnianie importu modułów Pythona
Name:		Zope-DeferredImport
Version:	3.4.0
Release:	3
License:	ZPL 2.1
Group:		Libraries/Python
Source0:	http://download.zope.org/distribution/zope.deferredimport-%{version}.tar.gz
# Source0-md5:	fb1929c582c470fe1bfe90f0568f7b20
URL:		http://www.zope.org/
BuildRequires:	python >= 1:2.5
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
Requires:	Zope-Proxy
Requires:	Zope-Testing
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Defer Python module import.

%description -l pl.UTF-8
Opóźnianie importu modułów Pythona.

%prep
%setup -q -n zope.deferredimport-%{version}

%build
python ./setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python ./setup.py install \
	--install-purelib=%{py_sitedir} \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitedir}/zope/deferredimport
%{py_sitedir}/zope.deferredimport-*.egg-info
%{py_sitedir}/zope.deferredimport-*-nspkg.pth
