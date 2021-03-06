# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'config_win.ui'
#
# Created: Thu May 22 12:37:15 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!


from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Config_Dialog(object):
    def setupUi(self, Dialog,config):
        self.Dialog = Dialog
        self.Dialog.setObjectName(_fromUtf8("Dialog"))
        self.Dialog.resize(413, 335)
        self.lineEdit = QtGui.QLineEdit(self.Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(180, 30, 181, 21))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 70, 181, 21))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(self.Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 110, 181, 21))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_3.setEchoMode(QLineEdit.Password)
        self.lineEdit_4 = QtGui.QLineEdit(self.Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(180, 150, 181, 21))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_5 = QtGui.QLineEdit(self.Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(180, 190, 181, 21))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.label = QtGui.QLabel(self.Dialog)
        self.label.setGeometry(QtCore.QRect(60, 30, 58, 15))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 70, 58, 15))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.Dialog)
        self.label_3.setGeometry(QtCore.QRect(60, 110, 58, 15))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.Dialog)
        self.label_4.setGeometry(QtCore.QRect(60, 150, 58, 15))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.Dialog)
        self.label_5.setGeometry(QtCore.QRect(60, 180, 58, 15))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.Dialog)
        self.label_6.setGeometry(QtCore.QRect(60, 220, 58, 15))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lineEdit_6 = QtGui.QLineEdit(self.Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(180, 220, 181, 21))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.pushButton_ok = QtGui.QPushButton(self.Dialog)
        self.pushButton_ok.setGeometry(QtCore.QRect(60, 270, 79, 25))
        self.pushButton_ok.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_cancel = QtGui.QPushButton(self.Dialog)
        self.pushButton_cancel.setGeometry(QtCore.QRect(220, 270, 79, 25))
        self.pushButton_cancel.setObjectName(_fromUtf8("pushButton_2"))
        self.Dialog.connect(self.pushButton_ok,QtCore.SIGNAL('clicked()'),self.save)
        self.Dialog.connect(self.pushButton_cancel,QtCore.SIGNAL('clicked()'),self.clear)
        self.retranslateUi(self.Dialog)
        self.loadConfig(config)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "选项配置", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "服务器地址", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "用户名", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "密码", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "远程目录", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "本地目录", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "排除文件", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_ok.setText(QtGui.QApplication.translate("Dialog", "确定", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_cancel.setText(QtGui.QApplication.translate("Dialog", "重置", None, QtGui.QApplication.UnicodeUTF8))
        
    
    def loadConfig(self,config):
        self.config = config
        if config.configuration is not None:
            if 'server' in config.configuration.keys():
                self.lineEdit.setText(config.configuration['server']);
            if 'username' in config.configuration.keys():
                self.lineEdit_2.setText(config.configuration['username']);
            if 'password' in config.configuration.keys():
                self.lineEdit_3.setText(config.configuration['password']);
            if 'dest_path' in config.configuration.keys():
                self.lineEdit_4.setText(config.configuration['dest_path']);
            if 'from_path' in config.configuration.keys():
                self.lineEdit_5.setText(config.configuration['from_path']);
            if 'from_exclude' in config.configuration.keys():
                self.lineEdit_6.setText(config.configuration['from_exclude']);
            
            
    
    def save(self):
        self.config.saveConfig(server=self.lineEdit.text(),username=self.lineEdit_2.text(),password=self.lineEdit_3.text(),frompath=self.lineEdit_5.text(),destpath=self.lineEdit_4.text(),fromexclude=self.lineEdit_6.text())
        #msgBox = QMessageBox()
        #msgBox.setTitle()
        #msgBox.setText(self.lineEdit.trUtf8('保存成功'))
        #msgBox.exec_()
        ret = QMessageBox.information(self.Dialog,self.lineEdit.trUtf8('提示'),self.lineEdit.trUtf8('保存成功'),QMessageBox.Save)
        self.Dialog.close()
        
    
    def clear(self):
        self.lineEdit.setText('');
        self.lineEdit_2.setText('');
        self.lineEdit_3.setText('');
        self.lineEdit_4.setText('');
        self.lineEdit_5.setText('');
        self.lineEdit_6.setText('');

