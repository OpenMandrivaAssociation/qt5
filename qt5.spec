%define debug_package %{nil}
%define beta %nil
%define api 5
%define major 5

%define _qt_prefix %{_prefix}/lib/qt%{api}
%define _qt_bindir %{_qt_prefix}/bin
%define _qt_docdir %{_docdir}/qt%{api}
%define _qt_libdir %{_qt_prefix}/%{_lib}
%define _qt_libexecdir %{_qt_prefix}/libexec
%define _qt_includedir %{_qt_prefix}/include
%define _qt_plugindir %{_libdir}/qt%{api}/plugins
%define _qt_demodir %{_qt_prefix}/demos
%define _qt_exampledir %{_qt_prefix}/examples
%define _qt_importdir %{_qt_prefix}/imports
%define _qt_datadir %{_qt_prefix}/share
%define _qt_sysconfdir %{_sysconfdir}/qt%{api}
%define _qt_testsdir %{_qt_prefix}/tests
%define _qt_translationsdir %{_qt_prefix}/translations

# qt base components
%define qtbootstrapd %mklibname qt%{api}bootstrap -d
%define qtconcurrent %mklibname qt%{api}concurrent %{major}
%define qtconcurrentd %mklibname qt%{api}concurrent -d
%define qtcore %mklibname qt%{api}core %{major}
%define qtcored %mklibname qt%{api}core -d
%define qtdbus %mklibname qt%{api}dbus %{major}
%define qtdbusd %mklibname qt%{api}dbus -d
%define qtgui %mklibname qt%{api}gui %{major}
%define qtguid %mklibname qt%{api}gui -d
%define qtnetwork %mklibname qt%{api}network %{major}
%define qtnetworkd %mklibname qt%{api}network -d
%define qtopengl %mklibname qt%{api}opengl %{major}
%define qtopengld %mklibname qt%{api}opengl -d
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
%define qtx11extras %mklibname qt%{api}x11extras %{major}
%define qtx11extrasd %mklibname qt%{api}x11extras -d
%define qtxml %mklibname qt%{api}xml %{major}
%define qtxmld %mklibname qt%{api}xml -d

# qt extras that might move to separate tarballs at some point
%define qgsttools_p %mklibname qgsttools_p 1
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
%define qtv8 %mklibname qt%{api}v8 %{major}
%define qtv8d %mklibname qt%{api}v8 -d
%define qtwebkit %mklibname qt%{api}webkit %{major}
%define qtwebkitd %mklibname qt%{api}webkit -d
%define qtwebkitwidgets %mklibname qt%{api}webkitwidgets %{major}
%define qtwebkitwidgetsd %mklibname qt%{api}webkitwidgets -d
%define qtxmlpatterns %mklibname qt%{api}xmlpatterns %{major}
%define qtxmlpatternsd %mklibname qt%{api}xmlpatterns -d

%bcond_without directfb

Summary:	Version 5 of the Qt toolkit
Name:		qt5
Version:	5.1.0
License:	LGPLv3+
Group:		Development/KDE and Qt
Url:		http://qt-project.org/
%if "%{beta}" == ""
Source0:	qt-everywhere-opensource-src-%{version}.tar.gz
Release:	5
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

#----------------------------------------------------------------------------
# qt base components
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
%{_libdir}/pkgconfig/Qt%{api}Bootstrap.pc

#----------------------------------------------------------------------------

%package -n %{qtconcurrent}
Summary:	Qt threading library
Group:		System/Libraries

%description -n %{qtconcurrent}
Qt threading library.

%files -n %{qtconcurrent}
%{_qt_libdir}/libQt%{api}Concurrent.so.*
%{_libdir}/libQt%{api}Concurrent.so.*

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
%{_qt_libdir}/libQt%{api}Concurrent.so
%{_qt_libdir}/libQt%{api}Concurrent.prl
%{_qt_libdir}/pkgconfig/Qt%{api}Concurrent.pc
%{_libdir}/pkgconfig/Qt%{api}Concurrent.pc
%{_qt_includedir}/QtConcurrent
%{_qt_libdir}/cmake/Qt%{api}Concurrent

#----------------------------------------------------------------------------

%package -n %{qtcore}
Summary:	Qt Core library
Group:		System/Libraries

%description -n %{qtcore}
Qt Core library.

%files -n %{qtcore}
%{_qt_libdir}/libQt%{api}Core.so.*
%{_libdir}/libQt%{api}Core.so.*
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

#----------------------------------------------------------------------------

%package -n %{qtcored}
Summary:	Development files for version 5 of the QtCore library
Group:		Development/KDE and Qt
Requires:	%{qtcore} = %{EVRD}

%description -n %{qtcored}
Development files for version 5 of the QtCore library.

%files -n %{qtcored}
%{_qt_bindir}/moc
%{_qt_bindir}/rcc
%{_qt_libdir}/libQt%{api}Core.so
%{_qt_libdir}/libQt%{api}Core.prl
%{_qt_includedir}/QtCore
%dir %{_qt_libdir}/cmake
%dir %{_qt_libdir}/cmake/Qt%{api}
%dir %{_qt_libdir}/pkgconfig
%{_qt_libdir}/pkgconfig/Qt%{api}Core.pc
%{_libdir}/pkgconfig/Qt%{api}Core.pc
%{_qt_libdir}/cmake/Qt%{api}Core
%{_qt_libdir}/cmake/Qt%{api}/Qt%{api}Config.cmake
%{_qt_libdir}/cmake/Qt%{api}/Qt%{api}ConfigVersion.cmake
%doc %{_docdir}/qt%{api}/global

#----------------------------------------------------------------------------

%package -n %{qtdbus}
Summary:	Qt DBus connector library
Group:		System/Libraries

%description -n %{qtdbus}
Qt DBus connector library.

%files -n %{qtdbus}
%{_qt_libdir}/libQt%{api}DBus.so.*
%{_libdir}/libQt%{api}DBus.so.*

#----------------------------------------------------------------------------

%package -n %{qtdbusd}
Summary:	Development files for version 5 of the QtDBus library
Group:		Development/KDE and Qt
Requires:	%{qtdbus} = %{EVRD}

%description -n %{qtdbusd}
Development files for version 5 of the QtDBus library.

%files -n %{qtdbusd}
%{_qt_libdir}/libQt%{api}DBus.so
%{_qt_libdir}/libQt%{api}DBus.prl
%{_qt_libdir}/pkgconfig/Qt%{api}DBus.pc
%{_libdir}/pkgconfig/Qt%{api}DBus.pc
%{_qt_includedir}/QtDBus
%{_qt_libdir}/cmake/Qt%{api}DBus
%{_qt_bindir}/qdbuscpp2xml
%{_qt_bindir}/qdbusxml2cpp

#----------------------------------------------------------------------------

%package -n %{qtgui}
Summary:	Qt GUI library
Group:		System/Libraries

%description -n %{qtgui}
Qt GUI library.

%files -n %{qtgui}
%{_qt_libdir}/libQt%{api}Gui.so.*
%{_libdir}/libQt%{api}Gui.so.*
%{_qt_plugindir}/imageformats
%dir %{_qt_plugindir}/platforminputcontexts
%dir %{_qt_plugindir}/platforms
%dir %{_qt_plugindir}/platformthemes
%dir %{_qt_plugindir}/iconengines
%{_qt_plugindir}/generic
%{_qt_plugindir}/printsupport

#----------------------------------------------------------------------------

%package -n %{qtguid}
Summary:	Development files for version 5 of the QtGui library
Group:		Development/KDE and Qt
Requires:	%{qtgui} = %{EVRD}

%description -n %{qtguid}
Development files for version 5 of the QtGui library.

%files -n %{qtguid}
%{_qt_bindir}/uic
%{_qt_libdir}/libQt%{api}Gui.so
%{_qt_libdir}/libQt%{api}Gui.prl
%{_qt_libdir}/pkgconfig/Qt%{api}Gui.pc
%{_libdir}/pkgconfig/Qt%{api}Gui.pc
%{_qt_includedir}/QtGui
%{_qt_libdir}/cmake/Qt%{api}Gui
%{_qt_libdir}/libQt%{api}PlatformSupport.a
%{_qt_libdir}/libQt%{api}PlatformSupport.prl
%{_qt_libdir}/pkgconfig/Qt%{api}PlatformSupport.pc
%{_libdir}/pkgconfig/Qt%{api}PlatformSupport.pc
%{_qt_includedir}/QtPlatformSupport
%{_qt_includedir}/QtUiTools
%{_qt_libdir}/cmake/Qt%{api}UiTools
%{_qt_libdir}/libQt%{api}UiTools.a
%{_qt_libdir}/libQt%{api}UiTools.prl
%{_qt_libdir}/pkgconfig/Qt%{api}UiTools.pc
%{_libdir}/pkgconfig/Qt%{api}UiTools.pc

#----------------------------------------------------------------------------

%package -n %{qtgui}-directfb
Summary:	DirectFB output driver for QtGui v5
Group:		System/Libraries
Requires:	%{qtgui} = %{EVRD}

%description -n %{qtgui}-directfb
DirectFB output driver for QtGui v5.

%files -n %{qtgui}-directfb
%{_qt_plugindir}/platforms/libqdirectfb.so

#----------------------------------------------------------------------------

%package -n %{qtgui}-linuxfb
Summary:	Linux Framebuffer output driver for QtGui v5
Group:		System/Libraries
Requires:	%{qtgui} = %{EVRD}

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

%description -n %{qtgui}-minimal
Minimal (Framebuffer based) output driver for QtGui v5.

%files -n %{qtgui}-minimal
%{_qt_plugindir}/platforms/libqminimal.so

#----------------------------------------------------------------------------

%package -n %{qtgui}-offscreen
Summary:	Offscreen output driver for QtGui v5
Group:		System/Libraries
Requires:	%{qtgui} = %{EVRD}

%description -n %{qtgui}-offscreen
Minimal (Framebuffer based) output driver for QtGui v5.

%files -n %{qtgui}-offscreen
%{_qt_plugindir}/platforms/libqoffscreen.so

#----------------------------------------------------------------------------

%package -n %{qtgui}-x11
Summary:	X11 output driver for QtGui v5
Group:		System/Libraries
Requires:	%{qtgui} = %{EVRD}

%description -n %{qtgui}-x11
X11 output driver for QtGui v5.

%files -n %{qtgui}-x11
%{_qt_plugindir}/platforms/libqxcb.so
%{_qt_plugindir}/platforminputcontexts/libibusplatforminputcontextplugin.so
%{_qt_plugindir}/platforminputcontexts/libmaliitplatforminputcontextplugin.so
%{_qt_plugindir}/platforminputcontexts/libcomposeplatforminputcontextplugin.so

#----------------------------------------------------------------------------

%package -n %{qtnetwork}
Summary:	Qt Networking library
Group:		System/Libraries

%description -n %{qtnetwork}
Qt Networking library.

%files -n %{qtnetwork}
%{_qt_libdir}/libQt%{api}Network.so.*
%{_libdir}/libQt%{api}Network.so.*
%{_qt_plugindir}/bearer

#----------------------------------------------------------------------------

%package -n %{qtnetworkd}
Summary:	Development files for version 5 of the QtNetwork library
Group:		Development/KDE and Qt
Requires:	%{qtnetwork} = %{EVRD}

%description -n %{qtnetworkd}
Development files for version 5 of the QtNetwork library.

%files -n %{qtnetworkd}
%{_qt_libdir}/libQt%{api}Network.so
%{_qt_libdir}/libQt%{api}Network.prl
%{_qt_libdir}/pkgconfig/Qt%{api}Network.pc
%{_libdir}/pkgconfig/Qt%{api}Network.pc
%{_qt_includedir}/QtNetwork
%{_qt_libdir}/cmake/Qt%{api}Network

#----------------------------------------------------------------------------

%package -n %{qtopengl}
Summary:	Qt OpenGL (3D Graphics) library
Group:		System/Libraries

%description -n %{qtopengl}
Qt OpenGL (3D Graphics) library.

%files -n %{qtopengl}
%{_qt_libdir}/libQt%{api}OpenGL.so.*
%{_libdir}/libQt%{api}OpenGL.so.*

#----------------------------------------------------------------------------

%package -n %{qtopengld}
Summary:	Development files for version 5 of the QtOpenGL library
Group:		Development/KDE and Qt
Requires:	%{qtopengl} = %{EVRD}

%description -n %{qtopengld}
Development files for version 5 of the QtOpenGL library.

%files -n %{qtopengld}
%{_qt_libdir}/libQt%{api}OpenGL.so
%{_qt_libdir}/libQt%{api}OpenGL.prl
%{_qt_libdir}/pkgconfig/Qt%{api}OpenGL.pc
%{_libdir}/pkgconfig/Qt%{api}OpenGL.pc
%{_qt_libdir}/pkgconfig/Qt%{api}OpenGLExtensions.pc
%{_libdir}/pkgconfig/Qt%{api}OpenGLExtensions.pc
%{_qt_includedir}/QtOpenGL
%{_qt_includedir}/QtOpenGLExtensions
%{_qt_libdir}/cmake/Qt%{api}OpenGL
%{_qt_libdir}/cmake/Qt%{api}OpenGLExtensions
%{_qt_libdir}/libQt%{api}OpenGLExtensions.a
%{_qt_libdir}/libQt%{api}OpenGLExtensions.prl

#----------------------------------------------------------------------------

%package -n %{qtprintsupport}
Summary:	Qt printing library
Group:		System/Libraries

%description -n %{qtprintsupport}
Qt printing library.

%files -n %{qtprintsupport}
%{_qt_libdir}/libQt%{api}PrintSupport.so.*
%{_libdir}/libQt%{api}PrintSupport.so.*

#----------------------------------------------------------------------------

%package -n %{qtprintsupportd}
Summary:	Development files for version 5 of the QtPrintSupport library
Group:		Development/KDE and Qt
Requires:	%{qtprintsupport} = %{EVRD}

%description -n %{qtprintsupportd}
Development files for version 5 of the QtPrintSupport library.

%files -n %{qtprintsupportd}
%{_qt_libdir}/libQt%{api}PrintSupport.so
%{_qt_libdir}/libQt%{api}PrintSupport.prl
%{_qt_libdir}/pkgconfig/Qt%{api}PrintSupport.pc
%{_libdir}/pkgconfig/Qt%{api}PrintSupport.pc
%{_qt_includedir}/QtPrintSupport
%{_qt_libdir}/cmake/Qt%{api}PrintSupport

#----------------------------------------------------------------------------

%package -n %{qtsensors}
Summary:	Qt Sensors library
Group:		System/Libraries

%description -n %{qtsensors}
Qt Sensors library.

%files -n %{qtsensors}
%{_qt_libdir}/libQt%{api}Sensors.so.*
%{_libdir}/libQt%{api}Sensors.so.*
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
%{_qt_libdir}/cmake/Qt%{api}Sensors
%{_qt_libdir}/libQt%{api}Sensors.so
%{_qt_libdir}/libQt%{api}Sensors.prl
%{_qt_libdir}/pkgconfig/Qt%{api}Sensors.pc
%{_libdir}/pkgconfig/Qt%{api}Sensors.pc

#----------------------------------------------------------------------------

%package -n %{qtserialport}
Summary:	Qt Serial Port library
Group:		System/Libraries

%description -n %{qtserialport}
Qt Serial Port library.

%files -n %{qtserialport}
%{_qt_libdir}/libQt%{api}SerialPort.so.*
%{_libdir}/libQt%{api}SerialPort.so.*

#----------------------------------------------------------------------------

%package -n %{qtserialportd}
Summary:	Development files for the QtSerialPort library
Group:		Development/KDE and Qt
Requires:	%{qtserialport} = %{EVRD}

%description -n %{qtserialportd}
Development files for the QtSerialPort library.

%files -n %{qtserialportd}
%{_qt_includedir}/QtSerialPort
%{_qt_libdir}/cmake/Qt%{api}SerialPort
%{_qt_libdir}/libQt%{api}SerialPort.so
%{_qt_libdir}/libQt%{api}SerialPort.prl
%{_qt_libdir}/pkgconfig/Qt%{api}SerialPort.pc
%{_libdir}/pkgconfig/Qt%{api}SerialPort.pc

#----------------------------------------------------------------------------

%package -n %{qtsql}
Summary:	Qt SQL library
Group:		System/Libraries

%description -n %{qtsql}
Qt SQL library.

%files -n %{qtsql}
%{_qt_libdir}/libQt%{api}Sql.so.*
%{_libdir}/libQt%{api}Sql.so.*
%dir %{_qt_plugindir}/sqldrivers

#----------------------------------------------------------------------------

%package -n %{qtsqld}
Summary:	Development files for version 5 of the QtSql library
Group:		Development/KDE and Qt
Requires:	%{qtsql} = %{EVRD}

%description -n %{qtsqld}
Development files for version 5 of the QtSql library.

%files -n %{qtsqld}
%{_qt_libdir}/libQt%{api}Sql.so
%{_qt_libdir}/libQt%{api}Sql.prl
%{_qt_libdir}/pkgconfig/Qt%{api}Sql.pc
%{_libdir}/pkgconfig/Qt%{api}Sql.pc
%{_qt_includedir}/QtSql
%{_qt_libdir}/cmake/Qt%{api}Sql

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
%{_qt_libdir}/libQt%{api}Test.so.*
%{_libdir}/libQt%{api}Test.so.*
%{_qt_prefix}/qml/QtTest

#----------------------------------------------------------------------------

%package -n %{qttestd}
Summary:	Development files for version 5 of the QtTest library
Group:		Development/KDE and Qt
Requires:	%{qttest} = %{EVRD}

%description -n %{qttestd}
Development files for version 5 of the QtTest library.

%files -n %{qttestd}
%{_qt_libdir}/libQt%{api}Test.so
%{_qt_libdir}/libQt%{api}Test.prl
%{_qt_libdir}/pkgconfig/Qt%{api}Test.pc
%{_libdir}/pkgconfig/Qt%{api}Test.pc
%{_qt_includedir}/QtTest
%{_qt_libdir}/cmake/Qt%{api}Test

#----------------------------------------------------------------------------

%package -n %{qtwidgets}
Summary:	Qt Widget library
Group:		System/Libraries

%description -n %{qtwidgets}
Qt Widget library.

%files -n %{qtwidgets}
%{_qt_libdir}/libQt%{api}Widgets.so.*
%{_libdir}/libQt%{api}Widgets.so.*
%{_qt_plugindir}/accessible

#----------------------------------------------------------------------------

%package -n %{qtwidgetsd}
Summary:	Development files for version 5 of the QtWidgets library
Group:		Development/KDE and Qt
Requires:	%{qtwidgets} = %{EVRD}

%description -n %{qtwidgetsd}
Development files for version 5 of the QtWidgets library.

%files -n %{qtwidgetsd}
%{_qt_libdir}/libQt%{api}Widgets.so
%{_qt_libdir}/libQt%{api}Widgets.prl
%{_qt_libdir}/pkgconfig/Qt%{api}Widgets.pc
%{_libdir}/pkgconfig/Qt%{api}Widgets.pc
%{_qt_includedir}/QtWidgets
%{_qt_libdir}/cmake/Qt%{api}Widgets

#----------------------------------------------------------------------------

%package -n %{qtxml}
Summary:	Qt XML library
Group:		System/Libraries

%description -n %{qtxml}
Qt XML library.

%files -n %{qtxml}
%{_qt_libdir}/libQt%{api}Xml.so.*
%{_libdir}/libQt%{api}Xml.so.*

#----------------------------------------------------------------------------

%package -n %{qtxmld}
Summary:	Development files for version 5 of the QtXml library
Group:		Development/KDE and Qt
Requires:	%{qtxml} = %{EVRD}

%description -n %{qtxmld}
Development files for version 5 of the QtXml library.

%files -n %{qtxmld}
%{_qt_libdir}/libQt%{api}Xml.so
%{_qt_libdir}/libQt%{api}Xml.prl
%{_qt_libdir}/pkgconfig/Qt%{api}Xml.pc
%{_libdir}/pkgconfig/Qt%{api}Xml.pc
%{_qt_includedir}/QtXml
%{_qt_libdir}/cmake/Qt%{api}Xml

#----------------------------------------------------------------------------
# qt extras
#----------------------------------------------------------------------------

%package -n %{qgsttools_p}
Summary:	Runtime library for GStreamer support in Qt 5
Group:		System/Libraries

%description -n %{qgsttools_p}
Runtime library for GStreamer support in Qt 5.

%files -n %{qgsttools_p}
%{_qt_libdir}/libqgsttools_p.so.*
%{_libdir}/libqgsttools_p.so.*

#----------------------------------------------------------------------------

%package -n %{qtclucene}
Summary:	Qt version of the CLucene search engine
Group:		System/Libraries

%description -n %{qtclucene}
Qt version of the CLucene search engine.

%files -n %{qtclucene}
%{_qt_libdir}/libQt%{api}CLucene.so.*
%{_libdir}/libQt%{api}CLucene.so.*

#----------------------------------------------------------------------------

%package -n %{qtclucened}
Summary:	Development files for the Qt version of the CLucene search engine
Group:		Development/KDE and Qt
Requires:	%{qtclucene} = %{EVRD}

%description -n %{qtclucened}
Development files for the Qt version of the CLucene search engine.

%files -n %{qtclucened}
%{_qt_libdir}/libQt%{api}CLucene.so
%{_qt_libdir}/libQt%{api}CLucene.prl
%{_qt_libdir}/pkgconfig/Qt%{api}CLucene.pc
%{_libdir}/pkgconfig/Qt%{api}CLucene.pc
%{_qt_includedir}/QtCLucene

#----------------------------------------------------------------------------

%package -n %{qtdeclarative}
Summary:	Runtime library for Qt Declarative
Group:		System/Libraries

%description -n %{qtdeclarative}
Runtime library for Qt Declarative.

%files -n %{qtdeclarative}
%{_qt_libdir}/libQt%{api}Declarative.so.*
%{_libdir}/libQt%{api}Declarative.so.*
%lang(de) %{_qt_translationsdir}/qtdeclarative_de.qm
%lang(ru) %{_qt_translationsdir}/qtdeclarative_ru.qm
%lang(sk) %{_qt_translationsdir}/qtdeclarative_sk.qm
%lang(uk) %{_qt_translationsdir}/qtdeclarative_uk.qm
%{_qt_plugindir}/qmltooling

#----------------------------------------------------------------------------

%package -n %{qtdeclaratived}
Summary:	Development files for Qt Declarative
Group:		Development/KDE and Qt
Requires:	%{qtdeclarative} = %{EVRD}

%description -n %{qtdeclaratived}
Development files for Qt Declarative.

%files -n %{qtdeclaratived}
%{_qt_libdir}/libQt%{api}Declarative.so
%{_qt_libdir}/libQt%{api}Declarative.prl
%{_qt_libdir}/pkgconfig/Qt%{api}Declarative.pc
%{_libdir}/pkgconfig/Qt%{api}Declarative.pc
%{_qt_includedir}/QtDeclarative
%{_qt_libdir}/cmake/Qt%{api}Declarative

#----------------------------------------------------------------------------

%package -n %{qtdesignercomponents}
Summary:	Components for Qt Designer
Group:		System/Libraries

%description -n %{qtdesignercomponents}
Components for Qt Designer.

%files -n %{qtdesignercomponents}
%{_qt_libdir}/libQt%{api}DesignerComponents.so.*
%{_libdir}/libQt%{api}DesignerComponents.so.*

#----------------------------------------------------------------------------

%package -n %{qtdesignercomponentsd}
Summary:	Development files for Qt Designer Components
Group:		Development/KDE and Qt
Requires:	%{qtdesignercomponents} = %{EVRD}

%description -n %{qtdesignercomponentsd}
Development files for Qt Designer Components.

%files -n %{qtdesignercomponentsd}
%{_qt_libdir}/libQt%{api}DesignerComponents.so
%{_qt_libdir}/libQt%{api}DesignerComponents.prl
%{_qt_libdir}/pkgconfig/Qt%{api}DesignerComponents.pc
%{_libdir}/pkgconfig/Qt%{api}DesignerComponents.pc
%{_qt_includedir}/QtDesignerComponents

#----------------------------------------------------------------------------

%package -n %{qtdesigner}
Summary:	Qt Designer runtime libraries
Group:		System/Libraries

%description -n %{qtdesigner}
Qt Designer runtime libraries.

%files -n %{qtdesigner}
%{_qt_libdir}/libQt%{api}Designer.so.*
%{_libdir}/libQt%{api}Designer.so.*

#----------------------------------------------------------------------------

%package -n %{qtdesignerd}
Summary:	Development files for Qt Designer
Group:		Development/KDE and Qt
Requires:	%{qtdesigner} = %{EVRD}

%description -n %{qtdesignerd}
Development files for Qt Designer.

%files -n %{qtdesignerd}
%{_qt_libdir}/libQt%{api}Designer.so
%{_qt_libdir}/libQt%{api}Designer.prl
%{_qt_libdir}/pkgconfig/Qt%{api}Designer.pc
%{_libdir}/pkgconfig/Qt%{api}Designer.pc
%{_qt_includedir}/QtDesigner
%{_qt_libdir}/cmake/Qt%{api}Designer

#----------------------------------------------------------------------------

%package -n %{qthelp}
Summary:	Runtime libraries for the Qt Help system
Group:		System/Libraries

%description -n %{qthelp}
Runtime libraries for the Qt Help system.

%files -n %{qthelp}
%{_qt_libdir}/libQt%{api}Help.so.*
%{_libdir}/libQt%{api}Help.so.*

#----------------------------------------------------------------------------

%package -n %{qthelpd}
Summary:	Development files for Qt Help
Group:		Development/KDE and Qt
Requires:	%{qthelp} = %{EVRD}

%description -n %{qthelpd}
Development files for Qt Help, useful if you wish to add a help system
to your application.

%files -n %{qthelpd}
%{_qt_libdir}/libQt%{api}Help.so
%{_qt_libdir}/libQt%{api}Help.prl
%{_qt_libdir}/pkgconfig/Qt%{api}Help.pc
%{_libdir}/pkgconfig/Qt%{api}Help.pc
%{_qt_includedir}/QtHelp
%{_qt_libdir}/cmake/Qt%{api}Help

#----------------------------------------------------------------------------

%package -n %{qtmultimedia}
Summary:	Qt Multimedia libraries
Group:		System/Libraries

%description -n %{qtmultimedia}
Qt Multimedia libraries.

%files -n %{qtmultimedia}
%{_qt_libdir}/libQt%{api}Multimedia.so.*
%{_libdir}/libQt%{api}Multimedia.so.*
%{_qt_plugindir}/audio
%{_qt_plugindir}/mediaservice
%{_qt_plugindir}/playlistformats
%lang(cs) %{_qt_translationsdir}/qtmultimedia_cs.qm
%lang(de) %{_qt_translationsdir}/qtmultimedia_de.qm
%lang(hu) %{_qt_translationsdir}/qtmultimedia_hu.qm
%lang(ru) %{_qt_translationsdir}/qtmultimedia_ru.qm
%lang(sk) %{_qt_translationsdir}/qtmultimedia_sk.qm
%lang(uk) %{_qt_translationsdir}/qtmultimedia_uk.qm

#----------------------------------------------------------------------------

%package -n %{qtmultimediad}
Summary:	Development files for Qt Multimedia
Group:		Development/KDE and Qt
Requires:	%{qtmultimedia} = %{EVRD}

%description -n %{qtmultimediad}
Development files for Qt Multimedia.

%files -n %{qtmultimediad}
%{_qt_libdir}/libQt%{api}Multimedia.so
%{_qt_libdir}/libQt%{api}Multimedia.prl
%{_qt_libdir}/pkgconfig/Qt%{api}Multimedia.pc
%{_libdir}/pkgconfig/Qt%{api}Multimedia.pc
%{_qt_includedir}/QtMultimedia
%{_qt_libdir}/cmake/Qt%{api}Multimedia
%{_qt_includedir}/QtMultimediaQuick_p

#----------------------------------------------------------------------------

%package -n %{qtmultimediaquick_p}
Summary:	Runtime support library for the Qt Multimedia Quick module
Group:		System/Libraries

%description -n %{qtmultimediaquick_p}
Runtime support library for the Qt Multimedia Quick module.

%files -n %{qtmultimediaquick_p}
%{_qt_libdir}/libQt%{api}MultimediaQuick_p.so.*
%{_libdir}/libQt%{api}MultimediaQuick_p.so.*

#----------------------------------------------------------------------------

%package -n %{qtmultimediawidgets}
Summary:	Qt Multimedia Widgets library
Group:		System/Libraries

%description -n %{qtmultimediawidgets}
Qt Multimedia Widgets library.

%files -n %{qtmultimediawidgets}
%{_qt_libdir}/libQt%{api}MultimediaWidgets.so.*
%{_libdir}/libQt%{api}MultimediaWidgets.so.*

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
%{_qt_libdir}/libQt%{api}MultimediaWidgets.so
%{_qt_libdir}/libQt%{api}MultimediaWidgets.prl
%{_qt_libdir}/pkgconfig/Qt%{api}MultimediaWidgets.pc
%{_libdir}/pkgconfig/Qt%{api}MultimediaWidgets.pc
%{_qt_includedir}/QtMultimediaWidgets
%{_qt_libdir}/cmake/Qt%{api}MultimediaWidgets

#----------------------------------------------------------------------------

%package -n %{qtqml}
Summary:	QML runtime support library
Group:		System/Libraries

%description -n %{qtqml}
QML runtime support library.

%files -n %{qtqml}
%{_qt_libdir}/libQt%{api}Qml.so.*
%{_libdir}/libQt%{api}Qml.so.*
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

#----------------------------------------------------------------------------

%package -n %{qtqmld}
Summary:	Development files for the Qt QML library
Group:		Development/KDE and Qt
Requires:	%{qtqml} = %{EVRD}

%description -n %{qtqmld}
Development files for the Qt QML library.

%files -n %{qtqmld}
%{_qt_libdir}/libQt%{api}Qml.so
%{_qt_libdir}/libQt%{api}Qml.prl
%{_qt_libdir}/pkgconfig/Qt%{api}Qml.pc
%{_libdir}/pkgconfig/Qt%{api}Qml.pc
%{_qt_includedir}/QtQml
%{_qt_libdir}/cmake/Qt%{api}Qml
%{_qt_libdir}/libQt%{api}QmlDevTools.a
%{_qt_libdir}/libQt%{api}QmlDevTools.prl
%{_qt_libdir}/pkgconfig/Qt%{api}QmlDevTools.pc
%{_libdir}/pkgconfig/Qt%{api}QmlDevTools.pc

#----------------------------------------------------------------------------

%package -n %{qtquick}
Summary:	Runtime library for Qt Quick
Group:		System/Libraries

%description -n %{qtquick}
Runtime library for Qt Quick.

%files -n %{qtquick}
%{_qt_libdir}/libQt%{api}Quick.so.*
%{_libdir}/libQt%{api}Quick.so.*
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

#----------------------------------------------------------------------------

%package -n %{qtquickd}
Summary:	Development files for Qt Quick
Group:		Development/KDE and Qt
Requires:	%{qtquick} = %{EVRD}

%description -n %{qtquickd}
Development files for Qt Quick.

%files -n %{qtquickd}
%{_qt_libdir}/libQt%{api}Quick.so
%{_qt_libdir}/libQt%{api}Quick.prl
%{_qt_libdir}/pkgconfig/Qt%{api}Quick.pc
%{_libdir}/pkgconfig/Qt%{api}Quick.pc
%{_qt_includedir}/QtQuick
%{_qt_libdir}/cmake/Qt%{api}Quick

#----------------------------------------------------------------------------

%package -n %{qtquickparticles}
Summary:	Runtime library for Qt Quick's particle engine
Group:		System/Libraries

%description -n %{qtquickparticles}
Runtime library for Qt Quick's particle engine.

%files -n %{qtquickparticles}
%{_qt_libdir}/libQt%{api}QuickParticles.so.*
%{_libdir}/libQt%{api}QuickParticles.so.*

#----------------------------------------------------------------------------

%package -n %{qtquickparticlesd}
Summary:	Development files for Qt Quick's particle engine
Group:		Development/KDE and Qt
Requires:	%{qtquickparticles} = %{EVRD}

%description -n %{qtquickparticlesd}
Development files for Qt Quick's particle engine.

%files -n %{qtquickparticlesd}
%{_qt_libdir}/libQt%{api}QuickParticles.so
%{_qt_libdir}/libQt%{api}QuickParticles.prl
%{_qt_libdir}/pkgconfig/Qt%{api}QuickParticles.pc
%{_libdir}/pkgconfig/Qt%{api}QuickParticles.pc
%{_qt_includedir}/QtQuickParticles

#----------------------------------------------------------------------------

%package -n %{qtquicktest}
Summary:	Qt Quick unit test module
Group:		System/Libraries

%description -n %{qtquicktest}
Qt Quick unit test module.

%files -n %{qtquicktest}
%{_qt_libdir}/libQt%{api}QuickTest.so.*
%{_libdir}/libQt%{api}QuickTest.so.*

#----------------------------------------------------------------------------

%package -n %{qtquicktestd}
Summary:	Development files for Qt Quick's unit test module
Group:		Development/KDE and Qt
Requires:	%{qtquicktest} = %{EVRD}

%description -n %{qtquicktestd}
Development files for Qt Quick's unit test module.

%files -n %{qtquicktestd}
%{_qt_libdir}/libQt%{api}QuickTest.so
%{_qt_libdir}/libQt%{api}QuickTest.prl
%{_qt_libdir}/pkgconfig/Qt%{api}QuickTest.pc
%{_libdir}/pkgconfig/Qt%{api}QuickTest.pc
%{_qt_includedir}/QtQuickTest
%{_qt_libdir}/cmake/Qt%{api}QuickTest

#----------------------------------------------------------------------------

%package -n %{qtscript}
Summary:	Qt Script runtime library
Group:		System/Libraries

%description -n %{qtscript}
Qt Script runtime library.

%files -n %{qtscript}
%{_qt_libdir}/libQt%{api}Script.so.*
%{_libdir}/libQt%{api}Script.so.*
%lang(cs) %{_qt_translationsdir}/qtscript_cs.qm
%lang(de) %{_qt_translationsdir}/qtscript_de.qm
%lang(hu) %{_qt_translationsdir}/qtscript_hu.qm
%lang(ru) %{_qt_translationsdir}/qtscript_ru.qm
%lang(sk) %{_qt_translationsdir}/qtscript_sk.qm
%lang(uk) %{_qt_translationsdir}/qtscript_uk.qm

#----------------------------------------------------------------------------

%package -n %{qtscriptd}
Summary:	Development files for Qt Script
Group:		Development/KDE and Qt
Requires:	%{qtscript} = %{EVRD}

%description -n %{qtscriptd}
Development files for Qt Script.

%files -n %{qtscriptd}
%{_qt_libdir}/libQt%{api}Script.so
%{_qt_libdir}/libQt%{api}Script.prl
%{_qt_libdir}/pkgconfig/Qt%{api}Script.pc
%{_libdir}/pkgconfig/Qt%{api}Script.pc
%{_qt_includedir}/QtScript
%{_qt_libdir}/cmake/Qt%{api}Script

#----------------------------------------------------------------------------

%package -n %{qtscripttools}
Summary:	Qt Script tools library
Group:		System/Libraries

%description -n %{qtscripttools}
Qt Script tools library.

%files -n %{qtscripttools}
%{_qt_libdir}/libQt%{api}ScriptTools.so.*
%{_libdir}/libQt%{api}ScriptTools.so.*

#----------------------------------------------------------------------------

%package -n %{qtscripttoolsd}
Summary:	Development files for Qt Script tools
Group:		Development/KDE and Qt
Requires:	%{qtscripttools} = %{EVRD}

%description -n %{qtscripttoolsd}
Development files for Qt Script tools.

%files -n %{qtscripttoolsd}
%{_qt_libdir}/libQt%{api}ScriptTools.so
%{_qt_libdir}/libQt%{api}ScriptTools.prl
%{_qt_libdir}/pkgconfig/Qt%{api}ScriptTools.pc
%{_libdir}/pkgconfig/Qt%{api}ScriptTools.pc
%{_qt_includedir}/QtScriptTools
%{_qt_libdir}/cmake/Qt%{api}ScriptTools

#----------------------------------------------------------------------------

%package -n %{qtsvg}
Summary:	Qt SVG rendering engine
Group:		System/Libraries

%description -n %{qtsvg}
Qt SVG rendering engine.

%files -n %{qtsvg}
%{_qt_libdir}/libQt%{api}Svg.so.*
%{_libdir}/libQt%{api}Svg.so.*
%{_qt_plugindir}/iconengines/libqsvgicon.so

#----------------------------------------------------------------------------

%package -n %{qtsvgd}
Summary:	Development files for Qt's SVG rendering engine
Group:		Development/KDE and Qt
Requires:	%{qtsvg} = %{EVRD}

%description -n %{qtsvgd}
Development files for Qt's SVG rendering engine.

%files -n %{qtsvgd}
%{_qt_libdir}/libQt%{api}Svg.so
%{_qt_libdir}/libQt%{api}Svg.prl
%{_qt_libdir}/pkgconfig/Qt%{api}Svg.pc
%{_libdir}/pkgconfig/Qt%{api}Svg.pc
%{_qt_includedir}/QtSvg
%{_qt_libdir}/cmake/Qt%{api}Svg

#----------------------------------------------------------------------------

%package -n %{qtv8}
Summary:	Qt version of the V8 JavaScript engine
Group:		System/Libraries

%description -n %{qtv8}
Qt version of the V8 JavaScript engine.

%files -n %{qtv8}
%{_qt_libdir}/libQt%{api}V8.so.*
%{_libdir}/libQt%{api}V8.so.*

#----------------------------------------------------------------------------

%package -n %{qtv8d}
Summary:	Development files for the Qt version of the V8 JavaScript engine
Group:		Development/KDE and Qt
Requires:	%{qtv8} = %{EVRD}

%description -n %{qtv8d}
Development files for the Qt version of the V8 JavaScript engine.

%files -n %{qtv8d}
%{_qt_libdir}/libQt%{api}V8.so
%{_qt_libdir}/libQt%{api}V8.prl
%{_qt_libdir}/pkgconfig/Qt%{api}V8.pc
%{_libdir}/pkgconfig/Qt%{api}V8.pc
%{_qt_includedir}/QtV8

#----------------------------------------------------------------------------

%package -n %{qtwebkit}
Summary:	Qt WebKit web browsing library
Group:		System/Libraries
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	flex bison gperf ruby
BuildRequires:	icu-devel

%description -n %{qtwebkit}
Qt WebKit web browsing library.

%files -n %{qtwebkit}
%{_qt_libdir}/libQt%{api}WebKit.so.*
%{_libdir}/libQt%{api}WebKit.so.*
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
%{_qt_libdir}/libQt%{api}WebKit.so
%{_qt_libdir}/libQt%{api}WebKit.prl
%{_qt_libdir}/pkgconfig/Qt%{api}WebKit.pc
%{_libdir}/pkgconfig/Qt%{api}WebKit.pc
%{_qt_includedir}/QtWebKit
%{_qt_libdir}/cmake/Qt%{api}WebKit

#----------------------------------------------------------------------------

%package -n %{qtwebkitwidgets}
Summary:	Qt WebKit Widgets library
Group:		System/Libraries

%description -n %{qtwebkitwidgets}
Qt WebKit Widgets library.

%files -n %{qtwebkitwidgets}
%{_qt_libdir}/libQt%{api}WebKitWidgets.so.*
%{_libdir}/libQt%{api}WebKitWidgets.so.*

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
%{_qt_libdir}/libQt%{api}WebKitWidgets.so
%{_qt_libdir}/libQt%{api}WebKitWidgets.prl
%{_qt_libdir}/pkgconfig/Qt%{api}WebKitWidgets.pc
%{_libdir}/pkgconfig/Qt%{api}WebKitWidgets.pc
%{_qt_includedir}/QtWebKitWidgets
%{_qt_libdir}/cmake/Qt%{api}WebKitWidgets

#----------------------------------------------------------------------------

%package -n %{qtx11extras}
Summary:	Qt X11 Extras library
Group:		System/Libraries

%description -n %{qtx11extras}
Qt X11 Extras library.

%files -n %{qtx11extras}
%{_qt_libdir}/libQt%{api}X11Extras.so.*
%{_libdir}/libQt%{api}X11Extras.so.*

#----------------------------------------------------------------------------

%package -n %{qtx11extrasd}
Summary:	Development files for the QtX11Extras library
Group:		Development/KDE and Qt
Requires:	%{qtx11extras} = %{EVRD}

%description -n %{qtx11extrasd}
Development files for the QtX11Extras library.

%files -n %{qtx11extrasd}
%{_qt_includedir}/QtX11Extras
%{_qt_libdir}/cmake/Qt%{api}X11Extras
%{_qt_libdir}/libQt%{api}X11Extras.so
%{_qt_libdir}/libQt%{api}X11Extras.prl
%{_qt_libdir}/pkgconfig/Qt%{api}X11Extras.pc
%{_libdir}/pkgconfig/Qt%{api}X11Extras.pc

#----------------------------------------------------------------------------

%package -n %{qtxmlpatterns}
Summary:	Qt XSLT engine
Group:		System/Libraries
Requires:	%{qtxml} = %{EVRD}

%description -n %{qtxmlpatterns}
Qt XSLT engine.

%files -n %{qtxmlpatterns}
%{_qt_libdir}/libQt%{api}XmlPatterns.so.*
%{_libdir}/libQt%{api}XmlPatterns.so.*
%lang(cs) %{_qt_translationsdir}/qtxmlpatterns_cs.qm
%lang(de) %{_qt_translationsdir}/qtxmlpatterns_de.qm
%lang(hu) %{_qt_translationsdir}/qtxmlpatterns_hu.qm
%lang(ru) %{_qt_translationsdir}/qtxmlpatterns_ru.qm
%lang(sk) %{_qt_translationsdir}/qtxmlpatterns_sk.qm
%lang(uk) %{_qt_translationsdir}/qtxmlpatterns_uk.qm

#----------------------------------------------------------------------------

%package -n %{qtxmlpatternsd}
Summary:	Development files for Qt's XSLT engine
Group:		Development/KDE and Qt
Requires:	%{qtxmlpatterns} = %{EVRD}
Requires:	%{qtxmld} = %{EVRD}

%description -n %{qtxmlpatternsd}
Development files for Qt's XSLT engine.

%files -n %{qtxmlpatternsd}
%{_qt_libdir}/libQt%{api}XmlPatterns.so
%{_qt_libdir}/libQt%{api}XmlPatterns.prl
%{_qt_libdir}/pkgconfig/Qt%{api}XmlPatterns.pc
%{_libdir}/pkgconfig/Qt%{api}XmlPatterns.pc
%{_qt_includedir}/QtXmlPatterns
%{_qt_libdir}/cmake/Qt%{api}XmlPatterns

#----------------------------------------------------------------------------

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

%files devel
# Intentionally empty, we just pull in dependencies

#----------------------------------------------------------------------------
# qt tools etc
#----------------------------------------------------------------------------

%package assistant
Summary:	Qt help system
Group:		Development/KDE and Qt

%description assistant
Qt help system.

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
Summary:	Makefile generation system for Qt5
Group:		Development/KDE and Qt
Requires:	%{name}-macros = %{EVRD}

%description -n qmake%{api}
Makefile generation system for Qt5.

%files -n qmake%{api}
%{_bindir}/qmake-qt%{api}
%{_qt_bindir}/qmake
%{_qt_prefix}/mkspecs

#----------------------------------------------------------------------------

%package qml-tools
Summary:	QML tools for Qt 5
Group:		Development/KDE and Qt

%description qml-tools
QML tools for Qt 5.

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
%{_qt_bindir}/qhelpconverter
%{_qt_bindir}/qhelpgenerator
%{_qt_bindir}/xmlpatterns
%{_qt_bindir}/xmlpatternsvalidator

#----------------------------------------------------------------------------

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
rm -f %{buildroot}%{_qt_libdir}/libQt%{api}MultimediaQuick_p.so %{buildroot}%{_qt_libdir}/libQt%{api}MultimediaQuick_p.prl %{buildroot}%{_qt_libdir}/pkgconfig/Qt%{api}MultimediaQuick_p.pc
# qtconfig doesn't exist anymore - we don't need its translations
rm -f %{buildroot}%{_qt_translationsdir}/qtconfig_*.qm
# Let's make life easier for packagers
mkdir -p %{buildroot}%{_bindir}
ln -s ../lib/qt%{api}/bin/qmake %{buildroot}%{_bindir}/qmake-qt%{api}

cd %{buildroot}%{_libdir}
ln -s ../lib/qt%{api}/%{_lib}/*.so.* .
mkdir pkgconfig
cd pkgconfig
ln -s ../../lib/qt%{api}/%{_lib}/pkgconfig/*.pc .
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

