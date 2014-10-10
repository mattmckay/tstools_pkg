#!/bin/sh
# Run this script from the parent directory e.g.  $ . scripts/build.sh
# Clear the rpmbuild/ directory
rm -r ~/rpmbuild/


# Build the SOURCES/ and SPECS/ directories
mkdir -p ~/rpmbuild/SOURCES/
mkdir -p ~/rpmbuild/SPECS/


# Copy the specfile into the rpmbuild/ directory
cp tstools.spec ~/rpmbuild/SPECS/

# download the source files into the src dir
wget -P ~/rpmbuild/SOURCES https://tstools.googlecode.com/archive/77f94dff7e4f616dfab40ea98f10491b5a2f33e6.tar.gz 

# Build the rpms
rpmbuild -ba ~/rpmbuild/SPECS/tstools.spec