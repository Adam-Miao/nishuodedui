# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from json import load, dumps
from api import rightGen



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(71, 40, 651, 521))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_2.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_2.addWidget(self.lineEdit_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_2.addWidget(self.lineEdit_5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_3.addWidget(self.lineEdit_6)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_3.addWidget(self.lineEdit_7)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_3.addWidget(self.lineEdit_8)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.horizontalLayout_3.addWidget(self.lineEdit_9)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.horizontalLayout_4.addWidget(self.lineEdit_10)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.horizontalLayout_4.addWidget(self.lineEdit_11)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.horizontalLayout_4.addWidget(self.lineEdit_12)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.horizontalLayout_4.addWidget(self.lineEdit_13)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.horizontalLayout_5.addWidget(self.lineEdit_17)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.horizontalLayout_5.addWidget(self.lineEdit_15)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_5.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.textBrowser = QtWidgets.QTextBrowser(self.layoutWidget)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.i)
        self.pushButton_2.clicked.connect(self.s)
        self.pushButton_3.clicked.connect(self.gen)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle('"You\'re right" Generator')
        self.label.setText(_translate("MainWindow", "Template Name:"))
        self.pushButton.setText(_translate("MainWindow", "Import"))
        self.pushButton_2.setText(_translate("MainWindow", "Save"))
        self.pushButton_3.setText(_translate("MainWindow", "Generate"))


    def s_t(self, nme):
        return {
            "NAME": nme,
            'game': self.lineEdit_2.text(),
            'author': self.lineEdit_3.text(),
            'kind': self.lineEdit_4.text(),
            'world': self.lineEdit_5.text(),
            'selector': self.lineEdit_6.text(),
            'whom': self.lineEdit_7.text(),
            'award': self.lineEdit_8.text(),
            'power': self.lineEdit_9.text(),
            'player': self.lineEdit_10.text(),
            'colleague': self.lineEdit_11.text(),
            'friend': self.lineEdit_12.text(),
            'enemy': self.lineEdit_13.text(),
            'lost': self.lineEdit_17.text(),
            'truth': self.lineEdit_15.text()
        }

    def l_t(self, js):
        default = {
            'game': '',
            'author': '',
            'kind': '',
            'world': '',
            'selector': '',
            'whom': '',
            'award': '',
            'power': '',
            'player': '',
            'colleague': '',
            'friend': '',
            'enemy': '',
            'lost': '',
            'truth': ''
        }
        default.update(js)
        self.lineEdit_2.setText(default['game'])
        self.lineEdit_3.setText(default['author'])
        self.lineEdit_4.setText(default['kind'])
        self.lineEdit_5.setText(default['world'])
        self.lineEdit_6.setText(default['selector'])
        self.lineEdit_7.setText(default['whom'])
        self.lineEdit_8.setText(default['award'])
        self.lineEdit_9.setText(default['power'])
        self.lineEdit_10.setText(default['player'])
        self.lineEdit_11.setText(default['colleague'])
        self.lineEdit_12.setText(default['friend'])
        self.lineEdit_13.setText(default['enemy'])
        self.lineEdit_17.setText(default['lost'])
        self.lineEdit_15.setText(default['truth'])

    def i(self):
        x = load(open("templates/count.json"))
        title = self.lineEdit.text()
        try:
            fn = x[title]["Filename"]
            k = load(open("templates/" + fn))
            self.l_t(k)

        except KeyError:
            QtWidgets.QMessageBox.information(None, "Error", "Template not found or invalid",
                                              QtWidgets.QMessageBox.Yes)
        except FileNotFoundError:
            QtWidgets.QMessageBox.information(None, "Error", "Template deleted",
                                              QtWidgets.QMessageBox.Yes)

    def s(self):
        x = load(open("templates/count.json"))
        title = self.lineEdit.text()
        try:
            fn = x[title]["Filename"]
            print("Exist.")
            a = QtWidgets.QMessageBox.question(None, "", "Template exists. Cover?",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if a == QtWidgets.QMessageBox.Yes:
                with open("templates/" + fn, "w") as file:
                    file.write(dumps(self.s_t(title)))
        except KeyError:
            print("WRI")
            with open("templates/count.json", "w") as file:
                x[title] = {"Filename": title + ".json"}
                file.write(dumps(x))
            with open("templates/" + title + ".json", "w") as file:
                file.write(dumps(self.s_t(title)))

    def gen(self):
        a = self.s_t("")
        del a["NAME"]
        self.textBrowser.setText(rightGen(a))


from PyQt5.QtWidgets import QApplication, QMainWindow

app = QApplication([])
w = QMainWindow()
wd = Ui_MainWindow()
wd.setupUi(w)
w.show()
app.exec_()
