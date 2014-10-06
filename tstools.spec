Summary:	Command line tools for working with MPEG streams
Name:		tstools
Version:	1.11
Release:	1.1
License:	MPL v1.1
Group:		Applications/Networking
Source0:	http://tstools.googlecode.com/files/%{name}-1_11.tgz
# Source0-md5:	2650a09f828b19bb22829a7828f13cde
URL:		http://tstools.berlios.de/
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
#sed -e 's/libtstools.a/libtstools.so/' -i Makefile
#sed -e 's/$(LIB): $(LIB)($(OBJS))/$(LIB): $(OBJS)\n	$(CC) $(CFLAGS) -shared $(OBJS) -o $@/' -i Makefile

%build
make

%install
rm -rf $RPM_BUILD_ROOT
OPT_DIR=${RPM_BUILD_ROOT}/opt
TSTOOLS_DIR=${OPT_DIR}/tstools

mkdir -p ${TSTOOLS_DIR}
OBJ_TSTOOL=${TSTOOLS_DIR}/obj
LIB_TSTOOL=${TSTOOLS_DIR}/lib
BIN_TSTOOL=${TSTOOLS_DIR}/bin
mkdir -p $OBJ_TSTOOL $LIB_TSTOOL $BIN_TSTOOL

cp -a obj/* $OBJ_TSTOOL
cp -a lib/* $LIB_TSTOOL
cp -a bin/* $BIN_TSTOOL

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(755,root,root,755)
%doc data docs/*
%attr(755,root,root) ${TSTOOLS_DIR}/*
%attr(755,root,root) ${OBJ_TSTOOL}/*
%attr(755,root,root) ${LIB_TSTOOL}/*
%attr(755,root,root) ${BIN_TSTOOL}/*

%define date	%(echo `LC_ALL="C" date +"%a %b %d %Y"`)
%changelog
* %{date} PLD Team <feedback@pld-linux.org>
All persons listed below can be reached at <cvs_login>@pld-linux.org

$Log: tstools.spec,v $
Revision 1.3  2012/01/03 21:29:11  gotar
- oops, all object files need to be position independent

Revision 1.2  2012/01/03 21:25:51  gotar
- -fPIC for shared library

Revision 1.1  2012/01/03 21:22:40  gotar
- initial PLD release