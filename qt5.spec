%define beta %nil
%define _qt_prefix %_prefix/lib/qt5
%define _qt_bindir %_qt_prefix/bin
%define _qt_docdir %_docdir/qt5
%define _qt_libdir %_prefix/lib/qt5/%_lib
%define _qt_libexecdir %_prefix/lib/qt5/libexec
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

# qtbase components
%define qtbootstrapd %mklibname qt%{major}bootstrap -d
%define qtconcurrent %mklibname qt%{major}concurrent %major
%define qtconcurrentd %mklibname qt%{major}concurrent%major -d
%define qtcore %mklibname qt%{major}core %major
%define qtcored %mklibname qt%{major}core -d
%define qtdbus %mklibname qt%{major}dbus %major
%define qtdbusd %mklibname qt%{major}dbus -d
%define qtgui %mklibname qt%{major}gui %major
%define qtguid %mklibname qt%{major}gui -d
%define qtnetwork %mklibname qt%{major}network %major
%define qtnetworkd %mklibname qt%{major}network -d
%define qtopengl %mklibname qt%{major}opengl %major
%define qtopengld %mklibname qt%{major}opengl -d
%define qtprintsupport %mklibname qt%{major}printsupport %major
%define qtprintsupportd %mklibname qt%{major}printsupport -d
%define qtsql %mklibname qt%{major}sql %major
%define qtsqld %mklibname qt%{major}sql -d
%define qttest %mklibname qt%{major}test %major
%define qttestd %mklibname qt%{major}test -d
%define qtwidgets %mklibname qt%{major}widgets %major
%define qtwidgetsd %mklibname qt%{major}widgets -d
%define qtxml %mklibname qt%{major}xml %major
%define qtxmld %mklibname qt%{major}xml -d

# Extras that might move to separate tarballs at some point
%define qgsttools_p %mklibname qgsttools_p 1
%define qtclucene %mklibname qt%{major}clucene %major
%define qtclucened %mklibname qt%{major}clucene -d
%define qtdeclarative %mklibname qt%{major}declarative %major
%define qtdeclaratived %mklibname qt%{major}declarative -d
%define qtdesignercomponents %mklibname qt%{major}designercomponents %major
%define qtdesignercomponentsd %mklibname qt%{major}designercomponents -d
%define qtdesigner %mklibname qt%{major}designer %major
%define qtdesignerd %mklibname qt%{major}designer -d
%define qthelp %mklibname qt%{major}help %major
%define qthelpd %mklibname qt%{major}help -d
%define qtmultimedia %mklibname qt%{major}multimedia %major
%define qtmultimediad %mklibname qt%{major}multimedia -d
%define qtmultimediaquick_p %mklibname qt%{major}multimediaquick_p %major
%define qtmultimediawidgets %mklibname qt%{major}multimediawidgets %major
%define qtmultimediawidgetsd %mklibname qt%{major}multimediawidgets -d
%define qtqml %mklibname qt%{major}qml %major
%define qtqmld %mklibname qt%{major}qml -d
%define qtquick %mklibname qt%{major}quick %major
%define qtquickd %mklibname qt%{major}quick -d
%define qtquickparticles %mklibname qt%{major}quickparticles %major
%define qtquickparticlesd %mklibname qt%{major}quickparticles -d
%define qtquicktest %mklibname qt%{major}quicktest %major
%define qtquicktestd %mklibname qt%{major}quicktest -d
%define qtscript %mklibname qt%{major}script %major
%define qtscriptd %mklibname qt%{major}script -d
%define qtscripttools %mklibname qt%{major}scripttools %major
%define qtscripttoolsd %mklibname qt%{major}scripttools -d
%define qtsvg %mklibname qt%{major}svg %major
%define qtsvgd %mklibname qt%{major}svg -d
%define qtv8 %mklibname qt%{major}v8 %major
%define qtv8d %mklibname qt%{major}v8 -d
%define qtwebkit %mklibname qt%{major}webkit %major
%define qtwebkitd %mklibname qt%{major}webkit -d
%define qtwebkitwidgets %mklibname qt%{major}webkitwidgets %major
%define qtwebkitwidgetsd %mklibname qt%{major}webkitwidgets -d
%define qtxmlpatterns %mklibname qt%{major}xmlpatterns %major
%define qtxmlpatternsd %mklibname qt%{major}xmlpatterns -d

%bcond_without directfb

Name: qt5
Version: 5.0.1
%if "%beta" == ""
Source0: http://releases.qt-project.org/qt5/%version/single/qt-everywhere-opensource-src-%version.tar.gz
Release: 1
%else
Source0: http://releases.qt-project.org/qt5.0/%beta/single/qt-everywhere-opensource-src-%version-%beta.tar.xz
Release: 0.%beta.1
%endif
Source100: %name.rpmlintrc
License: LGPLv3+
Summary: Version 5 of the Qt toolkit
URL: http://qt-project.org/
Group: Development/KDE and Qt

# CUPS
BuildRequires: cups-devel

# OpenGL
BuildRequires: pkgconfig(gl)

# Event loop
BuildRequires: pkgconfig(glib-2.0)

# ICU
BuildRequires: pkgconfig(icu-uc)

# Multimedia
BuildRequires: pkgconfig(gstreamer-0.10)

# For XCB platform plugin:
BuildRequires: pkgconfig(xcb) >= 1.5
BuildRequires: pkgconfig(xcb-icccm)
BuildRequires: pkgconfig(xcb-image)
BuildRequires: pkgconfig(xcb-renderutil)
BuildRequires: pkgconfig(xcb-keysyms)
BuildRequires: pkgconfig(xrender)

%if %with directfb
# DirectFB platform plugin:
BuildRequires: pkgconfig(directfb)
%endif

# Accessibility
BuildRequires: pkgconfig(atspi-2)

# Assorted...
BuildRequires: pkgconfig(libudev)
BuildRequires: flex bison gperf

%description
Version 5 of the Qt toolkit

%package -n %qtconcurrent
Summary: Qt threading library
Group: System/Libraries

%description -n %qtconcurrent
Qt threading library

%package -n %qtbootstrapd
Summary: Development files for version %major if the QtBootstrap library
Group: Development/KDE and Qt

%description -n %qtbootstrapd
Development files for version %major if the QtBootstrap library

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

%package -n %qtgui-linuxfb
Summary: Linux Framebuffer output driver for QtGui v%major
Group: System/Libraries
Requires: %qtgui = %version-%release

%description -n %qtgui-linuxfb
Linux Framebuffer output driver for QtGui v%major

%package -n %qtgui-directfb
Summary: DirectFB output driver for QtGui v%major
Group: System/Libraries
Requires: %qtgui = %version-%release

%description -n %qtgui-directfb
DirectFB output driver for QtGui v%major

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

%package -n %qgsttools_p
Summary: Runtime library for GStreamer support in Qt
Group: System/Libraries

%description -n %qgsttools_p
Runtime library for GStreamer support in Qt

%package -n %qtclucene
Summary: Qt version of the CLucene search engine
Group: System/Libraries

%description -n %qtclucene
Qt version of the CLucene search engine

%package -n %qtclucened
Summary: Development files for the Qt version of the CLucene search engine
Group: Development/KDE and Qt
Requires: %qtclucene = %EVRD

%description -n %qtclucened
Development files for the Qt version of the CLucene search engine

%package -n %qtdeclarative
Summary: Runtime library for Qt Declarative
Group: System/Libraries

%description -n %qtdeclarative
Runtime library for Qt Declarative

%package -n %qtdeclaratived
Summary: Development files for Qt Declarative
Group: Development/KDE and Qt
Requires: %qtdeclarative = %EVRD

%description -n %qtdeclaratived
Development files for Qt Declarative

%package -n %qtdesignercomponents
Summary: Components for Qt Designer
Group: System/Libraries

%description -n %qtdesignercomponents
Components for Qt Designer

%package -n %qtdesignercomponentsd
Summary: Development files for Qt Designer Components
Group: Development/KDE and Qt
Requires: %qtdesignercomponents = %EVRD

%description -n %qtdesignercomponentsd
Development files for Qt Designer Components

%package -n %qtdesigner
Summary: Qt Designer runtime libraries
Group: System/Libraries

%description -n %qtdesigner
Qt Designer runtime libraries

%package -n %qtdesignerd
Summary: Development files for Qt Designer
Group: Development/KDE and Qt
Requires: %qtdesigner = %EVRD

%description -n %qtdesignerd
Development files for Qt Designer

%package -n %qthelp
Summary: Runtime libraries for the Qt Help system
Group: System/Libraries

%description -n %qthelp
Runtime libraries for the Qt Help system

%package -n %qthelpd
Summary: Development files for Qt Help
Group: Development/KDE and Qt
Requires: %qthelp = %EVRD

%description -n %qthelpd
Development files for Qt Help, useful if you wish to add a help system
to your application.

%package -n %qtmultimedia
Summary: Qt Multimedia libraries
Group: System/Libraries

%description -n %qtmultimedia
Qt Multimedia libraries

%package -n %qtmultimediad
Summary: Development files for Qt Multimedia
Group: Development/KDE and Qt
Requires: %qtmultimedia = %EVRD

%description -n %qtmultimediad
Development files for Qt Multimedia

%package -n %qtmultimediaquick_p
Summary: Runtime support library for the Qt Multimedia Quick module
Group: System/Libraries

%description -n %qtmultimediaquick_p
Runtime support library for the Qt Multimedia Quick module

%package -n %qtmultimediawidgets
Summary: Qt Multimedia Widgets library
Group: System/Libraries

%description -n %qtmultimediawidgets
Qt Multimedia Widgets library

%package -n %qtmultimediawidgetsd
Summary: Development files for the Qt Multimedia Widgets library
Group: Development/KDE and Qt
Requires: %qtmultimediawidgets = %EVRD
Requires: %qtmultimediad = %EVRD
Requires: %qtwidgetsd = %EVRD

%description -n %qtmultimediawidgetsd
Development files for the Qt Multimedia Widgets library

%package -n %qtqml
Summary: QML runtime support library
Group: System/Libraries

%description -n %qtqml
QML runtime support library

%package -n %qtqmld
Summary: Development files for the Qt QML library
Group: Development/KDE and Qt
Requires: %qtqml = %EVRD

%description -n %qtqmld
Development files for the Qt QML library

%package -n %qtquick
Summary: Runtime library for Qt Quick
Group: System/Libraries

%description -n %qtquick
Runtime library for Qt Quick

%package -n %qtquickd
Summary: Development files for Qt Quick
Group: Development/KDE and Qt
Requires: %qtquick = %EVRD

%description -n %qtquickd
Development files for Qt Quick

%package -n %qtquickparticles
Summary: Runtime library for Qt Quick's particle engine
Group: System/Libraries

%description -n %qtquickparticles
Runtime library for Qt Quick's particle engine

%package -n %qtquickparticlesd
Summary: Development files for Qt Quick's particle engine
Group: Development/KDE and Qt
Requires: %qtquickparticles = %EVRD

%description -n %qtquickparticlesd
Development files for Qt Quick's particle engine

%package -n %qtquicktest
Summary: Qt Quick unit test module
Group: System/Libraries

%description -n %qtquicktest
Qt Quick unit test module

%package -n %qtquicktestd
Summary: Development files for Qt Quick's unit test module
Group: Development/KDE and Qt
Requires: %qtquicktest = %EVRD

%description -n %qtquicktestd
Development files for Qt Quick's unit test module

%package -n %qtscript
Summary: Qt Script runtime library
Group: System/Libraries

%description -n %qtscript
Qt Script runtime library

%package -n %qtscriptd
Summary: Development files for Qt Script
Group: Development/KDE and Qt
Requires: %qtscript = %EVRD

%description -n %qtscriptd
Development files for Qt Script

%package -n %qtscripttools
Summary: Qt Script tools library
Group: System/Libraries

%description -n %qtscripttools
Qt Script tools library

%package -n %qtscripttoolsd
Summary: Development files for Qt Script tools
Group: Development/KDE and Qt
Requires: %qtscripttools = %EVRD

%description -n %qtscripttoolsd
Development files for Qt Script tools

%package -n %qtsvg
Summary: Qt SVG rendering engine
Group: System/Libraries

%description -n %qtsvg
Qt SVG rendering engine

%package -n %qtsvgd
Summary: Development files for Qt's SVG rendering engine
Group: Development/KDE and Qt
Requires: %qtsvg = %EVRD

%description -n %qtsvgd
Development files for Qt's SVG rendering engine

%package -n %qtv8
Summary: Qt version of the V8 JavaScript engine
Group: System/Libraries

%description -n %qtv8
Qt version of the V8 JavaScript engine

%package -n %qtv8d
Summary: Development files for the Qt version of the V8 JavaScript engine
Group: Development/KDE and Qt
Requires: %qtv8 = %EVRD

%description -n %qtv8d
Development files for the Qt version of the V8 JavaScript engine

%package -n %qtwebkit
Summary: Qt WebKit web browsing library
Group: System/Libraries

%description -n %qtwebkit
Qt WebKit web browsing library

%package -n %qtwebkitd
Summary: Development files for the Qt WebKit web browsing library
Group: Development/KDE and Qt
Requires: %qtwebkit = %EVRD

%description -n %qtwebkitd
Development files for the Qt WebKit web browsing library

%package -n %qtwebkitwidgets
Summary: Qt WebKit Widgets library
Group: System/Libraries

%description -n %qtwebkitwidgets
Qt WebKit Widgets library

%package -n %qtwebkitwidgetsd
Summary: Development files for the Qt WebKit Widgets library
Group: Development/KDE and Qt
Requires: %qtwebkitwidgets = %EVRD
Requires: %qtwebkitd = %EVRD
Requires: %qtwidgetsd = %EVRD

%description -n %qtwebkitwidgetsd
Development files for the Qt WebKit Widgets library

%package -n %qtxmlpatterns
Summary: Qt XSLT engine
Group: System/Libraries
Requires: %qtxml = %EVRD

%description -n %qtxmlpatterns
Qt XSLT engine

%package -n %qtxmlpatternsd
Summary: Development files for Qt's XSLT engine
Group: Development/KDE and Qt
Requires: %qtxmlpatterns = %EVRD
Requires: %qtxmld = %EVRD

%description -n %qtxmlpatternsd
Development files for Qt's XSLT engine

%package devel
Summary: Meta-package for installing all Qt %{major} development files
Group: Development/KDE and Qt
Requires: %qtbootstrapd = %EVRD
Requires: %qtconcurrentd = %EVRD
Requires: %qtcored = %EVRD
Requires: %qtdbusd = %EVRD
Requires: %qtguid = %EVRD
Requires: %qtnetworkd = %EVRD
Requires: %qtopengld = %EVRD
Requires: %qtprintsupportd = %EVRD
Requires: %qtsqld = %EVRD
Requires: %qttestd = %EVRD
Requires: %qtwidgetsd = %EVRD
Requires: %qtxmld = %EVRD
Requires: %qtclucened = %EVRD
Requires: %qtdeclaratived = %EVRD
Requires: %qtdesignercomponentsd = %EVRD
Requires: %qtdesignerd = %EVRD
Requires: %qthelpd = %EVRD
Requires: %qtmultimediad = %EVRD
Requires: %qtmultimediawidgetsd = %EVRD
Requires: %qtqmld = %EVRD
Requires: %qtquickd = %EVRD
Requires: %qtquickparticlesd = %EVRD
Requires: %qtquicktestd = %EVRD
Requires: %qtscriptd = %EVRD
Requires: %qtscripttoolsd = %EVRD
Requires: %qtsvgd = %EVRD
Requires: %qtv8d = %EVRD
Requires: %qtwebkitd = %EVRD
Requires: %qtwebkitwidgetsd = %EVRD
Requires: %qtxmlpatternsd = %EVRD

%description devel
Meta-package for installing all Qt %{major} development files

%package assistant
Summary: Qt help system
Group: Development/KDE and Qt

%description assistant
Qt help system

%package designer
Summary: Qt interface design tool
Group: Development/KDE and Qt

%description designer
Qt interface design tool

%package linguist
Summary: Translation tool for Qt based applications
Group: Development/KDE and Qt
Requires: %name-linguist-tools = %EVRD

%description linguist
Translation tool for Qt based applications

%package linguist-tools
Summary: Tools for creating and updating Qt Linguist translation files
Group: Development/KDE and Qt

%description linguist-tools
Tools for creating and updating Qt Linguist translation files

%package tools

%package qml-tools

%prep
%if "%beta" != ""
%setup -q -n qt-everywhere-opensource-src-%version-%beta
%else
%setup -q -n qt-everywhere-opensource-src-%version
%endif
./configure \
	-prefix %_qt_prefix \
	-bindir %_qt_bindir \
	-libdir %_qt_libdir \
	-docdir %_qt_docdir \
	-headerdir %_qt_includedir \
	-plugindir %_qt_plugindir \
	-importdir %_qt_importdir \
	-translationdir %_qt_translationsdir \
	-sysconfdir %_qt_sysconfdir \
	-examplesdir %_qt_exampledir \
	-testsdir %_qt_testsdir \
	-release \
	-opensource \
	-shared \
	-c++11 \
	-largefile \
	-accessibility \
	-no-sql-db2 \
	-no-sql-ibase \
	-plugin-sql-mysql \
	-no-sql-oci \
	-plugin-sql-odbc \
	-plugin-sql-psql \
	-plugin-sql-sqlite \
	-no-sql-sqlite2 \
	-no-sql-tds \
	-system-sqlite \
	-javascript-jit \
%ifarch x86_64
	-platform linux-g++-64 \
%else
	-platform linux-g++-32 \
%endif
	-system-zlib \
	-system-libpng \
	-system-libjpeg \
	-openssl-linked \
	-system-pcre \
	-system-xcb \
	-optimized-qmake \
	-no-nis \
	-cups \
	-iconv \
	-icu \
	-no-strip \
	-pch \
	-dbus-linked \
	-reduce-relocations \
	-xcb \
%if %with directfb
	-directfb \
%endif
	-qpa xcb \
	-opengl \
	-confirm-license \
	-system-proxies \
	-glib \
	-no-separate-debug-info \
	-v

# FIXME we should also build the KMS and EGLFS output plugins (-kms -eglfs), but
# they require OpenGL ES v2 -- while we typically want to build Desktop GL bits

%build
%make STRIP=true

%install
make install STRIP=true INSTALL_ROOT=%buildroot

# Installed, but not useful
rm -f %buildroot%_qt_bindir/syncqt
# Probably not useful outside of Qt source tree?
rm -f %buildroot%_qt_bindir/qtmodule-configtests
# Let's not ship -devel files for private libraries... At least not until
# applications teach us otherwise
rm -f %buildroot%_qt_libdir/libqgsttools_p.so %buildroot%_qt_libdir/libqgsttools_p.prl
rm -f %buildroot%_qt_libdir/libQt%{major}MultimediaQuick_p.so %buildroot%_qt_libdir/libQt%{major}MultimediaQuick_p.prl %buildroot%_qt_libdir/pkgconfig/Qt%{major}MultimediaQuick_p.pc
# qtconfig doesn't exist anymore - we don't need its translations
rm -f %buildroot%_qt_prefix/translations/qtconfig_*.qm

cd %buildroot%_libdir
ln -s ../lib/qt5/%_lib/*.so.* .

# Fix some wrong permissions
find %buildroot -type f -perm -0755 -name "*.png" |xargs chmod 0644
find %buildroot -type f -perm -0755 -name "*.svg" |xargs chmod 0644
find %buildroot -type f -perm -0755 -name "*.jpg" |xargs chmod 0644
find %buildroot -type f -perm -0755 -name "*.xml" |xargs chmod 0644
find %buildroot -type f -perm -0755 -name "*.xsl" |xargs chmod 0644
find %buildroot -type f -perm -0755 -name "*.php" |xargs chmod 0644
find %buildroot -type f -perm -0755 -name "*.html" |xargs chmod 0644
find %buildroot -type f -perm -0755 -name "*.js" |xargs chmod 0644
find %buildroot -type f -perm -0755 -name "*.plist.app" |xargs chmod 0644

# Workaround for
# *** ERROR: same build ID in nonidentical files!
#        /usr/lib/qt5/bin/qdbuscpp2xml
#   and  /usr/lib/qt5/bin/moc
#	...
# while generating debug info
find %buildroot -type f -perm -0755 |grep -v '\.so' |xargs %__strip --strip-unneeded


%files -n %qtconcurrent
%_qt_libdir/libQt%{major}Concurrent.so.*
%_libdir/libQt%{major}Concurrent.so.*

%files -n %qtbootstrapd
%_qt_libdir/libQt%{major}Bootstrap.a
%_qt_libdir/libQt%{major}Bootstrap.prl
%_qt_libdir/pkgconfig/Qt%{major}Bootstrap.pc

%files -n %qtconcurrentd
%_qt_libdir/libQt%{major}Concurrent.so
%_qt_libdir/libQt%{major}Concurrent.prl
%_qt_libdir/pkgconfig/Qt%{major}Concurrent.pc
%_qt_includedir/QtConcurrent
%_qt_libdir/cmake/Qt%{major}Concurrent

%files -n %qtcore
%_qt_libdir/libQt%{major}Core.so.*
%_libdir/libQt%{major}Core.so.*
%dir %_libdir/qt5/plugins
%dir %_qt_prefix/phrasebooks
%lang(da) %_qt_prefix/phrasebooks/danish.qph
%lang(nl) %_qt_prefix/phrasebooks/dutch.qph
%lang(fi) %_qt_prefix/phrasebooks/finnish.qph
%lang(fr) %_qt_prefix/phrasebooks/french.qph
%lang(de) %_qt_prefix/phrasebooks/german.qph
%lang(hu) %_qt_prefix/phrasebooks/hungarian.qph
%lang(it) %_qt_prefix/phrasebooks/italian.qph
%lang(ja) %_qt_prefix/phrasebooks/japanese.qph
%lang(no) %_qt_prefix/phrasebooks/norwegian.qph
%lang(pl) %_qt_prefix/phrasebooks/polish.qph
%lang(ru) %_qt_prefix/phrasebooks/russian.qph
%lang(es) %_qt_prefix/phrasebooks/spanish.qph
%lang(sv) %_qt_prefix/phrasebooks/swedish.qph
%dir %_qt_prefix/translations
%lang(ar) %_qt_prefix/translations/qt_ar.qm
%lang(cs) %_qt_prefix/translations/qt_cs.qm
%lang(da) %_qt_prefix/translations/qt_da.qm
%lang(de) %_qt_prefix/translations/qt_de.qm
%lang(es) %_qt_prefix/translations/qt_es.qm
%lang(fa) %_qt_prefix/translations/qt_fa.qm
%lang(fr) %_qt_prefix/translations/qt_fr.qm
%lang(gl) %_qt_prefix/translations/qt_gl.qm
%lang(he) %_qt_prefix/translations/qt_he.qm
%lang(hu) %_qt_prefix/translations/qt_hu.qm
%lang(ja) %_qt_prefix/translations/qt_ja.qm
%lang(ko) %_qt_prefix/translations/qt_ko.qm
%lang(lt) %_qt_prefix/translations/qt_lt.qm
%lang(pl) %_qt_prefix/translations/qt_pl.qm
%lang(pt) %_qt_prefix/translations/qt_pt.qm
%lang(ru) %_qt_prefix/translations/qt_ru.qm
%lang(sk) %_qt_prefix/translations/qt_sk.qm
%lang(sl) %_qt_prefix/translations/qt_sl.qm
%lang(sv) %_qt_prefix/translations/qt_sv.qm
%lang(uk) %_qt_prefix/translations/qt_uk.qm
%lang(zh_CN) %_qt_prefix/translations/qt_zh_CN.qm
%lang(zh_TW) %_qt_prefix/translations/qt_zh_TW.qm
%lang(cs) %_qt_prefix/translations/qt_help_cs.qm
%lang(da) %_qt_prefix/translations/qt_help_da.qm
%lang(de) %_qt_prefix/translations/qt_help_de.qm
%lang(fr) %_qt_prefix/translations/qt_help_fr.qm
%lang(gl) %_qt_prefix/translations/qt_help_gl.qm
%lang(hu) %_qt_prefix/translations/qt_help_hu.qm
%lang(ja) %_qt_prefix/translations/qt_help_ja.qm
%lang(ko) %_qt_prefix/translations/qt_help_ko.qm
%lang(pl) %_qt_prefix/translations/qt_help_pl.qm
%lang(ru) %_qt_prefix/translations/qt_help_ru.qm
%lang(sk) %_qt_prefix/translations/qt_help_sk.qm
%lang(sl) %_qt_prefix/translations/qt_help_sl.qm
%lang(uk) %_qt_prefix/translations/qt_help_uk.qm
%lang(zh_CN) %_qt_prefix/translations/qt_help_zh_CN.qm
%lang(zh_TW) %_qt_prefix/translations/qt_help_zh_TW.qm
%lang(de) %_qt_prefix/translations/qtbase_de.qm
%lang(ru) %_qt_prefix/translations/qtbase_ru.qm
%lang(sk) %_qt_prefix/translations/qtbase_sk.qm

%files -n %qtcored
%_qt_bindir/moc
%_qt_bindir/rcc
%_qt_libdir/libQt%{major}Core.so
%_qt_libdir/libQt%{major}Core.prl
%_qt_includedir/QtCore
%dir %_qt_libdir/cmake
%dir %_qt_libdir/pkgconfig
%_qt_libdir/pkgconfig/Qt%{major}Core.pc
%_qt_libdir/cmake/Qt%{major}Core
%doc %_docdir/qt5/global

%files -n %qtdbus
%_qt_libdir/libQt%{major}DBus.so.*
%_libdir/libQt%{major}DBus.so.*

%files -n %qtdbusd
%_qt_libdir/libQt%{major}DBus.so
%_qt_libdir/libQt%{major}DBus.prl
%_qt_libdir/pkgconfig/Qt%{major}DBus.pc
%_qt_includedir/QtDBus
%_qt_libdir/cmake/Qt%{major}DBus
%_qt_bindir/qdbuscpp2xml
%_qt_bindir/qdbusxml2cpp

%files -n qmake%major
%_qt_bindir/qmake
%_qt_prefix/mkspecs

%files -n %qtgui
%_qt_libdir/libQt%{major}Gui.so.*
%_libdir/libQt%{major}Gui.so.*
%_libdir/qt5/plugins/imageformats
%dir %_qt_plugindir/platforminputcontexts
%dir %_qt_plugindir/platforms
%dir %_qt_plugindir/iconengines
%_libdir/qt5/plugins/generic
%_libdir/qt5/plugins/printsupport

%files -n %qtgui-x11
%_libdir/qt5/plugins/platforms/libqxcb.so
%_libdir/qt5/plugins/platforminputcontexts/libibusplatforminputcontextplugin.so
%_libdir/qt5/plugins/platforminputcontexts/libmaliitplatforminputcontextplugin.so

%files -n %qtgui-linuxfb
%_libdir/qt5/plugins/platforms/libqlinuxfb.so
# FIXME need to determine why those aren't built all the time. We're probably
# missing a BuildRequires: somewhere.
%optional %_qt_libdir/fonts

%files -n %qtgui-minimal
%_libdir/qt5/plugins/platforms/libqminimal.so

%files -n %qtgui-directfb
%_qt_plugindir/platforms/libqdirectfb.so

%files -n %qtguid
%_qt_bindir/uic
%_qt_libdir/libQt%{major}Gui.so
%_qt_libdir/libQt%{major}Gui.prl
%_qt_libdir/pkgconfig/Qt%{major}Gui.pc
%_qt_includedir/QtGui
%_qt_libdir/cmake/Qt%{major}Gui
%_qt_libdir/libQt%{major}PlatformSupport.a
%_qt_libdir/libQt%{major}PlatformSupport.prl
%_qt_libdir/pkgconfig/Qt%{major}PlatformSupport.pc
%_qt_includedir/QtPlatformSupport
%_qt_includedir/QtUiTools
%_qt_libdir/cmake/Qt%{major}UiTools
%_qt_libdir/libQt%{major}UiTools.a
%_qt_libdir/libQt%{major}UiTools.prl
%_qt_libdir/pkgconfig/Qt%{major}UiTools.pc

%files -n %qtnetwork
%_qt_libdir/libQt%{major}Network.so.*
%_libdir/libQt%{major}Network.so.*
%_libdir/qt5/plugins/bearer

%files -n %qtnetworkd
%_qt_libdir/libQt%{major}Network.so
%_qt_libdir/libQt%{major}Network.prl
%_qt_libdir/pkgconfig/Qt%{major}Network.pc
%_qt_includedir/QtNetwork
%_qt_libdir/cmake/Qt%{major}Network

%files -n %qtopengl
%_qt_libdir/libQt%{major}OpenGL.so.*
%_libdir/libQt%{major}OpenGL.so.*

%files -n %qtopengld
%_qt_libdir/libQt%{major}OpenGL.so
%_qt_libdir/libQt%{major}OpenGL.prl
%_qt_libdir/pkgconfig/Qt%{major}OpenGL.pc
%_qt_includedir/QtOpenGL
%_qt_libdir/cmake/Qt%{major}OpenGL

%files -n %qtprintsupport
%_qt_libdir/libQt%{major}PrintSupport.so.*
%_libdir/libQt%{major}PrintSupport.so.*

%files -n %qtprintsupportd
%_qt_libdir/libQt%{major}PrintSupport.so
%_qt_libdir/libQt%{major}PrintSupport.prl
%_qt_libdir/pkgconfig/Qt%{major}PrintSupport.pc
%_qt_includedir/QtPrintSupport
%_qt_libdir/cmake/Qt%{major}PrintSupport

%files -n %qtsql
%_qt_libdir/libQt%{major}Sql.so.*
%_libdir/libQt%{major}Sql.so.*
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
%_qt_libdir/libQt%{major}Sql.so
%_qt_libdir/libQt%{major}Sql.prl
%_qt_libdir/pkgconfig/Qt%{major}Sql.pc
%_qt_includedir/QtSql
%_qt_libdir/cmake/Qt%{major}Sql

%files -n %qttest
%_qt_libdir/libQt%{major}Test.so.*
%_libdir/libQt%{major}Test.so.*
%_qt_prefix/qml/QtTest

%files -n %qttestd
%_qt_libdir/libQt%{major}Test.so
%_qt_libdir/libQt%{major}Test.prl
%_qt_libdir/pkgconfig/Qt%{major}Test.pc
%_qt_includedir/QtTest
%_qt_libdir/cmake/Qt%{major}Test

%files -n %qtwidgets
%_qt_libdir/libQt%{major}Widgets.so.*
%_libdir/libQt%{major}Widgets.so.*
%_libdir/qt5/plugins/accessible

%files -n %qtwidgetsd
%_qt_libdir/libQt%{major}Widgets.so
%_qt_libdir/libQt%{major}Widgets.prl
%_qt_libdir/pkgconfig/Qt%{major}Widgets.pc
%_qt_includedir/QtWidgets
%_qt_libdir/cmake/Qt%{major}Widgets

%files -n %qtxml
%_qt_libdir/libQt%{major}Xml.so.*
%_libdir/libQt%{major}Xml.so.*

%files -n %qtxmld
%_qt_libdir/libQt%{major}Xml.so
%_qt_libdir/libQt%{major}Xml.prl
%_qt_libdir/pkgconfig/Qt%{major}Xml.pc
%_qt_includedir/QtXml
%_qt_libdir/cmake/Qt%{major}Xml

%files -n qdoc%major
%_qt_bindir/qdoc

%files examples
%_qt_prefix/examples

# FIXME re-add when Qt/E is fixed
#%files fonts
#%_qt_libdir/fonts

%files -n %qgsttools_p
%_qt_libdir/libqgsttools_p.so.*
%_libdir/libqgsttools_p.so.*

%files -n %qtclucene
%_qt_libdir/libQt%{major}CLucene.so.*
%_libdir/libQt%{major}CLucene.so.*

%files -n %qtclucened
%_qt_libdir/libQt%{major}CLucene.so
%_qt_libdir/libQt%{major}CLucene.prl
%_qt_libdir/pkgconfig/Qt%{major}CLucene.pc
%_qt_includedir/QtCLucene

%files -n %qtdeclarative
%_qt_libdir/libQt%{major}Declarative.so.*
%_libdir/libQt%{major}Declarative.so.*
%lang(de) %_qt_prefix/translations/qtdeclarative_de.qm
%lang(ru) %_qt_prefix/translations/qtdeclarative_ru.qm
%lang(sk) %_qt_prefix/translations/qtdeclarative_sk.qm
%_qt_plugindir/qmltooling

%files -n %qtdeclaratived
%_qt_libdir/libQt%{major}Declarative.so
%_qt_libdir/libQt%{major}Declarative.prl
%_qt_libdir/pkgconfig/Qt%{major}Declarative.pc
%_qt_includedir/QtDeclarative
%_qt_libdir/cmake/Qt%{major}Declarative

%files -n %qtdesignercomponents
%_qt_libdir/libQt%{major}DesignerComponents.so.*
%_libdir/libQt%{major}DesignerComponents.so.*

%files -n %qtdesignercomponentsd
%_qt_libdir/libQt%{major}DesignerComponents.so
%_qt_libdir/libQt%{major}DesignerComponents.prl
%_qt_libdir/pkgconfig/Qt%{major}DesignerComponents.pc
%_qt_includedir/QtDesignerComponents

%files -n %qtdesigner
%_qt_libdir/libQt%{major}Designer.so.*
%_libdir/libQt%{major}Designer.so.*

%files -n %qtdesignerd
%_qt_libdir/libQt%{major}Designer.so
%_qt_libdir/libQt%{major}Designer.prl
%_qt_libdir/pkgconfig/Qt%{major}Designer.pc
%_qt_includedir/QtDesigner
%_qt_libdir/cmake/Qt%{major}Designer

%files -n %qthelp
%_qt_libdir/libQt%{major}Help.so.*
%_libdir/libQt%{major}Help.so.*

%files -n %qthelpd
%_qt_libdir/libQt%{major}Help.so
%_qt_libdir/libQt%{major}Help.prl
%_qt_libdir/pkgconfig/Qt%{major}Help.pc
%_qt_includedir/QtHelp
%_qt_libdir/cmake/Qt%{major}Help

%files -n %qtmultimedia
%_qt_libdir/libQt%{major}Multimedia.so.*
%_libdir/libQt%{major}Multimedia.so.*
%_qt_plugindir/audio
%_qt_plugindir/mediaservice
%_qt_plugindir/playlistformats
%lang(de) %_qt_prefix/translations/qtmultimedia_de.qm
%lang(ru) %_qt_prefix/translations/qtmultimedia_ru.qm
%lang(sk) %_qt_prefix/translations/qtmultimedia_sk.qm

%files -n %qtmultimediad
%_qt_libdir/libQt%{major}Multimedia.so
%_qt_libdir/libQt%{major}Multimedia.prl
%_qt_libdir/pkgconfig/Qt%{major}Multimedia.pc
%_qt_includedir/QtMultimedia
%_qt_libdir/cmake/Qt%{major}Multimedia
%_qt_includedir/QtMultimediaQuick_p

%files -n %qtmultimediaquick_p
%_qt_libdir/libQt%{major}MultimediaQuick_p.so.*
%_libdir/libQt%{major}MultimediaQuick_p.so.*

%files -n %qtmultimediawidgets
%_qt_libdir/libQt%{major}MultimediaWidgets.so.*
%_libdir/libQt%{major}MultimediaWidgets.so.*

%files -n %qtmultimediawidgetsd
%_qt_libdir/libQt%{major}MultimediaWidgets.so
%_qt_libdir/libQt%{major}MultimediaWidgets.prl
%_qt_libdir/pkgconfig/Qt%{major}MultimediaWidgets.pc
%_qt_includedir/QtMultimediaWidgets
%_qt_libdir/cmake/Qt%{major}MultimediaWidgets

%files -n %qtqml
%_qt_libdir/libQt%{major}Qml.so.*
%_libdir/libQt%{major}Qml.so.*
%dir %_qt_prefix/qml
%dir %_qt_prefix/qml/Qt
%dir %_qt_prefix/qml/Qt/labs
%_qt_prefix/qml/Qt/labs/folderlistmodel
%_qt_prefix/qml/QtAudioEngine
%_qt_prefix/qml/QtGraphicalEffects
%_qt_prefix/qml/QtMultimedia

%files -n %qtqmld
%_qt_libdir/libQt%{major}Qml.so
%_qt_libdir/libQt%{major}Qml.prl
%_qt_libdir/pkgconfig/Qt%{major}Qml.pc
%_qt_includedir/QtQml
%_qt_libdir/cmake/Qt%{major}Qml
%_qt_includedir/QtQmlDevTools
%_qt_libdir/libQt%{major}QmlDevTools.a
%_qt_libdir/libQt%{major}QmlDevTools.prl
%_qt_libdir/pkgconfig/Qt%{major}QmlDevTools.pc

%files -n %qtquick
%_qt_libdir/libQt%{major}Quick.so.*
%_libdir/libQt%{major}Quick.so.*
%dir %_qt_importdir
%dir %_qt_importdir/Qt
%dir %_qt_importdir/Qt/labs
%_qt_importdir/Qt/labs/folderlistmodel
%_qt_importdir/Qt/labs/gestures
%_qt_importdir/Qt/labs/particles
%_qt_importdir/Qt/labs/shaders
%_qt_importdir/builtins.qmltypes
%_qt_prefix/qml/QtQuick.2
%_qt_prefix/qml/QtQuick
%lang(de) %_qt_prefix/translations/qtquick1_de.qm
%lang(ru) %_qt_prefix/translations/qtquick1_ru.qm
%lang(sk) %_qt_prefix/translations/qtquick1_sk.qm

%files -n %qtquickd
%_qt_libdir/libQt%{major}Quick.so
%_qt_libdir/libQt%{major}Quick.prl
%_qt_libdir/pkgconfig/Qt%{major}Quick.pc
%_qt_includedir/QtQuick
%_qt_libdir/cmake/Qt%{major}Quick

%files -n %qtquickparticles
%_qt_libdir/libQt%{major}QuickParticles.so.*
%_libdir/libQt%{major}QuickParticles.so.*

%files -n %qtquickparticlesd
%_qt_libdir/libQt%{major}QuickParticles.so
%_qt_libdir/libQt%{major}QuickParticles.prl
%_qt_libdir/pkgconfig/Qt%{major}QuickParticles.pc
%_qt_includedir/QtQuickParticles

%files -n %qtquicktest
%_qt_libdir/libQt%{major}QuickTest.so.*
%_libdir/libQt%{major}QuickTest.so.*

%files -n %qtquicktestd
%_qt_libdir/libQt%{major}QuickTest.so
%_qt_libdir/libQt%{major}QuickTest.prl
%_qt_libdir/pkgconfig/Qt%{major}QuickTest.pc
%_qt_includedir/QtQuickTest
%_qt_libdir/cmake/Qt%{major}QuickTest

%files -n %qtscript
%_qt_libdir/libQt%{major}Script.so.*
%_libdir/libQt%{major}Script.so.*
%lang(de) %_qt_prefix/translations/qtscript_de.qm
%lang(ru) %_qt_prefix/translations/qtscript_ru.qm
%lang(sk) %_qt_prefix/translations/qtscript_sk.qm

%files -n %qtscriptd
%_qt_libdir/libQt%{major}Script.so
%_qt_libdir/libQt%{major}Script.prl
%_qt_libdir/pkgconfig/Qt%{major}Script.pc
%_qt_includedir/QtScript
%_qt_libdir/cmake/Qt%{major}Script

%files -n %qtscripttools
%_qt_libdir/libQt%{major}ScriptTools.so.*
%_libdir/libQt%{major}ScriptTools.so.*

%files -n %qtscripttoolsd
%_qt_libdir/libQt%{major}ScriptTools.so
%_qt_libdir/libQt%{major}ScriptTools.prl
%_qt_libdir/pkgconfig/Qt%{major}ScriptTools.pc
%_qt_includedir/QtScriptTools
%_qt_libdir/cmake/Qt%{major}ScriptTools

%files -n %qtsvg
%_qt_libdir/libQt%{major}Svg.so.*
%_libdir/libQt%{major}Svg.so.*
%_qt_plugindir/iconengines/libqsvgicon.so

%files -n %qtsvgd
%_qt_libdir/libQt%{major}Svg.so
%_qt_libdir/libQt%{major}Svg.prl
%_qt_libdir/pkgconfig/Qt%{major}Svg.pc
%_qt_includedir/QtSvg
%_qt_libdir/cmake/Qt%{major}Svg

%files -n %qtv8
%_qt_libdir/libQt%{major}V8.so.*
%_libdir/libQt%{major}V8.so.*

%files -n %qtv8d
%_qt_libdir/libQt%{major}V8.so
%_qt_libdir/libQt%{major}V8.prl
%_qt_libdir/pkgconfig/Qt%{major}V8.pc
%_qt_includedir/QtV8

%files -n %qtwebkit
%_qt_libdir/libQt%{major}WebKit.so.*
%_libdir/libQt%{major}WebKit.so.*
%_qt_importdir/QtWebKit
%_qt_prefix/qml/QtWebKit
%_qt_prefix/libexec/QtWebProcess
%_qt_prefix/libexec/QtWebPluginProcess

%files -n %qtwebkitd
%_qt_libdir/libQt%{major}WebKit.so
%_qt_libdir/libQt%{major}WebKit.prl
%_qt_libdir/pkgconfig/Qt%{major}WebKit.pc
%_qt_includedir/QtWebKit
%_qt_libdir/cmake/Qt%{major}WebKit

%files -n %qtwebkitwidgets
%_qt_libdir/libQt%{major}WebKitWidgets.so.*
%_libdir/libQt%{major}WebKitWidgets.so.*

%files -n %qtwebkitwidgetsd
%_qt_libdir/libQt%{major}WebKitWidgets.so
%_qt_libdir/libQt%{major}WebKitWidgets.prl
%_qt_libdir/pkgconfig/Qt%{major}WebKitWidgets.pc
%_qt_includedir/QtWebKitWidgets
%_qt_libdir/cmake/Qt%{major}WebKitWidgets

%files -n %qtxmlpatterns
%_qt_libdir/libQt%{major}XmlPatterns.so.*
%_libdir/libQt%{major}XmlPatterns.so.*
%lang(de) %_qt_prefix/translations/qtxmlpatterns_de.qm
%lang(ru) %_qt_prefix/translations/qtxmlpatterns_ru.qm
%lang(sk) %_qt_prefix/translations/qtxmlpatterns_sk.qm

%files -n %qtxmlpatternsd
%_qt_libdir/libQt%{major}XmlPatterns.so
%_qt_libdir/libQt%{major}XmlPatterns.prl
%_qt_libdir/pkgconfig/Qt%{major}XmlPatterns.pc
%_qt_includedir/QtXmlPatterns
%_qt_libdir/cmake/Qt%{major}XmlPatterns

%files devel
# Intentionally empty, we just pull in dependencies

%files assistant
%_qt_prefix/bin/assistant
%lang(cs) %_qt_prefix/translations/assistant_cs.qm
%lang(da) %_qt_prefix/translations/assistant_da.qm
%lang(de) %_qt_prefix/translations/assistant_de.qm
%lang(fr) %_qt_prefix/translations/assistant_fr.qm
%lang(hu) %_qt_prefix/translations/assistant_hu.qm
%lang(ja) %_qt_prefix/translations/assistant_ja.qm
%lang(ko) %_qt_prefix/translations/assistant_ko.qm
%lang(pl) %_qt_prefix/translations/assistant_pl.qm
%lang(ru) %_qt_prefix/translations/assistant_ru.qm
%lang(sk) %_qt_prefix/translations/assistant_sk.qm
%lang(sl) %_qt_prefix/translations/assistant_sl.qm
%lang(uk) %_qt_prefix/translations/assistant_uk.qm
%lang(zh_CN) %_qt_prefix/translations/assistant_zh_CN.qm
%lang(zh_TW) %_qt_prefix/translations/assistant_zh_TW.qm

%files designer
%_prefix/lib/qt%{major}/bin/designer
%lang(cs) %_qt_prefix/translations/designer_cs.qm
%lang(de) %_qt_prefix/translations/designer_de.qm
%lang(fr) %_qt_prefix/translations/designer_fr.qm
%lang(hu) %_qt_prefix/translations/designer_hu.qm
%lang(ja) %_qt_prefix/translations/designer_ja.qm
%lang(ko) %_qt_prefix/translations/designer_ko.qm
%lang(pl) %_qt_prefix/translations/designer_pl.qm
%lang(ru) %_qt_prefix/translations/designer_ru.qm
%lang(sl) %_qt_prefix/translations/designer_sl.qm
%lang(uk) %_qt_prefix/translations/designer_uk.qm
%lang(zh_CN) %_qt_prefix/translations/designer_zh_CN.qm
%lang(zh_TW) %_qt_prefix/translations/designer_zh_TW.qm
%_qt_plugindir/designer

%files linguist
%_prefix/lib/qt%{major}/bin/linguist
%lang(cs) %_qt_prefix/translations/linguist_cs.qm
%lang(de) %_qt_prefix/translations/linguist_de.qm
%lang(fr) %_qt_prefix/translations/linguist_fr.qm
%lang(hu) %_qt_prefix/translations/linguist_hu.qm
%lang(ja) %_qt_prefix/translations/linguist_ja.qm
%lang(ko) %_qt_prefix/translations/linguist_ko.qm
%lang(pl) %_qt_prefix/translations/linguist_pl.qm
%lang(ru) %_qt_prefix/translations/linguist_ru.qm
%lang(sk) %_qt_prefix/translations/linguist_sk.qm
%lang(sl) %_qt_prefix/translations/linguist_sl.qm
%lang(uk) %_qt_prefix/translations/linguist_uk.qm
%lang(zh_CN) %_qt_prefix/translations/linguist_zh_CN.qm
%lang(zh_TW) %_qt_prefix/translations/linguist_zh_TW.qm

%files linguist-tools
%_prefix/lib/qt%{major}/bin/lconvert
%_prefix/lib/qt%{major}/bin/lrelease
%_prefix/lib/qt%{major}/bin/lupdate
%_qt_libdir/cmake/Qt%{major}LinguistTools

%files tools
%_prefix/lib/qt%{major}/bin/pixeltool
%_prefix/lib/qt%{major}/bin/qcollectiongenerator
%_prefix/lib/qt%{major}/bin/qdbus
%_prefix/lib/qt%{major}/bin/qdbusviewer
%_prefix/lib/qt%{major}/bin/qhelpconverter
%_prefix/lib/qt%{major}/bin/qhelpgenerator
%_prefix/lib/qt%{major}/bin/xmlpatterns
%_prefix/lib/qt%{major}/bin/xmlpatternsvalidator

%files qml-tools
%_prefix/lib/qt%{major}/bin/qml1plugindump
%_prefix/lib/qt%{major}/bin/qmlbundle
%_prefix/lib/qt%{major}/bin/qmlmin
%_prefix/lib/qt%{major}/bin/qmlplugindump
%_prefix/lib/qt%{major}/bin/qmlprofiler
%_prefix/lib/qt%{major}/bin/qmlscene
%_prefix/lib/qt%{major}/bin/qmltestrunner
%_prefix/lib/qt%{major}/bin/qmlviewer
%lang(sk) %_qt_prefix/translations/qmlviewer_sk.qm
