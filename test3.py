# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(628, 1118)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 20, 471, 31))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(40, 70, 541, 181))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 50, 401, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(270, 280, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(40, 610, 541, 471))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 560, 111, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        # self.verticalScrollBar_3 = QtWidgets.QScrollBar(Dialog)
        # self.verticalScrollBar_3.setGeometry(QtCore.QRect(555, 620, 21, 451))
        # self.verticalScrollBar_3.setOrientation(QtCore.Qt.Vertical)
        # self.verticalScrollBar_3.setObjectName("verticalScrollBar_3")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(40, 350, 541, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(500)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        # self.checkBox = QtWidgets.QCheckBox(Dialog)
        # self.checkBox.setGeometry(QtCore.QRect(70, 380, 81, 16))
        # self.checkBox.setObjectName("checkBox")
        # self.verticalScrollBar = QtWidgets.QScrollBar(Dialog)
        # self.verticalScrollBar.setGeometry(QtCore.QRect(560, 360, 20, 171))
        # self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        # self.verticalScrollBar.setObjectName("verticalScrollBar")
        # self.verticalScrollBar_2 = QtWidgets.QScrollBar(Dialog)
        # self.verticalScrollBar_2.setGeometry(QtCore.QRect(560, 80, 20, 161))
        # self.verticalScrollBar_2.setOrientation(QtCore.Qt.Vertical)
        # self.verticalScrollBar_2.setObjectName("verticalScrollBar_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "아래 작성하려는 문서의 주제 혹은 간략한 요약을 입력하세요."))
        self.label_2.setText(_translate("Dialog", "예시) 자동차 판매 보고서 만들어 줘"))
        self.pushButton.setText(_translate("Dialog", "File Search"))
        self.pushButton_2.setText(_translate("Dialog", "Create Document"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "파일 이름"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "파일 경로"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 1)
        item = self.checkBox = QtWidgets.QCheckBox(Dialog)
        item = self.checkBox.setGeometry(QtCore.QRect(70, 380, 81, 16))
        item = self.checkBox.setObjectName("checkBox")
        item.setText(_translate("Dialog", "C:/user/home/자동차 판매"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.checkBox.setText(_translate("Dialog", "CheckBox"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
