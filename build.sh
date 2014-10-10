#!/bin/sh
# Run this script from the parent directory e.g.  $ . scripts/build.sh
# Clear the rpmbuild/ directory
rm -r ~/rpmbuild/


# Build the SOURCES/ and SPECS/ directories
mkdir -p ~/rpmbuild/SOURCES/
mkdir -p ~/rpmbuild/SPECS/


# Copy the specfile into the rpmbuild/ directory
cp tstools.spec ~/rpmbuild/SPECS/

# tar source files into the src dir
tar cvzf ~/rpmbuild/SOURCES/tstools.tgz tstools/*

# Build the rpms
rpmbuild -ba ~/rpmbuild/SPECS/tstools.spec