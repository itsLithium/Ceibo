import os
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *
from PyQt5.QtGui import QPainterPath
from highlighter import Highlighter
from core.Interpreter import Interpreter


import qrc_resources

class DebugConsole(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window")
        layout.addWidget(self.label)
        self.setLayout(layout)


class Window(QMainWindow):
    """Main Window."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.c = None 
        self.setWindowTitle("Albot")
        self.resize(700, 500)
        self.layout = QVBoxLayout()
        self.container = QWidget()
        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)
        self._createActions()
        self._createToolBars()
        self._createStatusBar()
        self._createTextBox()
        self._createCity()
             

    # def closeEvent(self, event):
    #     messageBox = QMessageBox()
    #     title = "Quit Application?"
    #     message = "WARNING !!\n\nIf you quit without saving, any changes made to the file will be lost.\n\nSave file before quitting?"
        
    #     reply = messageBox.question(self, title, message, messageBox.Yes | messageBox.No |
    #         messageBox.Cancel, messageBox.Cancel)
    #     if reply == messageBox.Yes:
    #         return_value = self.save_current_file()
    #         if return_value == False:
    #             event.ignore()
    #     elif reply == messageBox.No:
    #         event.accept()
    #     else:
    #         event.ignore()

    def _createTextBox(self):
        
        self.editor = QTextEdit()
        font = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        self.editor.setFont(font)
        self.highlighter = Highlighter(self.editor.document())
        self.layout.addWidget(self.editor)
        
        
    
    
    # def paintEvent(self, event):
    #     painter = QPainter(self)
    #     painter.setPen(QPen(Qt.green,  8, Qt.SolidLine))
    #     painter.drawEllipse(40, 40, 400, 400)

    def _createCity(self):
        self.city = CityWidget()
        

        scroll = QScrollArea()
        scroll.setWidget(self.city)
        scroll.setWidgetResizable(True)

        self.layout.addWidget(scroll)
    
    def _createToolBars(self):
        # Using a title
        fileToolBar = self.addToolBar("File")
        fileToolBar.addAction(self.newAction)
        fileToolBar.addAction(self.openAction)
        fileToolBar.addAction(self.saveAction)
        fileToolBar.addAction(self.compileAction)
        fileToolBar.addAction(self.runAction)
        fileToolBar.addAction(self.consoleAction)



    
    def _createActions(self):
        # Creating action using the first constructor
        self.newAction = QAction(self)
        self.newAction.setText("&New")
        self.newAction.setIcon(QIcon(":file-new.svg"))
        self.newAction.triggered.connect(self.new_file)
        self.newAction.setStatusTip("Create a new file")
        self.newAction.setToolTip("Create a new file")

        self.openAction = QAction(QIcon(":file-open.svg"), "&Open...", self)
        self.openAction.triggered.connect(self.file_open)
        self.openAction.setStatusTip("Open existing file")
        self.openAction.setToolTip("Open existing file")
        self.saveAction = QAction(QIcon(":file-save.svg"), "&Save", self)
        self.saveAction.triggered.connect(self.file_saveas)
        self.saveAction.setStatusTip("Save file")
        self.saveAction.setToolTip("Save file")
        self.compileAction = QAction(QIcon(":file-compile.svg"), "&Compile", self)
        self.compileAction.triggered.connect(self.compile)
        self.compileAction.setStatusTip("Compile and verify the code")
        self.compileAction.setToolTip("Compile and verify the code")
        self.runAction = QAction(QIcon(":file-run.svg"), "&Run", self)
        self.runAction.setStatusTip("Run the code")
        self.runAction.setToolTip("Run the code")
        self.consoleAction = QAction(QIcon(":debug-console.svg"), "&Debug Console", self)
        self.consoleAction.triggered.connect(self.debug_console)
        self.consoleAction.setStatusTip("Open debug console")
        self.consoleAction.setToolTip("Open debug console")
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

    def file_save(self):
 
        # if there is no save path
        if self.path is None:
 
            # call save as method
            return self.file_saveas()
 
        # else call save to path method
        self._save_to_path(self.path)

    def new_file(self):
        self.editor.setPlainText("")
    
    def file_saveas(self):
 
        # opening path
        path, _ = QFileDialog.getSaveFileName(self, "Save file", "",
                             "Text documents (*.txt")
 
        # if dialog is cancelled i.e no path is selected
        if not path:
            # return this method
            # i.e no action performed
            return
 
        # else call save to path method
        self._save_to_path(path)
 
    # save to path method
    def _save_to_path(self, path):
 
        # get the text
        text = self.editor.toPlainText()
 
        # try catch block
        try:
 
            # opening file to write
            with open(path, 'w') as f:
 
                # write text in the file
                f.write(text)
 
        # if error occurs
        except Exception as e:
 
            # show error using critical
            self.dialog_critical(str(e))
 
        # else do this
        else:
            # change path
            self.path = path
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
    @pyqtSlot()
    def compile(self):
        print("compiled")
        program = self.editor.toPlainText()
        try:
            interpreter = Interpreter(program)
            interpreter.interpret()
            scope = interpreter.GLOBAL_SCOPE
            # symtab = interpreter.symtab_builder.symtab.symbols
            self.editor.setPlainText('\n'.join([f'{k}: {scope[k]}' for k in sorted(scope.keys())]))
            self.editor.setStyleSheet('color: black')
            # self.editor.setPlainText('\n'.join([f'{i}' for i in symtab.values()]))
            # print('\n'.join([f'{i}' for i in symtab.values()]))
            print("yes")

        except Exception as e:
            self.editor.setPlainText(str(e))
            self.editor.setStyleSheet('color: red')
            # self.editor.setPlainText('')
            print("no")
            print(str(e))
        # print(result)

    def debug_console(self):
        if self.c is None:
            self.c = DebugConsole()
            self.c.show()
        else:
            self.c = None
        

class CityWidget(QWidget):
        def __init__(self, parent=None):
            super().__init__(parent)

        def paintEvent(self, event):
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing)
            brush = QBrush(Qt.SolidPattern)
            brush.setColor(QColor("#dddddd"))
            painter.setBrush(brush)
            for i in range(50):
                for j in range(50):
                    x = 20 * i 
                    y = 20 * j
                    painter.drawRect(x, y, 10, 10)
        
        def sizeHint(self):
            return QSize(1000, 1000)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())