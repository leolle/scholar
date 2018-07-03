# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import (QPushButton, QWidget, QMainWindow, QLineEdit,
                             QApplication)
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag

import sys
import scihub


class Button(QPushButton):

    def __init__(self, title, parent):
        super().__init__(title, parent)

        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):

        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):

        self.setText(e.mimeData().text())

    def mousePressEvent(self, e):

        super().mousePressEvent(e)

        if e.button() == Qt.LeftButton:
            print('press')
            # self.statusBar().showMessage('press')


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        # self.setWindowTitle('Scholar manager')
        self.title = 'Scholar manager'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 140
        self.initUI()
        self.scihub = scihub.SciHub()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280, 40)

        # Create a button in the window
        self.button = QPushButton('Download', self)
        self.button.move(20, 80)
        self.statusBar().showMessage('Welcome to scholar manager.')

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        QMessageBox.question(self, 'Message - pythonspot.com',
                             "You typed: " + textboxValue, QMessageBox.Ok,
                             QMessageBox.Ok)
        self.textbox.setText("")
        results = self.scihub.search(textboxValue, 1)
        for paper in results['papers']:
            print(paper)
            paper['meta'] = self.scihub.find_meta(paper)
            pdf = self.scihub.download(paper, destination='pdf_files')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
