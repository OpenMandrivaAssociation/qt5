%define debug_package %{nil}
%define beta rc
%define api 5
%define major 5
%define qgstmajor 1

%define _qt_prefix %{_libdir}/qt%{api}
%define _qt_bindir %{_qt_prefix}/bin
%define _qt_docdir %{_docdir}/qt%{api}
#define _qt_libdir %{_qt_prefix}/%{_lib}
%define _qt_libdir %{_libdir}
%define _qt_libexecdir %{_qt_prefix}/libexec
%define _qt_includedir %{_includedir}/qt5
%define _qt_plugindir %{_libdir}/qt%{api}/plugins
%define _qt_demodir %{_qt_prefix}/demos
%define _qt_exampledir %{_qt_prefix}/examples
%define _qt_importdir %{_qt_prefix}/imports
%define _qt_datadir %{_datadir}/qt%{api}
%define _qt_sysconfdir %{_sysconfdir}/qt%{api}
%define _qt_testsdir %{_qt_prefix}/tests
%define _qt_translationsdir %{_qt_datadir}/translations

# qt base components
%define qtbluetooth %mklibname qt%{api}bluetooth %{major}
%define qtbluetoothd %mklibname qt%{api}bluetooth -d
%define qtbootstrapd %mklibname qt%{api}bootstrap -d
%define qtconcurrent %mklibname qt%{api}concurrent %{major}
%define qtconcurrentd %mklibname qt%{api}concurrent -d
%define qtcore %mklibname qt%{api}core %{major}
%define qtcored %mklibname qt%{api}core -d
%define qtdbus %mklibname qt%{api}dbus %{major}
%define qtdbusd %mklibname qt%{api}dbus -d
%define qtgui %mklibname qt%{api}gui %{major}
%define qtguid %mklibname qt%{api}gui -d
%define qtlocation %mklibname qt%{api}location %{major}
%define qtlocationd %mklibname qt%{api}location -d
%define qtnetwork %mklibname qt%{api}network %{major}
%define qtnetworkd %mklibname qt%{api}network -d
%define qtnfc %mklibname qt%{api}nfc %{major}
%define qtnfcd %mklibname qt%{api}nfc -d
%define qtopengl %mklibname qt%{api}opengl %{major}
%define qtopengld %mklibname qt%{api}opengl -d
%define qtpositioning %mklibname qt%{api}positioning %{major}
%define qtpositioningd %mklibname qt%{api}positioning -d
%define qtprintsupport %mklibname qt%{api}printsupport %{major}
%define qtprintsupportd %mklibname qt%{api}printsupport -d
%define qtsensors %mklibname qt%{api}sensors %{major}
%define qtsensorsd %mklibname qt%{api}sensors -d
%define qtserialport %mklibname qt%{api}serialport %{major}
%define qtserialportd %mklibname qt%{api}serialport -d
%define qtsql %mklibname qt%{api}sql %{major}
%define qtsqld %mklibname qt%{api}sql -d
%define qttest %mklibname qt%{api}test %{major}
%define qttestd %mklibname qt%{api}test -d
%define qtwidgets %mklibname qt%{api}widgets %{major}
%define qtwidgetsd %mklibname qt%{api}widgets -d
%define qtquickwidgets %mklibname qt%{api}quickwidgets %{major}
%define qtquickwidgetsd %mklibname qt%{api}quickwidgets -d
%define qtwebchannel %mklibname qt%{api}webchannel %{major}
%define qtwebchanneld %mklibname qt%{api}webchannel -d
%define qtwebsockets %mklibname qt%{api}websockets %{major}
%define qtwebsocketsd %mklibname qt%{api}websockets -d
%define qtx11extras %mklibname qt%{api}x11extras %{major}
%define qtx11extrasd %mklibname qt%{api}x11extras -d
%define qtxml %mklibname qt%{api}xml %{major}
%define qtxmld %mklibname qt%{api}xml -d

# qt extras that might move to separate tarballs at some point
%define qgsttools_p %mklibname qgsttools_p %{qgstmajor}
%define qtclucene %mklibname qt%{api}clucene %{major}
%define qtclucened %mklibname qt%{api}clucene -d
%define qtdeclarative %mklibname qt%{api}declarative %{major}
%define qtdeclaratived %mklibname qt%{api}declarative -d
%define qtdesignercomponents %mklibname qt%{api}designercomponents %{major}
%define qtdesignercomponentsd %mklibname qt%{api}designercomponents -d
%define qtdesigner %mklibname qt%{api}designer %{major}
%define qtdesignerd %mklibname qt%{api}designer -d
%define qthelp %mklibname qt%{api}help %{major}
%define qthelpd %mklibname qt%{api}help -d
%define qtmultimedia %mklibname qt%{api}multimedia %{major}
%define qtmultimediad %mklibname qt%{api}multimedia -d
%define qtmultimediaquick_p %mklibname qt%{api}multimediaquick_p %{major}
%define qtmultimediawidgets %mklibname qt%{api}multimediawidgets %{major}
%define qtmultimediawidgetsd %mklibname qt%{api}multimediawidgets -d
%define qtqml %mklibname qt%{api}qml %{major}
%define qtqmld %mklibname qt%{api}qml -d
%define qtquick %mklibname qt%{api}quick %{major}
%define qtquickd %mklibname qt%{api}quick -d
%define qtquickparticles %mklibname qt%{api}quickparticles %{major}
%define qtquickparticlesd %mklibname qt%{api}quickparticles -d
%define qtquicktest %mklibname qt%{api}quicktest %{major}
%define qtquicktestd %mklibname qt%{api}quicktest -d
%define qtscript %mklibname qt%{api}script %{major}
%define qtscriptd %mklibname qt%{api}script -d
%define qtscripttools %mklibname qt%{api}scripttools %{major}
%define qtscripttoolsd %mklibname qt%{api}scripttools -d
%define qtsvg %mklibname qt%{api}svg %{major}
%define qtsvgd %mklibname qt%{api}svg -d
%define qtwaylandclient %mklibname qt%{api}waylandclient %{major}
%define qtwaylandclientd %mklibname qt%{api}waylandclient -d
%define qtwaylandcompositor %mklibname qt%{api}waylandcompositor %{major}
%define qtwaylandcompositord %mklibname qt%{api}compositor -d
%define qtwebkit %mklibname qt%{api}webkit %{major}
%define qtwebkitd %mklibname qt%{api}webkit -d
%define qtwebkitwidgets %mklibname qt%{api}webkitwidgets %{major}
%define qtwebkitwidgetsd %mklibname qt%{api}webkitwidgets -d
%define qtxmlpatterns %mklibname qt%{api}xmlpatterns %{major}
%define qtxmlpatternsd %mklibname qt%{api}xmlpatterns -d
%define enginio %mklibname enginio 1
%define enginiod %mklibname enginio -d

%bcond_with directfb
# Requires qdoc5 and qt5-tools to build
%bcond_with docs
# https://bugs.gentoo.org/show_bug.cgi?id=433826
# 100%-related for cooker
# disable gtkstyle because it adds qt4 include paths to the compiler
# command line if x11-libs/cairo is built with USE=qt4 (bug 433826)
%bcond_with gtk

Summary:	Version 5 of the Qt toolkit
Name:		qt5
Version:	5.4.0
License:	LGPLv3+
Group:		Development/KDE and Qt
Url:		http://qt-project.org/
%if "%{beta}" == ""
Source0:	http://ftp.fau.de/qtproject/official_releases/qt/%(echo %{version} |cut -d. -f1-2)/%{version}/single/qt-everywhere-opensource-src-%{version}.tar.xz
Release:	1
%else
Source0:	http://ftp.fau.de/qtproject/development_releases/qt/%(echo %{version} |cut -d. -f1-2)/%{version}-%{beta}/single/qt-everywhere-opensource-src-%{version}-%{beta}.tar.xz
Release:	0.%{beta}.1
%endif
Source1:	qt5.macros
Source2:	openmandriva-assistant-qt%{api}.desktop
Source3:	openmandriva-designer-qt%{api}.desktop
Source4:	openmandriva-linguist-qt%{api}.desktop
Source100:	%{name}.rpmlintrc
# See http://bugs.rosalinux.ru/show_bug.cgi?id=2367
Patch1:		qt-everywhere-opensource-src-5.3.1-cmake-linguist.patch
# Build static library used in example to avoid missing dependency
Patch2:		qt-everywhere-opensource-src-5.2.0-staticgrue.patch
# upstream patch to build gsttools with gstreamer 1.0
Patch3:		Initial-porting-effort-to-GStreamer-1.0.patch
Patch4:		0001-Add-ARM-64-support.patch
Patch5:		qt5-5.4.0-qtwayland-enable-compositor.patch
BuildRequires:	jpeg-devel
# Build scripts
BuildRequires:	python >= 3.0 python2
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(zlib)
# CUPS
BuildRequires:	cups-devel
# OpenGL
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(egl)
BuildRequires:	pkgconfig(glesv2)
# Event loop
BuildRequires:	pkgconfig(glib-2.0)
%if %{with gtk}
# GTK theme
BuildRequires:	pkgconfig(gtk+-2.0)
%endif
# ICU
BuildRequires:	pkgconfig(icu-uc)
# Multimedia
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	pkgconfig(gstreamer-plugins-base-1.0)
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
BuildRequires:	pkgconfig(xkbcommon) >= 0.4.1
BuildRequires:	pkgconfig(xkbcommon-x11) >= 0.4.1
BuildRequires:	pkgconfig(libsystemd)
BuildRequires:	pkgconfig(libsystemd-journal)
BuildRequires:	pkgconfig(mtdev)
BuildRequires:	pkgconfig(harfbuzz)
# For proper font access
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(freetype2)
%if %{with directfb}
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
%if %{with docs}
BuildRequires:	qdoc5
BuildRequires:	qt5-tools
%endif

%description
Version 5 of the Qt toolkit.

#----------------------------------------------------------------------------
# qt base components
#----------------------------------------------------------------------------

%package -n %{qtbluetooth}
Summary:	Qt Bluetooth library
Group:		System/Libraries
BuildRequires:	pkgconfig(bluez)

%description -n %{qtbluetooth}
Qt Bluetooth library.

%files -n %{qtbluetooth}
%{_qt_libdir}/libQt%{api}Bluetooth.so.%{major}*
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/libQt%{api}Bluetooth.so.%{major}*
%endif
%{_qt_prefix}/qml/QtBluetooth
%{_qt_bindir}/sdpscanner

#----------------------------------------------------------------------------

%package -n %{qtbluetoothd}
Summary:	Development files for version 5 of the QtBluetooth library
Group:		Development/KDE and Qt
Requires:	%{qtbluetooth} = %{EVRD}

%description -n %{qtbluetoothd}
Development files for version 5 of the QtBluetooth library.

%files -n %{qtbluetoothd}
%{_qt_includedir}/QtBluetooth
%{_qt_libdir}/libQt%{api}Bluetooth.so
%{_qt_libdir}/libQt%{api}Bluetooth.prl
%{_qt_libdir}/cmake/Qt%{api}Bluetooth
%{_qt_libdir}/pkgconfig/Qt%{api}Bluetooth.pc
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/pkgconfig/Qt%{api}Bluetooth.pc
%endif

#----------------------------------------------------------------------------

%package -n %{qtbootstrapd}
Summary:	Development files for version 5 if the QtBootstrap library
Group:		Development/KDE and Qt

%description -n %{qtbootstrapd}
Development files for version 5 if the QtBootstrap library.

%files -n %{qtbootstrapd}
%{_qt_libdir}/libQt%{api}Bootstrap.a
%{_qt_libdir}/libQt%{api}Bootstrap.prl
%{_qt_libdir}/pkgconfig/Qt%{api}Bootstrap.pc
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/pkgconfig/Qt%{api}Bootstrap.pc
%endif

#----------------------------------------------------------------------------

%package -n %{qtconcurrent}
Summary:	Qt threading library
Group:		System/Libraries

%description -n %{qtconcurrent}
Qt threading library.

%files -n %{qtconcurrent}
%{_qt_libdir}/libQt%{api}Concurrent.so.%{major}*
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/libQt%{api}Concurrent.so.%{major}*
%endif

#----------------------------------------------------------------------------

%package -n %{qtconcurrentd}
Summary:	Development files for version 5 of the QtConcurrent library
Group:		Development/KDE and Qt
Requires:	%{qtconcurrent} = %{EVRD}
# Was introduced by mistake
Obsoletes:	%{_lib}qt5concurrent5-devel < %{EVRD}

%description -n %{qtconcurrentd}
Development files for version 5 of the QtConcurrent library.

%files -n %{qtconcurrentd}
%{_qt_includedir}/QtConcurrent
%{_qt_libdir}/libQt%{api}Concurrent.so
%{_qt_libdir}/libQt%{api}Concurrent.prl
%{_qt_libdir}/cmake/Qt%{api}Concurrent
%{_qt_libdir}/pkgconfig/Qt%{api}Concurrent.pc
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/pkgconfig/Qt%{api}Concurrent.pc
%endif

#----------------------------------------------------------------------------

%package -n %{qtcore}
Summary:	Qt Core library
Group:		System/Libraries
Requires:	%{name}-qtcore-i18n = %{EVRD}
Obsoletes:	%{_lib}qt5v85 < 5.1.0-8
Obsoletes:	%{_lib}qt5v8_5 < 5.2.0

%description -n %{qtcore}
Qt Core library.

%files -n %{qtcore}
%{_qt_libdir}/libQt%{api}Core.so.%{major}*
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/libQt%{api}Core.so.%{major}*
%endif
%dir %{_qt_plugindir}
%{_sysconfdir}/xdg/qtchooser/*.conf

#----------------------------------------------------------------------------

%package -n %{qtcored}
Summary:	Development files for version 5 of the QtCore library
Group:		Development/KDE and Qt
Requires:	%{qtcore} = %{EVRD}
Obsoletes:	%{_lib}qt5v8-devel < 5.2.0

%description -n %{qtcored}
Development files for version 5 of the QtCore library.

%files -n %{qtcored}
%{_qt_docdir}/global
%{_bindir}/moc-qt%{api}
%{_qt_bindir}/moc
%{_qt_bindir}/syncqt*
%{_bindir}/rcc-qt%{api}
%{_qt_bindir}/rcc
%{_qt_includedir}/QtCore
%{_qt_libdir}/libQt%{api}Core.so
%{_qt_libdir}/libQt%{api}Core.prl
%{_qt_libdir}/cmake/Qt%{api}Core
%{_qt_libdir}/cmake/Qt%{api}/Qt%{api}Config.cmake
%{_qt_libdir}/cmake/Qt%{api}/Qt%{api}ConfigVersion.cmake
%{_qt_libdir}/pkgconfig/Qt%{api}Core.pc
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/pkgconfig/Qt%{api}Core.pc
%endif
%dir %{_qt_libdir}/cmake
%dir %{_qt_libdir}/cmake/Qt%{api}
%dir %{_qt_libdir}/pkgconfig

#----------------------------------------------------------------------------

%package qtcore-i18n
Summary:	Qt Core translations
Group:		System/Libraries
Conflicts:	%{qtcore} < 5.1.0-6
BuildArch:	noarch

%description qtcore-i18n
Qt Core translations.

%files qtcore-i18n
%dir %{_qt_translationsdir}
%lang(ar) %{_qt_translationsdir}/qt_ar.qm
%lang(ca) %{_qt_translationsdir}/qt_ca.qm
%lang(cs) %{_qt_translationsdir}/qt_cs.qm
%lang(da) %{_qt_translationsdir}/qt_da.qm
%lang(de) %{_qt_translationsdir}/qt_de.qm
%lang(es) %{_qt_translationsdir}/qt_es.qm
%lang(fa) %{_qt_translationsdir}/qt_fa.qm
%lang(fi) %{_qt_translationsdir}/qt_fi.qm
%lang(fr) %{_qt_translationsdir}/qt_fr.qm
%lang(gl) %{_qt_translationsdir}/qt_gl.qm
%lang(he) %{_qt_translationsdir}/qt_he.qm
%lang(hu) %{_qt_translationsdir}/qt_hu.qm
%lang(it) %{_qt_translationsdir}/qt_it.qm
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
%lang(it) %{_qt_translationsdir}/qt_help_it.qm
%lang(ja) %{_qt_translationsdir}/qt_help_ja.qm
%lang(ko) %{_qt_translationsdir}/qt_help_ko.qm
%lang(pl) %{_qt_translationsdir}/qt_help_pl.qm
%lang(ru) %{_qt_translationsdir}/qt_help_ru.qm
%lang(sk) %{_qt_translationsdir}/qt_help_sk.qm
%lang(sl) %{_qt_translationsdir}/qt_help_sl.qm
%lang(uk) %{_qt_translationsdir}/qt_help_uk.qm
%lang(zh_CN) %{_qt_translationsdir}/qt_help_zh_CN.qm
%lang(zh_TW) %{_qt_translationsdir}/qt_help_zh_TW.qm
%lang(ca) %{_qt_translationsdir}/qtbase_ca.qm
%lang(cs) %{_qt_translationsdir}/qtbase_cs.qm
%lang(de) %{_qt_translationsdir}/qtbase_de.qm
%lang(fi) %{_qt_translationsdir}/qtbase_fi.qm
%lang(hu) %{_qt_translationsdir}/qtbase_hu.qm
%lang(it) %{_qt_translationsdir}/qtbase_it.qm
%lang(ja) %{_qt_translationsdir}/qtbase_ja.qm
%lang(ru) %{_qt_translationsdir}/qtbase_ru.qm
%lang(sk) %{_qt_translationsdir}/qtbase_sk.qm
%lang(uk) %{_qt_translationsdir}/qtbase_uk.qm
%lang(de) %{_qt_translationsdir}/qtconnectivity_de.qm
%lang(uk) %{_qt_translationsdir}/qtconnectivity_uk.qm
%lang(de) %{_qt_translationsdir}/qtlocation_de.qm
%lang(uk) %{_qt_translationsdir}/qtlocation_uk.qm

#----------------------------------------------------------------------------

%package -n %{qtdbus}
Summary:	Qt DBus connector library
Group:		System/Libraries

%description -n %{qtdbus}
Qt DBus connector library.

%files -n %{qtdbus}
%{_qt_libdir}/libQt%{api}DBus.so.%{major}*
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/libQt%{api}DBus.so.%{major}*
%endif

#----------------------------------------------------------------------------

%package -n %{qtdbusd}
Summary:	Development files for version 5 of the QtDBus library
Group:		Development/KDE and Qt
Requires:	%{qtdbus} = %{EVRD}

%description -n %{qtdbusd}
Development files for version 5 of the QtDBus library.

%files -n %{qtdbusd}
%{_qt_bindir}/qdbuscpp2xml
%{_bindir}/qdbuscpp2xml-qt%{api}
%{_qt_bindir}/qdbusxml2cpp
%{_bindir}/qdbusxml2cpp-qt%{api}
%{_qt_includedir}/QtDBus
%{_qt_libdir}/libQt%{api}DBus.so
%{_qt_libdir}/libQt%{api}DBus.prl
%{_qt_libdir}/cmake/Qt%{api}DBus
%{_qt_libdir}/pkgconfig/Qt%{api}DBus.pc
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/pkgconfig/Qt%{api}DBus.pc
%endif

#----------------------------------------------------------------------------

%package -n %{qtgui}
Summary:	Qt GUI library
Group:		System/Libraries
Suggests:	qt5-style-plugins
Requires:	qt5-output-driver = %{EVRD}
Suggests:	qt5-output-driver-default = %{EVRD}

%description -n %{qtgui}
Qt GUI library.

%files -n %{qtgui}
%{_qt_libdir}/libQt%{api}Gui.so.%{major}*
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/libQt%{api}Gui.so.%{major}*
%endif
%{_qt_plugindir}/imageformats
%dir %{_qt_plugindir}/platforminputcontexts
%dir %{_qt_plugindir}/platforms
%if %{with gtk}
%dir %{_qt_plugindir}/platformthemes
%endif
%dir %{_qt_plugindir}/iconengines
%{_qt_plugindir}/generic
%{_qt_plugindir}/printsupport

#----------------------------------------------------------------------------

%package -n %{qtguid}
Summary:	Development files for version 5 of the QtGui library
Group:		Development/KDE and Qt
Requires:	%{qtgui} = %{EVRD}
# We need all the Platform plugins because the plugin related cmake files in
# %{_qt_libdir}/cmake/Qt%{api}Gui cause fatal errors if the plugins aren't
# installed.
%if %{with directfb}
Requires:	%{qtgui}-directfb = %{EVRD}
%endif
%ifos linux
Requires:	%{qtgui}-linuxfb = %{EVRD}
%endif
Requires:	%{qtgui}-minimal = %{EVRD}
Requires:	%{qtgui}-offscreen = %{EVRD}
Requires:	%{qtgui}-x11 = %{EVRD}
Requires:	%{qtgui}-eglfs = %{EVRD}
Requires:	%{qtgui}-kms = %{EVRD}
Requires:	%{qtgui}-minimalegl = %{EVRD}
%if %{with gtk}
Requires:	%{name}-platformtheme-gtk2 = %{EVRD}
%endif
Requires:	pkgconfig(gl)
Requires:	pkgconfig(egl)
Requires:	pkgconfig(glesv2)

%description -n %{qtguid}
Development files for version 5 of the QtGui library.

%files -n %{qtguid}
%{_qt_bindir}/uic
%{_bindir}/uic-qt%{api}
%{_qt_includedir}/QtGui
%{_qt_includedir}/QtPlatformHeaders
%{_qt_includedir}/QtPlatformSupport
%{_qt_includedir}/QtUiTools
%{_qt_libdir}/libQt%{api}Gui.so
%{_qt_libdir}/libQt%{api}Gui.prl
%{_qt_libdir}/libQt%{api}PlatformSupport.a
%{_qt_libdir}/libQt%{api}PlatformSupport.prl
%{_qt_libdir}/libQt%{api}UiTools.a
%{_qt_libdir}/libQt%{api}UiTools.prl
%{_qt_libdir}/cmake/Qt%{api}Gui
%{_qt_libdir}/cmake/Qt%{api}UiTools
%{_qt_libdir}/pkgconfig/Qt%{api}Gui.pc
%{_qt_libdir}/pkgconfig/Qt%{api}PlatformSupport.pc
%{_qt_libdir}/pkgconfig/Qt%{api}UiTools.pc
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/pkgconfig/Qt%{api}Gui.pc
%{_libdir}/pkgconfig/Qt%{api}PlatformSupport.pc
%{_libdir}/pkgconfig/Qt%{api}UiTools.pc
%endif

#----------------------------------------------------------------------------
%if %{with directfb}
%package -n %{qtgui}-directfb
Summary:	DirectFB output driver for QtGui v5
Group:		System/Libraries
Requires:	%{qtgui} = %{EVRD}
Provides:	qt5-output-driver = %{EVRD}

%description -n %{qtgui}-directfb
DirectFB output driver for QtGui v5.

%files -n %{qtgui}-directfb
%{_qt_plugindir}/platforms/libqdirectfb.so
%endif

#----------------------------------------------------------------------------

%package -n %{qtgui}-linuxfb
Summary:	Linux Framebuffer output driver for QtGui v5
Group:		System/Libraries
Requires:	%{qtgui} = %{EVRD}
Provides:	qt5-output-driver = %{EVRD}

%description -n %{qtgui}-linuxfb
Linux Framebuffer output driver for QtGui v5.

%files -n %{qtgui}-linuxfb
%{_qt_plugindir}/platforms/libqlinuxfb.so
# FIXME need to determine why those aren't built all the time. We're probably
# missing a BuildRequires: somewhere.
%optional %{_qt_libdir}/fonts

#----------------------------------------------------------------------------

%package -n %{qtgui}-minimal
Summary:	Minimal (Framebuffer based) output driver for QtGui v5
Group:		System/Libraries
Requires:	%{qtgui} = %{EVRD}
Provides:	qt5-output-driver = %{EVRD}

%description -n %{qtgui}-minimal
Minimal (Framebuffer based) output driver for QtGui v5.

%files -n %{qtgui}-minimal
%{_qt_plugindir}/platforms/libqminimal.so

#----------------------------------------------------------------------------

%package -n %{qtgui}-offscreen
Summary:	Offscreen output driver for QtGui v5
Group:		System/Libraries
Requires:	%{qtgui} = %{EVRD}
Provides:	qt5-output-driver = %{EVRD}

%description -n %{qtgui}-offscreen
Minimal (Framebuffer based) output driver for QtGui v5.

%files -n %{qtgui}-offscreen
%{_qt_plugindir}/platforms/libqoffscreen.so

#----------------------------------------------------------------------------

%package -n %{qtgui}-x11
Summary:	X11 output driver for QtGui v5
Group:		System/Libraries
Requires:	%{qtgui} = %{EVRD}
Provides:	qt5-output-driver = %{EVRD}
Provides:	qt5-output-driver-default = %{EVRD}

%description -n %{qtgui}-x11
X11 output driver for QtGui v5.

%files -n %{qtgui}-x11
%{_qt_plugindir}/platforms/libqxcb.so
%{_qt_plugindir}/platforminputcontexts/libibusplatforminputcontextplugin.so
%{_qt_plugindir}/platforminputcontexts/libcomposeplatforminputcontextplugin.so

#----------------------------------------------------------------------------

%package -n %{qtgui}-eglfs
Summary:	EGL fullscreen output driver for QtGui v5
Group:		System/Libraries
Requires:	%{qtgui} = %{EVRD}
Provides:	qt5-output-driver = %{EVRD}

%description -n %{qtgui}-eglfs
EGL fullscreen output driver for QtGui v5.

%files -n %{qtgui}-eglfs
%{_qt_plugindir}/platforms/libqeglfs.so

#----------------------------------------------------------------------------

%package -n %{qtgui}-kms
Summary:	KMS output driver for QtGui v5
Group:		System/Libraries
Requires:	%{qtgui} = %{EVRD}
Provides:	qt5-output-driver = %{EVRD}

%description -n %{qtgui}-kms
KMS output driver for QtGui v5.

%files -n %{qtgui}-kms
%{_qt_plugindir}/platforms/libqkms.so

#----------------------------------------------------------------------------

%package -n %{qtgui}-minimalegl
Summary:	Minimalistic EGL output driver for QtGui v5
Group:		System/Libraries
Requires:	%{qtgui} = %{EVRD}
Provides:	qt5-output-driver = %{EVRD}

%description -n %{qtgui}-minimalegl
Minimalistic EGL output driver for QtGui v5.

%files -n %{qtgui}-minimalegl
%{_qt_plugindir}/platforms/libqminimalegl.so

#----------------------------------------------------------------------------
%package -n %{qtlocation}
Summary:	Qt Location library
Group:		System/Libraries

%description -n %{qtlocation}
Qt Location library

%files -n %{qtlocation}
%{_qt_libdir}/libQt%{api}Location.so.%{major}*
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/libQt%{api}Location.so.%{major}*
%endif
%dir %{_qt_plugindir}/geoservices
%{_qt_plugindir}/geoservices/libqtgeoservices_nokia.so
%{_qt_plugindir}/geoservices/libqtgeoservices_osm.so
%{_qt_prefix}/qml/QtLocation

#----------------------------------------------------------------------------

%package -n %{qtlocationd}
Summary:	Development files for version %{api} of the QtLocation library
Group:		Development/KDE and Qt
Requires:	%{qtlocation} = %{EVRD}

%description -n %{qtlocationd}
Development files for version %{api} of the QtLocation library.

%files -n %{qtlocationd}
%{_qt_includedir}/QtLocation
%{_qt_libdir}/libQt%{api}Location.so
%{_qt_libdir}/libQt%{api}Location.prl
%{_qt_libdir}/cmake/Qt%{api}Location
%{_qt_libdir}/pkgconfig/Qt%{api}Location.pc
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/pkgconfig/Qt%{api}Location.pc
%endif


#----------------------------------------------------------------------------

%package -n %{qtnetwork}
Summary:	Qt Networking library
Group:		System/Libraries

%description -n %{qtnetwork}
Qt Networking library.

%files -n %{qtnetwork}
%{_qt_libdir}/libQt%{api}Network.so.%{major}*
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/libQt%{api}Network.so.%{major}*
%endif
%{_qt_plugindir}/bearer

#----------------------------------------------------------------------------

%package -n %{qtnetworkd}
Summary:	Development files for version %{api} of the QtNetwork library
Group:		Development/KDE and Qt
Requires:	%{qtnetwork} = %{EVRD}

%description -n %{qtnetworkd}
Development files for version %{api} of the QtNetwork library.

%files -n %{qtnetworkd}
%{_qt_includedir}/QtNetwork
%{_qt_libdir}/libQt%{api}Network.so
%{_qt_libdir}/libQt%{api}Network.prl
%{_qt_libdir}/cmake/Qt%{api}Network
%{_qt_libdir}/pkgconfig/Qt%{api}Network.pc
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/pkgconfig/Qt%{api}Network.pc
%endif

#----------------------------------------------------------------------------

%package -n %{qtnfc}
Summary:	Qt NFC library
Group:		System/Libraries

%description -n %{qtnfc}
Qt NFC library.

NFC is an extremely short-range (less than 20 centimeters) wireless technology
and has a maximum transfer rate of 424 kbit/s. NFC is ideal for transferring
small packets of data when two devices are touched together.

%files -n %{qtnfc}
%{_qt_libdir}/libQt%{api}Nfc.so.%{major}*
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/libQt%{api}Nfc.so.%{major}*
%endif
%{_qt_prefix}/qml/QtNfc

#----------------------------------------------------------------------------

%package -n %{qtnfcd}
Summary:	Development files for version 5 of the QtNfc library
Group:		Development/KDE and Qt
Requires:	%{qtnfc} = %{EVRD}

%description -n %{qtnfcd}
Development files for version 5 of the QtNfc library.

%files -n %{qtnfcd}
%{_qt_includedir}/QtNfc
%{_qt_libdir}/libQt%{api}Nfc.so
%{_qt_libdir}/libQt%{api}Nfc.prl
%{_qt_libdir}/cmake/Qt%{api}Nfc
%{_qt_libdir}/pkgconfig/Qt%{api}Nfc.pc
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/pkgconfig/Qt%{api}Nfc.pc
%endif

#----------------------------------------------------------------------------

%package -n %{qtopengl}
Summary:	Qt OpenGL (3D Graphics) library
Group:		System/Libraries

%description -n %{qtopengl}
Qt OpenGL (3D Graphics) library.

%files -n %{qtopengl}
%{_qt_libdir}/libQt%{api}OpenGL.so.%{major}*
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/libQt%{api}OpenGL.so.%{major}*
%endif

#----------------------------------------------------------------------------

%package -n %{qtopengld}
Summary:	Development files for version 5 of the QtOpenGL library
Group:		Development/KDE and Qt
Requires:	%{qtopengl} = %{EVRD}

%description -n %{qtopengld}
Development files for version 5 of the QtOpenGL library.

%files -n %{qtopengld}
%{_qt_includedir}/QtOpenGL
%{_qt_includedir}/QtOpenGLExtensions
%{_qt_libdir}/libQt%{api}OpenGL.so
%{_qt_libdir}/libQt%{api}OpenGL.prl
%{_qt_libdir}/libQt%{api}OpenGLExtensions.a
%{_qt_libdir}/libQt%{api}OpenGLExtensions.prl
%{_qt_libdir}/cmake/Qt%{api}OpenGL
%{_qt_libdir}/cmake/Qt%{api}OpenGLExtensions
%{_qt_libdir}/pkgconfig/Qt%{api}OpenGL.pc
%{_qt_libdir}/pkgconfig/Qt%{api}OpenGLExtensions.pc
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/pkgconfig/Qt%{api}OpenGL.pc
%{_libdir}/pkgconfig/Qt%{api}OpenGLExtensions.pc
%endif

#----------------------------------------------------------------------------

%package -n %{qtpositioning}
Summary:	Qt Positioning library
Group:		System/Libraries

%description -n %{qtpositioning}
Qt Positioning library.

The Qt Positioning API gives developers the ability to determine a position by
using a variety of possible sources, including satellite, or wifi, or text
file, and so on. That information can then be used to for example determine
a position on a map. In addition satellite information can be retrieved and
area based monitoring can be performed.

%files -n %{qtpositioning}
%{_qt_libdir}/libQt%{api}Positioning.so.%{major}*
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/libQt%{api}Positioning.so.%{major}*
%endif
%{_qt_prefix}/qml/QtPositioning
%{_qt_plugindir}/position

#----------------------------------------------------------------------------

%package -n %{qtpositioningd}
Summary:	Development files for version 5 of the QtPositioning library
Group:		Development/KDE and Qt
Requires:	%{qtpositioning} = %{EVRD}

%description -n %{qtpositioningd}
Development files for version 5 of the QtPositioning library.

%files -n %{qtpositioningd}
%{_qt_includedir}/QtPositioning
%{_qt_libdir}/libQt%{api}Positioning.so
%{_qt_libdir}/libQt%{api}Positioning.prl
%{_qt_libdir}/cmake/Qt%{api}Positioning
%{_qt_libdir}/pkgconfig/Qt%{api}Positioning.pc
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/pkgconfig/Qt%{api}Positioning.pc
%endif

#----------------------------------------------------------------------------

%package -n %{qtprintsupport}
Summary:	Qt printing library
Group:		System/Libraries

%description -n %{qtprintsupport}
Qt printing library.

%files -n %{qtprintsupport}
%{_qt_libdir}/libQt%{api}PrintSupport.so.%{major}*
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/libQt%{api}PrintSupport.so.%{major}*
%endif

#----------------------------------------------------------------------------

%package -n %{qtprintsupportd}
Summary:	Development files for version 5 of the QtPrintSupport library
Group:		Development/KDE and Qt
Requires:	%{qtprintsupport} = %{EVRD}

%description -n %{qtprintsupportd}
Development files for version 5 of the QtPrintSupport library.

%files -n %{qtprintsupportd}
%{_qt_includedir}/QtPrintSupport
%{_qt_libdir}/libQt%{api}PrintSupport.so
%{_qt_libdir}/libQt%{api}PrintSupport.prl
%{_qt_libdir}/cmake/Qt%{api}PrintSupport
%{_qt_libdir}/pkgconfig/Qt%{api}PrintSupport.pc
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/pkgconfig/Qt%{api}PrintSupport.pc
%endif

#----------------------------------------------------------------------------

%package -n %{qtsensors}
Summary:	Qt Sensors library
Group:		System/Libraries

%description -n %{qtsensors}
Qt Sensors library.

%files -n %{qtsensors}
%{_qt_libdir}/libQt%{api}Sensors.so.%{major}*
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/libQt%{api}Sensors.so.%{major}*
%endif
%{_qt_prefix}/qml/QtSensors
%{_qt_plugindir}/sensorgestures
%{_qt_plugindir}/sensors

#----------------------------------------------------------------------------

%package -n %{qtsensorsd}
Summary:	Development files for the QtSensors library
Group:		Development/KDE and Qt
Requires:	%{qtsensors} = %{EVRD}

%description -n %{qtsensorsd}
Development files for the QtSensors library.

%files -n %{qtsensorsd}
%{_qt_includedir}/QtSensors
%{_qt_libdir}/libQt%{api}Sensors.so
%{_qt_libdir}/libQt%{api}Sensors.prl
%{_qt_libdir}/cmake/Qt%{api}Sensors
%{_qt_libdir}/pkgconfig/Qt%{api}Sensors.pc
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/pkgconfig/Qt%{api}Sensors.pc
%endif

#----------------------------------------------------------------------------

%package -n %{qtserialport}
Summary:	Qt Serial Port library
Group:		System/Libraries

%description -n %{qtserialport}
Qt Serial Port library.

%files -n %{qtserialport}
%{_qt_libdir}/libQt%{api}SerialPort.so.%{major}*
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/libQt%{api}SerialPort.so.%{major}*
%endif

#----------------------------------------------------------------------------

%package -n %{qtserialportd}
Summary:	Development files for the QtSerialPort library
Group:		Development/KDE and Qt
Requires:	%{qtserialport} = %{EVRD}

%description -n %{qtserialportd}
Development files for the QtSerialPort library.

%files -n %{qtserialportd}
%{_qt_includedir}/QtSerialPort
%{_qt_libdir}/libQt%{api}SerialPort.so
%{_qt_libdir}/libQt%{api}SerialPort.prl
%{_qt_libdir}/cmake/Qt%{api}SerialPort
%{_qt_libdir}/pkgconfig/Qt%{api}SerialPort.pc
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/pkgconfig/Qt%{api}SerialPort.pc
%endif

#----------------------------------------------------------------------------

%package -n %{qtsql}
Summary:	Qt SQL library
Group:		System/Libraries

%description -n %{qtsql}
Qt SQL library.

%files -n %{qtsql}
%{_qt_libdir}/libQt%{api}Sql.so.%{major}*
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/libQt%{api}Sql.so.%{major}*
%endif
%dir %{_qt_plugindir}/sqldrivers

#----------------------------------------------------------------------------

%package -n %{qtsqld}
Summary:	Development files for version 5 of the QtSql library
Group:		Development/KDE and Qt
Requires:	%{qtsql} = %{EVRD}
# We need all the QtSql plugins because the plugin related cmake files in
# %{_qt_libdir}/cmake/Qt%{api}Sql cause fatal errors if the plugins aren't
# installed.
Requires:	%{qtsql}-mysql = %{EVRD}
Requires:	%{qtsql}-odbc = %{EVRD}
Requires:	%{qtsql}-postgresql = %{EVRD}
Requires:	%{qtsql}-sqlite = %{EVRD}

%description -n %{qtsqld}
Development files for version 5 of the QtSql library.

%files -n %{qtsqld}
%{_qt_includedir}/QtSql
%{_qt_libdir}/libQt%{api}Sql.so
%{_qt_libdir}/libQt%{api}Sql.prl
%{_qt_libdir}/cmake/Qt%{api}Sql
%{_qt_libdir}/pkgconfig/Qt%{api}Sql.pc
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/pkgconfig/Qt%{api}Sql.pc
%endif

#----------------------------------------------------------------------------

%package -n %{qtsql}-mysql
Summary:	MySQL support for the QtSql library v5
Group:		System/Libraries
Requires:	%{qtsql} = %{EVRD}
Provides:	%{name}-database-plugin-mysql = %{EVRD}
BuildRequires:	mysql-devel

%description -n %{qtsql}-mysql
MySQL support for the QtSql library v5.

%files -n %{qtsql}-mysql
%{_qt_plugindir}/sqldrivers/libqsqlmysql.so

#----------------------------------------------------------------------------

%package -n %{qtsql}-odbc
Summary:	ODBC support for the QtSql library v5
Group:		System/Libraries
Requires:	%{qtsql} = %{EVRD}
Provides:	%{name}-database-plugin-odbc = %{EVRD}
BuildRequires:	pkgconfig(libiodbc)
BuildRequires:	unixODBC-devel

%description -n %{qtsql}-odbc
ODBC support for the QtSql library v5.

%files -n %{qtsql}-odbc
%{_qt_plugindir}/sqldrivers/libqsqlodbc.so

#----------------------------------------------------------------------------

%package -n %{qtsql}-postgresql
Summary:	PostgreSQL support for the QtSql library v5
Group:		System/Libraries
Requires:	%{qtsql} = %{EVRD}
Provides:	%{name}-database-plugin-postgresql = %{EVRD}
BuildRequires:	postgresql-devel >= 9.0

%description -n %{qtsql}-postgresql
PostgreSQL support for the QtSql library v5.

%files -n %{qtsql}-postgresql
%{_qt_plugindir}/sqldrivers/libqsqlpsql.so

#----------------------------------------------------------------------------

%package -n %{qtsql}-sqlite
Summary:	SQLite 3.x support for the QtSql library v5
Group:		System/Libraries
Requires:	%{qtsql} = %{EVRD}
Provides:	%{name}-database-plugin-sqlite = %{EVRD}
BuildRequires:	pkgconfig(sqlite3)

%description -n %{qtsql}-sqlite
SQLite 3.x support for the QtSql library v5.

%files -n %{qtsql}-sqlite
%{_qt_plugindir}/sqldrivers/libqsqlite.so

#----------------------------------------------------------------------------

%package -n %{qttest}
Summary:	Qt unit test library
Group:		System/Libraries

%description -n %{qttest}
Qt unit test library.

%files -n %{qttest}
%{_qt_libdir}/libQt%{api}Test.so.%{major}*
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/libQt%{api}Test.so.%{major}*
%endif
%{_qt_prefix}/qml/QtTest

#----------------------------------------------------------------------------

%package -n %{qttestd}
Summary:	Development files for version 5 of the QtTest library
Group:		Development/KDE and Qt
Requires:	%{qttest} = %{EVRD}

%description -n %{qttestd}
Development files for version 5 of the QtTest library.

%files -n %{qttestd}
%{_qt_includedir}/QtTest
%{_qt_libdir}/libQt%{api}Test.so
%{_qt_libdir}/libQt%{api}Test.prl
%{_qt_libdir}/cmake/Qt%{api}Test
%{_qt_libdir}/pkgconfig/Qt%{api}Test.pc
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/pkgconfig/Qt%{api}Test.pc
%endif

#----------------------------------------------------------------------------

%package -n %{qtwidgets}
Summary:	Qt Widget library
Group:		System/Libraries

%description -n %{qtwidgets}
Qt Widget library.

%files -n %{qtwidgets}
%{_qt_libdir}/libQt%{api}Widgets.so.%{major}*
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/libQt%{api}Widgets.so.%{major}*
%endif

#----------------------------------------------------------------------------

%package -n %{qtwidgetsd}
Summary:	Development files for version 5 of the QtWidgets library
Group:		Development/KDE and Qt
Requires:	%{qtwidgets} = %{EVRD}

%description -n %{qtwidgetsd}
Development files for version 5 of the QtWidgets library.

%files -n %{qtwidgetsd}
%{_qt_includedir}/QtWidgets
%{_qt_libdir}/libQt%{api}Widgets.so
%{_qt_libdir}/libQt%{api}Widgets.prl
%{_qt_libdir}/cmake/Qt%{api}Widgets
%{_qt_libdir}/pkgconfig/Qt%{api}Widgets.pc
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/pkgconfig/Qt%{api}Widgets.pc
%endif

#----------------------------------------------------------------------------
%package -n %{qtquickwidgets}
Summary:	Library for integrating QtQuick with traditional Qt widgets
Group:		System/Libraries

%description -n %{qtquickwidgets}
Library for integrating QtQuick with traditional Qt widgets

%files -n %{qtquickwidgets}
%{_qt_libdir}/libQt%{api}QuickWidgets.so.%{major}*
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/libQt%{api}QuickWidgets.so.%{major}*
%endif

#----------------------------------------------------------------------------
%package -n %{qtquickwidgetsd}
Summary:	Development files for version 5 of the QtQuickWidgets library
Group:		Development/KDE and Qt
Requires:	%{qtquickwidgets} = %{EVRD}

%description -n %{qtquickwidgetsd}
Development files for version 5 of the QtQuickWidgets library.

%files -n %{qtquickwidgetsd}
%{_qt_includedir}/QtQuickWidgets
%{_qt_libdir}/libQt%{api}QuickWidgets.so
%{_qt_libdir}/libQt%{api}QuickWidgets.prl
%{_qt_libdir}/cmake/Qt%{api}QuickWidgets
%{_qt_libdir}/pkgconfig/Qt%{api}QuickWidgets.pc
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/pkgconfig/Qt%{api}QuickWidgets.pc
%endif

#----------------------------------------------------------------------------
%package -n %{qtwebchannel}
Summary:	Qt %{api} WebChannel library
Group:		System/Libraries

%description -n %{qtwebchannel}
Qt %{api} WebChannel library,  a library for communication between
HTML/JavaScript and Qt/QML objects.

%files -n %{qtwebchannel}
%{_qt_libdir}/libQt%{api}WebChannel.so.%{major}*
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/libQt%{api}WebChannel.so.%{major}*
%endif
%{_qt_prefix}/qml/QtWebChannel

#----------------------------------------------------------------------------
%package -n %{qtwebchanneld}
Summary:	Development files for the Qt %{api} WebChannel library
Group:		Development/KDE and Qt
Requires:	%{qtwebchannel} = %{EVRD}

%description -n %{qtwebchanneld}
Development files for version %{api} of the QtWebChannel library,
a library for communication between HTML/JavaScript and Qt/QML
objects.

%files -n %{qtwebchanneld}
%{_qt_includedir}/QtWebChannel
%{_qt_libdir}/libQt%{api}WebChannel.so
%{_qt_libdir}/libQt%{api}WebChannel.prl
%{_qt_libdir}/cmake/Qt%{api}WebChannel
%{_qt_libdir}/pkgconfig/Qt%{api}WebChannel.pc
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/pkgconfig/Qt%{api}WebChannel.pc
%endif


#----------------------------------------------------------------------------
%package -n %{qtwebsockets}
Summary:	Qt %{api} WebSockets library
Group:		System/Libraries

%description -n %{qtwebsockets}
Qt %{api} WebSockets library

%files -n %{qtwebsockets}
%{_qt_libdir}/libQt%{api}WebSockets.so.%{major}*
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/libQt%{api}WebSockets.so.%{major}*
%endif
%{_qt_prefix}/qml/Qt/WebSockets

#----------------------------------------------------------------------------
%package -n %{qtwebsocketsd}
Summary:	Development files for the Qt %{api} WebSockets library
Group:		Development/KDE and Qt
Requires:	%{qtwebsockets} = %{EVRD}

%description -n %{qtwebsocketsd}
Development files for version 5 of the QtWebSockets library.

%files -n %{qtwebsocketsd}
%{_qt_includedir}/QtWebSockets
%{_qt_libdir}/libQt%{api}WebSockets.so
%{_qt_libdir}/libQt%{api}WebSockets.prl
%{_qt_libdir}/cmake/Qt%{api}WebSockets
%{_qt_libdir}/pkgconfig/Qt%{api}WebSockets.pc
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/pkgconfig/Qt%{api}WebSockets.pc
%endif

#----------------------------------------------------------------------------

%package -n %{qtxml}
Summary:	Qt XML library
Group:		System/Libraries

%description -n %{qtxml}
Qt XML library.

%files -n %{qtxml}
%{_qt_libdir}/libQt%{api}Xml.so.%{major}*
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/libQt%{api}Xml.so.%{major}*
%endif

#----------------------------------------------------------------------------

%package -n %{qtxmld}
Summary:	Development files for version 5 of the QtXml library
Group:		Development/KDE and Qt
Requires:	%{qtxml} = %{EVRD}

%description -n %{qtxmld}
Development files for version 5 of the QtXml library.

%files -n %{qtxmld}
%{_qt_includedir}/QtXml
%{_qt_libdir}/libQt%{api}Xml.so
%{_qt_libdir}/libQt%{api}Xml.prl
%{_qt_libdir}/cmake/Qt%{api}Xml
%{_qt_libdir}/pkgconfig/Qt%{api}Xml.pc
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/pkgconfig/Qt%{api}Xml.pc
%endif

#----------------------------------------------------------------------------
# qt extras
#----------------------------------------------------------------------------

%package -n %{qgsttools_p}
Summary:	Runtime library for GStreamer support in Qt 5
Group:		System/Libraries

%description -n %{qgsttools_p}
Runtime library for GStreamer support in Qt 5.

%files -n %{qgsttools_p}
%{_qt_libdir}/libqgsttools_p.so.%{qgstmajor}*
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/libqgsttools_p.so.%{qgstmajor}*
%endif

#----------------------------------------------------------------------------

%package -n %{qtclucene}
Summary:	Qt version of the CLucene search engine
Group:		System/Libraries

%description -n %{qtclucene}
Qt version of the CLucene search engine.

%files -n %{qtclucene}
%{_qt_libdir}/libQt%{api}CLucene.so.%{major}*
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/libQt%{api}CLucene.so.%{major}*
%endif

#----------------------------------------------------------------------------

%package -n %{qtclucened}
Summary:	Development files for the Qt version of the CLucene search engine
Group:		Development/KDE and Qt
Requires:	%{qtclucene} = %{EVRD}

%description -n %{qtclucened}
Development files for the Qt version of the CLucene search engine.

%files -n %{qtclucened}
%{_qt_includedir}/QtCLucene
%{_qt_libdir}/libQt%{api}CLucene.so
%{_qt_libdir}/libQt%{api}CLucene.prl
%{_qt_libdir}/pkgconfig/Qt%{api}CLucene.pc
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/pkgconfig/Qt%{api}CLucene.pc
%endif

#----------------------------------------------------------------------------

%package -n %{qtdeclarative}
Summary:	Runtime library for Qt Declarative
Group:		System/Libraries
Requires:	%{name}-qtdeclarative-i18n = %{EVRD}

%description -n %{qtdeclarative}
Runtime library for Qt Declarative.

%files -n %{qtdeclarative}
%{_qt_libdir}/libQt%{api}Declarative.so.%{major}*
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/libQt%{api}Declarative.so.%{major}*
%endif
%{_qt_plugindir}/qmltooling
%{_qt_bindir}/qmleasing
%{_qt_bindir}/qmllint

#----------------------------------------------------------------------------

%package -n %{qtdeclaratived}
Summary:	Development files for Qt Declarative
Group:		Development/KDE and Qt
Requires:	%{qtdeclarative} = %{EVRD}

%description -n %{qtdeclaratived}
Development files for Qt Declarative.

%files -n %{qtdeclaratived}
%{_qt_includedir}/QtDeclarative
%{_qt_libdir}/libQt%{api}Declarative.so
%{_qt_libdir}/libQt%{api}Declarative.prl
%{_qt_libdir}/cmake/Qt%{api}Declarative
%{_qt_libdir}/pkgconfig/Qt%{api}Declarative.pc
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/pkgconfig/Qt%{api}Declarative.pc
%endif

#----------------------------------------------------------------------------

%package qtdeclarative-i18n
Summary:	Qt Declarative translations
Group:		System/Libraries
Conflicts:	%{qtdeclarative} < 5.1.0-6
BuildArch:	noarch

%description qtdeclarative-i18n
Qt Declarative translations.

%files qtdeclarative-i18n
%lang(de) %{_qt_translationsdir}/qtdeclarative_de.qm
%lang(fi) %{_qt_translationsdir}/qtdeclarative_fi.qm
%lang(ja) %{_qt_translationsdir}/qtdeclarative_ja.qm
%lang(ru) %{_qt_translationsdir}/qtdeclarative_ru.qm
%lang(sk) %{_qt_translationsdir}/qtdeclarative_sk.qm
%lang(uk) %{_qt_translationsdir}/qtdeclarative_uk.qm

#----------------------------------------------------------------------------

%package -n %{qtdesignercomponents}
Summary:	Components for Qt Designer
Group:		System/Libraries

%description -n %{qtdesignercomponents}
Components for Qt Designer.

%files -n %{qtdesignercomponents}
%{_qt_libdir}/libQt%{api}DesignerComponents.so.%{major}*
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/libQt%{api}DesignerComponents.so.%{major}*
%endif

#----------------------------------------------------------------------------

%package -n %{qtdesignercomponentsd}
Summary:	Development files for Qt Designer Components
Group:		Development/KDE and Qt
Requires:	%{qtdesignercomponents} = %{EVRD}

%description -n %{qtdesignercomponentsd}
Development files for Qt Designer Components.

%files -n %{qtdesignercomponentsd}
%{_qt_includedir}/QtDesignerComponents
%{_qt_libdir}/libQt%{api}DesignerComponents.so
%{_qt_libdir}/libQt%{api}DesignerComponents.prl
%{_qt_libdir}/pkgconfig/Qt%{api}DesignerComponents.pc
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/pkgconfig/Qt%{api}DesignerComponents.pc
%endif

#----------------------------------------------------------------------------

%package -n %{qtdesigner}
Summary:	Qt Designer runtime libraries
Group:		System/Libraries

%description -n %{qtdesigner}
Qt Designer runtime libraries.

%files -n %{qtdesigner}
%{_qt_libdir}/libQt%{api}Designer.so.%{major}*
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/libQt%{api}Designer.so.%{major}*
%endif

#----------------------------------------------------------------------------

%package -n %{qtdesignerd}
Summary:	Development files for Qt Designer
Group:		Development/KDE and Qt
Requires:	%{qtdesigner} = %{EVRD}

%description -n %{qtdesignerd}
Development files for Qt Designer.

%files -n %{qtdesignerd}
%{_qt_includedir}/QtDesigner
%{_qt_libdir}/libQt%{api}Designer.so
%{_qt_libdir}/libQt%{api}Designer.prl
%{_qt_libdir}/cmake/Qt%{api}Designer
%{_qt_libdir}/pkgconfig/Qt%{api}Designer.pc
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/pkgconfig/Qt%{api}Designer.pc
%endif

#----------------------------------------------------------------------------

%package -n %{qthelp}
Summary:	Runtime libraries for the Qt Help system
Group:		System/Libraries

%description -n %{qthelp}
Runtime libraries for the Qt Help system.

%files -n %{qthelp}
%{_qt_libdir}/libQt%{api}Help.so.%{major}*
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/libQt%{api}Help.so.%{major}*
%endif

#----------------------------------------------------------------------------

%package -n %{qthelpd}
Summary:	Development files for Qt Help
Group:		Development/KDE and Qt
Requires:	%{qthelp} = %{EVRD}

%description -n %{qthelpd}
Development files for Qt Help, useful if you wish to add a help system
to your application.

%files -n %{qthelpd}
%{_qt_includedir}/QtHelp
%{_qt_libdir}/libQt%{api}Help.so
%{_qt_libdir}/libQt%{api}Help.prl
%{_qt_libdir}/cmake/Qt%{api}Help
%{_qt_libdir}/pkgconfig/Qt%{api}Help.pc
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/pkgconfig/Qt%{api}Help.pc
%endif

#----------------------------------------------------------------------------

%package -n %{qtmultimedia}
Summary:	Qt Multimedia libraries
Group:		System/Libraries
Requires:	%{name}-qtmultimedia-i18n = %{EVRD}

%description -n %{qtmultimedia}
Qt Multimedia libraries.

%files -n %{qtmultimedia}
%{_qt_libdir}/libQt%{api}Multimedia.so.%{major}*
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/libQt%{api}Multimedia.so.%{major}*
%endif
%{_qt_plugindir}/audio
%{_qt_plugindir}/mediaservice
%{_qt_plugindir}/playlistformats

#----------------------------------------------------------------------------

%package -n %{qtmultimediad}
Summary:	Development files for Qt Multimedia
Group:		Development/KDE and Qt
Requires:	%{qtmultimedia} = %{EVRD}

%description -n %{qtmultimediad}
Development files for Qt Multimedia.

%files -n %{qtmultimediad}
%{_qt_includedir}/QtMultimedia
%{_qt_includedir}/QtMultimediaQuick_p
%{_qt_libdir}/libQt%{api}Multimedia.so
%{_qt_libdir}/libQt%{api}Multimedia.prl
%{_qt_libdir}/cmake/Qt%{api}Multimedia
%{_qt_libdir}/pkgconfig/Qt%{api}Multimedia.pc
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/pkgconfig/Qt%{api}Multimedia.pc
%endif

#----------------------------------------------------------------------------

%package qtmultimedia-i18n
Summary:	Qt Multimedia translations
Group:		System/Libraries
Conflicts:	%{qtmultimedia} < 5.1.0-6
BuildArch:	noarch

%description qtmultimedia-i18n
Qt Multimedia translations.

%files qtmultimedia-i18n
%lang(ca) %{_qt_translationsdir}/qtmultimedia_ca.qm
%lang(cs) %{_qt_translationsdir}/qtmultimedia_cs.qm
%lang(de) %{_qt_translationsdir}/qtmultimedia_de.qm
%lang(fi) %{_qt_translationsdir}/qtmultimedia_fi.qm
%lang(hu) %{_qt_translationsdir}/qtmultimedia_hu.qm
%lang(it) %{_qt_translationsdir}/qtmultimedia_it.qm
%lang(ja) %{_qt_translationsdir}/qtmultimedia_ja.qm
%lang(ru) %{_qt_translationsdir}/qtmultimedia_ru.qm
%lang(sk) %{_qt_translationsdir}/qtmultimedia_sk.qm
%lang(uk) %{_qt_translationsdir}/qtmultimedia_uk.qm

#----------------------------------------------------------------------------

%package -n %{qtmultimediaquick_p}
Summary:	Runtime support library for the Qt Multimedia Quick module
Group:		System/Libraries

%description -n %{qtmultimediaquick_p}
Runtime support library for the Qt Multimedia Quick module.

%files -n %{qtmultimediaquick_p}
%{_qt_libdir}/libQt%{api}MultimediaQuick_p.so.%{major}*
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/libQt%{api}MultimediaQuick_p.so.%{major}*
%endif

#----------------------------------------------------------------------------

%package -n %{qtmultimediawidgets}
Summary:	Qt Multimedia Widgets library
Group:		System/Libraries

%description -n %{qtmultimediawidgets}
Qt Multimedia Widgets library.

%files -n %{qtmultimediawidgets}
%{_qt_libdir}/libQt%{api}MultimediaWidgets.so.%{major}*
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/libQt%{api}MultimediaWidgets.so.%{major}*
%endif

#----------------------------------------------------------------------------

%package -n %{qtmultimediawidgetsd}
Summary:	Development files for the Qt Multimedia Widgets library
Group:		Development/KDE and Qt
Requires:	%{qtmultimediawidgets} = %{EVRD}
Requires:	%{qtmultimediad} = %{EVRD}
Requires:	%{qtwidgetsd} = %{EVRD}

%description -n %{qtmultimediawidgetsd}
Development files for the Qt Multimedia Widgets library.

%files -n %{qtmultimediawidgetsd}
%{_qt_includedir}/QtMultimediaWidgets
%{_qt_libdir}/libQt%{api}MultimediaWidgets.so
%{_qt_libdir}/libQt%{api}MultimediaWidgets.prl
%{_qt_libdir}/cmake/Qt%{api}MultimediaWidgets
%{_qt_libdir}/pkgconfig/Qt%{api}MultimediaWidgets.pc
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/pkgconfig/Qt%{api}MultimediaWidgets.pc
%endif

#----------------------------------------------------------------------------

%package -n %{qtqml}
Summary:	QML runtime support library
Group:		System/Libraries

%description -n %{qtqml}
QML runtime support library.

%files -n %{qtqml}
%{_qt_libdir}/libQt%{api}Qml.so.%{major}*
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/libQt%{api}Qml.so.%{major}*
%endif
%dir %{_qt_prefix}/qml
%dir %{_qt_prefix}/qml/Qt
%dir %{_qt_prefix}/qml/Qt/labs
%{_qt_prefix}/qml/Qt/labs/folderlistmodel
%{_qt_prefix}/qml/Qt/labs/settings/
%{_qt_prefix}/qml/QtAudioEngine
%{_qt_prefix}/qml/QtGraphicalEffects
%{_qt_prefix}/qml/QtMultimedia
%{_qt_prefix}/qml/QtQml
%{_qt_plugindir}/qml1tooling/libqmldbg_inspector.so
%{_qt_plugindir}/qml1tooling/libqmldbg_tcp_qtdeclarative.so

#----------------------------------------------------------------------------

%package -n %{qtqmld}
Summary:	Development files for the Qt QML library
Group:		Development/KDE and Qt
Requires:	%{qtqml} = %{EVRD}

%description -n %{qtqmld}
Development files for the Qt QML library.

%files -n %{qtqmld}
%{_qt_includedir}/QtQml
%{_qt_libdir}/libQt%{api}Qml.so
%{_qt_libdir}/libQt%{api}Qml.prl
%{_qt_libdir}/libQt%{api}QmlDevTools.a
%{_qt_libdir}/libQt%{api}QmlDevTools.prl
%{_qt_libdir}/cmake/Qt%{api}Qml
%{_qt_libdir}/pkgconfig/Qt%{api}Qml.pc
%{_qt_libdir}/pkgconfig/Qt%{api}QmlDevTools.pc
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/pkgconfig/Qt%{api}Qml.pc
%{_libdir}/pkgconfig/Qt%{api}QmlDevTools.pc
%endif

#----------------------------------------------------------------------------

%package -n %{qtquick}
Summary:	Runtime library for Qt Quick
Group:		System/Libraries
Requires:	%{name}-qtquick-i18n = %{EVRD}

%description -n %{qtquick}
Runtime library for Qt Quick.

%files -n %{qtquick}
%{_qt_libdir}/libQt%{api}Quick.so.%{major}*
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/libQt%{api}Quick.so.%{major}*
%endif
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

#----------------------------------------------------------------------------

%package -n %{qtquickd}
Summary:	Development files for Qt Quick
Group:		Development/KDE and Qt
Requires:	%{qtquick} = %{EVRD}

%description -n %{qtquickd}
Development files for Qt Quick.

%files -n %{qtquickd}
%{_qt_includedir}/QtQuick
%{_qt_libdir}/libQt%{api}Quick.so
%{_qt_libdir}/libQt%{api}Quick.prl
%{_qt_libdir}/cmake/Qt%{api}Quick
%{_qt_libdir}/pkgconfig/Qt%{api}Quick.pc
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/pkgconfig/Qt%{api}Quick.pc
%endif

#----------------------------------------------------------------------------

%package qtquick-i18n
Summary:	Qt Quick translations
Group:		System/Libraries
Conflicts:	%{qtquick} < 5.1.0-6
BuildArch:	noarch

%description qtquick-i18n
Qt Quick translations.

%files qtquick-i18n
%lang(ca) %{_qt_translationsdir}/qtquick1_ca.qm
%lang(cs) %{_qt_translationsdir}/qtquick1_cs.qm
%lang(de) %{_qt_translationsdir}/qtquick1_de.qm
%lang(fi) %{_qt_translationsdir}/qtquick1_fi.qm
%lang(hu) %{_qt_translationsdir}/qtquick1_hu.qm
%lang(it) %{_qt_translationsdir}/qtquick1_it.qm
%lang(ja) %{_qt_translationsdir}/qtquick1_ja.qm
%lang(ru) %{_qt_translationsdir}/qtquick1_ru.qm
%lang(sk) %{_qt_translationsdir}/qtquick1_sk.qm
%lang(uk) %{_qt_translationsdir}/qtquick1_uk.qm
%lang(de) %{_qt_translationsdir}/qtquickcontrols_de.qm
%lang(ja) %{_qt_translationsdir}/qtquickcontrols_ja.qm
%lang(ru) %{_qt_translationsdir}/qtquickcontrols_ru.qm
%lang(uk) %{_qt_translationsdir}/qtquickcontrols_uk.qm

#----------------------------------------------------------------------------

%package -n %{qtquickparticles}
Summary:	Runtime library for Qt Quick's particle engine
Group:		System/Libraries

%description -n %{qtquickparticles}
Runtime library for Qt Quick's particle engine.

%files -n %{qtquickparticles}
%{_qt_libdir}/libQt%{api}QuickParticles.so.%{major}*
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/libQt%{api}QuickParticles.so.%{major}*
%endif

#----------------------------------------------------------------------------

%package -n %{qtquickparticlesd}
Summary:	Development files for Qt Quick's particle engine
Group:		Development/KDE and Qt
Requires:	%{qtquickparticles} = %{EVRD}

%description -n %{qtquickparticlesd}
Development files for Qt Quick's particle engine.

%files -n %{qtquickparticlesd}
%{_qt_includedir}/QtQuickParticles
%{_qt_libdir}/libQt%{api}QuickParticles.so
%{_qt_libdir}/libQt%{api}QuickParticles.prl
%{_qt_libdir}/pkgconfig/Qt%{api}QuickParticles.pc
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/pkgconfig/Qt%{api}QuickParticles.pc
%endif

#----------------------------------------------------------------------------

%package -n %{qtquicktest}
Summary:	Qt Quick unit test module
Group:		System/Libraries

%description -n %{qtquicktest}
Qt Quick unit test module.

%files -n %{qtquicktest}
%{_qt_libdir}/libQt%{api}QuickTest.so.%{major}*
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/libQt%{api}QuickTest.so.%{major}*
%endif

#----------------------------------------------------------------------------

%package -n %{qtquicktestd}
Summary:	Development files for Qt Quick's unit test module
Group:		Development/KDE and Qt
Requires:	%{qtquicktest} = %{EVRD}

%description -n %{qtquicktestd}
Development files for Qt Quick's unit test module.

%files -n %{qtquicktestd}
%{_qt_includedir}/QtQuickTest
%{_qt_libdir}/libQt%{api}QuickTest.so
%{_qt_libdir}/libQt%{api}QuickTest.prl
%{_qt_libdir}/cmake/Qt%{api}QuickTest
%{_qt_libdir}/pkgconfig/Qt%{api}QuickTest.pc
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/pkgconfig/Qt%{api}QuickTest.pc
%endif

#----------------------------------------------------------------------------

%package -n %{qtscript}
Summary:	Qt Script runtime library
Group:		System/Libraries
Requires:	%{name}-qtscript-i18n = %{EVRD}

%description -n %{qtscript}
Qt Script runtime library.

%files -n %{qtscript}
%{_qt_libdir}/libQt%{api}Script.so.%{major}*
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/libQt%{api}Script.so.%{major}*
%endif

#----------------------------------------------------------------------------

%package -n %{qtscriptd}
Summary:	Development files for Qt Script
Group:		Development/KDE and Qt
Requires:	%{qtscript} = %{EVRD}

%description -n %{qtscriptd}
Development files for Qt Script.

%files -n %{qtscriptd}
%{_qt_includedir}/QtScript
%{_qt_libdir}/libQt%{api}Script.so
%{_qt_libdir}/libQt%{api}Script.prl
%{_qt_libdir}/cmake/Qt%{api}Script
%{_qt_libdir}/pkgconfig/Qt%{api}Script.pc
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/pkgconfig/Qt%{api}Script.pc
%endif

#----------------------------------------------------------------------------

%package qtscript-i18n
Summary:	Qt Script translations
Group:		System/Libraries
Conflicts:	%{qtscript} < 5.1.0-6
BuildArch:	noarch

%description qtscript-i18n
Qt Script translations.

%files qtscript-i18n
%lang(ca) %{_qt_translationsdir}/qtscript_ca.qm
%lang(cs) %{_qt_translationsdir}/qtscript_cs.qm
%lang(de) %{_qt_translationsdir}/qtscript_de.qm
%lang(fi) %{_qt_translationsdir}/qtscript_fi.qm
%lang(hu) %{_qt_translationsdir}/qtscript_hu.qm
%lang(it) %{_qt_translationsdir}/qtscript_it.qm
%lang(ja) %{_qt_translationsdir}/qtscript_ja.qm
%lang(ru) %{_qt_translationsdir}/qtscript_ru.qm
%lang(sk) %{_qt_translationsdir}/qtscript_sk.qm
%lang(uk) %{_qt_translationsdir}/qtscript_uk.qm

#----------------------------------------------------------------------------

%package -n %{qtscripttools}
Summary:	Qt Script tools library
Group:		System/Libraries

%description -n %{qtscripttools}
Qt Script tools library.

%files -n %{qtscripttools}
%{_qt_libdir}/libQt%{api}ScriptTools.so.%{major}*
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/libQt%{api}ScriptTools.so.%{major}*
%endif

#----------------------------------------------------------------------------

%package -n %{qtscripttoolsd}
Summary:	Development files for Qt Script tools
Group:		Development/KDE and Qt
Requires:	%{qtscripttools} = %{EVRD}

%description -n %{qtscripttoolsd}
Development files for Qt Script tools.

%files -n %{qtscripttoolsd}
%{_qt_includedir}/QtScriptTools
%{_qt_libdir}/libQt%{api}ScriptTools.so
%{_qt_libdir}/libQt%{api}ScriptTools.prl
%{_qt_libdir}/cmake/Qt%{api}ScriptTools
%{_qt_libdir}/pkgconfig/Qt%{api}ScriptTools.pc
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/pkgconfig/Qt%{api}ScriptTools.pc
%endif

#----------------------------------------------------------------------------

%package -n %{qtsvg}
Summary:	Qt SVG rendering engine
Group:		System/Libraries

%description -n %{qtsvg}
Qt SVG rendering engine.

%files -n %{qtsvg}
%{_qt_libdir}/libQt%{api}Svg.so.%{major}*
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/libQt%{api}Svg.so.%{major}*
%endif
%{_qt_plugindir}/iconengines/libqsvgicon.so

#----------------------------------------------------------------------------

%package -n %{qtsvgd}
Summary:	Development files for Qt's SVG rendering engine
Group:		Development/KDE and Qt
Requires:	%{qtsvg} = %{EVRD}

%description -n %{qtsvgd}
Development files for Qt's SVG rendering engine.

%files -n %{qtsvgd}
%{_qt_includedir}/QtSvg
%{_qt_libdir}/libQt%{api}Svg.so
%{_qt_libdir}/libQt%{api}Svg.prl
%{_qt_libdir}/cmake/Qt%{api}Svg
%{_qt_libdir}/pkgconfig/Qt%{api}Svg.pc
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/pkgconfig/Qt%{api}Svg.pc
%endif

#----------------------------------------------------------------------------

%package -n %{qtwaylandclient}
Summary:	Wayland display system integration for Qt
Group:		System/Libraries
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-cursor)
BuildRequires:	pkgconfig(wayland-egl)
BuildRequires:	pkgconfig(wayland-scanner)
BuildRequires:	pkgconfig(wayland-server)
BuildRequires:	pkgconfig(xcomposite)

%description -n %{qtwaylandclient}
Wayland display system integration for Qt

%files -n %{qtwaylandclient}
%{_qt_bindir}/qtwaylandscanner
%{_qt_libdir}/libQt%{api}WaylandClient.so.%{major}*
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/libQt%{api}WaylandClient.so.%{major}*
%endif
%{_qt_plugindir}/platforms/libqwayland-egl.so
%{_qt_plugindir}/platforms/libqwayland-generic.so
%{_qt_plugindir}/wayland-decoration-client
%{_qt_plugindir}/wayland-graphics-integration-client

#----------------------------------------------------------------------------

%package -n %{qtwaylandclientd}
Summary:	Development files for the Qt WebKit web browsing library
Group:		Development/KDE and Qt
Requires:	%{qtwaylandclient} = %{EVRD}

%description -n %{qtwaylandclientd}
Development files for the Qt Wayland display system integration for Qt

%files -n %{qtwaylandclientd}
%{_qt_includedir}/QtWaylandClient
%{_qt_libdir}/libQt%{api}WaylandClient.so
%{_qt_libdir}/libQt%{api}WaylandClient.prl
%{_qt_libdir}/cmake/Qt%{api}WaylandClient
%{_qt_libdir}/pkgconfig/Qt%{api}WaylandClient.pc
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/pkgconfig/Qt%{api}WaylandClient.pc
%endif

#----------------------------------------------------------------------------

%package -n	%{qtwaylandcompositor}
Summary:	Wayland platform QtCompositor module
Group:		System/Libraries

%description -n %{qtwaylandcompositor}
Qt Wayland QtCompositor module

%files -n %{qtwaylandcompositor}
%{_qt_libdir}/libQt%{api}Compositor.so.%{major}*
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/libQt%{api}Compositor.so.%{major}*
%endif
%{_qt_plugindir}/platforms/libqwayland-xcomposite-egl.so
%{_qt_plugindir}/platforms/libqwayland-xcomposite-glx.so
%{_qt_plugindir}/wayland-graphics-integration-server/libdrm-egl-server.so
%{_qt_plugindir}/wayland-graphics-integration-server/libwayland-egl.so
%{_qt_plugindir}/wayland-graphics-integration-server/libxcomposite-egl.so
%{_qt_plugindir}/wayland-graphics-integration-server/libxcomposite-glx.so

#----------------------------------------------------------------------------

%package -n %{qtwaylandcompositord}
Summary:	Development files for the Qt WebKit web browsing library
Group:		Development/KDE and Qt
Requires:	%{qtwaylandcompositor} = %{EVRD}
Requires:	%{qtwaylandclient} = %{EVRD}
Requires:	%{qtwaylandclient} = %{EVRD}
Requires:	%{qtwaylandclientd} = %{EVRD}

%description -n %{qtwaylandcompositord}
Development files for the Qt Wayland QtCompositor module

%files -n %{qtwaylandcompositord}
%{_qt_includedir}/QtCompositor
%{_qt_libdir}/libQt%{api}Compositor.so
%{_qt_libdir}/libQt%{api}Compositor.prl
%{_qt_libdir}/cmake/Qt%{api}Compositor
%{_qt_libdir}/pkgconfig/Qt%{api}Compositor.pc
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/pkgconfig/Qt%{api}Compositor.pc
%endif

#----------------------------------------------------------------------------

%package -n %{qtwebkit}
Summary:	Qt WebKit web browsing library
Group:		System/Libraries
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	flex bison gperf ruby ruby(rubygems)
BuildRequires:	icu-devel

%description -n %{qtwebkit}
Qt WebKit web browsing library.

%files -n %{qtwebkit}
%{_qt_libdir}/libQt%{api}WebKit.so.%{major}*
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/libQt%{api}WebKit.so.%{major}*
%endif
%{_qt_importdir}/QtWebKit
%{_qt_prefix}/qml/QtWebKit
%{_qt_libexecdir}/QtWebProcess
%{_qt_libexecdir}/QtWebPluginProcess

#----------------------------------------------------------------------------

%package -n %{qtwebkitd}
Summary:	Development files for the Qt WebKit web browsing library
Group:		Development/KDE and Qt
Requires:	%{qtwebkit} = %{EVRD}

%description -n %{qtwebkitd}
Development files for the Qt WebKit web browsing library.

%files -n %{qtwebkitd}
%{_qt_includedir}/QtWebKit
%{_qt_libdir}/libQt%{api}WebKit.so
%{_qt_libdir}/libQt%{api}WebKit.prl
%{_qt_libdir}/cmake/Qt%{api}WebKit
%{_qt_libdir}/pkgconfig/Qt%{api}WebKit.pc
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/pkgconfig/Qt%{api}WebKit.pc
%endif

#----------------------------------------------------------------------------

%package -n %{qtwebkitwidgets}
Summary:	Qt WebKit Widgets library
Group:		System/Libraries

%description -n %{qtwebkitwidgets}
Qt WebKit Widgets library.

%files -n %{qtwebkitwidgets}
%{_qt_libdir}/libQt%{api}WebKitWidgets.so.%{major}*
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/libQt%{api}WebKitWidgets.so.%{major}*
%endif

#----------------------------------------------------------------------------

%package -n %{qtwebkitwidgetsd}
Summary:	Development files for the Qt WebKit Widgets library
Group:		Development/KDE and Qt
Requires:	%{qtwebkitwidgets} = %{EVRD}
Requires:	%{qtwebkitd} = %{EVRD}
Requires:	%{qtwidgetsd} = %{EVRD}

%description -n %{qtwebkitwidgetsd}
Development files for the Qt WebKit Widgets library.

%files -n %{qtwebkitwidgetsd}
%{_qt_includedir}/QtWebKitWidgets
%{_qt_libdir}/libQt%{api}WebKitWidgets.so
%{_qt_libdir}/libQt%{api}WebKitWidgets.prl
%{_qt_libdir}/cmake/Qt%{api}WebKitWidgets
%{_qt_libdir}/pkgconfig/Qt%{api}WebKitWidgets.pc
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/pkgconfig/Qt%{api}WebKitWidgets.pc
%endif

#----------------------------------------------------------------------------

%package -n %{qtx11extras}
Summary:	Qt X11 Extras library
Group:		System/Libraries

%description -n %{qtx11extras}
Qt X11 Extras library.

%files -n %{qtx11extras}
%{_qt_libdir}/libQt%{api}X11Extras.so.%{major}*
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/libQt%{api}X11Extras.so.%{major}*
%endif

#----------------------------------------------------------------------------

%package -n %{qtx11extrasd}
Summary:	Development files for the QtX11Extras library
Group:		Development/KDE and Qt
Requires:	%{qtx11extras} = %{EVRD}

%description -n %{qtx11extrasd}
Development files for the QtX11Extras library.

%files -n %{qtx11extrasd}
%{_qt_includedir}/QtX11Extras
%{_qt_libdir}/libQt%{api}X11Extras.so
%{_qt_libdir}/libQt%{api}X11Extras.prl
%{_qt_libdir}/cmake/Qt%{api}X11Extras
%{_qt_libdir}/pkgconfig/Qt%{api}X11Extras.pc
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/pkgconfig/Qt%{api}X11Extras.pc
%endif

#----------------------------------------------------------------------------

%package -n %{qtxmlpatterns}
Summary:	Qt XSLT engine
Group:		System/Libraries
Requires:	%{qtxml} = %{EVRD}
Requires:	%{name}-qtxmlpatterns-i18n = %{EVRD}

%description -n %{qtxmlpatterns}
Qt XSLT engine.

%files -n %{qtxmlpatterns}
%{_qt_libdir}/libQt%{api}XmlPatterns.so.%{major}*
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/libQt%{api}XmlPatterns.so.%{major}*
%endif

#----------------------------------------------------------------------------

%package -n %{qtxmlpatternsd}
Summary:	Development files for Qt's XSLT engine
Group:		Development/KDE and Qt
Requires:	%{qtxmlpatterns} = %{EVRD}
Requires:	%{qtxmld} = %{EVRD}

%description -n %{qtxmlpatternsd}
Development files for Qt's XSLT engine.

%files -n %{qtxmlpatternsd}
%{_qt_includedir}/QtXmlPatterns
%{_qt_libdir}/libQt%{api}XmlPatterns.so
%{_qt_libdir}/libQt%{api}XmlPatterns.prl
%{_qt_libdir}/cmake/Qt%{api}XmlPatterns
%{_qt_libdir}/pkgconfig/Qt%{api}XmlPatterns.pc
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/pkgconfig/Qt%{api}XmlPatterns.pc
%endif

#----------------------------------------------------------------------------

%package -n %{enginio}
Summary:	Enginio (Qt Cloud Storage) library
Group:		Development/KDE and Qt

%description -n %{enginio}
Enginio (Qt Cloud Storage) library

%files -n %{enginio}
%{_qt_libdir}/libEnginio.so.1*
%if "%{_qt_libdir}" != "%{_libdir}"
%{_libdir}/libEnginio.so.1*
%endif
%{_qt_prefix}/qml/Enginio

#----------------------------------------------------------------------------

%package -n %{enginiod}
Summary:	Development files for Enginio (Qt Cloud Storage)
Group:		Development/KDE and Qt
Requires:	%{enginio} = %{EVRD}

%description -n %{enginiod}
Development files for Enginio (Qt Cloud Storage)

%files -n %{enginiod}
%{_qt_includedir}/Enginio
%{_qt_libdir}/libEnginio.so
%{_qt_libdir}/libEnginio.prl
%{_qt_libdir}/cmake/Qt%{api}Enginio
%{_libdir}/pkgconfig/Enginio.pc

#----------------------------------------------------------------------------

%package qtxmlpatterns-i18n
Summary:	Qt XSLT engine translations
Group:		System/Libraries
Conflicts:	%{qtxmlpatterns} < 5.1.0-6
BuildArch:	noarch

%description qtxmlpatterns-i18n
Qt XSLT engine translations.

%files qtxmlpatterns-i18n
%lang(ca) %{_qt_translationsdir}/qtxmlpatterns_ca.qm
%lang(cs) %{_qt_translationsdir}/qtxmlpatterns_cs.qm
%lang(de) %{_qt_translationsdir}/qtxmlpatterns_de.qm
%lang(hu) %{_qt_translationsdir}/qtxmlpatterns_hu.qm
%lang(it) %{_qt_translationsdir}/qtxmlpatterns_it.qm
%lang(ja) %{_qt_translationsdir}/qtxmlpatterns_ja.qm
%lang(ru) %{_qt_translationsdir}/qtxmlpatterns_ru.qm
%lang(sk) %{_qt_translationsdir}/qtxmlpatterns_sk.qm
%lang(uk) %{_qt_translationsdir}/qtxmlpatterns_uk.qm

#----------------------------------------------------------------------------

%package devel
Summary:	Meta-package for installing all Qt 5 development files
Group:		Development/KDE and Qt
Requires:	%{enginiod} = %{EVRD}
Requires:	%{qtbluetoothd} = %{EVRD}
Requires:	%{qtbootstrapd} = %{EVRD}
Requires:	%{qtconcurrentd} = %{EVRD}
Requires:	%{qtcored} = %{EVRD}
Requires:	%{qtdbusd} = %{EVRD}
Requires:	%{qtguid} = %{EVRD}
Requires:	%{qtlocationd} = %{EVRD}
Requires:	%{qtnetworkd} = %{EVRD}
Requires:	%{qtopengld} = %{EVRD}
Requires:	%{qtpositioningd} = %{EVRD}
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
Requires:	%{qtnfcd} = %{EVRD}
Requires:	%{qtqmld} = %{EVRD}
Requires:	%{qtquickd} = %{EVRD}
Requires:	%{qtquickparticlesd} = %{EVRD}
Requires:	%{qtquicktestd} = %{EVRD}
Requires:	%{qtquickwidgetsd} = %{EVRD}
Requires:	%{qtscriptd} = %{EVRD}
Requires:	%{qtscripttoolsd} = %{EVRD}
Requires:	%{qtsvgd} = %{EVRD}
Suggests:	%{qtwaylandclientd} = %{EVRD}
Suggests:	%{qtwaylandcompositord} = %{EVRD}
Requires:	%{qtwebkitd} = %{EVRD}
Requires:	%{qtwebkitwidgetsd} = %{EVRD}
Requires:	%{qtwebchanneld} = %{EVRD}
Requires:	%{qtwebsocketsd} = %{EVRD}
Requires:	%{qtxmlpatternsd} = %{EVRD}
Requires:	qmake%{api} = %{EVRD}
Requires:	qlalr%{api} = %{EVRD}
Requires:	%{name}-macros = %{EVRD}

%description devel
Meta-package for installing all Qt 5 development files.

%files devel
# Intentionally empty, we just pull in dependencies

#----------------------------------------------------------------------------
# qt tools etc
#----------------------------------------------------------------------------

%package assistant
Summary:	Qt help system
Group:		Development/KDE and Qt
Suggests:	%{name}-doc = %{EVRD}

%description assistant
Qt help system.

%files assistant
%{_qt_bindir}/assistant
%{_datadir}/applications/openmandriva-assistant-qt%{api}.desktop
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

#----------------------------------------------------------------------------

%package designer
Summary:	Qt interface design tool
Group:		Development/KDE and Qt
Requires:	%{qtgui}-x11 = %{EVRD}
# for /usr/lib/qt5/bin/uic
Requires:	%{qtguid} = %{EVRD}

%description designer
Qt interface design tool.

%files designer
%{_qt_bindir}/designer
%{_datadir}/applications/openmandriva-designer-qt%{api}.desktop
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

#----------------------------------------------------------------------------

%if %{with docs}
%package doc
Summary:	Qt QCH documentation
Group:		Books/Computer books
BuildArch:	noarch

%description doc
QCH documentation for the Qt toolkit.

%files doc
%{_qt_docdir}/*.qch
%endif

#----------------------------------------------------------------------------

%package examples
Summary:	Example applications for %{name}
Group:		Development/KDE and Qt

%description examples
Example applications for %{name}.

%files examples
%{_qt_exampledir}

#----------------------------------------------------------------------------

%package fonts
Summary:	Fonts for use with some %{name} output plugins
Group:		System/Libraries

%description fonts
Fonts for use with some %{name} output plugins.

These fonts are required for various non-X11 output
plugins (framebuffer device etc.).

They are not required for the normal X11 output.

# FIXME re-add when Qt/E is fixed
#%%files fonts
#%%{_qt_libdir}/fonts

#----------------------------------------------------------------------------

%package linguist
Summary:	Translation tool for Qt based applications
Group:		Development/KDE and Qt
Requires:	%{name}-linguist-tools = %{EVRD}

%description linguist
Translation tool for Qt based applications.

%files linguist
%{_qt_bindir}/linguist
%{_datadir}/applications/openmandriva-linguist-qt%{api}.desktop
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
%dir %{_qt_datadir}/phrasebooks
%lang(da) %{_qt_datadir}/phrasebooks/danish.qph
%lang(nl) %{_qt_datadir}/phrasebooks/dutch.qph
%lang(fi) %{_qt_datadir}/phrasebooks/finnish.qph
%lang(fr) %{_qt_datadir}/phrasebooks/french.qph
%lang(de) %{_qt_datadir}/phrasebooks/german.qph
%lang(hu) %{_qt_datadir}/phrasebooks/hungarian.qph
%lang(it) %{_qt_datadir}/phrasebooks/italian.qph
%lang(ja) %{_qt_datadir}/phrasebooks/japanese.qph
%lang(no) %{_qt_datadir}/phrasebooks/norwegian.qph
%lang(pl) %{_qt_datadir}/phrasebooks/polish.qph
%lang(ru) %{_qt_datadir}/phrasebooks/russian.qph
%lang(es) %{_qt_datadir}/phrasebooks/spanish.qph
%lang(sv) %{_qt_datadir}/phrasebooks/swedish.qph

#----------------------------------------------------------------------------

%package linguist-tools
Summary:	Tools for creating and updating Qt Linguist translation files
Group:		Development/KDE and Qt

%description linguist-tools
Tools for creating and updating Qt Linguist translation files.

%files linguist-tools
%{_qt_bindir}/lconvert
%{_qt_bindir}/lrelease
%{_qt_bindir}/lupdate
%{_bindir}/lconvert-qt%{api}
%{_bindir}/lrelease-qt%{api}
%{_bindir}/lupdate-qt%{api}
%{_qt_libdir}/cmake/Qt%{api}LinguistTools

#----------------------------------------------------------------------------

%package macros
Summary:	Base macros for Qt 5
Group:		Development/KDE and Qt

%description macros
Base macros for Qt 5.

%files macros
%{_sysconfdir}/rpm/macros.d/qt5.macros

#----------------------------------------------------------------------------
%if %{with gtk}
%package platformtheme-gtk2
Summary:	GTK 2.x platform theme for Qt 5
Group:		Graphical desktop/KDE
Requires:	%{qtgui} = %{EVRD}
BuildRequires:	pkgconfig(gtk+-x11-2.0)

%description platformtheme-gtk2
GTK 2.x platform theme for Qt 5. This plugin allows Qt to render
controls using GTK 2.x themes - making it integrate better with GTK
based desktops.

%files platformtheme-gtk2
%{_qt_plugindir}/platformthemes/libqgtk2.so
%endif
#----------------------------------------------------------------------------

%package -n qdoc%{api}
Summary:	Qt documentation generator, version 5
Group:		Development/KDE and Qt

%description -n qdoc%{api}
Qt documentation generator, version 5.

%files -n qdoc%{api}
%{_qt_bindir}/qdoc

#----------------------------------------------------------------------------

%package -n qmake%{api}
Summary:	Makefile generation system for Qt 5
Group:		Development/KDE and Qt
Requires:	%{name}-macros = %{EVRD}

%description -n qmake%{api}
Makefile generation system for Qt 5.

%files -n qmake%{api}
%{_bindir}/qmake-qt%{api}
%{_qt_bindir}/qmake
%{_qt_prefix}/mkspecs

#----------------------------------------------------------------------------

%package -n qlalr%{api}
Summary:	Qt LALR parser generator
Group:		Development/KDE and Qt
Provides:	qlalr = %{EVRD}

%description -n qlalr%{api}
Qt LALR parser generator

%files -n qlalr%{api}
%{_qt_bindir}/qlalr

#----------------------------------------------------------------------------

%package qml-tools
Summary:	QML tools for Qt 5
Group:		Development/KDE and Qt

%description qml-tools
QML tools for Qt 5.

%files qml-tools
%{_qt_bindir}/qml
%{_qt_bindir}/qml1plugindump
%{_qt_bindir}/qmlbundle
%{_qt_bindir}/qmlimportscanner
%{_qt_bindir}/qmlmin
%{_qt_bindir}/qmlplugindump
%{_qt_bindir}/qmlprofiler
%{_qt_bindir}/qmlscene
%{_qt_bindir}/qmltestrunner
%{_qt_bindir}/qmlviewer
%lang(cs) %{_qt_translationsdir}/qmlviewer_cs.qm
%lang(fi) %{_qt_translationsdir}/qmlviewer_fi.qm
%lang(hu) %{_qt_translationsdir}/qmlviewer_hu.qm
%lang(ja) %{_qt_translationsdir}/qmlviewer_ja.qm
%lang(sk) %{_qt_translationsdir}/qmlviewer_sk.qm
%lang(ru) %{_qt_translationsdir}/qmlviewer_ru.qm
%lang(uk) %{_qt_translationsdir}/qmlviewer_uk.qm

#----------------------------------------------------------------------------

%package tools
Summary:	Tools for Qt 5
Group:		Development/KDE and Qt
Requires:	%{qtgui}-minimal = %{EVRD}
Requires:	%{name}-database-plugin-sqlite = %{EVRD}

%description tools
Tools for Qt 5.

%files tools
%{_qt_bindir}/pixeltool
%{_qt_bindir}/qcollectiongenerator
%{_qt_bindir}/qdbus
%{_qt_bindir}/qdbusviewer
%{_qt_bindir}/qtdiag
%{_qt_bindir}/qhelpconverter
%{_qt_bindir}/qhelpgenerator
%{_qt_bindir}/qtpaths
%{_qt_bindir}/xmlpatterns
%{_qt_bindir}/xmlpatternsvalidator

#----------------------------------------------------------------------------

%prep
%if "%{beta}" != ""
%setup -q -n qt-everywhere-opensource-src-%{version}-%{beta}
%else
%setup -q -n qt-everywhere-opensource-src-%{version}
%endif
%if "%{_qt_libdir}" == "%{_libdir}"
%patch1 -p1 -b .0001~
%endif

%patch2 -p1 -b .0002~

pushd qtmultimedia
%patch3 -p1 -b .gst1
popd
# aarch64 support in webkit
%patch4 -p1
# if you know how to pass an argue to build env
# CONFIG+=wayland-compositor
# remove this patch
%patch5 -p1

# Build scripts aren't ready for python3
grep -rl "env python" . |xargs sed -i -e "s,env python,env python2,g"
grep -rl "/python" . |xargs sed -i -e "s,/python,/python2,g"
sed -i -e "s,python,python2,g" qtwebkit/Source/*/DerivedSources.pri

# respect cflags
sed -i -e '/^CPPFLAGS\s*=/ s/-g //' \
	qtbase/qmake/Makefile.unix

sed -i -e "s|^\(QMAKE_LFLAGS_RELEASE.*\)|\1 %{ldflags}|" \
  qtbase/mkspecs/common/g++-unix.conf

sed -i -e "s|-O2|%{optflags}|g" qtbase/mkspecs/common/gcc-base.conf
sed -i -e "s|-O3|%{optflags}|g" qtbase/mkspecs/common/gcc-base.conf
# replace c++ with g++
# c++ -Xassembler --version -x assembler -c /dev/null
# clang: error: unsupported argument '--version' to option 'Xassembler'
sed -i 's/c++/g++/g' qtwebengine/src/3rdparty/chromium/build/compiler_version.py

# drop weird X11R6 lib from path in *.pc files
sed -i 's!X11R6/!!g' qtbase/mkspecs/linux-g++*/qmake.conf

# move some bundled libs to ensure they're not accidentally used
#pushd qtbase/src/3rdparty
#mkdir UNUSED
#mv freetype libjpeg libpng zlib xcb sqlite UNUSED/
#popd

%build
# build with python2
mkdir pybin
ln -s %{_bindir}/python2 pybin/python
export PATH=`pwd`/pybin:$PATH

./configure \
	-prefix %{_qt_prefix} \
	-bindir %{_qt_bindir} \
	-libdir %{_qt_libdir} \
	-datadir %{_qt_datadir} \
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
%ifarch x86_64
	-platform linux-g++-64 \
%endif
%ifarch %{ix86}
	-platform linux-g++-32 \
%endif
%ifarch %{armx}
	-platform linux-g++ \
%endif
	-system-zlib \
	-system-libpng \
	-system-libjpeg \
	-openssl-linked \
	-system-pcre \
	-system-xcb \
	-system-harfbuzz \
	-optimized-qmake \
	-no-nis \
	-cups \
	-iconv \
	-icu \
	-no-strip \
	-no-pch \
	-dbus-linked \
%ifarch %ix86 x86_64
	-reduce-relocations \
%endif
	-xcb \
%if %{with directfb}
	-directfb \
%endif
	-qpa xcb \
	-fontconfig \
	-accessibility \
	-eglfs \
	-gnumake \
	-pkg-config \
	-kms \
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
	-mtdev \
	-journald \
	-pulseaudio \
	-alsa \
	-linuxfb \
	-kms \
	-no-separate-debug-info \
	-no-strip \
%if "%{_qt_libdir}" == "%{_libdir}"
	-no-rpath \
%endif
	-v \
	-I %{_includedir}/iodbc \
	-I %{_includedir}/mysql

# FIXME reduce-relocations is disabled for anything but x86 because
# of QTBUG-36129. This should be changed as soon as we get a new
# binutils and/or switch to linaro binutils.

# Fix confused Makefiles refering to Enginio includes by Enginio's version number
# (1.0.4) while other bits refer to it by Qt's version number
ln -s %{version} qtenginio/include/Enginio/1.0.4

%make STRIP=true

%if %{with docs}
%make docs
%endif

%install
make install STRIP=true INSTALL_ROOT=%{buildroot}

%if %{with docs}
make install_qch_docs INSTALL_ROOT=%{buildroot}
%endif

# Probably not useful outside of Qt source tree?
rm -f %{buildroot}%{_qt_bindir}/qtmodule-configtests
# Let's not ship -devel files for private libraries... At least not until
# applications teach us otherwise
rm -f %{buildroot}%{_qt_libdir}/libqgsttools_p.so %{buildroot}%{_qt_libdir}/libqgsttools_p.prl
rm -f %{buildroot}%{_qt_libdir}/libQt%{api}MultimediaQuick_p.so %{buildroot}%{_qt_libdir}/libQt%{api}MultimediaQuick_p.prl %{buildroot}%{_qt_libdir}/pkgconfig/Qt%{api}MultimediaQuick_p.pc
# qtconfig doesn't exist anymore - we don't need its translations
rm -f %{buildroot}%{_qt_translationsdir}/qtconfig_*.qm
# Let's make life easier for packagers
mkdir -p %{buildroot}%{_bindir}
for i in qmake moc uic rcc qdbuscpp2xml qdbusxml2cpp lrelease lupdate lconvert; do
	ln -s ../%{_lib}/qt%{api}/bin/$i %{buildroot}%{_bindir}/$i-qt%{api}
done

%if "%{_qt_libdir}" != "%{_libdir}"
pushd %{buildroot}%{_libdir}
ln -s ../%{_lib}/qt%{api}/%{_lib}/*.so.* .
mkdir pkgconfig
cd pkgconfig
ln -s ../../%{_lib}/qt%{api}/%{_lib}/pkgconfig/*.pc .
popd
%endif

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

# "make dep" output packaged into examples is bogus...
find %{buildroot} -name .deps |xargs rm -rf

# Workaround for
# *** ERROR: same build ID in nonidentical files!
#        /usr/lib/qt5/bin/qdbuscpp2xml
#   and  /usr/lib/qt5/bin/moc
# ...
# while generating debug info
find %{buildroot} -type f -perm -0755 |grep -vE '\.(so|qml|sh|pl)' |xargs %__strip --strip-unneeded

# Install rpm macros
mkdir -p %{buildroot}%{_sysconfdir}/rpm/macros.d
install -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/rpm/macros.d

# Install .desktop files for assistant, designer and linguist
mkdir -p %{buildroot}%{_datadir}/applications
install -m 644 %{SOURCE2} %{buildroot}%{_datadir}/applications
install -m 644 %{SOURCE3} %{buildroot}%{_datadir}/applications
install -m 644 %{SOURCE4} %{buildroot}%{_datadir}/applications

sed -i s,"/usr/lib/qt5/bin","%{_qt_bindir}",g %{buildroot}%{_datadir}/applications/*.desktop

# Tell qtchooser about us
mkdir -p %{buildroot}%{_sysconfdir}/xdg/qtchooser
cat >%{buildroot}%{_sysconfdir}/xdg/qtchooser/%{name}.conf <<'EOF'
%{_qt_bindir}
%{_qt_libdir}
EOF

# QMAKE_PRL_BUILD_DIR = /builddir/build/BUILD/qt-everywhere-opensource-src-5.4.0-beta/qtwayland/src/client
## .prl/.la file love
# nuke .prl reference(s) to %%buildroot, excessive (.la-like) libs
pushd %{buildroot}%{_qt_libdir}
for prl_file in libQt5*.prl ; do
  sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" ${prl_file}
  if [ -f "$(basename ${prl_file} .prl).so" ]; then
    rm -fv "$(basename ${prl_file} .prl).la"
    sed -i -e "/^QMAKE_PRL_LIBS/d" ${prl_file}
  fi
done
popd
