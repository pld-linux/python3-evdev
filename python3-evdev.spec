%define		module	evdev
Summary:	Python bindings for the Linux input subsystem
Name:		python3-%{module}
Version:	2.0.0
Release:	1
License:	BSD
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/e/evdev/%{module}-%{version}.tar.gz
# Source0-md5:	d2352944714abd2a29e817045261df05
URL:		https://github.com/gvalkov/python-evdev
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
Requires:	python3-modules >= 3.11
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides bindings to the generic input event interface in
Linux. The evdev interface serves the purpose of passing events
generated in the kernel directly to userspace through character
devices that are typically located in /dev/input/.

This package also comes with bindings to uinput, the userspace input
subsystem. Uinput allows userspace programs to create and handle input
devices that can inject events directly into the input subsystem.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build %{?with_tests:test}

%install
rm -rf $RPM_BUILD_ROOT
%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%dir %{py3_sitedir}/%{module}
%{py3_sitedir}/%{module}/*.py
%{py3_sitedir}/%{module}/py.typed
%attr(755,root,root) %{py3_sitedir}/%{module}/*.so
%{py3_sitedir}/%{module}/__pycache__
%{py3_sitedir}/%{module}-%{version}-py*.egg-info
