import sys
import time
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1360, 748)
        MainWindow.setStyleSheet("background-color: rgb(52, 73, 94);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(529, 180, 351, 371))
        self.frame.setStyleSheet("background-color: rgb(51, 51, 51);\n"
"border-radius:20px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 341, 361))
        self.frame_3.setStyleSheet("background-color: rgb(25, 25, 25);\n"
"background-color: rgb(0, 0, 0);\n"
"border:3px solid green;\n"
"border-radius:20px;\n"
"color:white;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(10, 40, 321, 51))
        self.label.setStyleSheet("border-radius:none;\n"
"border:none;")
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.frame_3)
        self.textEdit.setGeometry(QtCore.QRect(30, 130, 281, 41))
        self.textEdit.setStyleSheet("border-radius:20px;\n"
"border:2px solid green;")
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setPlaceholderText("                                      UserName")
        self.textEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.textEdit_2 = QtWidgets.QTextEdit(self.frame_3)
        self.textEdit_2.setGeometry(QtCore.QRect(60, 200, 221, 41))
        self.textEdit_2.setStyleSheet("border-radius:20px;\n"
"border:2px solid blue;")
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setPlaceholderText("                            PassWord")
        self.textEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setGeometry(QtCore.QRect(120, 260, 101, 41))
        self.pushButton.setMouseTracking(True)
        self.pushButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton.setAcceptDrops(True)
        self.pushButton.setStyleSheet("border-radius:20px;\n"
"border:2px solid green;")
        self.pushButton.setDefault(True)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.fade)
        self.pushButton.setStyleSheet("QPushButton"
                             "{"
                              "border-radius:20"
                              "}"
                            "QPushButton::hover"
                             "{"
                             "background-color : green;"
                             "}"
                             "QPushButton::clicked"
                             "{"
                             "background-color : violet;"
                             "}")

    def fade(self):
        print("done")
        if self.textEdit_2.toPlainText() != "":
            self.frame_3.setStyleSheet("border:2px solid blue;background-color:black;color:white;")
            self.pushButton.setStyleSheet("border-radius:20px;border:2px solid green;")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#ffffff;\">LOGIN</span></p></body></html>"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Login"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    #Developed by Atron13
