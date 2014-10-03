Name:           lxc-initscripts-patch
Version:        1.0.0
Release:        1
Summary:        Patch CentOS 6.x initscripts for lxc guests.
Group:          Server
License:        MIT
URL:            https://github.com/jbrunner/%{name}
BuildArch:      noarch
Requires:       sed
%description
Put a trigger in initscript which runs when the installation 
status of initscript changes. The script will add the patch 
from the centos template again.

%clean
%install
%files

%triggerin -- initscripts
# only patch if /etc/rc.d/lxc.sysinit is present. 
if [ -f /etc/rc.d/lxc.sysinit -a -f  /etc/rc.d/rc.sysinit ]; then
  sed -i 's/^\s*\/sbin\/start_udev/#\0/' /etc/rc.d/rc.sysinit
  sed -i 's/^\s*mount.*\/dev\/pts/#\0/'  /etc/rc.d/rc.sysinit
fi
