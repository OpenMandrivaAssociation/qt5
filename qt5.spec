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
%define qtprintsupportd %mklibname qtprintsupportd -d
%define qtsql %mklibname qtsql %major
%define qtsqld %mklibname qtsql%major -d
%define qttest %mklibname qttest %major
%define qttestd %mklibname qttest%major -d
%define qtwidgets %mklibname qtwidgets %major
%define qtwidgetsd %mklibname qtwidgets%major -d
%define qtxml %mklibname qtxml %major
%define qtxmld %mklibname qtxml%major -d

Name: qt5
Version: 5.0.0
%if "%beta" == ""
Source0: http://releases.qt-project.org/qt5.0/release/qt-everywhere-opensource-src-%version.tar.xz
Release: 1
%else
Source0: http://releases.qt-project.org/qt5.0/%beta/qt-everywhere-opensource-src-%version-%beta.tar.xz
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

# For XCB platform plugin:
BuildRequires: pkgconfig(xcb) >= 1.5
BuildRequires: pkgconfig(xcb-icccm)
BuildRequires: pkgconfig(xcb-image)
BuildRequires: pkgconfig(xcb-renderutil)
BuildRequires: pkgconfig(xcb-keysyms)
BuildRequires: pkgconfig(xrender)

# For MySQL plugin:
BuildRequires: mysql-devel

# For PostgreSQL plugin:
BuildRequires: postgresql-devel >= 9.0

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

%description -n %qtsql-sqlite
SQLite 3.x support for the QtSql library v%major

%package -n %qtsql-mysql
Summary: MySQL support for the QtSql library v%major
Group: System/Libraries
Requires: %qtsql = %version-%release

%description -n %qtsql-mysql
MySQL support for the QtSql library v%major

%package -n %qtsql-odbc
Summary: ODBC support for the QtSql library v%major
Group: System/Libraries
Requires: %qtsql = %version-%release

%description -n %qtsql-odbc
ODBC support for the QtSql library v%major

%package -n %qtsql-postgresql
Summary: PostgreSQL support for the QtSql library v%major
Group: System/Libraries
Requires: %qtsql = %version-%release

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

%prep
%setup -q -n qt-everywhere-opensource-src-%version
cd qtbase
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
	-largefile \
	-exceptions \
	-accessibility \
	-stl \
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
	-phonon-backend \
	-javascript-jit \
%ifarch x86_64
	-platform linux-g++-64 \
%else
	-platform linux-g++-32 \
%endif
	-system-zlib \
	-system-libpng \
	-system-libjpeg \
	-openssl \
	-system-pcre \
	-optimized-qmake \
	-no-nis \
	-cups \
	-iconv \
	-pch \
	-dbus \
	-reduce-relocations \
	-xcb \
	-opengl \
	-confirm-license \
	-glib \
	-no-separate-debug-info

%build
cd qtbase
%make STRIP=true

%install
cd qtbase
make install STRIP=true INSTALL_ROOT=%buildroot

# Installed, but not useful
rm -f %buildroot%_qt_bindir/syncqt
# Probably not useful outside of Qt source tree?
rm -f %buildroot%_qt_bindir/qtmodule-configtests

cd %buildroot%_libdir
ln -s ../lib/qt5/%_lib/*.so.* .

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
%_qt_bindir/uic
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

%files -n qdoc%major
%_qt_bindir/qdoc

%files examples
%_qt_prefix/examples
