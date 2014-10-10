#!/bin/sh
sudo yum remove tstools
# Install the newly built packages
sudo yum install --nogpgcheck ~/rpmbuild/RPMS/x86_64/tstools-1.12-1.0.x86_64.rpm