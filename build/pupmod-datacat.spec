Summary: Datacat Puppet Module
Name: pupmod-richardc-datacat
Version: 0.6.1
Release: 0
License: Apache 2.0
Group: Applications/System
Source: %{name}-%{version}-%{release}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: puppet >= 3.3.0
Buildarch: noarch
Obsoletes: pupmod-datacat-test

Prefix:"/etc/puppet/environments/simp/modules"

%description
Puppet types for concatenating data via a template

The datacat and datacat_fragment types allow you to build up a data structure
which is rendered using a template. This is similar to some of the common
concatenation patterns though the intent should be clearer as it pushes the
boilerplate down into the type.

Project Code: https://github.com/richardc/puppet-datacat

%prep
%setup -q

%build

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/%{prefix}/datacat

dirs='files lib manifests templates'
for dir in $dirs; do
  test -d $dir && cp -r $dir %{buildroot}/%{prefix}/datacat
done

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/%{prefix}/datacat

%files
%defattr(0640,root,puppet,0750)
/etc/puppet/environments/simp/modules/datacat

%post
#!/bin/sh

if [ -d /etc/puppet/environments/simp/modules/datacat/plugins ]; then
  /bin/mv /etc/puppet/environments/simp/modules/datacat/plugins /etc/puppet/environments/simp/modules/datacat/plugins.bak
fi

%postun
# Post uninstall stuff

%changelog
* Fri Jan 16 2015 Trevor Vaughan <tvaughan@onyxpoint.com> - 0.6.1-0
- Updated release of the Datacat module.
