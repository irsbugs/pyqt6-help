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

# List of modules that are installed.
(venv-qt6) ~/venv-qt6$ ls -1 lib/python3.10/site-packages/PyQt6/bindings
Restart qt6-help.py in venv-qt6 and it should now run OK.
```
