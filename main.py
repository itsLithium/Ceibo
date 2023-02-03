import os
import sys
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QPushButton, QToolBar, QAction
# from PyQt5.QtGui import QIcon
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *
from PyQt5.QtCore import pyqtSlot

import qrc_resources


class Window(QMainWindow):
    """Main Window."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle("R-Info++")
        self.resize(700, 500)
        self._createActions()
        self._createToolBars()
        self._createStatusBar()
        self._createTextBox()
        
        
        

    def _createTextBox(self):
        layout = QVBoxLayout()
        self.editor = QPlainTextEdit()
        fixedfont = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        fixedfont.setPointSize(12)
        self.editor.setFont(fixedfont)
        layout.addWidget(self.editor)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def _createToolBars(self):
        # Using a title
        fileToolBar = self.addToolBar("File")
        fileToolBar.addAction(self.newAction)
        fileToolBar.addAction(self.openAction)
        fileToolBar.addAction(self.saveAction)
        fileToolBar.addAction(self.compileAction)
        fileToolBar.addAction(self.runAction)
        # Using a QToolBar object
        editToolBar = QToolBar("Edit", self)
        self.addToolBar(editToolBar)
        # Using a QToolBar object and a toolbar area
        helpToolBar = QToolBar("Help", self)
        self.addToolBar(Qt.LeftToolBarArea, helpToolBar)


    
    def _createActions(self):
        # Creating action using the first constructor
        self.newAction = QAction(self)
        self.newAction.setText("&New")
        self.newAction.setIcon(QIcon(":file-new.svg"))
        newTip = "Create a new file"
        self.newAction.setStatusTip(newTip)
        self.newAction.setToolTip(newTip)

        self.openAction = QAction(QIcon(":file-open.svg"), "&Open...", self)
        self.saveAction = QAction(QIcon(":file-save.svg"), "&Save", self)
        self.compileAction = QAction(QIcon(":file-compile.svg"), "&Compile", self)
        self.runAction = QAction(QIcon(":file-run.svg"), "&Run", self)
        self.exitAction = QAction("&Exit", self)
        self.copyAction = QAction("&Copy", self)
        self.pasteAction = QAction("&Paste", self)
        self.cutAction = QAction("C&ut", self)
        self.helpContentAction = QAction("&Help Content", self)
        self.aboutAction = QAction("&About", self)

    def _createStatusBar(self):
        self.statusbar = self.statusBar()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())