Name:       rfkill
Summary:    Simple /dev/rfkill userspace tool
Version:    0.4
Release:    1
Group:      Applications/System
License:    TO BE FILLED IN
Source0:    %{name}-%{version}.tar.bz2

%description
simple /dev/rfkill userspace tool

%prep
%setup -q 

%build

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%remove_docs

mkdir -p %{buildroot}/usr/share/license
cp COPYING %{buildroot}/usr/share/license/%{name}

%files
/usr/share/license/%{name}
%manifest rfkill.manifest
%defattr(-,root,root,-)
/usr/sbin/rfkill

