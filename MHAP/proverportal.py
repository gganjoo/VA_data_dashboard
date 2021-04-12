# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'patient_data.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
import math
import pandas as pd
import matplotlib.pyplot as plt


df_cmpt_demo = pd.read_json('JSON_data_files/2019_suicidepct_bycmpt_bydemo.json')
df_cmpt = pd.read_json('JSON_data_files/2019_suicidepct_bycmpt.json', typ='series')
df_cmpt = df_cmpt.to_frame()
df_cmpt.columns=['pct']

soldier_data = pd.read_csv('Soldier_data_fake1_20210409 copy.csv')

class Ui_provider_window(object):
    def setupUi(self, provider_window):
        provider_window.setObjectName("provider_window")
        provider_window.resize(1189, 711)
        provider_window.setStyleSheet("background-color: rgb(243, 243, 243)")
        self.textEdit_8 = QtWidgets.QTextEdit(provider_window)
        self.textEdit_8.setGeometry(QtCore.QRect(90, 560, 1071, 121))
        self.textEdit_8.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.textEdit_8.setObjectName("textEdit_8")
        self.lineEdit = QtWidgets.QLineEdit(provider_window)
        self.lineEdit.setGeometry(QtCore.QRect(90, 520, 113, 25))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(provider_window)
        self.dateTimeEdit.setGeometry(QtCore.QRect(960, 520, 194, 26))
        self.dateTimeEdit.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.verticalScrollBar = QtWidgets.QScrollBar(provider_window)
        self.verticalScrollBar.setGeometry(QtCore.QRect(1140, 560, 20, 121))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.textEdit_9 = QtWidgets.QTextEdit(provider_window)
        self.textEdit_9.setGeometry(QtCore.QRect(3, 20, 1191, 71))
        self.textEdit_9.setStyleSheet("background-color:rgb(85, 87, 83)")
        self.textEdit_9.setObjectName("textEdit_9")
        self.graphicsView = QtWidgets.QGraphicsView(provider_window)
        self.graphicsView.setGeometry(QtCore.QRect(435, 121, 721, 381))
        self.graphicsView.setObjectName("graphicsView")
        #Dataframe data
        self.listView = QtWidgets.QListView(provider_window)
        self.listView.setGeometry(QtCore.QRect(90, 120, 311, 381))
        self.listView.setObjectName("listView")

        self.retranslateUi(provider_window)
        QtCore.QMetaObject.connectSlotsByName(provider_window)

    def retranslateUi(self, provider_window):
        _translate = QtCore.QCoreApplication.translate
        provider_window.setWindowTitle(_translate("provider_window", "Form"))
        self.lineEdit.setText(_translate("provider_window", "Notes:"))
        self.textEdit_9.setHtml(_translate("provider_window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; font-weight:600; color:#f3f3f3;\">MHAP- Provider Portal</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    provider_window = QtWidgets.QWidget()
    ui = Ui_provider_window()
    ui.setupUi(provider_window)
    provider_window.show()
    sys.exit(app.exec_())

