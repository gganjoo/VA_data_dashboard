# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dodid.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets

soldier_data = pd.read_csv('Soldier_data_fake1_20210409 copy.csv')


class Ui_DODID(object):
    def roster(self, dataframe):
        dataframe['dodid'] = dataframe['dodid'].fillna(0).astype('int')
        dataframe = dataframe.set_index('dodid')
        self.roster = dataframe.to_dict(orient = 'index')
        ros = self.roster(soldier_data)

    def setupUi(self, DODID):
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
        self.label.setPixmap(QtGui.QPixmap("fdab4217-ca15-4704-ae4c-216721245620_1.6373d75f8bcf8cea46755552d5d19d71.jpeg"))
        self.label.setScaledContents(True)
        self.label.setOpenExternalLinks(False)
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName("label")
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
        #dropdown menu
        self.comboBox = QtWidgets.QComboBox(DODID)
        self.comboBox.setGeometry(QtCore.QRect(340, 380, 231, 25))
        self.comboBox.setObjectName("comboBox")
        for dodid in ros:
            self.comboBox.addItem(dodid)
        self.comboBox.currentIndex.connect(self.selectionchange)

        self.retranslateUi(DODID)
        QtCore.QMetaObject.connectSlotsByName(DODID)

    def retranslateUi(self, DODID):
        _translate = QtCore.QCoreApplication.translate
        DODID.setWindowTitle(_translate("DODID", "Form"))
        self.banner.setHtml(_translate("DODID", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600; color:#4e9a06;\">Mental Health Assessment Portal</span></p></body></html>"))
        self.cont.setText(_translate("DODID", "Continue"))
        self.label_2.setText(_translate("DODID", "Please select a valid DODID number below to continue"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DODID = QtWidgets.QWidget()
    ui = Ui_DODID()
    ui.setupUi(DODID)
    DODID.show()
    sys.exit(app.exec_())

