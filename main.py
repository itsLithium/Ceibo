import os
import sys
import re
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QPushButton, QToolBar, QAction
# from PyQt5.QtGui import QIcon
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *

import qrc_resources

class Highlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super(Highlighter, self).__init__(parent)

        keywordFormat = QTextCharFormat()
        keywordFormat.setForeground(Qt.red)
        keywordFormat.setFontWeight(QFont.Bold)

        keywordPatterns = ["\\bprograma\\b", "\\bareas\\b", "\\bvariables\\b",
                "\\brobots\\b", "\\bcomenzar\\b", "\\bfin\\b", "\\bfriend\\b",
                "\\binline\\b", "\\bint\\b", "\\blong\\b", "\\bnamespace\\b",
                "\\boperator\\b", "\\bprivate\\b", "\\bprotected\\b",
                "\\bpublic\\b", "\\bshort\\b", "\\bsignals\\b", "\\bsigned\\b",
                "\\bslots\\b", "\\bstatic\\b", "\\bstruct\\b",
                "\\btemplate\\b", "\\btypedef\\b", "\\btypename\\b",
                "\\bunion\\b", "\\bunsigned\\b", "\\bvirtual\\b", "\\bvoid\\b",
                "\\bvolatile\\b"]

        self.highlightingRules = [(QRegExp(pattern), keywordFormat)
                for pattern in keywordPatterns]

        classFormat = QTextCharFormat()
        classFormat.setFontWeight(QFont.Bold)
        classFormat.setForeground(Qt.darkMagenta)
        self.highlightingRules.append((QRegExp("\\bQ[A-Za-z]+\\b"),
                classFormat))

        singleLineCommentFormat = QTextCharFormat()
        singleLineCommentFormat.setForeground(Qt.red)
        self.highlightingRules.append((QRegExp("//[^\n]*"),
                singleLineCommentFormat))

        self.multiLineCommentFormat = QTextCharFormat()
        self.multiLineCommentFormat.setForeground(Qt.red)

        quotationFormat = QTextCharFormat()
        quotationFormat.setForeground(Qt.darkGreen)
        self.highlightingRules.append((QRegExp("\".*\""), quotationFormat))

        functionFormat = QTextCharFormat()
        functionFormat.setFontItalic(True)
        functionFormat.setForeground(Qt.blue)
        self.highlightingRules.append((QRegExp("\\b[A-Za-z0-9_]+(?=\\()"),
                functionFormat))

        self.commentStartExpression = QRegExp("/\\*")
        self.commentEndExpression = QRegExp("\\*/")

    def highlightBlock(self, text):
        for pattern, format in self.highlightingRules:
            expression = QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)

        startIndex = 0
        if self.previousBlockState() != 1:
            startIndex = self.commentStartExpression.indexIn(text)

        while startIndex >= 0:
            endIndex = self.commentEndExpression.indexIn(text, startIndex)

            if endIndex == -1:
                self.setCurrentBlockState(1)
                commentLength = len(text) - startIndex
            else:
                commentLength = endIndex - startIndex + self.commentEndExpression.matchedLength()

            self.setFormat(startIndex, commentLength,
                    self.multiLineCommentFormat)
            startIndex = self.commentStartExpression.indexIn(text,
                    startIndex + commentLength);

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
        self.editor = QTextEdit()
        font = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        self.editor.setFont(font)
        self.highlighter = Highlighter(self.editor.document())
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
        self.openAction.triggered.connect(self.file_open)
        self.saveAction = QAction(QIcon(":file-save.svg"), "&Save", self)
        self.compileAction = QAction(QIcon(":file-compile.svg"), "&Compile", self)
        self.compileAction.triggered.connect(self.compile)
        self.runAction = QAction(QIcon(":file-run.svg"), "&Run", self)
        self.exitAction = QAction("&Exit", self)
        self.copyAction = QAction("&Copy", self)
        self.pasteAction = QAction("&Paste", self)
        self.cutAction = QAction("C&ut", self)
        self.helpContentAction = QAction("&Help Content", self)
        self.aboutAction = QAction("&About", self)



    def _createStatusBar(self):
        self.statusbar = self.statusBar()

    def dialog_critical(self, s):
 
        # creating a QMessageBox object
        dlg = QMessageBox(self)
 
        # setting text to the dlg
        dlg.setText(s)
 
        # setting icon to it
        dlg.setIcon(QMessageBox.Critical)
 
        # showing it
        dlg.show()

    def file_open(self):
        # getting path and bool value
        path, _ = QFileDialog.getOpenFileName(self, "Open file", "",
                             "Text documents (*.txt);All files (*.*)")
        # if path is true
        if path:
            # try opening path
            try:
                with open(path) as f:
                    # read the file
                    text = f.read()
 
            # if some error occurred
            except Exception as e:
                # show error using critical method
                self.dialog_critical(str(e))
            # else
            else:
                # update path value
                self.path = path
                # update the text
                self.editor.setPlainText(text)
                # update the title
                self.update_title()

    def file_print(self):
 
        # creating a QPrintDialog
        dlg = QPrintDialog()
 
        # if executed
        if dlg.exec_():
 
            # print the text
            self.editor.print_(dlg.printer())

    def update_title(self):
 
        # setting window title with prefix as file name
        # suffix as PyQt5 Notepad
        self.setWindowTitle("%s - PyQt5 Notepad" %(os.path.basename(self.path)
                                                  if self.path else "Untitled"))
    
    def compile(self):
        self.txt = self.editor.toPlainText()
        print(self.txt)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())