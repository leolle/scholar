# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import (QPushButton, QWidget, QMainWindow, QLineEdit,
                             QApplication)
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag

import sys


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


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        edit = QLineEdit('', self)
        edit.setDragEnabled(True)
        edit.move(30, 65)
        # edit.resize(280, 40)

        button = Button("Download", self)
        button.move(190, 65)

        self.setWindowTitle('Scholar manager')
        self.setGeometry(300, 300, 500, 300)
        self.statusBar().showMessage('Welcome to scholar manager.')

        @pyqtSlot()
        def on_click(self):
            textboxValue = self.textbox.text()
            QMessageBox.question(self, 'Message - pythonspot.com',
                                 "You typed: " + textboxValue, QMessageBox.Ok,
                                 QMessageBox.Ok)
            self.textbox.setText("")


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()
