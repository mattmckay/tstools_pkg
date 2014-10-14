%define debug_package %{nil}
Summary:	Command line tools for working with MPEG streams
Name:		tstools
Version:	1.12
Release:	1.0
License:	MPL v1.1
Group:		Applications/Networking
Source0:	%{name}-%{version}.tgz
URL:		https://code.google.com/p/tstools/source/detail?r=77f94dff7e4f616dfab40ea98f10491b5a2f33e6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The tools are focussed on:
* Quick reporting of useful data (tsinfo, stream_type)
* Giving a quick overview of the entities in the stream (esdots, psdots)
* Reporting on TS packets (tsreport) or ES units/frames/fields (esreport)
* Simple manipulation of stream data (es2ts, esfilter, esreverse, esmerge, ts2es)
* Streaming of data, possibly with introduced errors (tsplay)

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT

OBJ_TSTOOL=${RPM_BUILD_ROOT}/opt/tstools/obj
LIB_TSTOOL=${RPM_BUILD_ROOT}/opt/tstools/lib
BIN_TSTOOL=${RPM_BUILD_ROOT}/opt/tstools/bin
#DOC_TSTOOL=${RPM_BUILD_ROOT}/opt/tstools/docs

mkdir -p $OBJ_TSTOOL $LIB_TSTOOL $BIN_TSTOOL 

cp -a obj/* ${OBJ_TSTOOL}/
cp -a lib/* ${LIB_TSTOOL}/
cp -a bin/* ${BIN_TSTOOL}/


%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(755,root,root,755)

%attr(755,root,root) /opt/tstools/*

%define date	%(echo `LC_ALL="C" date +"%a %b %d %Y"`)

