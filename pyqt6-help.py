#/usr/bin/env python3
#
# pyqt6-help.py
# 
# If PyQt6 has been installed using pip then it should provide 29 modules
# The modules are imported and a Tree is built to get help on any Module, a
# Class in a module, or a Method in a Class.
#
# There is also a search facility to find help.
#
# Ian Stewart - ©CC0 2022-09-06
#
import sys
import contextlib
from io import StringIO
error_stop = False
# These are the Qt Modules from a PyPI install of PyQt6 as of Sep 2022.
try: 
    import PyQt6.QtBluetooth as QtBluetooth
    import PyQt6.QtCore as QtCore
    import PyQt6.QtDBus as QtDBus
    import PyQt6.QtDesigner as QtDesigner
    import PyQt6.QtGui as QtGui
    import PyQt6.QtHelp as QtHelp
    import PyQt6.QtMultimedia as QtMultimedia
    import PyQt6.QtMultimediaWidgets as QtMultimediaWidgets
    import PyQt6.QtNetwork as QtNetwork
    import PyQt6.QtNfc as QtNfc
    import PyQt6.QtOpenGL as QtOpenGL
    import PyQt6.QtOpenGLWidgets as QtOpenGLWidgets
    import PyQt6.QtPositioning as QtPositioning
    import PyQt6.QtPrintSupport as QtPrintSupport
    import PyQt6.QtQml as QtQml
    import PyQt6.QtQuick as QtQuick
    import PyQt6.QtQuick3D as QtQuick3D
    import PyQt6.QtQuickWidgets as QtQuickWidgets
    import PyQt6.QtRemoteObjects as QtRemoteObjects
    import PyQt6.QtSensors as QtSensors
    import PyQt6.QtSerialPort as QtSerialPort
    import PyQt6.QtSql as QtSql
    import PyQt6.QtSvg as QtSvg
    import PyQt6.QtSvgWidgets as QtSvgWidgets
    import PyQt6.QtTest as QtTest
    import PyQt6.QtWebChannel as QtWebChannel
    import PyQt6.QtWebSockets as QtWebSockets
    import PyQt6.QtWidgets as QtWidgets
    import PyQt6.QtXml as QtXml
except ModuleNotFoundError as e:
    print(e)
    error_stop = True
    
# version
VERSION = "2022-09-06"
PYTHON_VERSION = sys.version.split(" ")[0]
# Qt version
QT_VERSION = "{}".format(QtCore.qVersion())
# Provide the column header with a heading.
HEADING = 'PyQt6 Categories'
# Welcome message
WELCOME = """
Welcome to PyQt6 Help Gui 
Version:{}
Python:{} 
Qt Version:{}
App:{}
Select a Help Category and then an item within the category.
""".format(VERSION, PYTHON_VERSION, QT_VERSION, sys.argv[0])


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, dictionary) -> None:
        super().__init__()
        self.setWindowTitle("PyQt6 Help")
        self.resize(1400,600)
        # Where does QGuiApplication come from?)
        #self.resize(QGuiApplication.primaryScreen().availableGeometry().size() * 0.7)
        splitter_h = QtWidgets.QSplitter()
        splitter_h.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.setCentralWidget(splitter_h)
        splitter_v = QtWidgets.QSplitter()
        splitter_v.setOrientation(QtCore.Qt.Orientation.Vertical)
        
        self.textedit = QtWidgets.QTextEdit()
        self.textedit.setText("")  
        self.textedit.setStyleSheet("font: 12pt Monospace")     
        splitter_h.addWidget(self.textedit)

        # Right panel of horizontal splitter is a vertical splitter
        splitter_h.addWidget(splitter_v) 
        
        label = QtWidgets.QLabel()
        label.setText("Search: Enter 4+ Characters...")
        splitter_v.addWidget(label)        
        search_field = QtWidgets.QLineEdit()
        #search_field.textChanged.connect(self.search_changed) # Uses qt6_dict
        search_field.textChanged.connect(lambda x: self.search_changed(x, dictionary)) 
        #button.clicked.connect(lambda: calluser(name))          
        splitter_v.addWidget(search_field)
        #splitter_v.setStyleSheet("""
        #        border-width: 4px;
        #        border-radius: 5px;
        #        """) # border-style: outset;
          
        self.list_widget = QtWidgets.QListWidget()
        self.list_widget.clicked.connect(self.search_list_clicked)
        splitter_v.addWidget(self.list_widget)

        tree_widget = QtWidgets.QTreeWidget()       
        splitter_v.addWidget(tree_widget)        
        tree_widget.clear()
        tree_widget.setHeaderLabel(HEADING)        
        tree_widget.setColumnCount(1)
        tree_widget.clicked.connect(self.treewidget_clicked)
        self.fill_tree_widget_item(tree_widget.invisibleRootItem(), dictionary)        
        
        splitter_h.setStretchFactor(0,4)
        splitter_h.setStretchFactor(1,1) 
 
        splitter_v.setStretchFactor(0,1)
        splitter_v.setStretchFactor(1,1)       
        splitter_v.setStretchFactor(2,1)
        splitter_v.setStretchFactor(3,1)
                
        self.textedit.setText(WELCOME + MESSAGE)       


    def search_changed(self, search_text, dictionary): 
        # Passed the dictionary rather than using global qt6_dict):
        #print(len(search_text))
        # Don't do any searches until 4th character is entered.
        if len(search_text) <= 3:
            return  
    
        self.list_widget.clear()
        
        # Top level search - modules
        #for module, class_dict in qt6_dict.items():
        for module, class_dict in dictionary.items():        
            if search_text.lower() in module.lower():
                self.list_widget.addItem("PyQt6." + module)
                
            # 2nd Level search - Classes
            for class_name, method_list in class_dict.items():
                if search_text.lower() in class_name.lower():
                    self.list_widget.addItem("PyQt6." + module + "." + class_name)
                            
                # 3rd level search - Methods
                for method in method_list:
                    if search_text.lower() in method.lower(): 
                        self.list_widget.addItem("PyQt6." + module + "." +
                            class_name + "." + method)                        
                
          
    def search_list_clicked(self, model_index):
        item = model_index.data()
        item_list = item.split(".")
        self.setWindowTitle("PyQt6 Help - Selection: {}".format(item)) 

        string_1 = ""
        if len(item_list) > 2:
            string_1 = "\n\nfrom PyQt6.{} import {}\n".format(item_list[1], item_list[2])

        # get the help data         
        string_2 = display_pyqt6_help(item_list)
        
        self.textedit.setText(item + string_1 + string_2)       

        #string = display_pyqt6_help(item_list) 
        #self.textedit.setText(string)         
                      
    def fill_tree_widget_item(self, invisible_root_item, dictionary):
        for top_key, class_dict in dictionary.items():
            
            # Dictionaries: 'QDomText': ['EncodingPolicy', 'NodeType', ...'toText']}
        
            parent = QtWidgets.QTreeWidgetItem([str(top_key)])
            #parent.setFlags(parent.flags() & ~ QtCore.Qt.ItemFlag.ItemIsSelectable) 
            invisible_root_item.addChild(parent) 
            
                                                   
            for class_name, method_list in class_dict.items(): 
                child = QtWidgets.QTreeWidgetItem([str(class_name)])
                #child.setFlags(child.flags() & ~ QtCore.Qt.ItemFlag.ItemIsSelectable) 
                parent.addChild(child) 
                       
                #print(len(method_list))
                for method in method_list:
                    grandchild = QtWidgets.QTreeWidgetItem([str(method)])
                    child.addChild(grandchild)

                #print(dictionary[top_key][class_name])

                    
    def treewidget_clicked(self, model_index):
        """
        The parent, child or grand-child has been clicked.
        Build a list
        """
        #print(model_index) # PyQt6.QtCore.QModelIndex object
        #print(model_index.flags().value) # 60 parent or 61 child        
        # Check is ItemIsSelectable based on model_index.flags()
        if not model_index.flags() & QtCore.Qt.ItemFlag.ItemIsSelectable:
            #print("Item is not selectable")
            return
            
        item_list = []
        item_list.append(model_index.data())
        
        # Potential for between 1 to 3 levels above.
        try:
            parent = model_index.parent()
            if parent.data():
                item_list.insert(0, parent.data())
        except:
            pass

        try:            
            grandparent = parent.parent()
            if grandparent.data():
                item_list.insert(0, grandparent.data())
        except:
            pass
                
        # Insert the root of the tree
        item_list.insert(0, "PyQt6")
        item_str  = ".".join(item_list)
        
        self.setWindowTitle("PyQt6 Help - Selection: {}".format(item_str))        
        
        string_1 = ""
        if len(item_list) > 2:
            string_1 = "\n\nfrom PyQt6.{} import {}\n".format(item_list[1], item_list[2])

        # get the help data         
        string_2 = display_pyqt6_help(item_list)
        
        self.textedit.setText(item_str + string_1 + string_2)       

# Functions shared by both Window classes and initial launch code.
def display_pyqt6_help(item_list):
    """
    Build the string that is displayed in the textview panel.
    Only provide two levels of help. Current and one above.
    """
    level_current = ".".join(item_list)
    #print(level_current)
    
    item_list.pop()
    level_1_up = ".".join(item_list)
    #print(level_1_up)    
            
    # Get the help information strings
    level_current_str = get_help(level_current)
    level_1_up_str = get_help(level_1_up)
                 
    # Build text and display
    string = "\n" + "=" * 100 + "\n"
     
    string += level_current + ":\n"
    string += "\n" + level_current_str
    string += "\n" + "=" * 100 + "\n"

    string += level_1_up + ":\n"
    string += "\n" + level_1_up_str
    string += "\n" + "=" * 100 + "\n"    
    
    return string
    
    
def get_help(func):
    """
    Write the output of help() to a text buffer and return as text string.
    Usage example: get_help("PyQt6.QtCore")
    Requires: contextlib and io.StringIO
    """
    output = StringIO()
    with contextlib.redirect_stdout(output):
        help(func)       
    contents = output.getvalue()
    output.close()
    return contents


# Initial setup / data collection routines, etc.
def build_dictionary(module_list):
    """
    Build the dictionary
    """
    count_0 = 0
    count_1 = 0
    count_2 = 0
    count_3 = 0

    qt6_dict = {}
    for module in module_list:
        if module.startswith("Qt"):
            count_0 += 1 # 29
            qt6_dict[module] = {}      

    #print(len(qt6_dict))
    #print(qt6_dict)

    for module, classes in qt6_dict.items():
        classes_list = dir(eval(module))
        #print(classes_list)
        
        
        for subgroup in classes_list:
            count_1 += 1  # 1174
            qt6_dict[module].update ( {subgroup: None} ) 
            module_subgroup_str = module + "." + subgroup
            
            method_list = (dir(eval(module_subgroup_str)))
            count_2 += len(method_list)  # 107896
            qt6_dict[module][subgroup] = method_list        
            
            # Are the method_lists still attached, and dict is not independent.
    #print("Initial Dictionary. Modules:", count_0, "SubGroups:", count_1, 
    #       "Methods:", count_2) 
    # Initial Dictionary. Modules: 29 SubGroups: 1174 Methods: 107896        
    return qt6_dict


def remove_classes_double_underscore(qt6_dict):
    """
    Remove any subgroup that starts with a double under. 
    E.g. QtBluetooth.__spec__  or QtCore.__doc__
    Notes: 
    No Group level starts with __
    This Works OK: print(qt6_dict['QtBluetooth']['__doc__'])
    RuntimeError: dictionary changed size during iteration <-- Therefore make a list 
    of deletions to make to the dictionary and then implement the list.            
    """
    count_0 = 0
    count_1 = 0

    for module, classes_list in qt6_dict.items():
        
        #if module.startswith("__"): #<-- Nothing at group level starts with __
            #print(module) # Nothing
        
        methods_to_delete_list = []
          
        for subgroup, method_list in classes_list.items():
            count_0 += 1  # 1174

            if subgroup.startswith("__"):
                # Build a list of subgroup to be deleted
                methods_to_delete_list.append(subgroup)
                count_1 += 1  # 175
                
        #print(methods_to_delete_list) # ['__doc__', '__file__', ... '__spec__']
        for item in methods_to_delete_list:
            del qt6_dict[module][item]
         
         
    #print("Double Unders Classes removed. SubGroups:", count_0, "Subgroups removed:", 
    #        count_1, "Remain:", count_0 - count_1)
    # Double Unders Classes removed. SubGroups: 1174 Subgroups removed: 175 Remain: 999
    return qt6_dict
    

def remove_methods_double_underscore(qt6_dict):
    """
    Remove and the double_under from the methods list's. 
    Need to do reverse list popping
    """
    count_0 = 0
    count_1 = 0

    for group, classes in qt6_dict.items():
        for subgroup, method_list in classes.items():
            length = len(method_list)
            for index, method in enumerate(reversed(method_list)):
                count_0 += 1  #       
                if method.startswith("__"):
                    count_1 += 1  # 
                    method_list.pop((length-1) - index)

    #print("Double Unders removed from Methods. Initial:", count_0, "Removed", count_1, 
    #        "Remain:", count_0 - count_1) 
    # Double Unders removed from Methods. Initial: 98057 Removed 27112 Remain: 70945
    return qt6_dict

    
def remove_methods_single_underscore(qt6_dict):    
    """
    Remove and the single_under from the methods list's
    """
    count_0 = 0
    count_1 = 0

    for group, classes in qt6_dict.items():
        for subgroup, method_list in classes.items():
            string = group + "." + subgroup
            #print(key, subkey, len(item_list), type(eval(string)))
            length = len(method_list)
            for index, method in enumerate(reversed(method_list)):
                count_0 += 1  # 
                string_1 = group + "." + subgroup + "." + method
                #print(string_1)        
                if method.startswith("_"):
                    count_1 += 1  # 
                    method_list.pop((length-1) - index)
    #print(qt6_dict)
    #print("Single Unders removed from Methods. Initial:", count_0, "Removed", count_1, 
    #        "Remain:", count_0 - count_1) 
    # Single Unders removed from Methods. Initial: 70945 Removed 0 Remain: 70945
    return qt6_dict
 
        
def remove_no_type(qt6_dict):
    """
    Remove the items that don't have a type()
    """
    count_0 = 0
    count_1 = 0
    count_2 = 0
    count_3 = 0
    bad_type_list = []

    for key, value in qt6_dict.items():
        #print("\n" + key)
        for subkey, item_list in value.items():
            string = key + "." + subkey
            #print(type(eval(string)))
            
            length = len(item_list)
            for index, item in enumerate(reversed(item_list)):
                count_0 += 1
                string_1 = key + "." + subkey + "." + item
                #print(string_1)        
                try:
                    x = type(eval(string_1))
                    #print(string_1, x)
                except Exception as e:
                    #print(string_1)
                    count_1 += 1
                    #print(string_1, ":",  e)
                    
                    # Pop the failure from the list
                    item_list.pop((length-1) - index)
                    
                    bad_type_list.append(string_1)
                                   
    #print("No type() methods removed. Initial: ", count_0, "Removed:", count_1, 
    #            "Remain:", count_0 - count_1) 
    # No type() methods removed. Initial:  70945 Removed: 385 Remain: 70560
    # print(bad_type_list)    
    return qt6_dict
    

def analyse_dictionary(qt6_dict):

    module_count = dir(qt6_dict)
    
    count_0 = 0
    count_1 = 0
    count_2 = 0
    for classes, classes_dict in qt6_dict.items():
        count_0 += 1
        for methods, method_list in classes_dict.items():        
            count_1 += 1
            count_2 += len(method_list)

    return "Modules:{} Classes:{} Methods:{}".format(count_0, count_1, count_2)


def fail_to_import_modules():
    return """    
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

    """ 

if __name__=="__main__":

    if error_stop:
        sys.exit(fail_to_import_modules())    

    module_list = dir()

    qt6_dict = build_dictionary(module_list)
    #print(len(qt6_dict)) # 29

    qt6_dict = remove_classes_double_underscore(qt6_dict)
    
    qt6_dict = remove_methods_double_underscore(qt6_dict)

    qt6_dict = remove_methods_single_underscore(qt6_dict)

    qt6_dict = remove_no_type(qt6_dict)
    
    #print(qt6_dict)    
    MESSAGE = analyse_dictionary(qt6_dict)
    
    #app = QtWidgets.QApplication(sys.argv)
    app = QtWidgets.QApplication([])
    #app.setStyle("Plastique") 
    w = MainWindow(qt6_dict)
    w.show()
    app.exec()


