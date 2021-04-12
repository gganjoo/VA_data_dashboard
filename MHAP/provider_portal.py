# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'patient_data.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_provider_window(object):
    def setupUi(self, provider_window):
        provider_window.setObjectName("provider_window")
        provider_window.resize(1189, 711)
        provider_window.setStyleSheet("background-color: rgb(243, 243, 243)")
        self.textEdit = QtWidgets.QTextEdit(provider_window)
        self.textEdit.setGeometry(QtCore.QRect(20, 100, 81, 31))
        self.textEdit.setStyleSheet("background-color:rgb(136, 138, 133)")
        self.textEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(provider_window)
        self.textEdit_2.setGeometry(QtCore.QRect(20, 140, 81, 31))
        self.textEdit_2.setStyleSheet("background-color:rgb(136, 138, 133)\n"
"")
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(provider_window)
        self.textEdit_3.setGeometry(QtCore.QRect(20, 260, 81, 31))
        self.textEdit_3.setStyleSheet("background-color:rgb(136, 138, 133)")
        self.textEdit_3.setReadOnly(True)
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(provider_window)
        self.textEdit_4.setGeometry(QtCore.QRect(20, 300, 81, 31))
        self.textEdit_4.setStyleSheet("background-color:rgb(136, 138, 133)")
        self.textEdit_4.setReadOnly(True)
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_5 = QtWidgets.QTextEdit(provider_window)
        self.textEdit_5.setGeometry(QtCore.QRect(20, 340, 81, 31))
        self.textEdit_5.setStyleSheet("background-color:rgb(136, 138, 133)")
        self.textEdit_5.setReadOnly(True)
        self.textEdit_5.setObjectName("textEdit_5")
        self.textEdit_6 = QtWidgets.QTextEdit(provider_window)
        self.textEdit_6.setGeometry(QtCore.QRect(20, 380, 81, 31))
        self.textEdit_6.setStyleSheet("background-color:rgb(136, 138, 133)")
        self.textEdit_6.setReadOnly(True)
        self.textEdit_6.setObjectName("textEdit_6")
        self.textEdit_7 = QtWidgets.QTextEdit(provider_window)
        self.textEdit_7.setGeometry(QtCore.QRect(20, 220, 81, 31))
        self.textEdit_7.setStyleSheet("background-color:rgb(136, 138, 133)")
        self.textEdit_7.setReadOnly(True)
        self.textEdit_7.setObjectName("textEdit_7")
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
        self.graph2 = QtWidgets.QGraphicsView(provider_window)
        self.graph2.setGeometry(QtCore.QRect(370, 100, 751, 391))
        self.graph2.setObjectName("graph2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(provider_window)
        self.plainTextEdit.setGeometry(QtCore.QRect(110, 100, 221, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(provider_window)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(110, 140, 221, 31))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(provider_window)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(110, 180, 221, 31))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(provider_window)
        self.plainTextEdit_4.setGeometry(QtCore.QRect(110, 220, 221, 31))
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")
        self.plainTextEdit_5 = QtWidgets.QPlainTextEdit(provider_window)
        self.plainTextEdit_5.setGeometry(QtCore.QRect(110, 260, 221, 31))
        self.plainTextEdit_5.setObjectName("plainTextEdit_5")
        self.plainTextEdit_6 = QtWidgets.QPlainTextEdit(provider_window)
        self.plainTextEdit_6.setGeometry(QtCore.QRect(110, 300, 221, 31))
        self.plainTextEdit_6.setObjectName("plainTextEdit_6")
        self.plainTextEdit_7 = QtWidgets.QPlainTextEdit(provider_window)
        self.plainTextEdit_7.setGeometry(QtCore.QRect(110, 340, 221, 31))
        self.plainTextEdit_7.setObjectName("plainTextEdit_7")
        self.plainTextEdit_8 = QtWidgets.QPlainTextEdit(provider_window)
        self.plainTextEdit_8.setGeometry(QtCore.QRect(110, 460, 221, 31))
        self.plainTextEdit_8.setObjectName("plainTextEdit_8")
        self.plainTextEdit_9 = QtWidgets.QPlainTextEdit(provider_window)
        self.plainTextEdit_9.setGeometry(QtCore.QRect(110, 420, 221, 31))
        self.plainTextEdit_9.setObjectName("plainTextEdit_9")
        self.plainTextEdit_10 = QtWidgets.QPlainTextEdit(provider_window)
        self.plainTextEdit_10.setGeometry(QtCore.QRect(110, 380, 221, 31))
        self.plainTextEdit_10.setObjectName("plainTextEdit_10")
        self.verticalScrollBar = QtWidgets.QScrollBar(provider_window)
        self.verticalScrollBar.setGeometry(QtCore.QRect(1140, 560, 20, 121))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.textEdit_9 = QtWidgets.QTextEdit(provider_window)
        self.textEdit_9.setGeometry(QtCore.QRect(3, 20, 1191, 71))
        self.textEdit_9.setStyleSheet("background-color:rgb(85, 87, 83)")
        self.textEdit_9.setObjectName("textEdit_9")

        self.retranslateUi(provider_window)
        QtCore.QMetaObject.connectSlotsByName(provider_window)

    def retranslateUi(self, provider_window):
        _translate = QtCore.QCoreApplication.translate
        provider_window.setWindowTitle(_translate("provider_window", "Form"))
        self.textEdit.setHtml(_translate("provider_window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Name:</span></p></body></html>"))
        self.textEdit_2.setHtml(_translate("provider_window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Address:</span></p></body></html>"))
        self.textEdit_3.setHtml(_translate("provider_window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Phone:</span></p></body></html>"))
        self.textEdit_4.setHtml(_translate("provider_window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Service:</span></p></body></html>"))
        self.textEdit_5.setHtml(_translate("provider_window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">BASD:</span></p></body></html>"))
        self.textEdit_6.setHtml(_translate("provider_window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">NOK:</span></p></body></html>"))
        self.textEdit_7.setHtml(_translate("provider_window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Email:</span></p></body></html>"))
        self.lineEdit.setText(_translate("provider_window", "Notes:"))
        self.plainTextEdit.setPlainText(_translate("provider_window", "name"))
        self.plainTextEdit_2.setPlainText(_translate("provider_window", "address"))
        self.plainTextEdit_3.setPlainText(_translate("provider_window", "state"))
        self.plainTextEdit_4.setPlainText(_translate("provider_window", "email"))
        self.plainTextEdit_5.setPlainText(_translate("provider_window", "phone"))
        self.plainTextEdit_6.setPlainText(_translate("provider_window", "service"))
        self.plainTextEdit_7.setPlainText(_translate("provider_window", "basd"))
        self.plainTextEdit_8.setPlainText(_translate("provider_window", "nok email"))
        self.plainTextEdit_9.setPlainText(_translate("provider_window", "nok phone"))
        self.plainTextEdit_10.setPlainText(_translate("provider_window", "nok name"))
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

