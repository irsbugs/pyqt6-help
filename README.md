# pyqt6-help

If you have installed PyQt6 from PyPI, then this program will provide help on the topic that you select. 
Selections may be made through a Tree widget or by entering a Search string.

The panels are divided by a splitter, so using a mouse you may adjust the size of each panel.


If it is detected that PyQt6 modules are not installed on you system / virtual environment, then you will
receive the following information to guide you in installing PyQt6 in a virtual environment.

```
Detected that PyQt6 modules are not installed.

To install PyQt6 in a virtual environment on a Linux system:

~$ python3 -m venv venv-qt6
~$ source venv-qt6/bin/activate
(venv-qt6) ~/venv-qt6$ cd venv-qt6
(venv-qt6) ~/venv-qt6$ bin/python -m pip install -U pip setuptools wheel
(venv-qt6) ~/venv-qt6$ pip install PyQt6

# For a list of modules that are installed:
(venv-qt6) ~/venv-qt6$ ls -1 lib/python3.10/site-packages/PyQt6/bindings

# Run program:
(venv-qt6) ~/venv-qt6$ python qt6-help.py
```

The following Modules are installed as part of the $ pip install PyQt6:

QtBluetooth - Classes to support connectivity between Bluetooth enabled devices
QtCore - The core Qt classes
QtDBus - Classes to support IPC using the D-Bus protocol
QtDesigner - Classes to allow Qt Designer to be extended using Python
QtGui - The core classes common to widget and OpenGL GUIs
QtHelp - Classes for creating and viewing searchable documentation
QtMultimedia - Classes for multimedia content, cameras and radios
QtMultimediaWidgets - Provides additional multimedia related widgets and controls
QtNetwork - The core network classes
QtNfc - Classes to support connectivity between NFC enabled devices
QtOpenGL - Classes for using OpenGL in PyQt user interfaces
QtOpenGLWidgets - Classes for rendering OpenGL in a widget
QtPositioning - Classes for obtaining positioning information from satellite, wifi etc.
QtPrintSupport - Classes to make printing easier and more portable
QtQml - Classes for integrating with the QML language
QtQuick - Classes for extending QML applications with Python code
QtQuick3D - Classes for rendering 3D Qt Quick content
QtQuickWidgets - Classes for rendering a QML scene in traditional widgets
QtRemoteObjects - Classes for sharing the API of a QObject between processes or systems
QtSensors - Classes for accessing a system's hardware sensors
QtSerialPort - Classes for accessing a system's serial ports
QtSql - Classes for integrating with SQL databases
QtSvg - Classes providing support for SVG
QtSvgWidgets - Classes for rendering SVG images in a widget
QtTest - Support for unit testing of GUI applications
QtWebChannel - Classes for peer-to-peer communication between Python and HTML/JavaScript
QtWebSockets - Classes that implement the WebSocket protocol
QtWidgets - Classes for creating classic desktop-style UIs
QtXml - Classes for supporting the DOM interface to XML

lupdate - Functions for handling translation files used by Qt Linguist
sip - Utilities for bindings developers and users
uic - Functions for handling the files created by Qt Designer


Additional Modules:

Charts - $ pip install PyQt6-Charts
    QtCharts - Classes to support the creation of 2D charts

3D - $ pip install PyQt6-3D
    Qt3DAnimation - Classes that support animations in simulations
    Qt3DCore - The core classes to support near-realtime simulation systems
    Qt3DExtras - Pre-built elements for use with Qt3D
    Qt3DInput - Classes to handle user input when using Qt3D
    Qt3DLogic - Classes that enable frame synchronization
    Qt3DRender - Classes that enable 2D and 3D rendering

DataVisualization - $ pip install PyQt6-DataVisualization
    QtDataVisualization - Classes to support the visualization of data in 3D

NetworkAuth - $ pip install PyQt6-NetworkAuth
    QtNetworkAuth - Classes for OAuth-based authorization to online services
    
WebEngine - $ pip install PyQt6-WebEngine
    QtWebEngineCore - The core Web Engine classes
    QtWebEngineQuick - Classes for integrating QML Web Engine objects with Python
    QtWebEngineWidgets - A Chromium based web browser
    
QScintilla - $ pip install PyQt6-QScintilla
    QScintilla - A source code editing software module - https://qscintilla.com/
