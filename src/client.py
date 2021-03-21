import sys, os
from PyQt5 import QtCore, QtGui, QtWidgets
import Protocol
import socket
import threading
import re

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
sock.connect(('localhost', 30000))
sock.send(b'1')
print(sock.recv(1024).decode("unicode_escape"))

# 文件选择对话框
def open_file():
    fileName,fileType = QtWidgets.QFileDialog.getOpenFileName(None, "select", os.getcwd(), "Image Files(*.jpg *.png);;All Files(*)")
    print(fileName)
    print(fileType)
    return fileName

# 重载pyqt5的Label以实现点击事件
class myLabel(QtWidgets.QLabel):
    def __init__(self,parent = None):
        super(myLabel,self).__init__(parent)
        self.label = QtWidgets.QLabel("")
        self.file_name = ""
    
    def mousePressEvent(self, e):
        self.file_name = open_file()
        #self.setText(self.file_name)
        self.setPixmap(QtGui.QPixmap(self.file_name).scaled(80, 80))

    # def mouseDoublePressEvent(self, e):
    #     pass
    #     #print("you clicked the label")

    # # dis show the image
    # def leaveEvent(self, e):  # 鼠标离开label
    #     #print("leave")
    #     if os.path.isfile(self.file_name):
    #         self.label.setPixmap(QtGui.QPixmap(self.file_name))
    #         self.show()
    
    # # show the image besige
    # def enterEvent(self, e):  # 鼠标移入label
    #     #print("enter")
    #     self.label.hide()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1145, 751)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(190, 10, 951, 731))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setEnabled(True)
        self.page.setObjectName("page")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.page)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 60, 751, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_1_id = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_1_id.setMinimumSize(QtCore.QSize(0, 45))
        self.lineEdit_1_id.setObjectName("lineEdit_1_id")
        self.horizontalLayout.addWidget(self.lineEdit_1_id)
        self.lineEdit_1_name = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_1_name.setMinimumSize(QtCore.QSize(0, 45))
        self.lineEdit_1_name.setObjectName("lineEdit_1_name")
        self.horizontalLayout.addWidget(self.lineEdit_1_name)
        self.lineEdit_1_sex = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_1_sex.setMinimumSize(QtCore.QSize(0, 45))
        self.lineEdit_1_sex.setObjectName("lineEdit_1_sex")
        self.horizontalLayout.addWidget(self.lineEdit_1_sex)
        self.lineEdit_1_age = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_1_age.setMinimumSize(QtCore.QSize(0, 45))
        self.lineEdit_1_age.setObjectName("lineEdit_1_age")
        self.horizontalLayout.addWidget(self.lineEdit_1_age)
        self.pushButton_1_search = QtWidgets.QPushButton(self.page)
        self.pushButton_1_search.setGeometry(QtCore.QRect(820, 10, 131, 41))
        self.pushButton_1_search.setObjectName("pushButton_1_search")
        self.pushButton_1_clear = QtWidgets.QPushButton(self.page)
        self.pushButton_1_clear.setGeometry(QtCore.QRect(0, 10, 131, 41))
        self.pushButton_1_clear.setObjectName("pushButton_1_clear")
        self.tableWidget_1_search = QtWidgets.QTableWidget(self.page)
        self.tableWidget_1_search.setGeometry(QtCore.QRect(0, 110, 951, 621))
        self.tableWidget_1_search.setObjectName("tableWidget_1_search")
        self.tableWidget_1_search.setColumnCount(5)
        self.tableWidget_1_search.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1_search.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1_search.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1_search.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1_search.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1_search.setHorizontalHeaderItem(4, item)
        self.tableWidget_1_search.horizontalHeader().setDefaultSectionSize(189)
        self.tableWidget_1_search.horizontalHeader().setMinimumSectionSize(26)
        self.tableWidget_1_search.verticalHeader().setDefaultSectionSize(80)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.textBrowser_2_insert = QtWidgets.QTextBrowser(self.page_2)
        self.textBrowser_2_insert.setGeometry(QtCore.QRect(0, 60, 571, 61))
        self.textBrowser_2_insert.setObjectName("textBrowser_2_insert")
        self.pushButton_2_import = QtWidgets.QPushButton(self.page_2)
        self.pushButton_2_import.setGeometry(QtCore.QRect(820, 10, 131, 41))
        self.pushButton_2_import.setObjectName("pushButton_2_import")
        self.plainTextEdit_2_insert = QtWidgets.QPlainTextEdit(self.page_2)
        self.plainTextEdit_2_insert.setGeometry(QtCore.QRect(0, 130, 951, 601))
        self.plainTextEdit_2_insert.setObjectName("plainTextEdit_2_insert")
        self.pushButton_2_clear = QtWidgets.QPushButton(self.page_2)
        self.pushButton_2_clear.setGeometry(QtCore.QRect(0, 10, 131, 41))
        self.pushButton_2_clear.setObjectName("pushButton_2_clear")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.pushButton_3_insert = QtWidgets.QPushButton(self.page_3)
        self.pushButton_3_insert.setGeometry(QtCore.QRect(820, 10, 131, 41))
        self.pushButton_3_insert.setObjectName("pushButton_3_insert")
        self.pushButton_3_back = QtWidgets.QPushButton(self.page_3)
        self.pushButton_3_back.setGeometry(QtCore.QRect(0, 10, 131, 41))
        self.pushButton_3_back.setObjectName("pushButton_3_back")
        self.tableWidget_3_insert = QtWidgets.QTableWidget(self.page_3)
        self.tableWidget_3_insert.setGeometry(QtCore.QRect(0, 110, 951, 621))
        self.tableWidget_3_insert.setObjectName("tableWidget_3_insert")
        self.tableWidget_3_insert.setColumnCount(6)
        self.tableWidget_3_insert.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3_insert.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3_insert.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3_insert.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3_insert.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3_insert.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3_insert.setHorizontalHeaderItem(5, item)
        self.tableWidget_3_insert.horizontalHeader().setDefaultSectionSize(158)
        self.tableWidget_3_insert.verticalHeader().setDefaultSectionSize(80)
        self.pushButton_3_check = QtWidgets.QPushButton(self.page_3)
        self.pushButton_3_check.setGeometry(QtCore.QRect(150, 10, 131, 41))
        self.pushButton_3_check.setObjectName("pushButton_3_check")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.pushButton_4_update = QtWidgets.QPushButton(self.page_4)
        self.pushButton_4_update.setGeometry(QtCore.QRect(820, 10, 131, 41))
        self.pushButton_4_update.setObjectName("pushButton_4_update")
        self.pushButton_4_search = QtWidgets.QPushButton(self.page_4)
        self.pushButton_4_search.setGeometry(QtCore.QRect(300, 10, 131, 41))
        self.pushButton_4_search.setObjectName("pushButton_4_search")
        self.formLayoutWidget = QtWidgets.QWidget(self.page_4)
        self.formLayoutWidget.setGeometry(QtCore.QRect(160, 240, 251, 281))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(10, 45))
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit_4_old_id = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_4_old_id.setMinimumSize(QtCore.QSize(0, 45))
        self.lineEdit_4_old_id.setReadOnly(False)
        self.lineEdit_4_old_id.setObjectName("lineEdit_4_old_id")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4_old_id)
        self.lineEdit_4_old_name = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_4_old_name.setMinimumSize(QtCore.QSize(0, 45))
        self.lineEdit_4_old_name.setReadOnly(True)
        self.lineEdit_4_old_name.setObjectName("lineEdit_4_old_name")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4_old_name)
        self.lineEdit_4_old_sex = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_4_old_sex.setMinimumSize(QtCore.QSize(0, 45))
        self.lineEdit_4_old_sex.setReadOnly(True)
        self.lineEdit_4_old_sex.setObjectName("lineEdit_4_old_sex")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4_old_sex)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(10, 45))
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(20, 45))
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(10, 45))
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_4_old_age = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_4_old_age.setMinimumSize(QtCore.QSize(0, 45))
        self.lineEdit_4_old_age.setReadOnly(True)
        self.lineEdit_4_old_age.setObjectName("lineEdit_4_old_age")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4_old_age)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setMinimumSize(QtCore.QSize(20, 45))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_5)
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.page_4)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(570, 240, 251, 281))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_6.setMinimumSize(QtCore.QSize(10, 45))
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_4_new_id = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_4_new_id.setMinimumSize(QtCore.QSize(0, 45))
        self.lineEdit_4_new_id.setReadOnly(True)
        self.lineEdit_4_new_id.setObjectName("lineEdit_4_new_id")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4_new_id)
        self.lineEdit_4_new_name = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_4_new_name.setMinimumSize(QtCore.QSize(0, 45))
        self.lineEdit_4_new_name.setReadOnly(False)
        self.lineEdit_4_new_name.setObjectName("lineEdit_4_new_name")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4_new_name)
        self.lineEdit_4_new_sex = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_4_new_sex.setMinimumSize(QtCore.QSize(0, 45))
        self.lineEdit_4_new_sex.setReadOnly(False)
        self.lineEdit_4_new_sex.setObjectName("lineEdit_4_new_sex")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4_new_sex)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_7.setMinimumSize(QtCore.QSize(10, 45))
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_8.setMinimumSize(QtCore.QSize(20, 45))
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_9.setMinimumSize(QtCore.QSize(10, 45))
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.lineEdit_4_new_age = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_4_new_age.setMinimumSize(QtCore.QSize(0, 45))
        self.lineEdit_4_new_age.setReadOnly(False)
        self.lineEdit_4_new_age.setObjectName("lineEdit_4_new_age")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4_new_age)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_10.setMinimumSize(QtCore.QSize(20, 45))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_10)
        self.pushButton_4_clear = QtWidgets.QPushButton(self.page_4)
        self.pushButton_4_clear.setGeometry(QtCore.QRect(0, 10, 131, 41))
        self.pushButton_4_clear.setObjectName("pushButton_4_clear")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.page_4)
        self.textBrowser_3.setGeometry(QtCore.QRect(0, 60, 191, 61))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.pushButton_4_check = QtWidgets.QPushButton(self.page_4)
        self.pushButton_4_check.setGeometry(QtCore.QRect(150, 10, 131, 41))
        self.pushButton_4_check.setObjectName("pushButton_4_check")
        self.lineEdit_4_state = QtWidgets.QLineEdit(self.page_4)
        self.lineEdit_4_state.setGeometry(QtCore.QRect(650, 150, 171, 45))
        self.lineEdit_4_state.setMinimumSize(QtCore.QSize(0, 45))
        self.lineEdit_4_state.setReadOnly(False)
        self.lineEdit_4_state.setObjectName("lineEdit_4_state")
        self.label_11 = QtWidgets.QLabel(self.page_4)
        self.label_11.setGeometry(QtCore.QRect(588, 150, 61, 45))
        self.label_11.setMinimumSize(QtCore.QSize(20, 45))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.pushButton_5_import = QtWidgets.QPushButton(self.page_5)
        self.pushButton_5_import.setGeometry(QtCore.QRect(820, 10, 131, 41))
        self.pushButton_5_import.setObjectName("pushButton_5_import")
        self.plainTextEdit_5_delete = QtWidgets.QPlainTextEdit(self.page_5)
        self.plainTextEdit_5_delete.setGeometry(QtCore.QRect(0, 130, 951, 601))
        self.plainTextEdit_5_delete.setObjectName("plainTextEdit_5_delete")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.page_5)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 60, 111, 61))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton_5_clear = QtWidgets.QPushButton(self.page_5)
        self.pushButton_5_clear.setGeometry(QtCore.QRect(0, 10, 131, 41))
        self.pushButton_5_clear.setObjectName("pushButton_5_clear")
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.pushButton_6_delete = QtWidgets.QPushButton(self.page_6)
        self.pushButton_6_delete.setGeometry(QtCore.QRect(820, 10, 131, 41))
        self.pushButton_6_delete.setObjectName("pushButton_6_delete")
        self.pushButton_6_back = QtWidgets.QPushButton(self.page_6)
        self.pushButton_6_back.setGeometry(QtCore.QRect(0, 10, 131, 41))
        self.pushButton_6_back.setObjectName("pushButton_6_back")
        self.tableWidget_6_delete = QtWidgets.QTableWidget(self.page_6)
        self.tableWidget_6_delete.setGeometry(QtCore.QRect(0, 110, 951, 611))
        self.tableWidget_6_delete.setObjectName("tableWidget_6_delete")
        self.tableWidget_6_delete.setColumnCount(6)
        self.tableWidget_6_delete.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6_delete.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6_delete.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6_delete.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6_delete.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6_delete.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6_delete.setHorizontalHeaderItem(5, item)
        self.tableWidget_6_delete.horizontalHeader().setDefaultSectionSize(158)
        self.tableWidget_6_delete.verticalHeader().setDefaultSectionSize(80)
        self.pushButton_6_check = QtWidgets.QPushButton(self.page_6)
        self.pushButton_6_check.setGeometry(QtCore.QRect(150, 10, 131, 41))
        self.pushButton_6_check.setObjectName("pushButton_6_check")
        self.stackedWidget.addWidget(self.page_6)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(5, 11, 181, 731))
        self.listWidget.setObjectName("listWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 20, 171, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 90, 171, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 160, 171, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 230, 171, 61))
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # add code below
        # left browser button
        self.pushButton.clicked.connect(self.btn1)
        self.pushButton_2.clicked.connect(self.btn2)
        self.pushButton_3.clicked.connect(self.btn3)
        self.pushButton_4.clicked.connect(self.btn4)

        # page 1
        self.pushButton_1_search.clicked.connect(self.btn_1_serarch)
        self.pushButton_1_clear.clicked.connect(self.btn_1_clear)

        # page 2
        self.pushButton_2_import.clicked.connect(self.btn_2_import)
        self.pushButton_2_clear.clicked.connect(self.btn_2_clear)

        # page 3
        self.pushButton_3_back.clicked.connect(self.btn_3_back)
        self.pushButton_3_insert.clicked.connect(self.btn_3_inert)
        self.pushButton_3_check.clicked.connect(self.btn_3_check)

        # page 4
        self.pushButton_4_search.clicked.connect(self.btn_4_search)
        self.pushButton_4_clear.clicked.connect(self.btn_4_clear)
        self.pushButton_4_update.clicked.connect(self.btn_4_update)
        self.pushButton_4_check.clicked.connect(self.btn_4_check)

        # page 5
        self.pushButton_5_clear.clicked.connect(self.btn_5_clear)
        self.pushButton_5_import.clicked.connect(self.btn_5_import)

        # page 6
        self.pushButton_6_back.clicked.connect(self.btn_6_back)
        self.pushButton_6_check.clicked.connect(self.btn_6_check)
        self.pushButton_6_delete.clicked.connect(self.btn_6_delete)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "demo"))
        self.pushButton_1_search.setText(_translate("MainWindow", "Search"))
        self.pushButton_1_clear.setText(_translate("MainWindow", "Clear"))
        item = self.tableWidget_1_search.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.tableWidget_1_search.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "name"))
        item = self.tableWidget_1_search.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "sex"))
        item = self.tableWidget_1_search.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "age"))
        item = self.tableWidget_1_search.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "image"))
        self.textBrowser_2_insert.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The format is: [id name sex age image_path], id is 6 numbers, sex 1 for male, 0 for female</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">e.g. 100001 Tom 1 18</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Only an item in a line</p></body></html>"))
        self.pushButton_2_import.setText(_translate("MainWindow", "Import"))
        self.pushButton_2_clear.setText(_translate("MainWindow", "Clear"))
        self.pushButton_3_insert.setText(_translate("MainWindow", "Insert"))
        self.pushButton_3_back.setText(_translate("MainWindow", "Back"))
        item = self.tableWidget_3_insert.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.tableWidget_3_insert.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "name"))
        item = self.tableWidget_3_insert.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "sex"))
        item = self.tableWidget_3_insert.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "age"))
        item = self.tableWidget_3_insert.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "state"))
        item = self.tableWidget_3_insert.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "image"))
        self.pushButton_3_check.setText(_translate("MainWindow", "Check"))
        self.pushButton_4_update.setText(_translate("MainWindow", "Update"))
        self.pushButton_4_search.setText(_translate("MainWindow", "Search"))
        self.label.setText(_translate("MainWindow", "id"))
        self.label_3.setText(_translate("MainWindow", "sex"))
        self.label_2.setText(_translate("MainWindow", "name"))
        self.label_4.setText(_translate("MainWindow", "age"))
        self.label_5.setText(_translate("MainWindow", "Old Data"))
        self.label_6.setText(_translate("MainWindow", "id"))
        self.label_7.setText(_translate("MainWindow", "sex"))
        self.label_8.setText(_translate("MainWindow", "name"))
        self.label_9.setText(_translate("MainWindow", "age"))
        self.label_10.setText(_translate("MainWindow", "New Data"))
        self.pushButton_4_clear.setText(_translate("MainWindow", "Clear"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Search the item by id</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Edit the new data and update</p></body></html>"))
        self.pushButton_4_check.setText(_translate("MainWindow", "Check"))
        self.label_11.setText(_translate("MainWindow", "State"))
        self.pushButton_5_import.setText(_translate("MainWindow", "Import"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Just need an id</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">An id in a line</p></body></html>"))
        self.pushButton_5_clear.setText(_translate("MainWindow", "Clear"))
        self.pushButton_6_delete.setText(_translate("MainWindow", "Delete"))
        self.pushButton_6_back.setText(_translate("MainWindow", "Back"))
        item = self.tableWidget_6_delete.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.tableWidget_6_delete.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "name"))
        item = self.tableWidget_6_delete.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "sex"))
        item = self.tableWidget_6_delete.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "age"))
        item = self.tableWidget_6_delete.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "state"))
        item = self.tableWidget_6_delete.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "image"))
        self.pushButton_6_check.setText(_translate("MainWindow", "Check"))
        self.pushButton.setText(_translate("MainWindow", "search"))
        self.pushButton_2.setText(_translate("MainWindow", "insert"))
        self.pushButton_3.setText(_translate("MainWindow", "update"))
        self.pushButton_4.setText(_translate("MainWindow", "delete"))

    # add code below
    # 检查插入的数据是否符合要求
    @staticmethod
    def check_item(item):
        id = item[0]
        name = item[1]
        sex = item[2]
        age = item[3]
        path = item[4]
        ck1 = re.match(r"\b\d{6}\b", id) # id必须为6位数字
        ck3 = re.match(r"\b[01]\b", sex) # 性别只能为0或1
        ck4 = re.match(r"\b[1-9](\d{0,1})\b", age) # 年龄只能为2位数字
        path_not_empty = re.match(r"\S+", path) # 检查图片路径是否存在
        ck5 = os.path.isfile(item[4]) # 检查是否为有效路径
        if ck1 and ck3 and ck4:
            if not path_not_empty: # path is empty
                return True
            else: # path is not empty
                if ck5: # path is valid
                    return True
                else: # path is invalid
                    return False
        return False

    # left broswer button
    def btn1(self):
        self.stackedWidget.setCurrentIndex(0)

    def btn2(self):
        self.stackedWidget.setCurrentIndex(1)

    def btn3(self):
        self.stackedWidget.setCurrentIndex(3)

    def btn4(self):
        self.stackedWidget.setCurrentIndex(4)

    # page 1
    # 使用多个信息搜索时还有错误????
    def btn_1_serarch(self):
        # 表格不可编辑
        self.tableWidget_1_search.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        # 清空原来的表格内容
        row_count = self.tableWidget_1_search.rowCount()
        for i in range(row_count):
            self.tableWidget_1_search.removeRow(0)
        # 获取文本输入框内容
        id = self.lineEdit_1_id.text()
        if not id:
            id = "$"
        name = self.lineEdit_1_name.text()
        if not name:
            name = "$"
        sex = self.lineEdit_1_sex.text()
        if not sex:
            sex = "$"
        age = self.lineEdit_1_age.text()
        if not age:
            age = "$"
        # data is list[item_str1, item_str2, ...]
        # item_str is "id name sex age"
        # item is ["id", "name", "sex", "age"]
        # 打包数据并发送
        data = []
        item_str = Protocol.item_pack(id, name, sex, age)
        data.append(item_str)
        header = Protocol.gen_default_header()
        smsg = Protocol.msg_pack("SEARCH", header, data)
        #print(smsg, end="")
        sock.send(smsg.encode("unicode_escape"))
        # 接收服务器发回的信息
        rmsg = sock.recv(1024).decode("unicode_escape")
        print(rmsg)
        rst = Protocol.msg_unpack(rmsg)
        rhead_line = rst[0]
        rheader = rst[1]
        rdata = rst[2]

        #print(rhead_line)
        #print(rheader)
        #print(rdata)
        # 根据服务器发回的信息显示查询结果
        for item_str in rdata:
            item = item_str.split()
            row_count = self.tableWidget_1_search.rowCount()
            self.tableWidget_1_search.insertRow(row_count)
            self.tableWidget_1_search.setItem(row_count, 0, QtWidgets.QTableWidgetItem(item[0]))
            self.tableWidget_1_search.setItem(row_count, 1, QtWidgets.QTableWidgetItem(item[1]))
            self.tableWidget_1_search.setItem(row_count, 2, QtWidgets.QTableWidgetItem(item[2]))
            self.tableWidget_1_search.setItem(row_count, 3, QtWidgets.QTableWidgetItem(item[3]))
            #label = myLabel(item[4])
            if item[4]=="$":
                label = QtWidgets.QLabel("")
            else:
                #label = QtWidgets.QLabel(item[4])
                file_name = item[4]
                label = QtWidgets.QLabel("")
                if os.path.isfile(file_name):
                    label.setPixmap(QtGui.QPixmap(file_name).scaled(80, 80))
            #label.setWordWrap(True)
            self.tableWidget_1_search.setCellWidget(row_count, 4, label)
    
    # 清除输入框和表格内容
    def btn_1_clear(self):
        self.lineEdit_1_id.clear()
        self.lineEdit_1_name.clear()
        self.lineEdit_1_sex.clear()
        self.lineEdit_1_age.clear()
        row_count = self.tableWidget_1_search.rowCount()
        for i in range(row_count):
            self.tableWidget_1_search.removeRow(0)

    # page 2
    def btn_2_import(self):
        # 获取文本框数据
        doc = self.plainTextEdit_2_insert.document()
        n = doc.blockCount()
        data = []
        for i in range(n):
            item_str = doc.findBlockByLineNumber(i).text()
            # 删除前后空格
            data.append(item_str.strip())

        # 导入数据前先清除原有表格内容
        row_count = self.tableWidget_3_insert.rowCount()
        for i in range(row_count):
            self.tableWidget_3_insert.removeRow(0)
        # 在表格内显示数据
        if len(data):
            # 切换到下一页
            self.stackedWidget.setCurrentIndex(2)
            for item_str in data:
                item = item_str.split()
                if len(item)<5:
                    for i in range(5-len(item)):
                        item.append(" ")
                #print(item)
                row_count = self.tableWidget_3_insert.rowCount()
                self.tableWidget_3_insert.insertRow(row_count)
                self.tableWidget_3_insert.setItem(row_count, 0, QtWidgets.QTableWidgetItem(item[0]))
                self.tableWidget_3_insert.setItem(row_count, 1, QtWidgets.QTableWidgetItem(item[1]))
                self.tableWidget_3_insert.setItem(row_count, 2, QtWidgets.QTableWidgetItem(item[2]))
                self.tableWidget_3_insert.setItem(row_count, 3, QtWidgets.QTableWidgetItem(item[3]))
                label = myLabel(item[4])
                label.setWordWrap(True)
                self.tableWidget_3_insert.setCellWidget(row_count, 5, label)
                if self.check_item(item):
                    self.tableWidget_3_insert.setItem(row_count, 4, QtWidgets.QTableWidgetItem("Ready"))
                else:
                    self.tableWidget_3_insert.setItem(row_count, 4, QtWidgets.QTableWidgetItem("Error"))
                
    def btn_2_clear(self):
        self.plainTextEdit_2_insert.clear()

    # page 3
    def btn_3_back(self):
        self.stackedWidget.setCurrentIndex(1)

    def btn_3_inert(self):
        data = []
        image = {}
        id_line = {}
        row_count = self.tableWidget_3_insert.rowCount()
        # 获取当前表格内的数据
        for i in range(row_count):
            id = self.tableWidget_3_insert.item(i, 0).text()
            name = self.tableWidget_3_insert.item(i, 1).text()
            sex = self.tableWidget_3_insert.item(i, 2).text()
            age = self.tableWidget_3_insert.item(i, 3).text()
            label = self.tableWidget_3_insert.cellWidget(i, 5)
            # 发送前再次检查数据
            path = ""
            if label:
                path = label.file_name
            # 如果数据还是不符合规范，则此条目不会发送给服务器
            if not self.check_item([id, name, sex, age, path]):
                self.tableWidget_3_insert.setItem(i, 4, QtWidgets.QTableWidgetItem("Error"))
                continue
            item_str = Protocol.item_pack(id, name, sex, age)
            image[id] = path
            # 出错条目的id不会出现在image和id_line中，也不会发送图片
            id_line[id] = i
            data.append(item_str)
        # 发送数据
        header = Protocol.gen_default_header()
        smsg = Protocol.msg_pack("INSERT", header, data)
        sock.send(smsg.encode("unicode_escape"))
        
        #print(image)
        # 接收服务器发回的信息
        rmsg = sock.recv(1024).decode("unicode_escape")
        print(rmsg)
        rst = Protocol.msg_unpack(rmsg)
        rhear_line = rst[0]
        rheader = rst[1]
        rdata = rst[2]
        # 根据收到的服务器信息更新已发送条目的状态
        for id in id_line:
            self.tableWidget_3_insert.setItem(id_line[id], 4, QtWidgets.QTableWidgetItem(rheader[id]))
        
        # 发送图片数据，每次发送一张图片，未通过检查的条目不会发送图片数据
        #print(rheader)
        for id in id_line:
            # 已发送但服务器处理失败的条目不会发送图片
            if rheader[id]=="FAIL":
                continue
            path = image[id]
            # 路径不存在则不会发送图片
            if not os.path.isfile(path):
                continue
            fp = open(path, 'rb')
            file_name = os.path.basename(path)
            file_size = os.stat(path).st_size
            # 发送一个预处理信息，包含一些图片的基本信息
            header = Protocol.gen_default_header()
            header.update({"Image": id, "FileName": file_name, "FileSize": file_size})
            smsg = Protocol.msg_pack("IMAGE", header, [])
            sock.send(smsg.encode("unicode_escape"))
            # 接收服务器发回的预处理信息回复
            rmsg = sock.recv(1024).decode("unicode_escape")
            print(rmsg)
            img_rst = Protocol.msg_unpack(rmsg)
            img_rhear_line = img_rst[0]
            img_rheader = img_rst[1]
            #rdata = img_rst[2]
            info = "Image_" + id
            # 得到服务器许可后开始发送图片数据
            if img_rheader[info] and img_rheader[info]=="READY":
            #tmp = open("./" + file_name, "wb")
                path = img_rheader["Path"]
                while True:
                    img_data = fp.read(1024)
                    if not img_data:
                        print (file_name, " file send over...")
                        #tmp.write(data)
                        break
                    #data = struct.pack("64s", path.encode("unicode_escape")) + img_data
                    # 直接发送1024 bytes的二进制原始图片数据，不需要编码，不含头部信息
                    sock.send(img_data)
                # 发送图片结束，等待服务器发送回复信息
                #tmp.close()
                rmsg = sock.recv(1024).decode("unicode_escape")
                print(rmsg)
                img_rst = Protocol.msg_unpack(rmsg)
                img_rhear_line = img_rst[0]
                img_rheader = img_rst[1]
                # 更新发送图片的状态信息
                label = self.tableWidget_3_insert.cellWidget(id_line[id], 5)
                if img_rheader[info] and img_rheader[info]=="SUCCESS":
                    label.setText("SUCCESS")
                else:
                    label.setText("FAIL")
                # rdata = rst[2]
    
    # 检查表格的数据是否合法
    def btn_3_check(self):
        row_count = self.tableWidget_3_insert.rowCount()
        for i in range(row_count):
            id = self.tableWidget_3_insert.item(i, 0).text()
            name = self.tableWidget_3_insert.item(i, 1).text()
            sex = self.tableWidget_3_insert.item(i, 2).text()
            age = self.tableWidget_3_insert.item(i, 3).text()
            label = self.tableWidget_3_insert.cellWidget(i, 5)
            file_name = ""
            if label:
                file_name = label.file_name
            if self.check_item([id, name, sex, age, file_name]):
                self.tableWidget_3_insert.setItem(i, 4, QtWidgets.QTableWidgetItem("Ready"))
            else:
                self.tableWidget_3_insert.setItem(i, 4, QtWidgets.QTableWidgetItem("Error"))

    # page 4
    def btn_4_clear(self):
        self.lineEdit_4_old_id.clear()
        self.lineEdit_4_old_name.clear()
        self.lineEdit_4_old_sex.clear()
        self.lineEdit_4_old_age.clear()
        self.lineEdit_4_new_id.clear()
        self.lineEdit_4_new_name.clear()
        self.lineEdit_4_new_sex.clear()
        self.lineEdit_4_new_age.clear()
        self.lineEdit_4_state.clear()

    # 更新前先使用id查询当前条目信息，实现方法同之前的search
    def btn_4_search(self):
        id = self.lineEdit_4_old_id.text()
        if not id:
            id = "$"
        name = "$"
        sex = "$"
        age = "$"
        data = []
        item_str = Protocol.item_pack(id, name, sex, age)
        data.append(item_str)
        header = Protocol.gen_default_header()
        smsg = Protocol.msg_pack("SEARCH", header, data)
        #print(smsg, end="")
        sock.send(smsg.encode("unicode_escape"))

        rmsg = sock.recv(1024).decode("unicode_escape")
        print(rmsg)
        rst = Protocol.msg_unpack(rmsg)
        rhead_line = rst[0]
        rheader = rst[1]
        rdata = rst[2]
        #item_str = rdata[0]

        if len(rdata)>0:
            item_str = rdata[0]
            item = item_str.split()
            self.lineEdit_4_old_id.setText(item[0])
            self.lineEdit_4_old_name.setText(item[1])
            self.lineEdit_4_old_sex.setText(item[2])
            self.lineEdit_4_old_age.setText(item[3])
            self.lineEdit_4_new_id.setText(item[0])
            self.lineEdit_4_new_name.setText(item[1])
            self.lineEdit_4_new_sex.setText(item[2])
            self.lineEdit_4_new_age.setText(item[3])
    # 更新条目信息
    def btn_4_update(self):
        # 获取文本框内容
        id = self.lineEdit_4_new_id.text()
        if not id:
            id = "$"
        name = self.lineEdit_4_new_name.text()
        if not name:
            name = "$"
        sex = self.lineEdit_4_new_sex.text()
        if not sex:
            sex = "$"
        age = self.lineEdit_4_new_age.text()
        if not age:
            age = "$"
        # 检查数据是否符合规范
        if self.check_item([id, name, sex, age, ""]):
            # 发送更新的条目信息
            data = []
            item_str = Protocol.item_pack(id, name, sex, age)
            data.append(item_str)
            header = Protocol.gen_default_header()
            smsg = Protocol.msg_pack("UPDATE", header, data)
            #print(smsg, end="")
            sock.send(smsg.encode("unicode_escape"))
            # 接收服务器发回的信息
            rmsg = sock.recv(1024).decode("unicode_escape")
            print(rmsg)
            rst = Protocol.msg_unpack(rmsg)
            rhead_line = rst[0]
            rheader = rst[1]
            rdata = rst[2]
            self.lineEdit_4_state.setText(rheader[id])
        else:
            self.lineEdit_4_state.setText("Error")

    # 检查修改后的信息是否合法
    def btn_4_check(self):
        id = self.lineEdit_4_new_id.text()
        name = self.lineEdit_4_new_name.text()
        sex = self.lineEdit_4_new_sex.text()
        age = self.lineEdit_4_new_age.text()
        if self.check_item([id, name, sex, age, ""]):
            self.lineEdit_4_state.setText("Ready")
        else:
            self.lineEdit_4_state.setText("Error")

    # page 5
    def btn_5_clear(self):
        self.plainTextEdit_5_delete.clear()
    
    # 和之前insert的导入数据功能相同
    def btn_5_import(self):
        doc = self.plainTextEdit_5_delete.document()
        n = doc.blockCount()
        data = []
        for i in range(n):
            item_str = doc.findBlockByLineNumber(i).text()
            # 删除前后空格
            data.append(item_str.strip())

        # 导入前先请求原有表格内容
        row_count = self.tableWidget_6_delete.rowCount()
        for i in range(row_count):
            self.tableWidget_6_delete.removeRow(0)

        if len(data):
            self.stackedWidget.setCurrentIndex(5)
            for item_str in data:
                item = item_str.split()
                if len(item)<4:
                    for i in range(4-len(item)):
                        item.append(" ")
                #print(item)
                row_count = self.tableWidget_6_delete.rowCount()
                self.tableWidget_6_delete.insertRow(row_count)
                self.tableWidget_6_delete.setItem(row_count, 0, QtWidgets.QTableWidgetItem(item[0]))
                self.tableWidget_6_delete.setItem(row_count, 1, QtWidgets.QTableWidgetItem(item[1]))
                self.tableWidget_6_delete.setItem(row_count, 2, QtWidgets.QTableWidgetItem(item[2]))
                self.tableWidget_6_delete.setItem(row_count, 3, QtWidgets.QTableWidgetItem(item[3]))
                # 删除只需要id符合规范即可，服务器处理时也只用id检索删除，忽略其他信息
                if re.match(r"\b\d{6}\b", item[0]):
                    self.tableWidget_6_delete.setItem(row_count, 4, QtWidgets.QTableWidgetItem("Ready"))
                else:
                    self.tableWidget_6_delete.setItem(row_count, 4, QtWidgets.QTableWidgetItem("Error"))

    # page 6
    def btn_6_back(self):
        self.stackedWidget.setCurrentIndex(4)

    # 删除只需要对id进行检查即可
    def btn_6_check(self):
        row_count = self.tableWidget_6_delete.rowCount()
        for i in range(row_count):
            id = self.tableWidget_6_delete.item(i, 0).text()
            #name = self.tableWidget_6_delete.item(i, 1).text()
            #sex = self.tableWidget_6_delete.item(i, 2).text()
            #age = self.tableWidget_6_delete.item(i, 3).text()
            if re.match(r"\b\d{6}\b", id):
                self.tableWidget_6_delete.setItem(i, 4, QtWidgets.QTableWidgetItem("Ready"))
            else:
                self.tableWidget_6_delete.setItem(i, 4, QtWidgets.QTableWidgetItem("Error"))

    def btn_6_delete(self):
        data = []
        id_line = {}
        row_count = self.tableWidget_6_delete.rowCount()
        for i in range(row_count):
            id = self.tableWidget_6_delete.item(i, 0).text()
            # 不需要发送其他信息，因为服务器只用id检索条目进行删除
            if not id:
                id = "$"
            name = "$"
            sex = "$"
            age = "$"
            #name = self.tableWidget_6_delete.item(i, 1).text()
            #sex = self.tableWidget_6_delete.item(i, 2).text()
            #age = self.tableWidget_6_delete.item(i, 3).text()
            if not re.match(r"\b\d{6}\b", id):
                self.tableWidget_6_delete.setItem(i, 4, QtWidgets.QTableWidgetItem("Error"))
                continue
            item_str = Protocol.item_pack(id, name, sex, age)
            id_line[id] = i
            data.append(item_str)
        # 发送信息
        header = Protocol.gen_default_header()
        smsg = Protocol.msg_pack("DELETE", header, data)
        sock.send(smsg.encode("unicode_escape"))
        # 接收服务器发回的信息
        rmsg = sock.recv(1024).decode("unicode_escape")
        print(rmsg)
        rst = Protocol.msg_unpack(rmsg)
        rhear_line = rst[0]
        rheader = rst[1]
        rdata = rst[2]
        for id in id_line:
            self.tableWidget_6_delete.setItem(id_line[id], 4, QtWidgets.QTableWidgetItem(rheader[id]))

# main
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mw = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mw)
    mw.show()
    sys.exit(app.exec_())