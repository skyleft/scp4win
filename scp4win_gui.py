# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scp4win.ui'
#
# Created: Wed May 21 13:58:52 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import config_gui
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(289, 115)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(40, 40, 79, 25))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        Dialog.connect(self.pushButton,QtCore.SIGNAL('clicked()'),self.showConfig);
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 40, 79, 25))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "同步工具", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog", "配置", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Dialog", "开始同步", None, QtGui.QApplication.UnicodeUTF8))

    def showConfig(self):
        config_dialog_ui = config_gui.Config_Dialog()
        self.config_dialog = QDialog();
        config_dialog_ui.setupUi(self.config_dialog)
        self.config_dialog.show()


app=QApplication(sys.argv)
b=Ui_Dialog()
d=QDialog()
b.setupUi(d)
d.show()
app.exec_()
