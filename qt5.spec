%define debug_package %{nil}
%define beta %nil
%define major 5

%define _qt_prefix %{_prefix}/lib/qt%{major}
%define _qt_bindir %{_qt_prefix}/bin
%define _qt_docdir %{_docdir}/qt%{major}
%define _qt_libdir %{_qt_prefix}/%{_lib}
%define _qt_libexecdir %{_qt_prefix}/libexec
%define _qt_includedir %{_qt_prefix}/include
%define _qt_plugindir %{_libdir}/qt%{major}/plugins
%define _qt_demodir %{_qt_prefix}/demos
%define _qt_exampledir %{_qt_prefix}/examples
%define _qt_importdir %{_qt_prefix}/imports
%define _qt_datadir %{_qt_prefix}/share
%define _qt_sysconfdir %{_sysconfdir}/qt%{major}
%define _qt_testsdir %{_qt_prefix}/tests
%define _qt_translationsdir %{_qt_prefix}/translations

# qtbase components
%define qtbootstrapd %mklibname qt%{major}bootstrap -d
%define qtconcurrent %mklibname qt%{major}concurrent %{major}
%define qtconcurrentd %mklibname qt%{major}concurrent%{major} -d
%define qtcore %mklibname qt%{major}core %{major}
%define qtcored %mklibname qt%{major}core -d
%define qtdbus %mklibname qt%{major}dbus %{major}
%define qtdbusd %mklibname qt%{major}dbus -d
%define qtgui %mklibname qt%{major}gui %{major}
%define qtguid %mklibname qt%{major}gui -d
%define qtnetwork %mklibname qt%{major}network %{major}
%define qtnetworkd %mklibname qt%{major}network -d
%define qtopengl %mklibname qt%{major}opengl %{major}
%define qtopengld %mklibname qt%{major}opengl -d
%define qtprintsupport %mklibname qt%{major}printsupport %{major}
%define qtprintsupportd %mklibname qt%{major}printsupport -d
%define qtsensors %mklibname qt%{major}sensors %{major}
%define qtsensorsd %mklibname qt%{major}sensors -d
%define qtserialport %mklibname qt%{major}serialport %{major}
%define qtserialportd %mklibname qt%{major}serialport -d
%define qtsql %mklibname qt%{major}sql %{major}
%define qtsqld %mklibname qt%{major}sql -d
%define qttest %mklibname qt%{major}test %{major}
%define qttestd %mklibname qt%{major}test -d
%define qtwidgets %mklibname qt%{major}widgets %{major}
%define qtwidgetsd %mklibname qt%{major}widgets -d
%define qtx11extras %mklibname qt%{major}x11extras %{major}
%define qtx11extrasd %mklibname qt%{major}x11extras -d
%define qtxml %mklibname qt%{major}xml %{major}
%define qtxmld %mklibname qt%{major}xml -d

# Extras that might move to separate tarballs at some point
%define qgsttools_p %mklibname qgsttools_p 1
%define qtclucene %mklibname qt%{major}clucene %{major}
%define qtclucened %mklibname qt%{major}clucene -d
%define qtdeclarative %mklibname qt%{major}declarative %{major}
%define qtdeclaratived %mklibname qt%{major}declarative -d
%define qtdesignercomponents %mklibname qt%{major}designercomponents %{major}
%define qtdesignercomponentsd %mklibname qt%{major}designercomponents -d
%define qtdesigner %mklibname qt%{major}designer %{major}
%define qtdesignerd %mklibname qt%{major}designer -d
%define qthelp %mklibname qt%{major}help %{major}
%define qthelpd %mklibname qt%{major}help -d
%define qtmultimedia %mklibname qt%{major}multimedia %{major}
%define qtmultimediad %mklibname qt%{major}multimedia -d
%define qtmultimediaquick_p %mklibname qt%{major}multimediaquick_p %{major}
%define qtmultimediawidgets %mklibname qt%{major}multimediawidgets %{major}
%define qtmultimediawidgetsd %mklibname qt%{major}multimediawidgets -d
%define qtqml %mklibname qt%{major}qml %{major}
%define qtqmld %mklibname qt%{major}qml -d
%define qtquick %mklibname qt%{major}quick %{major}
%define qtquickd %mklibname qt%{major}quick -d
%define qtquickparticles %mklibname qt%{major}quickparticles %{major}
%define qtquickparticlesd %mklibname qt%{major}quickparticles -d
%define qtquicktest %mklibname qt%{major}quicktest %{major}
%define qtquicktestd %mklibname qt%{major}quicktest -d
%define qtscript %mklibname qt%{major}script %{major}
%define qtscriptd %mklibname qt%{major}script -d
%define qtscripttools %mklibname qt%{major}scripttools %{major}
%define qtscripttoolsd %mklibname qt%{major}scripttools -d
%define qtsvg %mklibname qt%{major}svg %{major}
%define qtsvgd %mklibname qt%{major}svg -d
%define qtv8 %mklibname qt%{major}v8 %{major}
%define qtv8d %mklibname qt%{major}v8 -d
%define qtwebkit %mklibname qt%{major}webkit %{major}
%define qtwebkitd %mklibname qt%{major}webkit -d
%define qtwebkitwidgets %mklibname qt%{major}webkitwidgets %{major}
%define qtwebkitwidgetsd %mklibname qt%{major}webkitwidgets -d
%define qtxmlpatterns %mklibname qt%{major}xmlpatterns %{major}
%define qtxmlpatternsd %mklibname qt%{major}xmlpatterns -d

%bcond_without directfb

Summary:	Version 5 of the Qt toolkit
Name:		qt5
Version:	5.1.0
License:	LGPLv3+
Group:		Development/KDE and Qt
Url:		http://qt-project.org/
%if "%{beta}" == ""
Source0:	qt-everywhere-opensource-src-%{version}.tar.gz
Release:	4
%else
Source0:	qt-everywhere-opensource-src-%{version}-%{beta}.tar.xz
Release:	0.%{beta}.1
%endif
Source1:	qt5.macros
Source2:	rosa-assistant-qt5.desktop
Source3:	rosa-designer-qt5.desktop
Source4:	rosa-linguist-qt5.desktop
Source100:	%{name}.rpmlintrc
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(zlib)
# CUPS
BuildRequires:	cups-devel
# OpenGL
BuildRequires:	pkgconfig(gl)
# Event loop
BuildRequires:	pkgconfig(glib-2.0)
# GTK theme
BuildRequires:	pkgconfig(gtk+-2.0)
# ICU
BuildRequires:	pkgconfig(icu-uc)
# Multimedia
BuildRequires:	pkgconfig(gstreamer-0.10)
BuildRequires:	pkgconfig(gstreamer-plugins-base-0.10)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(openal)
# For XCB platform plugin:
BuildRequires:	pkgconfig(xcb) >= 1.5
BuildRequires:	pkgconfig(xcb-icccm)
BuildRequires:	pkgconfig(xcb-image)
BuildRequires:	pkgconfig(xcb-renderutil)
BuildRequires:	pkgconfig(xcb-keysyms)
BuildRequires:	pkgconfig(xrender)
BuildRequires:	pkgconfig(xcb-render)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xcb-xinerama)
BuildRequires:	pkgconfig(xcb-shape)
BuildRequires:	pkgconfig(xv)
BuildRequires:	pkgconfig(xcb-xv)
BuildRequires:	pkgconfig(inputproto)
BuildRequires:	pkgconfig(xi)
BuildRequires:	pkgconfig(xcb-xfixes)
BuildRequires:	pkgconfig(xfixes)
BuildRequires:	pkgconfig(xcb-randr)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(xkbcomp)
BuildRequires:	pkgconfig(xkbfile)
# For proper font access
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(freetype2)
%if %with directfb
# DirectFB platform plugin:
BuildRequires:	pkgconfig(directfb)
%endif
# Accessibility
BuildRequires:	pkgconfig(atspi-2)
# Assorted...
BuildRequires:	pkgconfig(libudev)
BuildRequires:	flex bison gperf
# Used for CPU feature detection in configure step
BuildRequires:	gdb

%description
Version 5 of the Qt toolkit.

%package -n %{qtconcurrent}
Summary:	Qt threading library
Group:		System/Libraries

%description -n %{qtconcurrent}
Qt threading library.

%package -n %{qtbootstrapd}
Summary:	Development files for version 5 if the QtBootstrap library
Group:		Development/KDE and Qt

%description -n %{qtbootstrapd}
Development files for version 5 if the QtBootstrap library.

%package -n %{qtconcurrentd}
Summary:	Development files for version 5 of the QtConcurrent library
Group:		Development/KDE and Qt
Requires:	%{qtconcurrent} = %{EVRD}

%description -n %{qtconcurrentd}
Development files for version 5 of the QtConcurrent library.

%package -n %{qtcore}
Summary:	Qt Core library
Group:		System/Libraries

%description -n %{qtcore}
Qt Core library.

%package -n %{qtcored}
Summary:	Development files for version 5 of the QtCore library
Group:		Development/KDE and Qt
Requires:	%{qtcore} = %{EVRD}

%description -n %{qtcored}
Development files for version 5 of the QtCore library.

%package -n qmake5
Summary:	Makefile generation system for Qt5
Group:		Development/KDE and Qt
Requires:	%{name}-macros = %{EVRD}

%description -n qmake5
Makefile generation system for Qt5.

%package -n %{qtdbus}
Summary:	Qt DBus connector library
Group:		System/Libraries

%description -n %{qtdbus}
Qt DBus connector library.

%package -n %{qtdbusd}
Summary:	Development files for version 5 of the QtDBus library
Group:		Development/KDE and Qt
Requires:	%{qtdbus} = %{EVRD}

%description -n %{qtdbusd}
Development files for version 5 of the QtDBus library.

%package -n %{qtgui}
Summary:	Qt GUI library
Group:		System/Libraries

%description -n %{qtgui}
Qt GUI library.

%package -n %{qtguid}
Summary:	Development files for version 5 of the QtGui library
Group:		Development/KDE and Qt
Requires:	%{qtgui} = %{EVRD}

%description -n %{qtguid}
Development files for version 5 of the QtGui library.

%package -n %{qtgui}-x11
Summary:	X11 output driver for QtGui v5
Group:		System/Libraries
Requires:	%{qtgui} = %{EVRD}

%description -n %{qtgui}-x11
X11 output driver for QtGui v5.

%package -n %{qtgui}-linuxfb
Summary:	Linux Framebuffer output driver for QtGui v5
Group:		System/Libraries
Requires:	%{qtgui} = %{EVRD}

%description -n %{qtgui}-linuxfb
Linux Framebuffer output driver for QtGui v5.

%package -n %{qtgui}-directfb
Summary:	DirectFB output driver for QtGui v5
Group:		System/Libraries
Requires:	%{qtgui} = %{EVRD}

%description -n %{qtgui}-directfb
DirectFB output driver for QtGui v5.

%package -n %{qtgui}-minimal
Summary:	Minimal (Framebuffer based) output driver for QtGui v5
Group:		System/Libraries
Requires:	%{qtgui} = %{EVRD}

%description -n %{qtgui}-minimal
Minimal (Framebuffer based) output driver for QtGui v5.

%package -n %{qtgui}-offscreen
Summary:	Offscreen output driver for QtGui v5
Group:		System/Libraries
Requires:	%{qtgui} = %{EVRD}

%description -n %{qtgui}-offscreen
Minimal (Framebuffer based) output driver for QtGui v5.

%package -n %{qtnetwork}
Summary:	Qt Networking library
Group:		System/Libraries

%description -n %{qtnetwork}
Qt Networking library.

%package -n %{qtnetworkd}
Summary:	Development files for version 5 of the QtNetwork library
Group:		Development/KDE and Qt
Requires:	%{qtnetwork} = %{EVRD}

%description -n %{qtnetworkd}
Development files for version 5 of the QtNetwork library.

%package -n %{qtopengl}
Summary:	Qt OpenGL (3D Graphics) library
Group:		System/Libraries

%description -n %{qtopengl}
Qt OpenGL (3D Graphics) library.

%package -n %{qtopengld}
Summary:	Development files for version 5 of the QtOpenGL library
Group:		Development/KDE and Qt
Requires:	%{qtopengl} = %{EVRD}

%description -n %{qtopengld}
Development files for version 5 of the QtOpenGL library.

%package -n %{qtprintsupport}
Summary:	Qt printing library
Group:		System/Libraries

%description -n %{qtprintsupport}
Qt printing library.

%package -n %{qtprintsupportd}
Summary:	Development files for version 5 of the QtPrintSupport library
Group:		Development/KDE and Qt
Requires:	%{qtprintsupport} = %{EVRD}

%description -n %{qtprintsupportd}
Development files for version 5 of the QtPrintSupport library.

%package -n %{qtsensors}
Summary:	Qt Sensors library
Group:		System/Libraries

%description -n %{qtsensors}
Qt Sensors library.

%package -n %{qtsensorsd}
Summary:	Development files for the QtSensors library
Group:		Development/KDE and Qt
Requires:	%{qtsensors} = %{EVRD}

%description -n %{qtsensorsd}
Development files for the QtSensors library.

%package -n %{qtserialport}
Summary:	Qt Serial Port library
Group:		System/Libraries

%description -n %{qtserialport}
Qt Serial Port library.

%package -n %{qtserialportd}
Summary:	Development files for the QtSerialPort library
Group:		Development/KDE and Qt
Requires:	%{qtserialport} = %{EVRD}

%description -n %{qtserialportd}
Development files for the QtSerialPort library.

%package -n %{qtsql}
Summary:	Qt SQL library
Group:		System/Libraries

%description -n %{qtsql}
Qt SQL library.

%package -n %{qtsql}-sqlite
Summary:	SQLite 3.x support for the QtSql library v5
Group:		System/Libraries
Requires:	%{qtsql} = %{EVRD}
Provides:	%{name}-database-plugin-sqlite = %{EVRD}
BuildRequires:	pkgconfig(sqlite3)

%description -n %{qtsql}-sqlite
SQLite 3.x support for the QtSql library v5.

%package -n %{qtsql}-mysql
Summary:	MySQL support for the QtSql library v5
Group:		System/Libraries
Requires:	%{qtsql} = %{EVRD}
Provides:	%{name}-database-plugin-mysql = %{EVRD}
BuildRequires:	mysql-devel

%description -n %{qtsql}-mysql
MySQL support for the QtSql library v5.

%package -n %{qtsql}-odbc
Summary:	ODBC support for the QtSql library v5
Group:		System/Libraries
Requires:	%{qtsql} = %{EVRD}
Provides:	%{name}-database-plugin-odbc = %{EVRD}
BuildRequires:	pkgconfig(libiodbc)

%description -n %{qtsql}-odbc
ODBC support for the QtSql library v5.

%package -n %{qtsql}-postgresql
Summary:	PostgreSQL support for the QtSql library v5
Group:		System/Libraries
Requires:	%{qtsql} = %{EVRD}
Provides:	%{name}-database-plugin-postgresql = %{EVRD}
BuildRequires:	postgresql-devel >= 9.0

%description -n %{qtsql}-postgresql
PostgreSQL support for the QtSql library v5.

%package -n %{qtsqld}
Summary:	Development files for version 5 of the QtSql library
Group:		Development/KDE and Qt
Requires:	%{qtsql} = %{EVRD}

%description -n %{qtsqld}
Development files for version 5 of the QtSql library.

%package -n %{qttest}
Summary:	Qt unit test library
Group:		System/Libraries

%description -n %{qttest}
Qt unit test library.

%package -n %{qttestd}
Summary:	Development files for version 5 of the QtTest library
Group:		Development/KDE and Qt
Requires:	%{qttest} = %{EVRD}

%description -n %{qttestd}
Development files for version 5 of the QtTest library.

%package -n %{qtwidgets}
Summary:	Qt Widget library
Group:		System/Libraries

%description -n %{qtwidgets}
Qt Widget library.

%package -n %{qtwidgetsd}
Summary:	Development files for version 5 of the QtWidgets library
Group:		Development/KDE and Qt
Requires:	%{qtwidgets} = %{EVRD}

%description -n %{qtwidgetsd}
Development files for version 5 of the QtWidgets library.

%package -n %{qtxml}
Summary:	Qt XML library
Group:		System/Libraries

%description -n %{qtxml}
Qt XML library.

%package -n %{qtxmld}
Summary:	Development files for version 5 of the QtXml library
Group:		Development/KDE and Qt
Requires:	%{qtxml} = %{EVRD}

%description -n %{qtxmld}
Development files for version 5 of the QtXml library.

%package platformtheme-gtk2
Summary:	GTK 2.x platform theme for Qt 5
Group:		Graphical desktop/KDE
Requires:	%{qtgui} = %{EVRD}
BuildRequires:	pkgconfig(gtk+-x11-2.0)

%description platformtheme-gtk2
GTK 2.x platform theme for Qt 5. This plugin allows Qt to render
controls using GTK 2.x themes - making it integrate better with GTK
based desktops.

%package -n qdoc5
Summary:	Qt documentation generator, version 5
Group:		Development/KDE and Qt

%description -n qdoc5
Qt documentation generator, version 5.

%package examples
Summary:	Example applications for %{name}
Group:		Development/KDE and Qt

%description examples
Example applications for %{name}.

%package fonts
Summary:	Fonts for use with some %{name} output plugins
Group:		System/Libraries

%description fonts
Fonts for use with some %{name} output plugins.

These fonts are required for various non-X11 output
plugins (framebuffer device etc.).

They are not required for the normal X11 output.

%package -n %{qgsttools_p}
Summary:	Runtime library for GStreamer support in Qt 5
Group:		System/Libraries

%description -n %{qgsttools_p}
Runtime library for GStreamer support in Qt 5.

%package -n %{qtclucene}
Summary:	Qt version of the CLucene search engine
Group:		System/Libraries

%description -n %{qtclucene}
Qt version of the CLucene search engine.

%package -n %{qtclucened}
Summary:	Development files for the Qt version of the CLucene search engine
Group:		Development/KDE and Qt
Requires:	%{qtclucene} = %{EVRD}

%description -n %{qtclucened}
Development files for the Qt version of the CLucene search engine.

%package -n %{qtdeclarative}
Summary:	Runtime library for Qt Declarative
Group:		System/Libraries

%description -n %{qtdeclarative}
Runtime library for Qt Declarative.

%package -n %{qtdeclaratived}
Summary:	Development files for Qt Declarative
Group:		Development/KDE and Qt
Requires:	%{qtdeclarative} = %{EVRD}

%description -n %{qtdeclaratived}
Development files for Qt Declarative.

%package -n %{qtdesignercomponents}
Summary:	Components for Qt Designer
Group:		System/Libraries

%description -n %{qtdesignercomponents}
Components for Qt Designer.

%package -n %{qtdesignercomponentsd}
Summary:	Development files for Qt Designer Components
Group:		Development/KDE and Qt
Requires:	%{qtdesignercomponents} = %{EVRD}

%description -n %{qtdesignercomponentsd}
Development files for Qt Designer Components.

%package -n %{qtdesigner}
Summary:	Qt Designer runtime libraries
Group:		System/Libraries

%description -n %{qtdesigner}
Qt Designer runtime libraries.

%package -n %{qtdesignerd}
Summary:	Development files for Qt Designer
Group:		Development/KDE and Qt
Requires:	%{qtdesigner} = %{EVRD}

%description -n %{qtdesignerd}
Development files for Qt Designer.

%package -n %{qthelp}
Summary:	Runtime libraries for the Qt Help system
Group:		System/Libraries

%description -n %{qthelp}
Runtime libraries for the Qt Help system.

%package -n %{qthelpd}
Summary:	Development files for Qt Help
Group:		Development/KDE and Qt
Requires:	%{qthelp} = %{EVRD}

%description -n %{qthelpd}
Development files for Qt Help, useful if you wish to add a help system
to your application.

%package -n %{qtmultimedia}
Summary:	Qt Multimedia libraries
Group:		System/Libraries

%description -n %{qtmultimedia}
Qt Multimedia libraries.

%package -n %{qtmultimediad}
Summary:	Development files for Qt Multimedia
Group:		Development/KDE and Qt
Requires:	%{qtmultimedia} = %{EVRD}

%description -n %{qtmultimediad}
Development files for Qt Multimedia.

%package -n %{qtmultimediaquick_p}
Summary:	Runtime support library for the Qt Multimedia Quick module
Group:		System/Libraries

%description -n %{qtmultimediaquick_p}
Runtime support library for the Qt Multimedia Quick module.

%package -n %{qtmultimediawidgets}
Summary:	Qt Multimedia Widgets library
Group:		System/Libraries

%description -n %{qtmultimediawidgets}
Qt Multimedia Widgets library.

%package -n %{qtmultimediawidgetsd}
Summary:	Development files for the Qt Multimedia Widgets library
Group:		Development/KDE and Qt
Requires:	%{qtmultimediawidgets} = %{EVRD}
Requires:	%{qtmultimediad} = %{EVRD}
Requires:	%{qtwidgetsd} = %{EVRD}

%description -n %{qtmultimediawidgetsd}
Development files for the Qt Multimedia Widgets library.

%package -n %{qtqml}
Summary:	QML runtime support library
Group:		System/Libraries

%description -n %{qtqml}
QML runtime support library.

%package -n %{qtqmld}
Summary:	Development files for the Qt QML library
Group:		Development/KDE and Qt
Requires:	%{qtqml} = %{EVRD}

%description -n %{qtqmld}
Development files for the Qt QML library.

%package -n %{qtquick}
Summary:	Runtime library for Qt Quick
Group:		System/Libraries

%description -n %{qtquick}
Runtime library for Qt Quick.

%package -n %{qtquickd}
Summary:	Development files for Qt Quick
Group:		Development/KDE and Qt
Requires:	%{qtquick} = %{EVRD}

%description -n %{qtquickd}
Development files for Qt Quick.

%package -n %{qtquickparticles}
Summary:	Runtime library for Qt Quick's particle engine
Group:		System/Libraries

%description -n %{qtquickparticles}
Runtime library for Qt Quick's particle engine.

%package -n %{qtquickparticlesd}
Summary:	Development files for Qt Quick's particle engine
Group:		Development/KDE and Qt
Requires:	%{qtquickparticles} = %{EVRD}

%description -n %{qtquickparticlesd}
Development files for Qt Quick's particle engine.

%package -n %{qtquicktest}
Summary:	Qt Quick unit test module
Group:		System/Libraries

%description -n %{qtquicktest}
Qt Quick unit test module.

%package -n %{qtquicktestd}
Summary:	Development files for Qt Quick's unit test module
Group:		Development/KDE and Qt
Requires:	%{qtquicktest} = %{EVRD}

%description -n %{qtquicktestd}
Development files for Qt Quick's unit test module.

%package -n %{qtscript}
Summary:	Qt Script runtime library
Group:		System/Libraries

%description -n %{qtscript}
Qt Script runtime library.

%package -n %{qtscriptd}
Summary:	Development files for Qt Script
Group:		Development/KDE and Qt
Requires:	%{qtscript} = %{EVRD}

%description -n %{qtscriptd}
Development files for Qt Script.

%package -n %{qtscripttools}
Summary:	Qt Script tools library
Group:		System/Libraries

%description -n %{qtscripttools}
Qt Script tools library.

%package -n %{qtscripttoolsd}
Summary:	Development files for Qt Script tools
Group:		Development/KDE and Qt
Requires:	%{qtscripttools} = %{EVRD}

%description -n %{qtscripttoolsd}
Development files for Qt Script tools.

%package -n %{qtsvg}
Summary:	Qt SVG rendering engine
Group:		System/Libraries

%description -n %{qtsvg}
Qt SVG rendering engine.

%package -n %{qtsvgd}
Summary:	Development files for Qt's SVG rendering engine
Group:		Development/KDE and Qt
Requires:	%{qtsvg} = %{EVRD}

%description -n %{qtsvgd}
Development files for Qt's SVG rendering engine.

%package -n %{qtv8}
Summary:	Qt version of the V8 JavaScript engine
Group:		System/Libraries

%description -n %{qtv8}
Qt version of the V8 JavaScript engine.

%package -n %{qtv8d}
Summary:	Development files for the Qt version of the V8 JavaScript engine
Group:		Development/KDE and Qt
Requires:	%{qtv8} = %{EVRD}

%description -n %{qtv8d}
Development files for the Qt version of the V8 JavaScript engine.

%package -n %{qtwebkit}
Summary:	Qt WebKit web browsing library
Group:		System/Libraries
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	flex bison gperf ruby
BuildRequires:	icu-devel

%description -n %{qtwebkit}
Qt WebKit web browsing library.

%package -n %{qtwebkitd}
Summary:	Development files for the Qt WebKit web browsing library
Group:		Development/KDE and Qt
Requires:	%{qtwebkit} = %{EVRD}

%description -n %{qtwebkitd}
Development files for the Qt WebKit web browsing library.

%package -n %{qtwebkitwidgets}
Summary:	Qt WebKit Widgets library
Group:		System/Libraries

%description -n %{qtwebkitwidgets}
Qt WebKit Widgets library.

%package -n %{qtwebkitwidgetsd}
Summary:	Development files for the Qt WebKit Widgets library
Group:		Development/KDE and Qt
Requires:	%{qtwebkitwidgets} = %{EVRD}
Requires:	%{qtwebkitd} = %{EVRD}
Requires:	%{qtwidgetsd} = %{EVRD}

%description -n %{qtwebkitwidgetsd}
Development files for the Qt WebKit Widgets library.

%package -n %{qtx11extras}
Summary:	Qt X11 Extras library
Group:		System/Libraries

%description -n %{qtx11extras}
Qt X11 Extras library.

%package -n %{qtx11extrasd}
Summary:	Development files for the QtX11Extras library
Group:		Development/KDE and Qt
Requires:	%{qtx11extras} = %{EVRD}

%description -n %{qtx11extrasd}
Development files for the QtX11Extras library.

%package -n %{qtxmlpatterns}
Summary:	Qt XSLT engine
Group:		System/Libraries
Requires:	%{qtxml} = %{EVRD}

%description -n %{qtxmlpatterns}
Qt XSLT engine.

%package -n %{qtxmlpatternsd}
Summary:	Development files for Qt's XSLT engine
Group:		Development/KDE and Qt
Requires:	%{qtxmlpatterns} = %{EVRD}
Requires:	%{qtxmld} = %{EVRD}

%description -n %{qtxmlpatternsd}
Development files for Qt's XSLT engine.

%package devel
Summary:	Meta-package for installing all Qt 5 development files
Group:		Development/KDE and Qt
Requires:	%{qtbootstrapd} = %{EVRD}
Requires:	%{qtconcurrentd} = %{EVRD}
Requires:	%{qtcored} = %{EVRD}
Requires:	%{qtdbusd} = %{EVRD}
Requires:	%{qtguid} = %{EVRD}
Requires:	%{qtnetworkd} = %{EVRD}
Requires:	%{qtopengld} = %{EVRD}
Requires:	%{qtprintsupportd} = %{EVRD}
Requires:	%{qtsensorsd} = %{EVRD}
Requires:	%{qtsqld} = %{EVRD}
Requires:	%{qttestd} = %{EVRD}
Requires:	%{qtwidgetsd} = %{EVRD}
Requires:	%{qtxmld} = %{EVRD}
Requires:	%{qtclucened} = %{EVRD}
Requires:	%{qtdeclaratived} = %{EVRD}
Requires:	%{qtdesignercomponentsd} = %{EVRD}
Requires:	%{qtdesignerd} = %{EVRD}
Requires:	%{qthelpd} = %{EVRD}
Requires:	%{qtmultimediad} = %{EVRD}
Requires:	%{qtmultimediawidgetsd} = %{EVRD}
Requires:	%{qtqmld} = %{EVRD}
Requires:	%{qtquickd} = %{EVRD}
Requires:	%{qtquickparticlesd} = %{EVRD}
Requires:	%{qtquicktestd} = %{EVRD}
Requires:	%{qtscriptd} = %{EVRD}
Requires:	%{qtscripttoolsd} = %{EVRD}
Requires:	%{qtsvgd} = %{EVRD}
Requires:	%{qtv8d} = %{EVRD}
Requires:	%{qtwebkitd} = %{EVRD}
Requires:	%{qtwebkitwidgetsd} = %{EVRD}
Requires:	%{qtxmlpatternsd} = %{EVRD}
Requires:	qmake5 = %{EVRD}
Requires:	%{name}-macros = %{EVRD}

%description devel
Meta-package for installing all Qt 5 development files.

%package assistant
Summary:	Qt help system
Group:		Development/KDE and Qt

%description assistant
Qt help system.

%package designer
Summary:	Qt interface design tool
Group:		Development/KDE and Qt
Requires:	%{qtgui}-x11 = %{EVRD}
# for /usr/lib/qt5/bin/uic
Requires:	%{qtguid} = %{EVRD}

%description designer
Qt interface design tool.

%package linguist
Summary:	Translation tool for Qt based applications
Group:		Development/KDE and Qt
Requires:	%{name}-linguist-tools = %{EVRD}

%description linguist
Translation tool for Qt based applications.

%package linguist-tools
Summary:	Tools for creating and updating Qt Linguist translation files
Group:		Development/KDE and Qt

%description linguist-tools
Tools for creating and updating Qt Linguist translation files.

%package tools
Summary:	Tools for Qt 5
Group:		Development/KDE and Qt
Requires:	%{qtgui}-minimal = %{EVRD}
Requires:	%{name}-database-plugin-sqlite = %{EVRD}

%description tools
Tools for Qt 5.

%package qml-tools
Summary:	QML tools for Qt 5
Group:		Development/KDE and Qt

%description qml-tools
QML tools for Qt 5.

%package macros
Summary:	Base macros for Qt 5
Group:		Development/KDE and Qt

%description macros
Base macros for Qt 5.

%prep
%if "%{beta}" != ""
%setup -q -n qt-everywhere-opensource-src-%{version}-%{beta}
%else
%setup -q -n qt-everywhere-opensource-src-%{version}
%endif
./configure \
	-prefix %{_qt_prefix} \
	-bindir %{_qt_bindir} \
	-libdir %{_qt_libdir} \
	-docdir %{_qt_docdir} \
	-headerdir %{_qt_includedir} \
	-plugindir %{_qt_plugindir} \
	-importdir %{_qt_importdir} \
	-translationdir %{_qt_translationsdir} \
	-sysconfdir %{_qt_sysconfdir} \
	-examplesdir %{_qt_exampledir} \
	-testsdir %{_qt_testsdir} \
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
	-fontconfig \
	-accessibility \
	-gnumake \
	-pkg-config \
	-sm \
	-xinerama \
	-xshape \
	-xvideo \
	-xsync \
	-xinput2 \
	-xcursor \
	-xfixes \
	-xrandr \
	-xrender \
	-xkb \
	-opengl \
	-confirm-license \
	-system-proxies \
	-glib \
	-no-separate-debug-info \
	-no-strip \
	-v \
	-I %{_includedir}/iodbc

# FIXME we should also build the KMS and EGLFS output plugins (-kms -eglfs), but
# they require OpenGL ES v2 -- while we typically want to build Desktop GL bits

%build
%make STRIP=true

%install
make install STRIP=true INSTALL_ROOT=%{buildroot}

# Installed, but not useful
rm -f %{buildroot}%{_qt_bindir}/syncqt
rm -f %{buildroot}%{_qt_bindir}/syncqt.pl
# Probably not useful outside of Qt source tree?
rm -f %{buildroot}%{_qt_bindir}/qtmodule-configtests
# Let's not ship -devel files for private libraries... At least not until
# applications teach us otherwise
rm -f %{buildroot}%{_qt_libdir}/libqgsttools_p.so %{buildroot}%{_qt_libdir}/libqgsttools_p.prl
rm -f %{buildroot}%{_qt_libdir}/libQt%{major}MultimediaQuick_p.so %{buildroot}%{_qt_libdir}/libQt%{major}MultimediaQuick_p.prl %{buildroot}%{_qt_libdir}/pkgconfig/Qt%{major}MultimediaQuick_p.pc
# qtconfig doesn't exist anymore - we don't need its translations
rm -f %{buildroot}%{_qt_translationsdir}/qtconfig_*.qm
# Let's make life easier for packagers
mkdir -p %{buildroot}%{_bindir}
ln -s ../lib/qt%{major}/bin/qmake %{buildroot}%{_bindir}/qmake-qt%{major}

cd %{buildroot}%{_libdir}
ln -s ../lib/qt%{major}/%{_lib}/*.so.* .
mkdir pkgconfig
cd pkgconfig
ln -s ../../lib/qt%{major}/%{_lib}/pkgconfig/*.pc .
cd ..

# Fix some wrong permissions
find %{buildroot} -type f -perm -0755 -name "*.png" |xargs --no-run-if-empty chmod 0644
find %{buildroot} -type f -perm -0755 -name "*.svg" |xargs --no-run-if-empty chmod 0644
find %{buildroot} -type f -perm -0755 -name "*.jpg" |xargs --no-run-if-empty chmod 0644
find %{buildroot} -type f -perm -0755 -name "*.xml" |xargs --no-run-if-empty chmod 0644
find %{buildroot} -type f -perm -0755 -name "*.xsl" |xargs --no-run-if-empty chmod 0644
find %{buildroot} -type f -perm -0755 -name "*.php" |xargs --no-run-if-empty chmod 0644
find %{buildroot} -type f -perm -0755 -name "*.html" |xargs --no-run-if-empty chmod 0644
find %{buildroot} -type f -perm -0755 -name "*.js" |xargs --no-run-if-empty chmod 0644
find %{buildroot} -type f -perm -0755 -name "*.plist.app" |xargs --no-run-if-empty chmod 0644

# Workaround for
# *** ERROR: same build ID in nonidentical files!
#        /usr/lib/qt5/bin/qdbuscpp2xml
#   and  /usr/lib/qt5/bin/moc
# ...
# while generating debug info
find %{buildroot} -type f -perm -0755 |grep -vE '\.(so|qml)' |xargs %__strip --strip-unneeded

# Install rpm macros
mkdir -p %{buildroot}%{_sysconfdir}/rpm/macros.d
install -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/rpm/macros.d

# Install .desktop files for assistant, designer and linguist
mkdir -p %{buildroot}%{_datadir}/applications
install -m 644 %{SOURCE2} %{buildroot}%{_datadir}/applications
install -m 644 %{SOURCE3} %{buildroot}%{_datadir}/applications
install -m 644 %{SOURCE4} %{buildroot}%{_datadir}/applications

%files -n %{qtconcurrent}
%{_qt_libdir}/libQt%{major}Concurrent.so.*
%{_libdir}/libQt%{major}Concurrent.so.*

%files -n %{qtbootstrapd}
%{_qt_libdir}/libQt%{major}Bootstrap.a
%{_qt_libdir}/libQt%{major}Bootstrap.prl
%{_qt_libdir}/pkgconfig/Qt%{major}Bootstrap.pc
%{_libdir}/pkgconfig/Qt%{major}Bootstrap.pc

%files -n %{qtconcurrentd}
%{_qt_libdir}/libQt%{major}Concurrent.so
%{_qt_libdir}/libQt%{major}Concurrent.prl
%{_qt_libdir}/pkgconfig/Qt%{major}Concurrent.pc
%{_libdir}/pkgconfig/Qt%{major}Concurrent.pc
%{_qt_includedir}/QtConcurrent
%{_qt_libdir}/cmake/Qt%{major}Concurrent

%files -n %{qtcore}
%{_qt_libdir}/libQt%{major}Core.so.*
%{_libdir}/libQt%{major}Core.so.*
%dir %{_qt_plugindir}
%dir %{_qt_prefix}/phrasebooks
%lang(da) %{_qt_prefix}/phrasebooks/danish.qph
%lang(nl) %{_qt_prefix}/phrasebooks/dutch.qph
%lang(fi) %{_qt_prefix}/phrasebooks/finnish.qph
%lang(fr) %{_qt_prefix}/phrasebooks/french.qph
%lang(de) %{_qt_prefix}/phrasebooks/german.qph
%lang(hu) %{_qt_prefix}/phrasebooks/hungarian.qph
%lang(it) %{_qt_prefix}/phrasebooks/italian.qph
%lang(ja) %{_qt_prefix}/phrasebooks/japanese.qph
%lang(no) %{_qt_prefix}/phrasebooks/norwegian.qph
%lang(pl) %{_qt_prefix}/phrasebooks/polish.qph
%lang(ru) %{_qt_prefix}/phrasebooks/russian.qph
%lang(es) %{_qt_prefix}/phrasebooks/spanish.qph
%lang(sv) %{_qt_prefix}/phrasebooks/swedish.qph
%dir %{_qt_translationsdir}
%lang(ar) %{_qt_translationsdir}/qt_ar.qm
%lang(cs) %{_qt_translationsdir}/qt_cs.qm
%lang(da) %{_qt_translationsdir}/qt_da.qm
%lang(de) %{_qt_translationsdir}/qt_de.qm
%lang(es) %{_qt_translationsdir}/qt_es.qm
%lang(fa) %{_qt_translationsdir}/qt_fa.qm
%lang(fr) %{_qt_translationsdir}/qt_fr.qm
%lang(gl) %{_qt_translationsdir}/qt_gl.qm
%lang(he) %{_qt_translationsdir}/qt_he.qm
%lang(hu) %{_qt_translationsdir}/qt_hu.qm
%lang(ja) %{_qt_translationsdir}/qt_ja.qm
%lang(ko) %{_qt_translationsdir}/qt_ko.qm
%lang(lt) %{_qt_translationsdir}/qt_lt.qm
%lang(pl) %{_qt_translationsdir}/qt_pl.qm
%lang(pt) %{_qt_translationsdir}/qt_pt.qm
%lang(ru) %{_qt_translationsdir}/qt_ru.qm
%lang(sk) %{_qt_translationsdir}/qt_sk.qm
%lang(sl) %{_qt_translationsdir}/qt_sl.qm
%lang(sv) %{_qt_translationsdir}/qt_sv.qm
%lang(uk) %{_qt_translationsdir}/qt_uk.qm
%lang(zh_CN) %{_qt_translationsdir}/qt_zh_CN.qm
%lang(zh_TW) %{_qt_translationsdir}/qt_zh_TW.qm
%lang(cs) %{_qt_translationsdir}/qt_help_cs.qm
%lang(da) %{_qt_translationsdir}/qt_help_da.qm
%lang(de) %{_qt_translationsdir}/qt_help_de.qm
%lang(fr) %{_qt_translationsdir}/qt_help_fr.qm
%lang(gl) %{_qt_translationsdir}/qt_help_gl.qm
%lang(hu) %{_qt_translationsdir}/qt_help_hu.qm
%lang(ja) %{_qt_translationsdir}/qt_help_ja.qm
%lang(ko) %{_qt_translationsdir}/qt_help_ko.qm
%lang(pl) %{_qt_translationsdir}/qt_help_pl.qm
%lang(ru) %{_qt_translationsdir}/qt_help_ru.qm
%lang(sk) %{_qt_translationsdir}/qt_help_sk.qm
%lang(sl) %{_qt_translationsdir}/qt_help_sl.qm
%lang(uk) %{_qt_translationsdir}/qt_help_uk.qm
%lang(zh_CN) %{_qt_translationsdir}/qt_help_zh_CN.qm
%lang(zh_TW) %{_qt_translationsdir}/qt_help_zh_TW.qm
%lang(cs) %{_qt_translationsdir}/qtbase_cs.qm
%lang(de) %{_qt_translationsdir}/qtbase_de.qm
%lang(hu) %{_qt_translationsdir}/qtbase_hu.qm
%lang(ru) %{_qt_translationsdir}/qtbase_ru.qm
%lang(sk) %{_qt_translationsdir}/qtbase_sk.qm
%lang(uk) %{_qt_translationsdir}/qtbase_uk.qm

%files -n %{qtcored}
%{_qt_bindir}/moc
%{_qt_bindir}/rcc
%{_qt_libdir}/libQt%{major}Core.so
%{_qt_libdir}/libQt%{major}Core.prl
%{_qt_includedir}/QtCore
%dir %{_qt_libdir}/cmake
%dir %{_qt_libdir}/cmake/Qt%{major}
%dir %{_qt_libdir}/pkgconfig
%{_qt_libdir}/pkgconfig/Qt%{major}Core.pc
%{_libdir}/pkgconfig/Qt%{major}Core.pc
%{_qt_libdir}/cmake/Qt%{major}Core
%{_qt_libdir}/cmake/Qt%{major}/Qt%{major}Config.cmake
%{_qt_libdir}/cmake/Qt%{major}/Qt%{major}ConfigVersion.cmake
%doc %{_docdir}/qt%{major}/global

%files -n %{qtdbus}
%{_qt_libdir}/libQt%{major}DBus.so.*
%{_libdir}/libQt%{major}DBus.so.*

%files -n %{qtdbusd}
%{_qt_libdir}/libQt%{major}DBus.so
%{_qt_libdir}/libQt%{major}DBus.prl
%{_qt_libdir}/pkgconfig/Qt%{major}DBus.pc
%{_libdir}/pkgconfig/Qt%{major}DBus.pc
%{_qt_includedir}/QtDBus
%{_qt_libdir}/cmake/Qt%{major}DBus
%{_qt_bindir}/qdbuscpp2xml
%{_qt_bindir}/qdbusxml2cpp

%files -n qmake5
%{_bindir}/qmake-qt%{major}
%{_qt_bindir}/qmake
%{_qt_prefix}/mkspecs

%files -n %{qtgui}
%{_qt_libdir}/libQt%{major}Gui.so.*
%{_libdir}/libQt%{major}Gui.so.*
%{_qt_plugindir}/imageformats
%dir %{_qt_plugindir}/platforminputcontexts
%dir %{_qt_plugindir}/platforms
%dir %{_qt_plugindir}/platformthemes
%dir %{_qt_plugindir}/iconengines
%{_qt_plugindir}/generic
%{_qt_plugindir}/printsupport

%files -n %{qtgui}-x11
%{_qt_plugindir}/platforms/libqxcb.so
%{_qt_plugindir}/platforminputcontexts/libibusplatforminputcontextplugin.so
%{_qt_plugindir}/platforminputcontexts/libmaliitplatforminputcontextplugin.so
%{_qt_plugindir}/platforminputcontexts/libcomposeplatforminputcontextplugin.so

%files -n %{qtgui}-linuxfb
%{_qt_plugindir}/platforms/libqlinuxfb.so
# FIXME need to determine why those aren't built all the time. We're probably
# missing a BuildRequires: somewhere.
%optional %{_qt_libdir}/fonts

%files -n %{qtgui}-minimal
%{_qt_plugindir}/platforms/libqminimal.so

%files -n %{qtgui}-offscreen
%{_qt_plugindir}/platforms/libqoffscreen.so

%files -n %{qtgui}-directfb
%{_qt_plugindir}/platforms/libqdirectfb.so

%files -n %{qtguid}
%{_qt_bindir}/uic
%{_qt_libdir}/libQt%{major}Gui.so
%{_qt_libdir}/libQt%{major}Gui.prl
%{_qt_libdir}/pkgconfig/Qt%{major}Gui.pc
%{_libdir}/pkgconfig/Qt%{major}Gui.pc
%{_qt_includedir}/QtGui
%{_qt_libdir}/cmake/Qt%{major}Gui
%{_qt_libdir}/libQt%{major}PlatformSupport.a
%{_qt_libdir}/libQt%{major}PlatformSupport.prl
%{_qt_libdir}/pkgconfig/Qt%{major}PlatformSupport.pc
%{_libdir}/pkgconfig/Qt%{major}PlatformSupport.pc
%{_qt_includedir}/QtPlatformSupport
%{_qt_includedir}/QtUiTools
%{_qt_libdir}/cmake/Qt%{major}UiTools
%{_qt_libdir}/libQt%{major}UiTools.a
%{_qt_libdir}/libQt%{major}UiTools.prl
%{_qt_libdir}/pkgconfig/Qt%{major}UiTools.pc
%{_libdir}/pkgconfig/Qt%{major}UiTools.pc

%files -n %{qtnetwork}
%{_qt_libdir}/libQt%{major}Network.so.*
%{_libdir}/libQt%{major}Network.so.*
%{_qt_plugindir}/bearer

%files -n %{qtnetworkd}
%{_qt_libdir}/libQt%{major}Network.so
%{_qt_libdir}/libQt%{major}Network.prl
%{_qt_libdir}/pkgconfig/Qt%{major}Network.pc
%{_libdir}/pkgconfig/Qt%{major}Network.pc
%{_qt_includedir}/QtNetwork
%{_qt_libdir}/cmake/Qt%{major}Network

%files -n %{qtopengl}
%{_qt_libdir}/libQt%{major}OpenGL.so.*
%{_libdir}/libQt%{major}OpenGL.so.*

%files -n %{qtopengld}
%{_qt_libdir}/libQt%{major}OpenGL.so
%{_qt_libdir}/libQt%{major}OpenGL.prl
%{_qt_libdir}/pkgconfig/Qt%{major}OpenGL.pc
%{_libdir}/pkgconfig/Qt%{major}OpenGL.pc
%{_qt_libdir}/pkgconfig/Qt%{major}OpenGLExtensions.pc
%{_libdir}/pkgconfig/Qt%{major}OpenGLExtensions.pc
%{_qt_includedir}/QtOpenGL
%{_qt_includedir}/QtOpenGLExtensions
%{_qt_libdir}/cmake/Qt%{major}OpenGL
%{_qt_libdir}/cmake/Qt%{major}OpenGLExtensions
%{_qt_libdir}/libQt%{major}OpenGLExtensions.a
%{_qt_libdir}/libQt%{major}OpenGLExtensions.prl

%files -n %{qtprintsupport}
%{_qt_libdir}/libQt%{major}PrintSupport.so.*
%{_libdir}/libQt%{major}PrintSupport.so.*

%files -n %{qtprintsupportd}
%{_qt_libdir}/libQt%{major}PrintSupport.so
%{_qt_libdir}/libQt%{major}PrintSupport.prl
%{_qt_libdir}/pkgconfig/Qt%{major}PrintSupport.pc
%{_libdir}/pkgconfig/Qt%{major}PrintSupport.pc
%{_qt_includedir}/QtPrintSupport
%{_qt_libdir}/cmake/Qt%{major}PrintSupport

%files -n %{qtsensors}
%{_qt_libdir}/libQt%{major}Sensors.so.*
%{_libdir}/libQt%{major}Sensors.so.*
%{_qt_prefix}/qml/QtSensors
%{_qt_plugindir}/sensorgestures
%{_qt_plugindir}/sensors

%files -n %{qtsensorsd}
%{_qt_includedir}/QtSensors
%{_qt_libdir}/cmake/Qt%{major}Sensors
%{_qt_libdir}/libQt%{major}Sensors.so
%{_qt_libdir}/libQt%{major}Sensors.prl
%{_qt_libdir}/pkgconfig/Qt%{major}Sensors.pc
%{_libdir}/pkgconfig/Qt%{major}Sensors.pc

%files -n %{qtserialport}
%{_qt_libdir}/libQt%{major}SerialPort.so.*
%{_libdir}/libQt%{major}SerialPort.so.*

%files -n %{qtserialportd}
%{_qt_includedir}/QtSerialPort
%{_qt_libdir}/cmake/Qt%{major}SerialPort
%{_qt_libdir}/libQt%{major}SerialPort.so
%{_qt_libdir}/libQt%{major}SerialPort.prl
%{_qt_libdir}/pkgconfig/Qt%{major}SerialPort.pc
%{_libdir}/pkgconfig/Qt%{major}SerialPort.pc

%files -n %{qtsql}
%{_qt_libdir}/libQt%{major}Sql.so.*
%{_libdir}/libQt%{major}Sql.so.*
%dir %{_qt_plugindir}/sqldrivers

%files -n %{qtsql}-sqlite
%{_qt_plugindir}/sqldrivers/libqsqlite.so

%files -n %{qtsql}-mysql
%{_qt_plugindir}/sqldrivers/libqsqlmysql.so

%files -n %{qtsql}-odbc
%{_qt_plugindir}/sqldrivers/libqsqlodbc.so

%files -n %{qtsql}-postgresql
%{_qt_plugindir}/sqldrivers/libqsqlpsql.so

%files -n %{qtsqld}
%{_qt_libdir}/libQt%{major}Sql.so
%{_qt_libdir}/libQt%{major}Sql.prl
%{_qt_libdir}/pkgconfig/Qt%{major}Sql.pc
%{_libdir}/pkgconfig/Qt%{major}Sql.pc
%{_qt_includedir}/QtSql
%{_qt_libdir}/cmake/Qt%{major}Sql

%files -n %{qttest}
%{_qt_libdir}/libQt%{major}Test.so.*
%{_libdir}/libQt%{major}Test.so.*
%{_qt_prefix}/qml/QtTest

%files -n %{qttestd}
%{_qt_libdir}/libQt%{major}Test.so
%{_qt_libdir}/libQt%{major}Test.prl
%{_qt_libdir}/pkgconfig/Qt%{major}Test.pc
%{_libdir}/pkgconfig/Qt%{major}Test.pc
%{_qt_includedir}/QtTest
%{_qt_libdir}/cmake/Qt%{major}Test

%files -n %{qtwidgets}
%{_qt_libdir}/libQt%{major}Widgets.so.*
%{_libdir}/libQt%{major}Widgets.so.*
%{_qt_plugindir}/accessible

%files -n %{qtwidgetsd}
%{_qt_libdir}/libQt%{major}Widgets.so
%{_qt_libdir}/libQt%{major}Widgets.prl
%{_qt_libdir}/pkgconfig/Qt%{major}Widgets.pc
%{_libdir}/pkgconfig/Qt%{major}Widgets.pc
%{_qt_includedir}/QtWidgets
%{_qt_libdir}/cmake/Qt%{major}Widgets

%files -n %{qtx11extras}
%{_qt_libdir}/libQt%{major}X11Extras.so.*
%{_libdir}/libQt%{major}X11Extras.so.*

%files -n %{qtx11extrasd}
%{_qt_includedir}/QtX11Extras
%{_qt_libdir}/cmake/Qt%{major}X11Extras
%{_qt_libdir}/libQt%{major}X11Extras.so
%{_qt_libdir}/libQt%{major}X11Extras.prl
%{_qt_libdir}/pkgconfig/Qt%{major}X11Extras.pc
%{_libdir}/pkgconfig/Qt%{major}X11Extras.pc

%files -n %{qtxml}
%{_qt_libdir}/libQt%{major}Xml.so.*
%{_libdir}/libQt%{major}Xml.so.*

%files -n %{qtxmld}
%{_qt_libdir}/libQt%{major}Xml.so
%{_qt_libdir}/libQt%{major}Xml.prl
%{_qt_libdir}/pkgconfig/Qt%{major}Xml.pc
%{_libdir}/pkgconfig/Qt%{major}Xml.pc
%{_qt_includedir}/QtXml
%{_qt_libdir}/cmake/Qt%{major}Xml

%files platformtheme-gtk2
%{_qt_plugindir}/platformthemes/libqgtk2.so

%files -n qdoc%{major}
%{_qt_bindir}/qdoc

%files examples
%{_qt_exampledir}

# FIXME re-add when Qt/E is fixed
#%%files fonts
#%%{_qt_libdir}/fonts

%files -n %{qgsttools_p}
%{_qt_libdir}/libqgsttools_p.so.*
%{_libdir}/libqgsttools_p.so.*

%files -n %{qtclucene}
%{_qt_libdir}/libQt%{major}CLucene.so.*
%{_libdir}/libQt%{major}CLucene.so.*

%files -n %{qtclucened}
%{_qt_libdir}/libQt%{major}CLucene.so
%{_qt_libdir}/libQt%{major}CLucene.prl
%{_qt_libdir}/pkgconfig/Qt%{major}CLucene.pc
%{_libdir}/pkgconfig/Qt%{major}CLucene.pc
%{_qt_includedir}/QtCLucene

%files -n %{qtdeclarative}
%{_qt_libdir}/libQt%{major}Declarative.so.*
%{_libdir}/libQt%{major}Declarative.so.*
%lang(de) %{_qt_translationsdir}/qtdeclarative_de.qm
%lang(ru) %{_qt_translationsdir}/qtdeclarative_ru.qm
%lang(sk) %{_qt_translationsdir}/qtdeclarative_sk.qm
%lang(uk) %{_qt_translationsdir}/qtdeclarative_uk.qm
%{_qt_plugindir}/qmltooling

%files -n %{qtdeclaratived}
%{_qt_libdir}/libQt%{major}Declarative.so
%{_qt_libdir}/libQt%{major}Declarative.prl
%{_qt_libdir}/pkgconfig/Qt%{major}Declarative.pc
%{_libdir}/pkgconfig/Qt%{major}Declarative.pc
%{_qt_includedir}/QtDeclarative
%{_qt_libdir}/cmake/Qt%{major}Declarative

%files -n %{qtdesignercomponents}
%{_qt_libdir}/libQt%{major}DesignerComponents.so.*
%{_libdir}/libQt%{major}DesignerComponents.so.*

%files -n %{qtdesignercomponentsd}
%{_qt_libdir}/libQt%{major}DesignerComponents.so
%{_qt_libdir}/libQt%{major}DesignerComponents.prl
%{_qt_libdir}/pkgconfig/Qt%{major}DesignerComponents.pc
%{_libdir}/pkgconfig/Qt%{major}DesignerComponents.pc
%{_qt_includedir}/QtDesignerComponents

%files -n %{qtdesigner}
%{_qt_libdir}/libQt%{major}Designer.so.*
%{_libdir}/libQt%{major}Designer.so.*

%files -n %{qtdesignerd}
%{_qt_libdir}/libQt%{major}Designer.so
%{_qt_libdir}/libQt%{major}Designer.prl
%{_qt_libdir}/pkgconfig/Qt%{major}Designer.pc
%{_libdir}/pkgconfig/Qt%{major}Designer.pc
%{_qt_includedir}/QtDesigner
%{_qt_libdir}/cmake/Qt%{major}Designer

%files -n %{qthelp}
%{_qt_libdir}/libQt%{major}Help.so.*
%{_libdir}/libQt%{major}Help.so.*

%files -n %{qthelpd}
%{_qt_libdir}/libQt%{major}Help.so
%{_qt_libdir}/libQt%{major}Help.prl
%{_qt_libdir}/pkgconfig/Qt%{major}Help.pc
%{_libdir}/pkgconfig/Qt%{major}Help.pc
%{_qt_includedir}/QtHelp
%{_qt_libdir}/cmake/Qt%{major}Help

%files -n %{qtmultimedia}
%{_qt_libdir}/libQt%{major}Multimedia.so.*
%{_libdir}/libQt%{major}Multimedia.so.*
%{_qt_plugindir}/audio
%{_qt_plugindir}/mediaservice
%{_qt_plugindir}/playlistformats
%lang(cs) %{_qt_translationsdir}/qtmultimedia_cs.qm
%lang(de) %{_qt_translationsdir}/qtmultimedia_de.qm
%lang(hu) %{_qt_translationsdir}/qtmultimedia_hu.qm
%lang(ru) %{_qt_translationsdir}/qtmultimedia_ru.qm
%lang(sk) %{_qt_translationsdir}/qtmultimedia_sk.qm
%lang(uk) %{_qt_translationsdir}/qtmultimedia_uk.qm

%files -n %{qtmultimediad}
%{_qt_libdir}/libQt%{major}Multimedia.so
%{_qt_libdir}/libQt%{major}Multimedia.prl
%{_qt_libdir}/pkgconfig/Qt%{major}Multimedia.pc
%{_libdir}/pkgconfig/Qt%{major}Multimedia.pc
%{_qt_includedir}/QtMultimedia
%{_qt_libdir}/cmake/Qt%{major}Multimedia
%{_qt_includedir}/QtMultimediaQuick_p

%files -n %{qtmultimediaquick_p}
%{_qt_libdir}/libQt%{major}MultimediaQuick_p.so.*
%{_libdir}/libQt%{major}MultimediaQuick_p.so.*

%files -n %{qtmultimediawidgets}
%{_qt_libdir}/libQt%{major}MultimediaWidgets.so.*
%{_libdir}/libQt%{major}MultimediaWidgets.so.*

%files -n %{qtmultimediawidgetsd}
%{_qt_libdir}/libQt%{major}MultimediaWidgets.so
%{_qt_libdir}/libQt%{major}MultimediaWidgets.prl
%{_qt_libdir}/pkgconfig/Qt%{major}MultimediaWidgets.pc
%{_libdir}/pkgconfig/Qt%{major}MultimediaWidgets.pc
%{_qt_includedir}/QtMultimediaWidgets
%{_qt_libdir}/cmake/Qt%{major}MultimediaWidgets

%files -n %{qtqml}
%{_qt_libdir}/libQt%{major}Qml.so.*
%{_libdir}/libQt%{major}Qml.so.*
%dir %{_qt_prefix}/qml
%dir %{_qt_prefix}/qml/Qt
%dir %{_qt_prefix}/qml/Qt/labs
%{_qt_prefix}/qml/Qt/labs/folderlistmodel
%{_qt_prefix}/qml/QtAudioEngine
%{_qt_prefix}/qml/QtGraphicalEffects
%{_qt_prefix}/qml/QtMultimedia
%{_qt_prefix}/qml/QtQml
%{_qt_plugindir}/qml1tooling/libqmldbg_inspector.so
%{_qt_plugindir}/qml1tooling/libqmldbg_tcp_qtdeclarative.so

%files -n %{qtqmld}
%{_qt_libdir}/libQt%{major}Qml.so
%{_qt_libdir}/libQt%{major}Qml.prl
%{_qt_libdir}/pkgconfig/Qt%{major}Qml.pc
%{_libdir}/pkgconfig/Qt%{major}Qml.pc
%{_qt_includedir}/QtQml
%{_qt_libdir}/cmake/Qt%{major}Qml
%{_qt_libdir}/libQt%{major}QmlDevTools.a
%{_qt_libdir}/libQt%{major}QmlDevTools.prl
%{_qt_libdir}/pkgconfig/Qt%{major}QmlDevTools.pc
%{_libdir}/pkgconfig/Qt%{major}QmlDevTools.pc

%files -n %{qtquick}
%{_qt_libdir}/libQt%{major}Quick.so.*
%{_libdir}/libQt%{major}Quick.so.*
%dir %{_qt_importdir}
%dir %{_qt_importdir}/Qt
%dir %{_qt_importdir}/Qt/labs
%{_qt_importdir}/Qt/labs/folderlistmodel
%{_qt_importdir}/Qt/labs/gestures
%{_qt_importdir}/Qt/labs/particles
%{_qt_importdir}/Qt/labs/shaders
%{_qt_importdir}/builtins.qmltypes
%{_qt_prefix}/qml/QtQuick.2
%{_qt_prefix}/qml/QtQuick
%lang(cs) %{_qt_translationsdir}/qtquick1_cs.qm
%lang(de) %{_qt_translationsdir}/qtquick1_de.qm
%lang(hu) %{_qt_translationsdir}/qtquick1_hu.qm
%lang(ru) %{_qt_translationsdir}/qtquick1_ru.qm
%lang(sk) %{_qt_translationsdir}/qtquick1_sk.qm
%lang(uk) %{_qt_translationsdir}/qtquick1_uk.qm

%files -n %{qtquickd}
%{_qt_libdir}/libQt%{major}Quick.so
%{_qt_libdir}/libQt%{major}Quick.prl
%{_qt_libdir}/pkgconfig/Qt%{major}Quick.pc
%{_libdir}/pkgconfig/Qt%{major}Quick.pc
%{_qt_includedir}/QtQuick
%{_qt_libdir}/cmake/Qt%{major}Quick

%files -n %{qtquickparticles}
%{_qt_libdir}/libQt%{major}QuickParticles.so.*
%{_libdir}/libQt%{major}QuickParticles.so.*

%files -n %{qtquickparticlesd}
%{_qt_libdir}/libQt%{major}QuickParticles.so
%{_qt_libdir}/libQt%{major}QuickParticles.prl
%{_qt_libdir}/pkgconfig/Qt%{major}QuickParticles.pc
%{_libdir}/pkgconfig/Qt%{major}QuickParticles.pc
%{_qt_includedir}/QtQuickParticles

%files -n %{qtquicktest}
%{_qt_libdir}/libQt%{major}QuickTest.so.*
%{_libdir}/libQt%{major}QuickTest.so.*

%files -n %{qtquicktestd}
%{_qt_libdir}/libQt%{major}QuickTest.so
%{_qt_libdir}/libQt%{major}QuickTest.prl
%{_qt_libdir}/pkgconfig/Qt%{major}QuickTest.pc
%{_libdir}/pkgconfig/Qt%{major}QuickTest.pc
%{_qt_includedir}/QtQuickTest
%{_qt_libdir}/cmake/Qt%{major}QuickTest

%files -n %{qtscript}
%{_qt_libdir}/libQt%{major}Script.so.*
%{_libdir}/libQt%{major}Script.so.*
%lang(cs) %{_qt_translationsdir}/qtscript_cs.qm
%lang(de) %{_qt_translationsdir}/qtscript_de.qm
%lang(hu) %{_qt_translationsdir}/qtscript_hu.qm
%lang(ru) %{_qt_translationsdir}/qtscript_ru.qm
%lang(sk) %{_qt_translationsdir}/qtscript_sk.qm
%lang(uk) %{_qt_translationsdir}/qtscript_uk.qm

%files -n %{qtscriptd}
%{_qt_libdir}/libQt%{major}Script.so
%{_qt_libdir}/libQt%{major}Script.prl
%{_qt_libdir}/pkgconfig/Qt%{major}Script.pc
%{_libdir}/pkgconfig/Qt%{major}Script.pc
%{_qt_includedir}/QtScript
%{_qt_libdir}/cmake/Qt%{major}Script

%files -n %{qtscripttools}
%{_qt_libdir}/libQt%{major}ScriptTools.so.*
%{_libdir}/libQt%{major}ScriptTools.so.*

%files -n %{qtscripttoolsd}
%{_qt_libdir}/libQt%{major}ScriptTools.so
%{_qt_libdir}/libQt%{major}ScriptTools.prl
%{_qt_libdir}/pkgconfig/Qt%{major}ScriptTools.pc
%{_libdir}/pkgconfig/Qt%{major}ScriptTools.pc
%{_qt_includedir}/QtScriptTools
%{_qt_libdir}/cmake/Qt%{major}ScriptTools

%files -n %{qtsvg}
%{_qt_libdir}/libQt%{major}Svg.so.*
%{_libdir}/libQt%{major}Svg.so.*
%{_qt_plugindir}/iconengines/libqsvgicon.so

%files -n %{qtsvgd}
%{_qt_libdir}/libQt%{major}Svg.so
%{_qt_libdir}/libQt%{major}Svg.prl
%{_qt_libdir}/pkgconfig/Qt%{major}Svg.pc
%{_libdir}/pkgconfig/Qt%{major}Svg.pc
%{_qt_includedir}/QtSvg
%{_qt_libdir}/cmake/Qt%{major}Svg

%files -n %{qtv8}
%{_qt_libdir}/libQt%{major}V8.so.*
%{_libdir}/libQt%{major}V8.so.*

%files -n %{qtv8d}
%{_qt_libdir}/libQt%{major}V8.so
%{_qt_libdir}/libQt%{major}V8.prl
%{_qt_libdir}/pkgconfig/Qt%{major}V8.pc
%{_libdir}/pkgconfig/Qt%{major}V8.pc
%{_qt_includedir}/QtV8

%files -n %{qtwebkit}
%{_qt_libdir}/libQt%{major}WebKit.so.*
%{_libdir}/libQt%{major}WebKit.so.*
%{_qt_importdir}/QtWebKit
%{_qt_prefix}/qml/QtWebKit
%{_qt_libexecdir}/QtWebProcess
%{_qt_libexecdir}/QtWebPluginProcess

%files -n %{qtwebkitd}
%{_qt_libdir}/libQt%{major}WebKit.so
%{_qt_libdir}/libQt%{major}WebKit.prl
%{_qt_libdir}/pkgconfig/Qt%{major}WebKit.pc
%{_libdir}/pkgconfig/Qt%{major}WebKit.pc
%{_qt_includedir}/QtWebKit
%{_qt_libdir}/cmake/Qt%{major}WebKit

%files -n %{qtwebkitwidgets}
%{_qt_libdir}/libQt%{major}WebKitWidgets.so.*
%{_libdir}/libQt%{major}WebKitWidgets.so.*

%files -n %{qtwebkitwidgetsd}
%{_qt_libdir}/libQt%{major}WebKitWidgets.so
%{_qt_libdir}/libQt%{major}WebKitWidgets.prl
%{_qt_libdir}/pkgconfig/Qt%{major}WebKitWidgets.pc
%{_libdir}/pkgconfig/Qt%{major}WebKitWidgets.pc
%{_qt_includedir}/QtWebKitWidgets
%{_qt_libdir}/cmake/Qt%{major}WebKitWidgets

%files -n %{qtxmlpatterns}
%{_qt_libdir}/libQt%{major}XmlPatterns.so.*
%{_libdir}/libQt%{major}XmlPatterns.so.*
%lang(cs) %{_qt_translationsdir}/qtxmlpatterns_cs.qm
%lang(de) %{_qt_translationsdir}/qtxmlpatterns_de.qm
%lang(hu) %{_qt_translationsdir}/qtxmlpatterns_hu.qm
%lang(ru) %{_qt_translationsdir}/qtxmlpatterns_ru.qm
%lang(sk) %{_qt_translationsdir}/qtxmlpatterns_sk.qm
%lang(uk) %{_qt_translationsdir}/qtxmlpatterns_uk.qm

%files -n %{qtxmlpatternsd}
%{_qt_libdir}/libQt%{major}XmlPatterns.so
%{_qt_libdir}/libQt%{major}XmlPatterns.prl
%{_qt_libdir}/pkgconfig/Qt%{major}XmlPatterns.pc
%{_libdir}/pkgconfig/Qt%{major}XmlPatterns.pc
%{_qt_includedir}/QtXmlPatterns
%{_qt_libdir}/cmake/Qt%{major}XmlPatterns

%files devel
# Intentionally empty, we just pull in dependencies

%files assistant
%{_qt_bindir}/assistant
%{_datadir}/applications/rosa-assistant-qt5.desktop
%lang(cs) %{_qt_translationsdir}/assistant_cs.qm
%lang(da) %{_qt_translationsdir}/assistant_da.qm
%lang(de) %{_qt_translationsdir}/assistant_de.qm
%lang(fr) %{_qt_translationsdir}/assistant_fr.qm
%lang(hu) %{_qt_translationsdir}/assistant_hu.qm
%lang(ja) %{_qt_translationsdir}/assistant_ja.qm
%lang(ko) %{_qt_translationsdir}/assistant_ko.qm
%lang(pl) %{_qt_translationsdir}/assistant_pl.qm
%lang(ru) %{_qt_translationsdir}/assistant_ru.qm
%lang(sk) %{_qt_translationsdir}/assistant_sk.qm
%lang(sl) %{_qt_translationsdir}/assistant_sl.qm
%lang(uk) %{_qt_translationsdir}/assistant_uk.qm
%lang(zh_CN) %{_qt_translationsdir}/assistant_zh_CN.qm
%lang(zh_TW) %{_qt_translationsdir}/assistant_zh_TW.qm

%files designer
%{_qt_bindir}/designer
%{_datadir}/applications/rosa-designer-qt5.desktop
%lang(cs) %{_qt_translationsdir}/designer_cs.qm
%lang(de) %{_qt_translationsdir}/designer_de.qm
%lang(fr) %{_qt_translationsdir}/designer_fr.qm
%lang(hu) %{_qt_translationsdir}/designer_hu.qm
%lang(ja) %{_qt_translationsdir}/designer_ja.qm
%lang(ko) %{_qt_translationsdir}/designer_ko.qm
%lang(pl) %{_qt_translationsdir}/designer_pl.qm
%lang(ru) %{_qt_translationsdir}/designer_ru.qm
%lang(sk) %{_qt_translationsdir}/designer_sk.qm
%lang(sl) %{_qt_translationsdir}/designer_sl.qm
%lang(uk) %{_qt_translationsdir}/designer_uk.qm
%lang(zh_CN) %{_qt_translationsdir}/designer_zh_CN.qm
%lang(zh_TW) %{_qt_translationsdir}/designer_zh_TW.qm
%{_qt_plugindir}/designer

%files linguist
%{_qt_bindir}/linguist
%{_datadir}/applications/rosa-linguist-qt5.desktop
%lang(cs) %{_qt_translationsdir}/linguist_cs.qm
%lang(de) %{_qt_translationsdir}/linguist_de.qm
%lang(fr) %{_qt_translationsdir}/linguist_fr.qm
%lang(hu) %{_qt_translationsdir}/linguist_hu.qm
%lang(ja) %{_qt_translationsdir}/linguist_ja.qm
%lang(ko) %{_qt_translationsdir}/linguist_ko.qm
%lang(pl) %{_qt_translationsdir}/linguist_pl.qm
%lang(ru) %{_qt_translationsdir}/linguist_ru.qm
%lang(sk) %{_qt_translationsdir}/linguist_sk.qm
%lang(sl) %{_qt_translationsdir}/linguist_sl.qm
%lang(uk) %{_qt_translationsdir}/linguist_uk.qm
%lang(zh_CN) %{_qt_translationsdir}/linguist_zh_CN.qm
%lang(zh_TW) %{_qt_translationsdir}/linguist_zh_TW.qm

%files linguist-tools
%{_qt_bindir}/lconvert
%{_qt_bindir}/lrelease
%{_qt_bindir}/lupdate
%{_qt_libdir}/cmake/Qt%{major}LinguistTools

%files tools
%{_qt_bindir}/pixeltool
%{_qt_bindir}/qcollectiongenerator
%{_qt_bindir}/qdbus
%{_qt_bindir}/qdbusviewer
%{_qt_bindir}/qhelpconverter
%{_qt_bindir}/qhelpgenerator
%{_qt_bindir}/xmlpatterns
%{_qt_bindir}/xmlpatternsvalidator

%files qml-tools
%{_qt_bindir}/qml1plugindump
%{_qt_bindir}/qmlbundle
%{_qt_bindir}/qmlmin
%{_qt_bindir}/qmlplugindump
%{_qt_bindir}/qmlprofiler
%{_qt_bindir}/qmlscene
%{_qt_bindir}/qmltestrunner
%{_qt_bindir}/qmlviewer
%lang(cs) %{_qt_translationsdir}/qmlviewer_cs.qm
%lang(hu) %{_qt_translationsdir}/qmlviewer_hu.qm
%lang(sk) %{_qt_translationsdir}/qmlviewer_sk.qm
%lang(ru) %{_qt_translationsdir}/qmlviewer_ru.qm
%lang(uk) %{_qt_translationsdir}/qmlviewer_uk.qm

%files macros
%{_sysconfdir}/rpm/macros.d/qt5.macros

