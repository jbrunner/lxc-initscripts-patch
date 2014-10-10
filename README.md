# lxc-initscripts-patch

*Patch CentOS 6.x initscripts for lxc guests.*

The [lxc centos template](https://github.com/lxc/lxc/blob/2ba5eb93b8eeb82fbfb42e33324513d70e777dd5/templates/lxc-centos.in) applies a patch to /etc/rc.d/rc.sysinit wich is provided by the initscripts package.

After upgrading initscripts using yum, the patch is lost. 
The linux container is not bootable anymore. Errors shown:

    Starting udev: mkdir: cannot create directory `/dev/pts': File exists

lxc-initscripts-patch put a trigger in initscript which runs
when the installation status of initscript changes. 
The script applies the patch from the centos template again.

## Install

    yum install rpm-build
    mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
    rpmbuild -bb lxc-initscripts-patch.spec
    sudo rpm -Uvh ~/rpmbuild/RPMS/noarch/lxc-initscripts-patch-1.0.0-1.noarch
