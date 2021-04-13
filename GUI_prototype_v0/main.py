# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
#imported to create gui

class Ui_MainWindow (object):
	#this function tells the program to open a new window when the accept button is pushed
    def openWindow(self):
        self.window = QtWidgets.QMainWindow ()
        self.ui = Ui_DODID()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()

    def setupUi(self, MainWindow):
    #mainwindow frame
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1207, 697)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        MainWindow.setAnimated(False)
        
        # MAHP Banner Configuration
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1431, 701))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect (100, 10, 181, 141))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("fdab4217-ca15-4704-ae4c-216721245620_1.6373d75f8bcf8cea46755552d5d19d71"
                                             ".jpeg"))
        self.label.setScaledContents(True)
        self.label.setOpenExternalLinks(False)
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName("label")

        # Push button to accept terms in GUI button
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(660, 610, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.openWindow)
	#privacy act text 
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(260, 100, 881, 481))
        self.textEdit.setUndoRedoEnabled(False)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_2.setGeometry(QtCore.QRect(260, 40, 881, 41))
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton.raise_()
        self.label.raise_()
        self.textEdit.raise_()
        self.textEdit_2.raise_()
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1207, 22))
        self.menubar.setObjectName("menubar")
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        # QT Translator to convert HTML
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Accept"))
        # Text generated in GUI below
        self.textEdit.setHtml(_translate ("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                                         "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style "
                                                         "type=\"text/css\">\n "
                                                         "p, li { white-space: pre-wrap; }\n"
                                                         "</style></head><body style=\" font-family:\'Ubuntu\'; "
                                                         "font-size:11pt; font-weight:400; font-style:normal;\">\n "
                                                         "<p style=\" margin-top:12px; margin-bottom:12px; "
                                                         "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                                         "text-indent:0px;\"><span style=\" font-size:14pt; "
                                                         "font-weight:600; color:#3465a4;\">Acknowledgement of "
                                                         "Responsibilities of Receiving and Maintaining Privacy Act "
                                                         "Data</span></p>\n "
                                                         "<p style=\" margin-top:12px; margin-bottom:12px; "
                                                         "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                                         "text-indent:0px;\"><span style=\" font-size:12pt;\">DATA YOU "
                                                         "ARE ABOUT TO ACCESS COULD POTENTIALLY BE PROTECTED BY THE "
                                                         "PRIVACY ACT OF 1974. You must:</span></p>\n "
                                                         "<ul style=\"margin-top: 0px; margin-bottom: 0px; "
                                                         "margin-left: 0px; margin-right: 0px; -qt-list-indent: "
                                                         "1;\"><li "
                                                         "style=\" font-size:12pt;\" style=\" margin-top:12px; "
                                                         "margin-bottom:0px; margin-left:0px; margin-right:0px; "
                                                         "-qt-block-indent:0; text-indent:0px;\">Have completed the "
                                                         "necessary training with regards to Security Awareness and "
                                                         "safe-guarding Personally Identifiable Information.</li>\n "
                                                         "<li style=\" font-size:12pt;\" style=\" margin-top:0px; "
                                                         "margin-bottom:0px; margin-left:0px; margin-right:0px; "
                                                         "-qt-block-indent:0; text-indent:0px;\">Ensure that data is "
                                                         "not posted, stored or available in any way for uncontrolled "
                                                         "access on any media. </li>\n "
                                                         "<li style=\" font-size:12pt;\" style=\" margin-top:0px; "
                                                         "margin-bottom:0px; margin-left:0px; margin-right:0px; "
                                                         "-qt-block-indent:0; text-indent:0px;\">Ensure that data is "
                                                         "protected at all times as required by the Privacy Act of "
                                                         "1974 "
                                                         "(5 USC 552a(I)(3)) as amended and other applicable DOD "
                                                         "regulatory and statutory authority; data will not be shared "
                                                         "with offshore contractors; data from the application, "
                                                         "or any information derived from the application, shall not "
                                                         "be "
                                                         "published, disclosed, released, revealed, shown, sold, "
                                                         "rented, leased or loaned to anyone outside of the "
                                                         "performance "
                                                         "of official duties without prior DMDC approval.</li>\n "
                                                         "<li style=\" font-size:12pt;\" style=\" margin-top:0px; "
                                                         "margin-bottom:0px; margin-left:0px; margin-right:0px; "
                                                         "-qt-block-indent:0; text-indent:0px;\">Delete or destroy "
                                                         "data "
                                                         "from downloaded reports upon completion of the requirement "
                                                         "for their use on individual projects.</li>\n "
                                                         "<li style=\" font-size:12pt;\" style=\" margin-top:0px; "
                                                         "margin-bottom:0px; margin-left:0px; margin-right:0px; "
                                                         "-qt-block-indent:0; text-indent:0px;\">Ensure data will not "
                                                         "be used for marketing purposes.</li>\n "
                                                         "<li style=\" font-size:12pt;\" style=\" margin-top:0px; "
                                                         "margin-bottom:0px; margin-left:0px; margin-right:0px; "
                                                         "-qt-block-indent:0; text-indent:0px;\">Ensure distribution "
                                                         "of "
                                                         "data from a DMDC application is restricted to those with a "
                                                         "need-to-know. In no case shall data be shared with persons "
                                                         "or "
                                                         "entities that do not provide documented proof of a "
                                                         "need-to-know.</li>\n "
                                                         "<li style=\" font-size:12pt;\" style=\" margin-top:0px; "
                                                         "margin-bottom:12px; margin-left:0px; margin-right:0px; "
                                                         "-qt-block-indent:0; text-indent:0px;\">Be aware that "
                                                         "criminal "
                                                         "penalties under section 1106(a) of the Social Security Act ("
                                                         "42 USC 1306(a)), including possible imprisonment, "
                                                         "may apply with respect to any disclosure of information in "
                                                         "the application(s) that is inconsistent with the terms of "
                                                         "application access. The user further acknowledges that "
                                                         "criminal penalties under the Privacy Act (5 USC 552a(I)(3)) "
                                                         "may apply if it is determined that the user has knowingly "
                                                         "and "
                                                         "willfully obtained access to the application(s) under false "
                                                         "pretenses.</li></ul></body></html>"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                                           "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                                           "<html><head><meta name=\"qrichtext\" content=\"1\" "
                                                           "/><style type=\"text/css\">\n "
                                                           "p, li { white-space: pre-wrap; }\n"
                                                           "</style></head><body style=\" font-family:\'Ubuntu\'; "
                                                           "font-size:11pt; font-weight:400; font-style:normal;\">\n "
                                                           "<p align=\"center\" style=\" margin-top:0px; "
                                                           "margin-bottom:0px; margin-left:0px; margin-right:0px; "
                                                           "-qt-block-indent:0; text-indent:0px;\"><span style=\" "
                                                           "font-size:18pt; font-weight:600; color:#4e9a06;\">Mental "
                                                           "Health Assessment Portal</span></p></body></html>"))


if __name__ == "__main__":
    #runs gui
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
