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

%files
%defattr(-,root,root,-)
/usr/sbin/rfkill
%{_datadir}/man/man8/rfkill.8.gz

