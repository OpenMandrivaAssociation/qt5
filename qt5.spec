%define beta alpha
%define _qt_prefix %_prefix/lib/qt5
%define _qt_bindir %_qt_prefix/bin
%define _qt_docdir %_docdir/qt5
%define _qt_libdir %_prefix/lib/qt5/%_lib
%define _qt_includedir %_qt_prefix/include
%define _qt_plugindir %_libdir/qt5/plugins
%define _qt_demodir %_qt_prefix/demos
%define _qt_exampledir %_qt_prefix/examples
%define _qt_importdir %_qt_prefix/imports
%define _qt_datadir %_qt_prefix/share
%define _qt_sysconfdir %_sysconfdir/qt5
%define _qt_testsdir %_qt_prefix/tests
%define _qt_translationsdir %_qt_prefix/translations

%define major %(echo %version |cut -d. -f1)

# QtBase
%define qtconcurrent %mklibname qtconcurrent %major
%define qtconcurrentd %mklibname qtconcurrent%major -d
%define qtcore %mklibname qtcore %major
%define qtcored %mklibname qtcore%major -d
%define qtdbus %mklibname qtdbus %major
%define qtdbusd %mklibname qtdbus%major -d
%define qtgui %mklibname qtgui %major
%define qtguid %mklibname qtgui%major -d
%define qtnetwork %mklibname qtnetwork %major
%define qtnetworkd %mklibname qtnetwork%major -d
%define qtopengl %mklibname qtopengl %major
%define qtopengld %mklibname qtopengl%major -d
%define qtprintsupport %mklibname qtprintsupport %major
%define qtprintsupportd %mklibname qtprintsupport%major -d
%define qtsql %mklibname qtsql %major
%define qtsqld %mklibname qtsql%major -d
%define qttest %mklibname qttest %major
%define qttestd %mklibname qttest%major -d
%define qtwidgets %mklibname qtwidgets %major
%define qtwidgetsd %mklibname qtwidgets%major -d
%define qtxml %mklibname qtxml %major
%define qtxmld %mklibname qtxml%major -d
# Other components
%define gruesensor %mklibname gruesensor 1
%define qgsttools_p %mklibname qgsttools_p 1
%define qt3d %mklibname qt3d %major
%define qt3dd %mklibname qt3d -d
%define qt3dquick %mklibname qt3dquick %major
%define qt3dquickd %mklibname qt3dquick%major -d
%define qtclucene %mklibname qtclucene %major
%define qtclucened %mklibname qtclucene%major -d
%define qtdesignercomponents %mklibname qtdesignercomponents %major
%define qtdesignercomponentsd %mklibname qtdesignercomponents%major -d
%define qtdesigner %mklibname qtdesigner %major
%define qtdesignerd %mklibname qtdesigner%major -d
%define qthelp %mklibname qthelp %major
%define qthelpd %mklibname qthelp%major -d
%define qtlocation %mklibname qtlocation %major
%define qtlocationd %mklibname qtlocation%major -d
%define qtmultimedia %mklibname qtmultimedia %major
%define qtmultimediad %mklibname qtmultimedia%major -d
%define qtmultimediaquick_p %mklibname qtmultimediaquick_p %major
%define qtmultimediawidgets %mklibname qtmultimediawidgets %major
%define qtmultimediawidgetsd %mklibname qtmultimediawidgets%major -d
%define qtpublishsubscribe %mklibname qtpublishsubscribe %major
%define qtpublishsubscribed %mklibname qtpublishsubscribe%major -d
%define qtqml %mklibname qtqml %major
%define qtqmld %mklibname qtqml%major -d
%define qtquick1 %mklibname qtquick1 %major
%define qtquick1d %mklibname qtquick1_%major -d
%define qtquick %mklibname qtquick %major
%define qtquickd %mklibname qtquick%major -d
%define qtquicktest %mklibname qtquicktest %major
%define qtquicktestd %mklibname qtquicktest%major -d
%define qtscript %mklibname qtscript %major
%define qtscriptd %mklibname qtscript%major -d
%define qtscripttools %mklibname qtscripttools %major
%define qtscripttoolsd %mklibname qtscripttools%major -d
%define qtsensors %mklibname qtsensors %major
%define qtsensorsd %mklibname qtsensors%major -d
%define qtserviceframework %mklibname qtserviceframework %major
%define qtserviceframeworkd %mklibname qtserviceframework%major -d
%define qtsvg %mklibname qtsvg %major
%define qtsvgd %mklibname qtsvg%major -d
%define qtsysteminfo %mklibname qtsysteminfo %major
%define qtsysteminfod %mklibname qtsysteminfo%major -d
%define qtv8 %mklibname qtv8 %major
%define qtv8d %mklibname qtv8_%major -d
%define qtwebkit %mklibname qtwebkit %major
%define qtwebkitd %mklibname qtwebkit%major -d
%define qtxmlpatterns %mklibname qtxmlpatterns %major
%define qtxmlpatternsd %mklibname qtxmlpatterns%major -d

Name: qt5
Version: 5.0.0
%if "%beta" == ""
Source0: http://releases.qt-project.org/qt5.0/release/qt-everywhere-opensource-src-%version.tar.xz
Release: 1
%else
Source0: http://releases.qt-project.org/qt5.0/%beta/qt-everywhere-opensource-src-%version-%beta.tar.xz
Release: 0.%beta.2
%endif
Source100: %name.rpmlintrc
# QtLocation has an (unneeded) dependency on qtjsondb, but qtjsondb
# isn't actually part of the 5.0.0-alpha release
Patch0: qt-5.0.0-no-qtjsondb-dep.patch
License: LGPLv3+
Summary: Version 5 of the Qt toolkit
URL: http://qt-project.org/
Group: Development/KDE and Qt

BuildRequires: chrpath

# CUPS
BuildRequires: cups-devel

# OpenGL
BuildRequires: pkgconfig(gl)

# Event loop
BuildRequires: pkgconfig(glib-2.0)

# For XCB platform plugin:
BuildRequires: pkgconfig(xcb) >= 1.5
BuildRequires: pkgconfig(xcb-icccm)
BuildRequires: pkgconfig(xcb-image)
BuildRequires: pkgconfig(xcb-renderutil)
BuildRequires: pkgconfig(xcb-keysyms)
BuildRequires: pkgconfig(xrender)

# For WebKit
BuildRequires: flex
BuildRequires: bison

%if "%_lib" == "lib64"
%define platform linux-g++-64
%else
%define platform linux-g++-32
%endif

%define options \\\
	-release \\\
	-opensource \\\
	-shared \\\
	-largefile \\\
	-exceptions \\\
	-accessibility \\\
	-stl \\\
	-no-sql-db2 \\\
	-no-sql-ibase \\\
	-plugin-sql-mysql \\\
	-no-sql-oci \\\
	-plugin-sql-odbc \\\
	-plugin-sql-psql \\\
	-plugin-sql-sqlite \\\
	-no-sql-sqlite2 \\\
	-no-sql-tds \\\
	-system-sqlite \\\
	-phonon-backend \\\
	-javascript-jit \\\
	-system-zlib \\\
	-system-libpng \\\
	-system-libjpeg \\\
	-openssl \\\
	-system-pcre \\\
	-optimized-qmake \\\
	-no-nis \\\
	-cups \\\
	-iconv \\\
	-pch \\\
	-dbus \\\
	-reduce-relocations \\\
	-xcb \\\
	-opengl desktop \\\
	-confirm-license \\\
	-glib \\\
	-no-separate-debug-info \\\
	-platform %platform

%description
Version 5 of the Qt toolkit

%package -n %qtconcurrent
Summary: Qt threading library
Group: System/Libraries

%description -n %qtconcurrent
Qt threading library

%package -n %qtconcurrentd
Summary: Development files for version %major of the QtConcurrent library
Group: Development/KDE and Qt
Requires: %qtconcurrent = %version-%release

%description -n %qtconcurrentd
Development files for version %major of the QtConcurrent library

%package -n %qtcore
Summary: Qt Core library
Group: System/Libraries

%description -n %qtcore
Qt Core library

%package -n %qtcored
Summary: Development files for version %major of the QtCore library
Group: Development/KDE and Qt
Requires: %qtcore = %version-%release

%description -n %qtcored
Development files for version %major of the QtCore library

%package -n qmake%major
Summary: Makefile generation system for Qt%major
Group: Development/KDE and Qt

%description -n qmake%major
Makefile generation system for Qt%major

%package -n %qtdbus
Summary: Qt DBus connector library
Group: System/Libraries

%description -n %qtdbus
Qt DBus connector library

%package -n %qtdbusd
Summary: Development files for version %major of the QtDBus library
Group: Development/KDE and Qt
Requires: %qtdbus = %version-%release

%description -n %qtdbusd
Development files for version %major of the QtDBus library

%package -n %qtgui
Summary: Qt GUI library
Group: System/Libraries

%description -n %qtgui
Qt GUI library

%package -n %qtguid
Summary: Development files for version %major of the QtGui library
Group: Development/KDE and Qt
Requires: %qtgui = %version-%release

%description -n %qtguid
Development files for version %major of the QtGui library

%package -n %qtgui-x11
Summary: X11 output driver for QtGui v%major
Group: System/Libraries
Requires: %qtgui = %version-%release

%description -n %qtgui-x11
X11 output driver for QtGui v%major

%package -n %qtgui-minimal
Summary: Minimal (Framebuffer based) output driver for QtGui v%major
Group: System/Libraries
Requires: %qtgui = %version-%release

%description -n %qtgui-minimal
Minimal (Framebuffer based) output driver for QtGui v%major

%package -n %qtnetwork
Summary: Qt Networking library
Group: System/Libraries

%description -n %qtnetwork
Qt Networking library

%package -n %qtnetworkd
Summary: Development files for version %major of the QtNetwork library
Group: Development/KDE and Qt
Requires: %qtnetwork = %version-%release

%description -n %qtnetworkd
Development files for version %major of the QtNetwork library

%package -n %qtopengl
Summary: Qt OpenGL (3D Graphics) library
Group: System/Libraries

%description -n %qtopengl
Qt OpenGL (3D Graphics) library

%package -n %qtopengld
Summary: Development files for version %major of the QtOpenGL library
Group: Development/KDE and Qt
Requires: %qtopengl = %version-%release

%description -n %qtopengld
Development files for version %major of the QtOpenGL library

%package -n %qtprintsupport
Summary: Qt printing library
Group: System/Libraries

%description -n %qtprintsupport
Qt printing library

%package -n %qtprintsupportd
Summary: Development files for version %major of the QtPrintSupport library
Group: Development/KDE and Qt
Requires: %qtprintsupport = %version-%release

%description -n %qtprintsupportd
Development files for version %major of the QtPrintSupport library

%package -n %qtsql
Summary: Qt SQL library
Group: System/Libraries

%description -n %qtsql
Qt SQL library

%package -n %qtsql-sqlite
Summary: SQLite 3.x support for the QtSql library v%major
Group: System/Libraries
Requires: %qtsql = %version-%release
BuildRequires: pkgconfig(sqlite3)

%description -n %qtsql-sqlite
SQLite 3.x support for the QtSql library v%major

%package -n %qtsql-mysql
Summary: MySQL support for the QtSql library v%major
Group: System/Libraries
Requires: %qtsql = %version-%release
BuildRequires: mysql-devel

%description -n %qtsql-mysql
MySQL support for the QtSql library v%major

%package -n %qtsql-odbc
Summary: ODBC support for the QtSql library v%major
Group: System/Libraries
Requires: %qtsql = %version-%release
BuildRequires: pkgconfig(libiodbc)

%description -n %qtsql-odbc
ODBC support for the QtSql library v%major

%package -n %qtsql-postgresql
Summary: PostgreSQL support for the QtSql library v%major
Group: System/Libraries
Requires: %qtsql = %version-%release
BuildRequires: postgresql-devel >= 9.0

%description -n %qtsql-postgresql
PostgreSQL support for the QtSql library v%major

%package -n %qtsqld
Summary: Development files for version %major of the QtSql library
Group: Development/KDE and Qt
Requires: %qtsql = %version-%release

%description -n %qtsqld
Development files for version %major of the QtSql library

%package -n %qttest
Summary: Qt unit test library
Group: System/Libraries

%description -n %qttest
Qt unit test library

%package -n %qttestd
Summary: Development files for version %major of the QtTest library
Group: Development/KDE and Qt
Requires: %qttest = %version-%release

%description -n %qttestd
Development files for version %major of the QtTest library

%package -n %qtwidgets
Summary: Qt Widget library
Group: System/Libraries

%description -n %qtwidgets
Qt Widget library

%package -n %qtwidgetsd
Summary: Development files for version %major of the QtWidgets library
Group: Development/KDE and Qt
Requires: %qtwidgets = %version-%release

%description -n %qtwidgetsd
Development files for version %major of the QtWidgets library

%package -n %qtxml
Summary: Qt XML library
Group: System/Libraries

%description -n %qtxml
Qt XML library

%package -n %qtxmld
Summary: Development files for version %major of the QtXml library
Group: Development/KDE and Qt
Requires: %qtxml = %version-%release

%description -n %qtxmld
Development files for version %major of the QtXml library

%package -n qdoc%major
Summary: Qt documentation generator, version %major
Group: Development/KDE and Qt

%description -n qdoc%major
Qt documentation generator, version %major

%package examples
Summary: Example applications for %name
Group: Development/KDE and Qt

%description examples
Example applications for %name

%package fonts
Summary: Fonts for use with some %name output plugins
Group: System/Libraries

%description fonts
Fonts for use with some %name output plugins

These fonts are required for various non-X11 output
plugins (framebuffer device etc.).

They are not required for the normal X11 output.

%package -n %gruesensor
Summary: Sample sensor plugin for the Qt %major sensor library
Group: System/Libraries

%description -n %gruesensor
Sample sensor plugin for the Qt %major sensor library

%package -n %qgsttools_p
Summary: GStreamer helper library for Qt %major
Group: System/Libraries

%description -n %qgsttools_p
GStreamer helper library for Qt %major

%package -n %qt3d
Summary: Qt %major 3D math library
Group: System/Libraries

%description -n %qt3d
Qt %major 3D math library

%package -n %qt3dd
Summary: Development files for the Qt %major 3D math library
Group: Development/KDE and Qt
Requires: %qt3d = %version-%release

%description -n %qt3dd
Development files for the Qt %major 3D math library

%package -n %qt3dquick
Summary: Qt %major library for 3D QtQuick components
Group: System/Libraries

%description -n %qt3dquick
Qt %major library for 3D QtQuick components

%package -n %qt3dquickd
Summary: Development files for the Qt %major 3D QtQuick library
Group: Development/KDE and Qt
Requires: %qt3d = %version-%release

%description -n %qt3dquickd
Development files for the Qt %major 3D QtQuick library

%package -n %qtclucene
Summary: Qt version of the CLucene search engine library
Group: System/Libraries

%description -n %qtclucene
Qt version of the CLucene search engine library

%package -n %qtclucened
Summary: Development files for the Qt version of the CLucene search engine library
Group: Development/KDE and Qt
Requires: %qtclucene = %version-%release

%description -n %qtclucened
Development files for the Qt version of the CLucene search engine library

%package -n %qtdesignercomponents
Summary: Qt Designer %major component library
Group: System/Libraries

%description -n %qtdesignercomponents
Qt Designer %major component library

%package -n %qtdesignercomponentsd
Summary: Development files for the Qt Designer components library
Group: Development/KDE and Qt
Requires: %qtdesignercomponents = %version-%release

%description -n %qtdesignercomponentsd
Development files for the Qt Designer components library

%package -n %qtdesigner
Summary: Qt Designer %major runtime libraries
Group: System/Libraries

%description -n %qtdesigner
Qt Designer %major runtime libraries

%package -n %qtdesignerd
Summary: Development files for Qt %major Designer
Group: Development/KDE and Qt
Requires: %qtdesigner = %version-%release

%description -n %qtdesignerd
Development files for Qt %major Designer

%package -n %qthelp
Summary: Qt library for providing a help system
Group: System/Libraries

%description -n %qthelp
Qt library for providing a help system

%package -n %qthelpd
Summary: Development files for the Qt %major help library
Group: Development/KDE and Qt
Requires: %qthelp = %version-%release

%description -n %qthelpd
Development files for the Qt %major help library

%package -n %qtlocation
Summary: Qt library for location dependent services
Group: System/Libraries

%description -n %qtlocation
Qt library for location dependent services

%package -n %qtlocationd
Summary: Development files for the Qt Location library
Group: Development/KDE and Qt
Requires: %qtlocation = %version-%release

%description -n %qtlocationd
Development files for the Qt Location library

%package -n %qtmultimedia
Summary: Qt %major Multimedia library
Group: System/Libraries

%description -n %qtmultimedia
Qt %major Multimedia library

%package -n %qtmultimediad
Summary: Development files for the Qt multimedia library
Group: Development/KDE and Qt
Requires: %qtmultimedia = %version-%release

%description -n %qtmultimediad
Development files for the Qt multimedia library

%define qtmultimediaquick_p %mklibname qtmultimediaquick_p %major
%package -n %qtmultimediaquick_p
Summary: Helper library for using multimedia components in QtQuick
Group: System/Libraries

%description -n %qtmultimediaquick_p
Helper library for using multimedia components in QtQuick

%define qtmultimediawidgets %mklibname qtmultimediawidgets %major
%define qtmultimediawidgetsd %mklibname qtmultimediawidgets%major -d
%package -n %qtmultimediawidgets
Summary: Qt multimedia widget library
Group: System/Libraries

%description -n %qtmultimediawidgets
Qt multimedia widget library

%package -n %qtmultimediawidgetsd
Summary: Development files for the Qt multimedia widgets library
Group: Development/KDE and Qt
Requires: %qtmultimediawidgets = %version-%release

%description -n %qtmultimediawidgetsd
Development files for the Qt multimedia widgets library

%package -n %qtpublishsubscribe
Summary: Qt Publish Subscribe library
Group: System/Libraries

%description -n %qtpublishsubscribe
Qt Publish Subscribe library.

The Qt Publish Subscribe module enables applications to read item values,
navigate through and subscribe to change notifications.

%package -n %qtpublishsubscribed
Summary: Development files for the Qt Publish Subscribe Library
Group: Development/KDE and Qt
Requires: %qtpublishsubscribe = %version-%release

%description -n %qtpublishsubscribed
Development files for the Qt Publish Subscribe Library

%package -n %qtqml
Summary: Qt QML Library
Group: System/Libraries

%description -n %qtqml
Qt QML Library

%package -n %qtqmld
Summary: Development files for the Qt QML library
Group: Development/KDE and Qt
Requires: %qtqml = %version-%release

%description -n %qtqmld
Development files for the Qt QML library

%package -n %qtquick1
Summary: QtQuick 1.x backwards compatibility library
Group: System/Libraries

%description -n %qtquick1
QtQuick 1.x backwards compatibility library

%package -n %qtquick1d
Summary: Development files for the QtQuick 1.x backwards compatibility library
Group: Development/KDE and Qt
Requires: %qtquick1 = %version-%release

%description -n %qtquick1d
Development files for the QtQuick 1.x backwards compatibility library

%package -n %qtquick
Summary: QtQuick 2.x support library
Group: System/Libraries

%description -n %qtquick
QtQuick 2.x support library

%package -n %qtquickd
Summary: Development files for the QtQuick library
Group: Development/KDE and Qt
Requires: %qtquick = %version-%release

%description -n %qtquickd
Development files for the QtQuick library

%package -n %qtquicktest
Summary: Autotest framework for QtQuick
Group: System/Libraries

%description -n %qtquicktest
Autotest framework for QtQuick

%package -n %qtquicktestd
Summary: Development files for the QtQuick test library
Group: Development/KDE and Qt
Requires: %qtquicktest = %version-%release

%description -n %qtquicktestd
Development files for the QtQuick test library

%package -n %qtscript
Summary: QtScript library
Group: System/Libraries

%description -n %qtscript
QtScript library

%package -n %qtscriptd
Summary: Development files for QtScript
Group: Development/KDE and Qt
Requires: %qtscript = %version-%release

%description -n %qtscriptd
Development files for QtScript

%package -n %qtscripttools
Summary: QtScript tools library
Group: System/Libraries

%description -n %qtscripttools
QtScript tools library

%package -n %qtscripttoolsd
Summary: Development files for the QtScript tools library
Group: Development/KDE and Qt
Requires: %qtclucene = %version-%release

%description -n %qtscripttoolsd
Development files for the QtScript tools library

%package -n %qtsensors
Summary: Qt Sensor access library
Group: System/Libraries

%description -n %qtsensors
Qt Sensor access library

%package -n %qtsensorsd
Summary: Development files for the Qt Sensor library
Group: Development/KDE and Qt
Requires: %qtclucene = %version-%release

%description -n %qtsensorsd
Development files for the Qt Sensor library

%package -n %qtserviceframework
Summary: Qt Service Framework
Group: System/Libraries

%description -n %qtserviceframework
Qt Service Framework.

A set of Qt APIs that allows clients to discover and instantiate
arbitrary services.

%package -n %qtserviceframeworkd
Summary: Development files for the Qt Service Framework
Group: Development/KDE and Qt
Requires: %qtserviceframework = %version-%release

%description -n %qtserviceframeworkd
Development files for the Qt Service Framework, a set of Qt APIs
that allows clients to discover and instantiate arbitrary services.

%package -n %qtsvg
Summary: Qt SVG rendering library
Group: System/Libraries

%description -n %qtsvg
Qt SVG rendering library

%package -n %qtsvgd
Summary: Development files for the Qt SVG rendering library
Group: Development/KDE and Qt
Requires: %qtsvg = %version-%release

%description -n %qtsvgd
Development files for the Qt SVG rendering library

%package -n %qtsysteminfo
Summary: Qt System Info library
Group: System/Libraries

%description -n %qtsysteminfo
Qt System Info library.

The Qt System Info module provides a set of APIs to discover system
related information and capabilities, including the batteries being used,
activated locks, different hardware features, network, screen saver, and
storage, etc.

%package -n %qtsysteminfod
Summary: Development files for the Qt System Info library
Group: Development/KDE and Qt
Requires: %qtsysteminfo = %version-%release

%description -n %qtsysteminfod
Development files for the Qt System Info library

The Qt System Info module provides a set of APIs to discover system
related information and capabilities, including the batteries being used,
activated locks, different hardware features, network, screen saver, and
storage, etc.

%package -n %qtv8
Summary: Qt version of the V8 JavaScript engine
Group: System/Libraries

%description -n %qtv8
Qt version of the V8 JavaScript engine

%package -n %qtv8d
Summary: Development files for the Qt version of the V8 JavaScript engine
Group: Development/KDE and Qt
Requires: %qtv8 = %version-%release

%description -n %qtv8d
Development files for the Qt version of the V8 JavaScript engine

%package -n %qtwebkit
Summary: Qt WebKit (HTML/SVG/... rendering) library
Group: System/Libraries

%description -n %qtwebkit
Qt WebKit (HTML/SVG/... rendering) library

%package -n %qtwebkitd
Summary: Development files for the QtWebKit HTML renderer
Group: Development/KDE and Qt
Requires: %qtwebkit = %version-%release

%description -n %qtwebkitd
Development files for the Qt WebKit HTML/SVG/... renderer

%package -n %qtxmlpatterns
Summary: Qt XPath/XQuery/XSLT/XML Schema library
Group: System/Libraries

%description -n %qtxmlpatterns
Qt XPath/XQuery/XSLT/XML Schema library

%package -n %qtxmlpatternsd
Summary: Development files for the Qt XPath/XQuery/XSLT/XML Schema library
Group: Development/KDE and Qt
Requires: %qtxmlpatterns = %version-%release

%description -n %qtxmlpatternsd
Development files for the Qt XPath/XQuery/XSLT/XML Schema library

%package assistant
Summary: Qt help file reader
Group: Development/KDE and Qt

%description assistant
Qt help file reader

%package designer
Summary: Graphical interface designer for Qt
Group: Development/KDE and Qt

%description designer
Graphical interface designer for Qt

%package linguist
Summary: Graphical translation tool for Qt
Group: Development/KDE and Qt
Requires: %name-l10n-tools = %version-%release

%description linguist
Graphical translation tool for Qt

%package l10n-tools
Summary: Tools for working with Qt translation files
Group: Development/KDE and Qt
Suggests: %name-linguist = %version-%release

%description l10n-tools
Tools for working with Qt translation files

%package dbus-tools
Summary: Tools for working with D-Bus
Group: Development/KDE and Qt

%description dbus-tools
Tools for working with D-Bus

%package help-tools
Summary: Tools for working with Qt help files
Group: Development/KDE and Qt

%description help-tools
Tools for working with Qt help files

%package quick
Summary: Tools for working with QtQuick
Group: Development/KDE and Qt

%description quick
Tools for working with QtQuick

%package xmlpatterns-tools
Summary: Tools for running XMLPatterns queries
Group: Development/KDE and Qt

%description xmlpatterns-tools
Tools for running XMLPatterns queries

%package tools
Summary: Assorted tools that come with Qt
Group: Development/KDE and Qt

%description tools
Assorted tools that come with Qt

%prep
%setup -q -n qt-everywhere-opensource-src-%version
%patch0 -p1 -b .qtjsondb_dep~

# Enable STDC++11 support for all but QtWebKit (doesn't work yet)
sed -i -e "s|-O2|%optflags -std=gnu++0x|g" qtbase/mkspecs/common/g++-base.conf
sed -i -e "s|-O2|%optflags|g" -e 's|^QMAKE_CXXFLAGS .*|& -std=gnu++0x|' qtbase/mkspecs/common/gcc-base.conf

# Regenerate parsers with current flex to fix some bugs
pushd qtwebkit/Source/ThirdParty/ANGLE/src/compiler
./generate_parser.sh
popd

# WebKit isn't ready for C++11 yet
find qtwebkit/Source -name "*.pro" -o -name "*.pri" |while read r; do
	# Some *.pro files don't have a trailing newline, so
	# echo 'QMAKE_CXXFLAGS...' >>$r doesn't quite do what
	# it should do. Let's add a newline first.
	echo >>$r
	echo 'QMAKE_CXXFLAGS -= -std=gnu++0x' >>$r
done
echo 'QMAKE_CXXFLAGS -= -std=gnu++0x' >>qtwebkit/Source/QtWebKit.pro

# Correct path names to pass to configure would be
#
#	-prefix %_qt_prefix \
#	-bindir %_qt_bindir \
#	-libdir %_qt_libdir \
#	-docdir %_qt_docdir \
#	-headerdir %_qt_includedir \
#	-plugindir %_qt_plugindir \
#	-importdir %_qt_importdir \
#	-translationdir %_qt_translationsdir \
#	-sysconfdir %_qt_sysconfdir \
#	-examplesdir %_qt_exampledir \
#	-testsdir %_qt_testsdir
#
# but unfortunately Qt5 doesn't bootstrap unless the
# specified locations (the final ones) are writable by
# non-qtbase components.
#
# So the idea is to build qtbase in a temporary location
# so the non-qtbase components can be built, and fix the
# resulting incorrect pathname hardcodes manually.

./configure \
	%options \
	-prefix `pwd`/qtbase

%build
CPUS="`echo %?_smp_mflags |sed -e 's,.*-j,,g;s, .*,,g'`"
[ -z "$CPUS" ] && CPUS="`getconf _NPROCESSORS_ONLN`"
[ -z "$CPUS" ] && CPUS="`cat /proc/cpuinfo |grep -c processor`"
[ -z "$CPUS" ] && CPUS=2
[ "$CPUS" = "0" ] && CPUS=2
STRIP=true ./build -j $CPUS

# Fix up listed dependencies...
sed -i -e "s,`pwd`/qtbase/lib,%_qt_libdir,g;s,`pwd`/qtbase,%_qt_prefix,g" qtbase/lib/*.prl
sed -i -e "s,`pwd`/qtbase/lib,%_qt_libdir,g;s,`pwd`/qtbase,%_qt_prefix,g" qtbase/lib/pkgconfig/*.pc

# Fix up hardcoded locations
sed -i \
	-e 's,qt_prfxpath=[^"]*,qt_prfxpath=%_qt_prefix,g' \
	-e 's,qt_docspath=[^"]*,qt_docspath=%_qt_docdir,g' \
	-e 's,qt_hdrspath=[^"]*,qt_hdrspath=%_qt_includedir,g' \
	-e 's,qt_libspath=[^"]*,qt_libspath=%_qt_libdir,g' \
	-e 's,qt_binspath=[^"]*,qt_binspath=%_qt_bindir,g' \
	-e 's,qt_plugpath=[^"]*,qt_plugpath=%_qt_plugindir,g' \
	-e 's,qt_impspath=[^"]*,qt_impspath=%_qt_importdir,g' \
	-e 's,qt_datapath=[^"]*,qt_datapath=%_qt_prefix,g' \
	-e 's,qt_trnspath=[^"]*,qt_trnspath=%_qt_translationsdir,g' \
	-e 's,qt_xmplpath=[^"]*,qt_xmplpath=%_qt_exampledir,g' \
	-e 's,qt_tstspath=[^"]*,qt_tstspath=%_qt_testsdir,g' \
	-e 's,qt_hpfxpath=[^"]*,qt_hpfxpath=%_qt_prefix,g' \
	-e 's,qt_hbinpath=[^"]*,qt_hbinpath=%_qt_bindir,g' \
	-e 's,qt_hdatpath=[^"]*,qt_hdatpath=%_qt_prefix,g' \
	qtbase/src/corelib/global/qconfig.cpp

# And rebuild important parts... (Stuff that #includes qconfig.cpp)
find qtbase/src/tools -name main.o |xargs rm -f
find qtbase -name qlibraryinfo.o |xargs rm -f
cd qtbase
%make STRIP=true QMAKE=/bin/true
cd qmake
%make STRIP=true QMAKE=/bin/true

# Fix Makefiles for "make install"
find . -name Makefile |xargs sed -i -e "s,`pwd`/qtbase/lib,%_qt_libdir,g;s,`pwd`/qtbase,%_qt_prefix,g"

# Point rpaths at the final destination
# Allowing this to fail so we don't have to e.g. list
# every binary implicitly to avoid trying to change
# the rpath on a perl script
cd ../lib
chrpath -k -r %_qt_libdir *.so.* || :
cd ../bin
chrpath -k -r %_qt_libdir * || :


%install
mkdir -p %buildroot%_qt_prefix
cp -a qtbase/lib %buildroot%_qt_libdir
cp -a qtbase/bin %buildroot%_qt_bindir
cp -a qtbase/include %buildroot%_qt_includedir
cp -a qtbase/imports %buildroot%_qt_importdir
cp -a qtbase/examples %buildroot%_qt_exampledir
cp -a qtbase/mkspecs %buildroot%_qt_prefix/
mkdir -p %buildroot`dirname %_qt_plugindir`
cp -a qtbase/plugins %buildroot%_qt_plugindir

# Installed, but not useful
rm -f %buildroot%_qt_bindir/syncqt %buildroot%_qt_bindir/*.bat
# Probably not useful outside of Qt source tree?
rm -f %buildroot%_qt_bindir/qtmodule-configtests
rm -f %buildroot%_qt_libdir/README
# Death to libtool!
rm -f %buildroot%_qt_libdir/*.la

cd %buildroot%_libdir
ln -s ../lib/qt5/%_lib/*.so.* .

%files assistant
%_qt_bindir/assistant

%files designer
%_qt_bindir/designer

%files linguist
%_qt_bindir/linguist

%files l10n-tools
%_qt_bindir/findtr
%_qt_bindir/lconvert
%_qt_bindir/lrelease
%_qt_bindir/lupdate
%_qt_libdir/cmake/Qt5LinguistTools

%files dbus-tools
%_qt_bindir/qdbus*
%_qt_libdir/cmake/Qt5DBusTools

%files help-tools
%_qt_bindir/qhelpconverter
%_qt_bindir/qhelpgenerator

%files quick
%_qt_bindir/qmlmin
%_qt_bindir/qmlplugindump
%_qt_bindir/qmlprofiler
%_qt_bindir/qmlscene
%_qt_bindir/qmltestrunner
%_qt_bindir/qmlviewer
%_qt_importdir
%_qt_libdir/cmake/Qt5QmlDevTools
%dir %_qt_plugindir/qmltooling
%_qt_plugindir/qmltooling/libqmldbg_*.so

%files xmlpatterns-tools
%_qt_bindir/xmlpatterns
%_qt_bindir/xmlpatternsvalidator

%files tools
%_qt_bindir/QtWebProcess
%_qt_bindir/fixqt4headers.pl
%_qt_bindir/pixeltool
%_qt_bindir/qcollectiongenerator
%_qt_bindir/servicefw
%_qt_bindir/qttracereplay

%files -n %qtconcurrent
%_qt_libdir/libQtConcurrent.so.*
%_libdir/libQtConcurrent.so.*

%files -n %qtconcurrentd
%_qt_libdir/libQtConcurrent.so
%_qt_libdir/libQtConcurrent.prl
%_qt_libdir/pkgconfig/QtConcurrent.pc
%_qt_includedir/QtConcurrent
%_qt_includedir/Qt/QtConcurrent
%_qt_libdir/cmake/Qt%{major}Concurrent

%files -n %qtcore
%_qt_libdir/libQtCore.so.*
%_libdir/libQtCore.so.*
%dir %_libdir/qt5/plugins
%dir %_libdir/qt5/plugins/generic
%_libdir/qt5/plugins/generic/libqevdev*.so

%files -n %qtcored
%_qt_bindir/moc
%_qt_bindir/rcc
%_qt_libdir/libQtCore.so
%_qt_libdir/libQtCore.prl
%_qt_includedir/QtCore
%dir %_qt_libdir/cmake
%dir %_qt_libdir/pkgconfig
%_qt_libdir/pkgconfig/QtCore.pc
%_qt_libdir/cmake/Qt%{major}Core
%dir %_qt_includedir/Qt
%_qt_includedir/Qt/*.h
%_qt_includedir/Qt/QtCore

%files -n %qtdbus
%_qt_libdir/libQtDBus.so.*
%_libdir/libQtDBus.so.*

%files -n %qtdbusd
%_qt_libdir/libQtDBus.so
%_qt_libdir/libQtDBus.prl
%_qt_libdir/pkgconfig/QtDBus.pc
%_qt_includedir/QtDBus
%_qt_includedir/Qt/QtDBus
%_qt_libdir/cmake/Qt%{major}DBus

%files -n qmake%major
%_qt_bindir/qmake
%_qt_prefix/mkspecs

%files -n %qtgui
%_qt_libdir/libQtGui.so.*
%_libdir/libQtGui.so.*
%_libdir/qt5/plugins/imageformats
%dir %_libdir/qt5/plugins/platforminputcontexts
%dir %_libdir/qt5/plugins/platforms

%files -n %qtgui-x11
%_libdir/qt5/plugins/platforms/libxcb.so
%_libdir/qt5/plugins/platforminputcontexts/libibusplatforminputcontextplugin.so
%_libdir/qt5/plugins/platforminputcontexts/libmaliitplatforminputcontextplugin.so

%files -n %qtgui-minimal
%_libdir/qt5/plugins/platforms/libqminimal.so

%files -n %qtguid
%_qt_libdir/libQtGui.so
%_qt_libdir/libQtGui.prl
%_qt_libdir/pkgconfig/QtGui.pc
%_qt_includedir/QtGui
%_qt_includedir/Qt/QtGui
%_qt_libdir/cmake/Qt%{major}Gui
%_qt_libdir/libQtPlatformSupport.a
%_qt_libdir/libQtPlatformSupport.prl
%_qt_libdir/pkgconfig/QtPlatformSupport.pc
%_qt_libdir/cmake/Qt%{major}PlatformSupport
%_qt_includedir/QtPlatformSupport
%_qt_includedir/Qt/QtPlatformSupport

%files -n %qtnetwork
%_qt_libdir/libQtNetwork.so.*
%_libdir/libQtNetwork.so.*
%_libdir/qt5/plugins/bearer

%files -n %qtnetworkd
%_qt_libdir/libQtNetwork.so
%_qt_libdir/libQtNetwork.prl
%_qt_libdir/pkgconfig/QtNetwork.pc
%_qt_includedir/QtNetwork
%_qt_includedir/Qt/QtNetwork
%_qt_libdir/cmake/Qt%{major}Network

%files -n %qtopengl
%_qt_libdir/libQtOpenGL.so.*
%_libdir/libQtOpenGL.so.*

%files -n %qtopengld
%_qt_libdir/libQtOpenGL.so
%_qt_libdir/libQtOpenGL.prl
%_qt_libdir/pkgconfig/QtOpenGL.pc
%_qt_includedir/QtOpenGL
%_qt_includedir/Qt/QtOpenGL
%_qt_libdir/cmake/Qt%{major}OpenGL

%files -n %qtprintsupport
%_qt_libdir/libQtPrintSupport.so.*
%_libdir/libQtPrintSupport.so.*

%files -n %qtprintsupportd
%_qt_libdir/libQtPrintSupport.so
%_qt_libdir/libQtPrintSupport.prl
%_qt_libdir/pkgconfig/QtPrintSupport.pc
%_qt_includedir/QtPrintSupport
%_qt_includedir/Qt/QtPrintSupport
%_qt_libdir/cmake/Qt%{major}PrintSupport

%files -n %qtsql
%_qt_libdir/libQtSql.so.*
%_libdir/libQtSql.so.*
%dir %_libdir/qt5/plugins/sqldrivers

%files -n %qtsql-sqlite
%_libdir/qt5/plugins/sqldrivers/libqsqlite.so

%files -n %qtsql-mysql
%_libdir/qt5/plugins/sqldrivers/libqsqlmysql.so

%files -n %qtsql-odbc
%_libdir/qt5/plugins/sqldrivers/libqsqlodbc.so

%files -n %qtsql-postgresql
%_libdir/qt5/plugins/sqldrivers/libqsqlpsql.so

%files -n %qtsqld
%_qt_libdir/libQtSql.so
%_qt_libdir/libQtSql.prl
%_qt_libdir/pkgconfig/QtSql.pc
%_qt_includedir/QtSql
%_qt_includedir/Qt/QtSql
%_qt_libdir/cmake/Qt%{major}Sql

%files -n %qttest
%_qt_libdir/libQtTest.so.*
%_libdir/libQtTest.so.*

%files -n %qttestd
%_qt_libdir/libQtTest.so
%_qt_libdir/libQtTest.prl
%_qt_libdir/pkgconfig/QtTest.pc
%_qt_includedir/QtTest
%_qt_includedir/Qt/QtTest
%_qt_libdir/cmake/Qt%{major}Test

%files -n %qtwidgets
%_qt_libdir/libQtWidgets.so.*
%_libdir/libQtWidgets.so.*
%_libdir/qt5/plugins/accessible

%files -n %qtwidgetsd
%_qt_libdir/libQtWidgets.so
%_qt_libdir/libQtWidgets.prl
%_qt_libdir/pkgconfig/QtWidgets.pc
%_qt_includedir/QtWidgets
%_qt_includedir/Qt/QtWidgets
%_qt_libdir/cmake/Qt%{major}Widgets

%files -n %qtxml
%_qt_libdir/libQtXml.so.*
%_libdir/libQtXml.so.*

%files -n %qtxmld
%_qt_libdir/libQtXml.so
%_qt_libdir/libQtXml.prl
%_qt_libdir/pkgconfig/QtXml.pc
%_qt_includedir/QtXml
%_qt_includedir/Qt/QtXml
%_qt_libdir/cmake/Qt%{major}Xml

%files -n %gruesensor
%_qt_libdir/libgruesensor.so*
%_libdir/libgruesensor.so*

%files -n %qgsttools_p
%_qt_libdir/libqgsttools_p.so*
%_libdir/libqgsttools_p.so*

%files -n %qt3d
%_qt_libdir/libQt3D.so.*
%_libdir/libQt3D.so.*

%files -n %qt3dd
%_qt_libdir/libQt3D.so
%_qt_libdir/libQt3D.prl
%_qt_libdir/pkgconfig/Qt3D.pc
%_qt_includedir/Qt3D
%_qt_includedir/Qt/Qt3D
%_qt_libdir/cmake/Qt%{major}3D

%files -n %qt3dquick
%_qt_libdir/libQt3DQuick.so.*
%_libdir/libQt3DQuick.so.*

%files -n %qt3dquickd
%_qt_libdir/libQt3DQuick.so
%_qt_libdir/libQt3DQuick.prl
%_qt_libdir/pkgconfig/Qt3DQuick.pc
%_qt_includedir/Qt3DQuick
%_qt_includedir/Qt/Qt3DQuick
%_qt_libdir/cmake/Qt%{major}3DQuick

%files -n %qtclucene
%_qt_libdir/libQtCLucene.so.*
%_libdir/libQtCLucene.so.*

%files -n %qtclucened
%_qt_libdir/libQtCLucene.so
%_qt_libdir/libQtCLucene.prl
%_qt_libdir/pkgconfig/QtCLucene.pc
%_qt_includedir/QtCLucene
%_qt_includedir/Qt/QtCLucene
%_qt_libdir/cmake/Qt%{major}CLucene

%files -n %qtdesignercomponents
%_qt_libdir/libQtDesignerComponents.so.*
%_libdir/libQtDesignerComponents.so.*

%files -n %qtdesignercomponentsd
%_qt_libdir/libQtDesignerComponents.so
%_qt_libdir/libQtDesignerComponents.prl
%_qt_libdir/pkgconfig/QtDesignerComponents.pc
%_qt_includedir/QtDesignerComponents
%_qt_includedir/Qt/QtDesignerComponents
%_qt_libdir/cmake/Qt%{major}DesignerComponents

%files -n %qtdesigner
%_qt_libdir/libQtDesigner.so.*
%_libdir/libQtDesigner.so.*

%files -n %qtdesignerd
%_qt_bindir/uic
%_qt_libdir/libQtDesigner.so
%_qt_libdir/libQtDesigner.prl
%_qt_libdir/pkgconfig/QtDesigner.pc
%_qt_libdir/pkgconfig/QtUiTools.pc
%_qt_includedir/QtDesigner
%_qt_includedir/Qt/QtDesigner
%_qt_includedir/QtUiTools
%_qt_includedir/Qt/QtUiTools
%_qt_libdir/cmake/Qt5UiTools
%_qt_libdir/libQtUiTools.a
%_qt_libdir/libQtUiTools.prl
%_qt_libdir/cmake/Qt%{major}Designer

%files -n %qthelp
%_qt_libdir/libQtHelp.so.*
%_libdir/libQtHelp.so.*

%files -n %qthelpd
%_qt_libdir/libQtHelp.so
%_qt_libdir/libQtHelp.prl
%_qt_libdir/pkgconfig/QtHelp.pc
%_qt_includedir/QtHelp
%_qt_includedir/Qt/QtHelp
%_qt_libdir/cmake/Qt%{major}Help

%files -n %qtlocation
%_qt_libdir/libQtLocation.so.*
%_libdir/libQtLocation.so.*
%dir %_qt_plugindir/geoservices
%_qt_plugindir/geoservices/libqtgeoservices_nokia.so

%files -n %qtlocationd
%_qt_libdir/libQtLocation.so
%_qt_libdir/libQtLocation.prl
%_qt_libdir/pkgconfig/QtLocation.pc
%_qt_includedir/QtLocation
%_qt_includedir/Qt/QtLocation
%_qt_libdir/cmake/Qt%{major}Location

%files -n %qtmultimedia
%_qt_libdir/libQtMultimedia.so.*
%_libdir/libQtMultimedia.so.*
%dir %_qt_plugindir/audio
%_qt_plugindir/audio/libqtmedia_pulse.so
%dir %_qt_plugindir/mediaservice
%_qt_plugindir/mediaservice/libqgstengine.so
%dir %_qt_plugindir/playlistformats
%_qt_plugindir/playlistformats/libqtmultimedia_m3u.so

%files -n %qtmultimediad
%_qt_libdir/libQtMultimedia.so
%_qt_libdir/libQtMultimedia.prl
%_qt_libdir/pkgconfig/QtMultimedia.pc
%_qt_includedir/QtMultimedia
%_qt_includedir/Qt/QtMultimedia
%_qt_libdir/cmake/Qt%{major}Multimedia

%files -n %qtmultimediaquick_p
%_qt_libdir/libQtMultimediaQuick_p.so*
%_qt_libdir/libQtMultimediaQuick_p.prl
%_libdir/libQtMultimediaQuick_p.so*

%files -n %qtmultimediawidgets
%_qt_libdir/libQtMultimediaWidgets.so.*
%_libdir/libQtMultimediaWidgets.so.*

%files -n %qtmultimediawidgetsd
%_qt_libdir/libQtMultimediaWidgets.so
%_qt_libdir/libQtMultimediaWidgets.prl
%_qt_libdir/pkgconfig/QtMultimediaWidgets.pc
%_qt_includedir/QtMultimediaWidgets
%_qt_includedir/Qt/QtMultimediaWidgets
%_qt_libdir/cmake/Qt%{major}MultimediaWidgets

%files -n %qtpublishsubscribe
%_qt_libdir/libQtPublishSubscribe.so.*
%_libdir/libQtPublishSubscribe.so.*

%files -n %qtpublishsubscribed
%_qt_libdir/libQtPublishSubscribe.so
%_qt_libdir/libQtPublishSubscribe.prl
%_qt_libdir/pkgconfig/QtPublishSubscribe.pc
%_qt_includedir/QtPublishSubscribe
%_qt_includedir/Qt/QtPublishSubscribe
%_qt_libdir/cmake/Qt%{major}PublishSubscribe

%files -n %qtqml
%_qt_libdir/libQtQml.so.*
%_libdir/libQtQml.so.*
%dir %_qt_plugindir/sceneformats
%_qt_plugindir/sceneformats/libqsceneai.so
%_qt_plugindir/sceneformats/libqscenebezier.so

%files -n %qtqmld
%_qt_libdir/libQtQml.so
%_qt_libdir/libQtQml.prl
%_qt_libdir/libQtQmlDevTools.a
%_qt_libdir/libQtQmlDevTools.prl
%_qt_libdir/pkgconfig/QtQml.pc
%_qt_libdir/pkgconfig/QtQmlDevTools.pc
%_qt_includedir/QtQml
%_qt_includedir/Qt/QtQml
%_qt_includedir/Qt/QDeclarative*
%_qt_includedir/Qt/QtDeclarative
%_qt_includedir/QtDeclarative
%_qt_includedir/QtQmlDevTools
%_qt_includedir/Qt/QtQmlDevTools
%_qt_includedir/Qt/QJS*
%_qt_libdir/cmake/Qt%{major}Qml

%files -n %qtquick1
%_qt_libdir/libQtQuick1.so.*
%_libdir/libQtQuick1.so.*

%files -n %qtquick1d
%_qt_libdir/libQtQuick1.so
%_qt_libdir/libQtQuick1.prl
%_qt_libdir/pkgconfig/QtQuick1.pc
%_qt_includedir/QtQuick1
%_qt_includedir/Qt/QtQuick1
%_qt_libdir/cmake/Qt%{major}Quick1

%files -n %qtquick
%_qt_libdir/libQtQuick.so.*
%_libdir/libQtQuick.so.*

%files -n %qtquickd
%_qt_libdir/libQtQuick.so
%_qt_libdir/libQtQuick.prl
%_qt_libdir/pkgconfig/QtQuick.pc
%_qt_includedir/QtQuick
%_qt_includedir/Qt/QtQuick
%_qt_libdir/cmake/Qt%{major}Quick

%files -n %qtquicktest
%_qt_libdir/libQtQuickTest.so.*
%_libdir/libQtQuickTest.so.*

%files -n %qtquicktestd
%_qt_libdir/libQtQuickTest.so
%_qt_libdir/libQtQuickTest.prl
%_qt_libdir/pkgconfig/QtQuickTest.pc
%_qt_includedir/QtQuickTest
%_qt_includedir/Qt/QtQuickTest
%_qt_libdir/cmake/Qt%{major}QuickTest

%files -n %qtscript
%_qt_libdir/libQtScript.so.*
%_libdir/libQtScript.so.*

%files -n %qtscriptd
%_qt_libdir/libQtScript.so
%_qt_libdir/libQtScript.prl
%_qt_libdir/pkgconfig/QtScript.pc
%_qt_includedir/QtScript
%_qt_includedir/Qt/QtScript
%_qt_libdir/cmake/Qt%{major}Script

%files -n %qtscripttools
%_qt_libdir/libQtScriptTools.so.*
%_libdir/libQtScriptTools.so.*

%files -n %qtscripttoolsd
%_qt_libdir/libQtScriptTools.so
%_qt_libdir/libQtScriptTools.prl
%_qt_libdir/pkgconfig/QtScriptTools.pc
%_qt_includedir/QtScriptTools
%_qt_includedir/Qt/QtScriptTools
%_qt_libdir/cmake/Qt%{major}ScriptTools

%files -n %qtsensors
%_qt_libdir/libQtSensors.so.*
%_libdir/libQtSensors.so.*
%dir %_qt_plugindir/sensorgestures
%_qt_plugindir/sensorgestures/*.so
%dir %_qt_plugindir/sensors
%_qt_plugindir/sensors/*.so

%files -n %qtsensorsd
%_qt_libdir/libQtSensors.so
%_qt_libdir/libQtSensors.prl
%_qt_libdir/pkgconfig/QtSensors.pc
%_qt_includedir/QtSensors
%_qt_includedir/Qt/QtSensors
%_qt_libdir/cmake/Qt%{major}Sensors

%files -n %qtserviceframework
%_qt_libdir/libQtServiceFramework.so.*
%_libdir/libQtServiceFramework.so.*

%files -n %qtserviceframeworkd
%_qt_libdir/libQtServiceFramework.so
%_qt_libdir/libQtServiceFramework.prl
%_qt_libdir/pkgconfig/QtServiceFramework.pc
%_qt_includedir/QtServiceFramework
%_qt_includedir/Qt/QtServiceFramework
%_qt_libdir/cmake/Qt%{major}ServiceFramework

%files -n %qtsvg
%_qt_libdir/libQtSvg.so.*
%_libdir/libQtSvg.so.*

%files -n %qtsvgd
%_qt_libdir/libQtSvg.so
%_qt_libdir/libQtSvg.prl
%_qt_libdir/pkgconfig/QtSvg.pc
%_qt_includedir/QtSvg
%_qt_includedir/Qt/QtSvg
%_qt_libdir/cmake/Qt%{major}Svg

%files -n %qtsysteminfo
%_qt_libdir/libQtSystemInfo.so.*
%_libdir/libQtSystemInfo.so.*

%files -n %qtsysteminfod
%_qt_libdir/libQtSystemInfo.so
%_qt_libdir/libQtSystemInfo.prl
%_qt_libdir/pkgconfig/QtSystemInfo.pc
%_qt_includedir/QtSystemInfo
%_qt_includedir/Qt/QtSystemInfo
%_qt_libdir/cmake/Qt%{major}SystemInfo

%files -n %qtv8
%_qt_libdir/libQtV8.so.*
%_libdir/libQtV8.so.*

%files -n %qtv8d
%_qt_libdir/libQtV8.so
%_qt_libdir/libQtV8.prl
%_qt_libdir/pkgconfig/QtV8.pc
%_qt_includedir/QtV8
%_qt_includedir/Qt/QtV8
%_qt_libdir/cmake/Qt%{major}V8

%files -n %qtwebkit
%_qt_libdir/libQtWebKit.so.*
%_libdir/libQtWebKit.so.*

%files -n %qtwebkitd
%_qt_libdir/libQtWebKit.so
%_qt_libdir/libQtWebKit.prl
%_qt_libdir/pkgconfig/QtWebKit.pc
%_qt_includedir/QtWebKit
%_qt_includedir/Qt/QtWebKit
%_qt_libdir/cmake/Qt%{major}WebKit

%files -n %qtxmlpatterns
%_qt_libdir/libQtXmlPatterns.so.*
%_libdir/libQtXmlPatterns.so.*

%files -n %qtxmlpatternsd
%_qt_libdir/libQtXmlPatterns.so
%_qt_libdir/libQtXmlPatterns.prl
%_qt_libdir/pkgconfig/QtXmlPatterns.pc
%_qt_includedir/QtXmlPatterns
%_qt_includedir/Qt/QtXmlPatterns
%_qt_libdir/cmake/Qt%{major}XmlPatterns

%files -n qdoc%major
%_qt_bindir/qdoc

%files examples
%_qt_prefix/examples

%files fonts
%_qt_libdir/fonts
