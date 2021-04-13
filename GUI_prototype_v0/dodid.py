# -*- coding: utf-8 -*-

# this gui was not finalized as the there is still an outstanding issue of importing keys from a JSON
# into the combo box and then linking them to the generated data in the provider portal.  This will
# be addressed in future versions
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
import math
import pandas as pd
from test_combine import Roster


df_cmpt_demo = pd.read_json('JSON_data_files/2019_suicidepct_bycmpt_bydemo.json')
df_cmpt = pd.read_json('JSON_data_files/2019_suicidepct_bycmpt.json', typ='series')
df_cmpt = df_cmpt.to_frame()
df_cmpt.columns=['pct']

# This will not be imported in the real application as it should import the roster from the data class
# This file was imported just to draw in the data for testing and will be removed in future releases

soldier_data = pd.read_csv('Soldier_data_fake1_20210409 copy.csv')

class Ui_DODID (object):

    def setupUi(self, DODID):
        # Banner and Banner Image
        DODID.setObjectName("DODID")
        DODID.resize(886, 615)
        DODID.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.banner = QtWidgets.QTextEdit(DODID)
        self.banner.setGeometry(QtCore.QRect(250, 50, 451, 61))
        self.banner.setReadOnly(True)
        self.banner.setObjectName("banner")
        self.label = QtWidgets.QLabel(DODID)
        self.label.setGeometry(QtCore.QRect(0, 0, 181, 141))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("fdab4217-ca15-4704-ae4c-216721245620_1.6373d75f8bcf8cea46755552d5d19d71"
                                             ".jpeg"))
        self.label.setScaledContents(True)
        self.label.setOpenExternalLinks(False)
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName("label")

        # Push button created to select after selecting DODID to continue
        self.cont = QtWidgets.QPushButton(DODID)
        self.cont.setGeometry(QtCore.QRect(420, 570, 89, 25))
        self.cont.setObjectName("cont")
        self.label_2 = QtWidgets.QLabel(DODID)
        self.label_2.setGeometry(QtCore.QRect(230, 320, 501, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font-color: rgb(78, 154, 6)")
        self.label_2.setObjectName("label_2")

        #C Combo box created by importing 5 keys for testing to ensure it works
        self.comboBox = QtWidgets.QComboBox(DODID)
        self.comboBox.setGeometry(QtCore.QRect(340, 380, 231, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.retranslateUi(DODID)
        QtCore.QMetaObject.connectSlotsByName(DODID)

    def retranslateUi(self, DODID):
        #translated from HTML
        _translate = QtCore.QCoreApplication.translate
        DODID.setWindowTitle(_translate("DODID", "Form"))
        self.banner.setHtml(_translate("DODID",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                         "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style "
                                         "type=\"text/css\">\n "
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; "
                                         "font-weight:400; font-style:normal;\">\n "
                                         "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; "
                                         "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                         "text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600; "
                                         "color:#4e9a06;\">Mental Health Assessment Portal</span></p></body></html>"))
        self.cont.setText(_translate("DODID", "Continue"))
        self.label_2.setText(_translate("DODID", "Please select a valid DODID number below to continue"))
        self.comboBox.setItemText(0, _translate("DODID", "1373602072"))
        self.comboBox.setItemText(1, _translate("DODID", "1232804757"))
        self.comboBox.setItemText(2, _translate("DODID", "9600726439"))
        self.comboBox.setItemText(3, _translate("DODID", "908275015"))
        self.comboBox.setItemText(4, _translate("DODID", "7382178904"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    DODID = QtWidgets.QWidget()
    ui = Ui_DODID()
    ui.setupUi(DODID)
    DODID.show()
    sys.exit(app.exec_())
