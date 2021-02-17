

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog
import os
import re

global ScriptLoc
ScriptLoc = "/usr/lib/EmpowerSoc"
global DictPulse
DictPulse = {}
global StandbyValues
StandbyValues = {}
global StandbyCapacitance
StandbyCapacitance = {}
global CapacitanceValue
CapacitanceValue = {}
global TextFieldsMap
TextFieldsMap = {}
global TimeValues
TimeValues = {}
global StandbyTimeValues
StandbyTimeValues = {}
global PulseParameters
PulseParameters = ['Initial_Value','Pulsed_Value','Delay', 'Rise_Time', 'Fall_Time', 'Pulse_Width', 'Period']
global OutputText
global ProjectName
global inputArr
global outputArr
global moduleName
inputArr =[]
outputArr =[]
global DictDCValues
DictDCValues = {}
global filenames
filenames = []
global filenames1
filenames1 = []


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(936, 778)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_7)
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_8)
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_9)
        self.formLayout_5 = QtWidgets.QFormLayout()
        self.formLayout_5.setObjectName("formLayout_5")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab)
        self.pushButton_5.setStyleSheet("background-color: rgb(245, 121, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pushButton_5)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_5.setItem(0, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_10.setEnabled(True)
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_10)
        self.formLayout_2.setLayout(5, QtWidgets.QFormLayout.SpanningRole, self.formLayout_5)
        self.gridLayout_3.addLayout(self.formLayout_2, 1, 2, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        self.radioButton = QtWidgets.QRadioButton(self.tab)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.tab)
        self.radioButton_2.setObjectName("radioButton_2")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.radioButton_2)
        self.label_19 = QtWidgets.QLabel(self.tab)
        self.label_19.setObjectName("label_19")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setStyleSheet("background-color: rgb(245, 121, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.pushButton_3)
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_61 = QtWidgets.QLabel(self.tab)
        self.label_61.setObjectName("label_61")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_61)
        self.lineEdit_61 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_61.setText("")
        self.lineEdit_61.setObjectName("lineEdit_61")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_61)
        self.label_62 = QtWidgets.QLabel(self.tab)
        self.label_62.setObjectName("label_62")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_62)
        self.lineEdit_62 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_62.setText("")
        self.lineEdit_62.setObjectName("lineEdit_62")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_62)
        self.pushButton_21 = QtWidgets.QPushButton(self.tab)
        self.pushButton_21.setStyleSheet("background-color: rgb(245, 121, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.pushButton_21.setObjectName("pushButton_21")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.pushButton_21)
        self.gridLayout_4.addLayout(self.formLayout, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_4)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 2, 1)
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_3.addWidget(self.line, 0, 1, 2, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setStyleSheet("background-color: rgb(245, 121, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_3.addWidget(self.pushButton_2, 9, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setStyleSheet("background-color: rgb(245, 121, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 9, 2, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab)
        self.comboBox_2.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.verticalLayout_2.addWidget(self.comboBox_2)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setObjectName("label_11")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_12)
        self.pushButton_4 = QtWidgets.QPushButton(self.tab)
        self.pushButton_4.setStyleSheet("background-color: rgb(245, 121, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.pushButton_4)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_3.setItem(4, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        self.gridLayout_5.addLayout(self.formLayout_3, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_5)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 2, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_3.addWidget(self.textBrowser, 7, 0, 2, 3)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.comboBox_14 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_14.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.comboBox_14.setObjectName("comboBox_14")
        self.verticalLayout_14.addWidget(self.comboBox_14)
        self.gridLayout_22 = QtWidgets.QGridLayout()
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.formLayout_20 = QtWidgets.QFormLayout()
        self.formLayout_20.setObjectName("formLayout_20")
        self.label_65 = QtWidgets.QLabel(self.tab_2)
        self.label_65.setObjectName("label_65")
        self.formLayout_20.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_65)
        self.lineEdit_65 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_65.setObjectName("lineEdit_65")
        self.formLayout_20.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_65)
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_10.setStyleSheet("background-color: rgb(245, 121, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.formLayout_20.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.pushButton_10)
        self.gridLayout_22.addLayout(self.formLayout_20, 0, 0, 1, 1)
        self.verticalLayout_14.addLayout(self.gridLayout_22)
        self.gridLayout_20.addLayout(self.verticalLayout_14, 0, 2, 1, 1)
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.gridLayout_20.addWidget(self.textBrowser_3, 3, 0, 1, 3)
        self.line_2 = QtWidgets.QFrame(self.tab_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_20.addWidget(self.line_2, 0, 1, 2, 1)
        self.pushButton_19 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_19.setStyleSheet("background-color: rgb(245, 121, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"")
        self.pushButton_19.setObjectName("pushButton_19")
        self.gridLayout_20.addWidget(self.pushButton_19, 4, 0, 1, 1)
        self.pushButton_20 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_20.setStyleSheet("background-color: rgb(245, 121, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.pushButton_20.setObjectName("pushButton_20")
        self.gridLayout_20.addWidget(self.pushButton_20, 4, 2, 1, 1)
        self.formLayout_21 = QtWidgets.QFormLayout()
        self.formLayout_21.setObjectName("formLayout_21")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_21.setItem(0, QtWidgets.QFormLayout.FieldRole, spacerItem2)
        self.label_68 = QtWidgets.QLabel(self.tab_2)
        self.label_68.setObjectName("label_68")
        self.formLayout_21.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_68)
        self.lineEdit_66 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_66.setObjectName("lineEdit_66")
        self.formLayout_21.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_66)
        self.label_66 = QtWidgets.QLabel(self.tab_2)
        self.label_66.setObjectName("label_66")
        self.formLayout_21.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_66)
        self.lineEdit_67 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_67.setObjectName("lineEdit_67")
        self.formLayout_21.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_67)
        self.label_67 = QtWidgets.QLabel(self.tab_2)
        self.label_67.setObjectName("label_67")
        self.formLayout_21.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_67)
        self.lineEdit_68 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_68.setObjectName("lineEdit_68")
        self.formLayout_21.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_68)
        self.formLayout_8 = QtWidgets.QFormLayout()
        self.formLayout_8.setObjectName("formLayout_8")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setStyleSheet("background-color: rgb(245, 121, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.formLayout_8.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pushButton_6)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_8.setItem(0, QtWidgets.QFormLayout.FieldRole, spacerItem3)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_11.setEnabled(True)
        self.lineEdit_11.setReadOnly(True)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.formLayout_8.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_11)
        self.formLayout_21.setLayout(6, QtWidgets.QFormLayout.SpanningRole, self.formLayout_8)
        self.gridLayout_20.addLayout(self.formLayout_21, 1, 2, 1, 1)
        self.gridLayout_13 = QtWidgets.QGridLayout()
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.comboBox_13 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_13.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.comboBox_13.setObjectName("comboBox_13")

        inputArr,outputArr = self.getInputOutput()
        moduleName = self.getModuleName()

        for i in inputArr:
            self.comboBox_13.addItem(i)
        for i in inputArr:
            self.comboBox.addItem(i)
        for i in outputArr:
            self.comboBox_2.addItem(i)
        for i in outputArr:
            self.comboBox_14.addItem(i)

        self.verticalLayout_13.addWidget(self.comboBox_13)
        self.gridLayout_21 = QtWidgets.QGridLayout()
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.formLayout_19 = QtWidgets.QFormLayout()
        self.formLayout_19.setObjectName("formLayout_19")
        self.label_60 = QtWidgets.QLabel(self.tab_2)
        self.label_60.setObjectName("label_60")
        self.formLayout_19.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_60)
        self.lineEdit_60 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_60.setObjectName("lineEdit_60")
        self.formLayout_19.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_60)
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_9.setStyleSheet("background-color: rgb(245, 121, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.formLayout_19.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.pushButton_9)
        self.gridLayout_21.addLayout(self.formLayout_19, 0, 0, 1, 1)
        self.verticalLayout_13.addLayout(self.gridLayout_21)
        self.gridLayout_13.addLayout(self.verticalLayout_13, 0, 1, 1, 1)
        self.gridLayout_20.addLayout(self.gridLayout_13, 0, 0, 2, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_6.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 936, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_Project = QtWidgets.QAction(MainWindow)
        self.actionOpen_Project.setObjectName("actionOpen_Project")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionDocumentation = QtWidgets.QAction(MainWindow)
        self.actionDocumentation.setObjectName("actionDocumentation")

        self.menuFile.addAction(self.actionOpen_Project)

        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuHelp.addSeparator()
        TextFieldsMap['Initial_Value'] = self.lineEdit_61
        TextFieldsMap['Pulsed_Value'] = self.lineEdit_62
        TextFieldsMap['Delay'] = self.lineEdit_2
        TextFieldsMap['Rise_Time'] = self.lineEdit_5
        TextFieldsMap['Fall_Time'] = self.lineEdit_4
        TextFieldsMap['Pulse_Width'] = self.lineEdit_3
        TextFieldsMap['Period'] = self.lineEdit_6
        TextFieldsMap['Value'] = self.lineEdit_12


        self.menuHelp.addAction(self.actionDocumentation)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        
        if self.radioButton.isChecked() == True :
            self.lineEdit.setEnabled(False)
            self.pushButton_3.setEnabled(False)



        self.connectFunctions()

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        moduleName = self.getModuleName()
        MainWindow.setWindowTitle(_translate("MainWindow", "EmpowerSOC : " + moduleName))
        self.label_6.setText(_translate("MainWindow", "Supply Value [V]"))
        self.label_9.setText(_translate("MainWindow", "Stop Time"))
        self.label_7.setText(_translate("MainWindow", "Time Step Size"))
        self.pushButton_5.setText(_translate("MainWindow", "Add Model file"))
        self.label.setText(_translate("MainWindow", "Delay"))
        self.label_3.setText(_translate("MainWindow", "Rise Time"))
        self.label_4.setText(_translate("MainWindow", "Fall Time"))
        self.label_2.setText(_translate("MainWindow", "Pulse Width"))
        self.label_5.setText(_translate("MainWindow", "Period"))
        self.radioButton.setText(_translate("MainWindow", "Pulse"))
        self.radioButton_2.setText(_translate("MainWindow", "DC Input"))
        self.label_19.setText(_translate("MainWindow", "Value [V]"))
        self.pushButton_3.setText(_translate("MainWindow", "Add Input"))
        self.label_61.setText(_translate("MainWindow", "Initial Value [V]"))
        self.label_62.setText(_translate("MainWindow", "Pulsed Value "))
        self.pushButton_21.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Add Input Pulse to the selected node</p></body></html>"))
        self.pushButton_21.setText(_translate("MainWindow", "Add Pulse"))
        self.pushButton_2.setText(_translate("MainWindow", "Review Simulation Paramenters"))
        self.pushButton.setText(_translate("MainWindow", "Run Simulation"))
        self.label_11.setText(_translate("MainWindow", "Value"))
        self.pushButton_4.setText(_translate("MainWindow", "Add Load"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Active Power Consumption"))
        self.label_65.setText(_translate("MainWindow", "Value"))
        self.pushButton_10.setText(_translate("MainWindow", "Add Load"))
        self.pushButton_19.setText(_translate("MainWindow", "Review Simulation Paramenters"))
        self.pushButton_20.setText(_translate("MainWindow", "Run Simulation"))
        self.label_68.setText(_translate("MainWindow", "Supply Value (V)"))
        self.label_66.setText(_translate("MainWindow", "Stop Time"))
        self.label_67.setText(_translate("MainWindow", "Time Step Value"))
        self.pushButton_6.setText(_translate("MainWindow", "Add Model file"))
        self.label_60.setText(_translate("MainWindow", "DC Value (V)"))
        self.pushButton_9.setText(_translate("MainWindow", "Add Input"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Standby Power Consumption"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen_Project.setText(_translate("MainWindow", "Open Project"))
        self.actionSave.setText(_translate("MainWindow", "Save Project"))
        self.actionDocumentation.setText(_translate("MainWindow", "Documentation"))


        ### CALLBACKS ###

    def connectFunctions(self):
        self.radioButton.toggled.connect(self.PulseRadioButtonToggled)
        self.radioButton_2.toggled.connect(self.PulseRadioButtonToggled)
        self.comboBox.currentIndexChanged.connect(self.inputSelectionChange)
        self.pushButton_21.clicked.connect(self.setValues)
        self.pushButton_4.clicked.connect(self.setCapacitanceValues)
        self.pushButton_2.clicked.connect(self.setTimeValues)
        self.pushButton.clicked.connect(self.saveFile)
        self.comboBox_2.currentIndexChanged.connect(self.inputCapacitanceSelectionChange)
        self.comboBox_13.currentIndexChanged.connect(self.inputSelectionChangeStandby)
        self.pushButton_9.clicked.connect(self.standbySetValues)
        self.pushButton_10.clicked.connect(self.setStandbyCapacitanceValues)
        self.pushButton_19.clicked.connect(self.setStandbyTimeValues)
        self.pushButton_3.clicked.connect(self.setDCValues)
        self.comboBox_14.currentIndexChanged.connect(self.standbyCapacitanceChange)
        self.pushButton_20.clicked.connect(self.saveStandbyFile)
        self.pushButton_6.clicked.connect(self.getModelFileStandby)
        self.pushButton_5.clicked.connect(self.getModelFile)
        self.actionOpen_Project.triggered.connect(self.openFiles)

    def getModelFile(self):
        #print("Hello")
        dlg = QtWidgets.QFileDialog()
        dlg.setFileMode(QtWidgets.QFileDialog().AnyFile)

        if dlg.exec_():
            filenames = dlg.selectedFiles()
            #f = open(filenames[0], 'r')
            self.lineEdit_10.setText(filenames[0])

    def getModelFileStandby(self):
        #print("OK")
        dlg = QtWidgets.QFileDialog()
        dlg.setFileMode(QtWidgets.QFileDialog().AnyFile)
        filenames1 = []
        if dlg.exec_():
            filenames1 = dlg.selectedFiles()
            #f = open(filenames[0], 'r')
            self.lineEdit_11.setText(filenames1[0])

    def PulseRadioButtonToggled(self):
        if self.radioButton.isChecked() == True:
            self.lineEdit.setEnabled(False)
            self.pushButton_3.setEnabled(False)
            self.lineEdit_61.setEnabled(True)
            self.lineEdit_62.setEnabled(True)
            self.lineEdit_2.setEnabled(True)
            self.lineEdit_3.setEnabled(True)
            self.lineEdit_4.setEnabled(True)
            self.lineEdit_6.setEnabled(True)
            self.lineEdit_5.setEnabled(True)
            self.pushButton_21.setEnabled(True)
        if self.radioButton_2.isChecked() == True:
            self.lineEdit.setEnabled(True)
            self.pushButton_3.setEnabled(True)
            self.lineEdit_61.setEnabled(False)
            self.lineEdit_62.setEnabled(False)
            self.lineEdit_2.setEnabled(False)
            self.lineEdit_3.setEnabled(False)
            self.lineEdit_4.setEnabled(False)
            self.lineEdit_6.setEnabled(False)
            self.lineEdit_5.setEnabled(False)
            self.pushButton_21.setEnabled(False)

    def inputSelectionChange(self):

        currentInput = self.comboBox.currentText()

        res = not DictPulse
        #print(res)
        # if(res == False):
        inputKeys = DictPulse.keys()
        if currentInput in inputKeys:
            valueKeys = DictPulse[currentInput].keys()
            for i in valueKeys:
                # print(TextFieldsMap.get(i))
                TextFieldsMap.get(i).setText(DictPulse[currentInput].get(i))
        else:
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
            self.lineEdit_4.clear()
            self.lineEdit_5.clear()
            self.lineEdit_6.clear()
            self.lineEdit_62.clear()
            self.lineEdit_61.clear()

        if currentInput in DictDCValues.keys():
            self.lineEdit.setText(DictDCValues.get(currentInput))
        else:
            self.lineEdit.clear()


    def inputSelectionChangeStandby(self):

        currentInput = self.comboBox_13.currentText()
        
        if currentInput not in StandbyValues.keys():
            self.lineEdit_60.clear()
        else :
            self.lineEdit_60.setText(StandbyValues.get(currentInput))


    def inputCapacitanceSelectionChange(self):
        currentCapacitance = self.comboBox_2.currentText()
        #print(currentCapacitance)

        inputKeys = CapacitanceValue.keys()
        if currentCapacitance in inputKeys:
            capacitanceKeys = CapacitanceValue[currentCapacitance].keys()
            for i in capacitanceKeys:
                TextFieldsMap.get(i).setText(CapacitanceValue[currentCapacitance].get(i))

        else:
            self.lineEdit_12.setText("")

    def standbyCapacitanceChange(self):
        #print("hello")
        currentCapacitance1 = self.comboBox_14.currentText()
        #print(currentCapacitance1)

        inputKeys = StandbyCapacitance.keys()
        if currentCapacitance1 in inputKeys:
            self.lineEdit_65.setText(StandbyCapacitance[currentCapacitance1].get('Value'))


        else:
            self.lineEdit_65.clear()

    def setValues(self):

        currentInput = self.comboBox.currentText()
        delayText = self.label.text()
        delayValue = self.lineEdit_2.text()
        risetimeText = self.label_3.text()
        risetimeValue = self.lineEdit_5.text()
        falltimeText = self.label_4.text()
        falltimeValue = self.lineEdit_5.text()
        pulsewidthText = self.label_2.text()
        pulsewidthValue = self.lineEdit_3.text()
        periodText = self.label_5.text()
        periodValue = self.lineEdit_6.text()
        initialValue = self.lineEdit_61.text()
        pulsedValue= self.lineEdit_62.text()
        pattern2 = '^\d+(\.(\d+))?[dcmunpfazy]'
        pattern1 = '^\d+(\.(\d+))?$'
        res1 = re.match(pattern2,delayValue)
        res2 = re.match(pattern2,risetimeValue)
        res3 = re.match(pattern2,falltimeValue)
        res4 = re.match(pattern2,pulsewidthValue)
        res5 = re.match(pattern1,pulsedValue)
        res6 = re.match(pattern1,initialValue)
        res7 = re.match(pattern2,periodValue)
        if not res1 or not res2 or not res3 or not res4 or not res7:
            msg1 = QtWidgets.QMessageBox()
            msg1.setIcon(QtWidgets.QMessageBox.Critical)
            msg1.setText('Check entered parameters!')
            msg1.setWindowTitle("Error")
            msg1.exec_()
        elif initialValue and not res6 :
            msg1 = QtWidgets.QMessageBox()
            msg1.setIcon(QtWidgets.QMessageBox.Critical)
            msg1.setText('Check entered parameters!')
            msg1.setWindowTitle("Error")
            msg1.exec_()
        elif pulsedValue and not res5 :
            msg1 = QtWidgets.QMessageBox()
            msg1.setIcon(QtWidgets.QMessageBox.Critical)
            msg1.setText('Check entered parameters!')
            msg1.setWindowTitle("Error")
            msg1.exec_()

        else :
            if currentInput in DictDCValues.keys():
                del DictDCValues[currentInput]
            DictPulse[currentInput] = {}
            DictPulse[currentInput].update({'Initial_Value': initialValue})
            DictPulse[currentInput].update({'Pulsed_Value': pulsedValue})
            DictPulse[currentInput].update({'Delay': delayValue})
            DictPulse[currentInput].update({'Rise_Time': risetimeValue})
            DictPulse[currentInput].update({'Fall_Time': falltimeValue})
            DictPulse[currentInput].update({'Pulse_Width': pulsewidthValue})
            DictPulse[currentInput].update({'Period': periodValue})

    def setDCValues(self):

        currentInput = self.comboBox.currentText()
        if currentInput in DictPulse.keys():
            res = not DictPulse[currentInput]
            if res == False :
                DictPulse[currentInput].clear()
                del DictPulse[currentInput]

        value = self.lineEdit.text()
        pattern1 = '^\d+(\.(\d+))?$'
        res1 = re.match(pattern1, value)
        if not res1:
            msg1 = QtWidgets.QMessageBox()
            msg1.setIcon(QtWidgets.QMessageBox.Critical)
            msg1.setText('Check entered parameters!')
            msg1.setWindowTitle("Error")
            msg1.exec_()

        else:

            DictDCValues[currentInput] = value
            #print(DictDCValues)

    def standbySetValues(self):
        currentInput = self.comboBox_13.currentText()
        valueText = self.lineEdit_60.text()
        pattern1 = '^\d+(\.(\d+))?$'
        res1 = re.match(pattern1, valueText)
        if not res1:
            msg1 = QtWidgets.QMessageBox()
            msg1.setIcon(QtWidgets.QMessageBox.Critical)
            msg1.setText('Check entered parameters!')
            msg1.setWindowTitle("Error")
            msg1.exec_()
        else:

            StandbyValues[currentInput] = valueText

    def setCapacitanceValues(self):

        currentCapacitance = self.comboBox_2.currentText()
        valueText = self.label_11.text()
        valueCapacitance = self.lineEdit_12.text()
        pattern2 = '^\d+(\.(\d+))?[dcmunpfazy]f'
        res = re.match(pattern2,valueCapacitance)
        if not res:
            msg1 = QtWidgets.QMessageBox()
            msg1.setIcon(QtWidgets.QMessageBox.Critical)
            msg1.setText('Check entered parameters!')
            msg1.setWindowTitle("Error")
            msg1.exec_()

        else:
            CapacitanceValue[currentCapacitance] = {}
            CapacitanceValue[currentCapacitance].update({'Value': valueCapacitance})
            if (CapacitanceValue[currentCapacitance].get('Value') == ""):
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText('Enter Capacitance')
                # msg.setInformativeText()
                msg.setWindowTitle("Error")
                msg.exec_()
            #print(CapacitanceValue)

    def setStandbyCapacitanceValues(self):

        currentCapacitance = self.comboBox_14.currentText()
        valueCapacitance = self.lineEdit_65.text()
        pattern2 = '^\d+(\.(\d+))?[dcmunpfazy]f'
        res = re.match(pattern2,valueCapacitance)
        if not res :
            msg1 = QtWidgets.QMessageBox()
            msg1.setIcon(QtWidgets.QMessageBox.Critical)
            msg1.setText('Check entered parameters!')
            msg1.setWindowTitle("Error")
            msg1.exec_()

        else :

            StandbyCapacitance[currentCapacitance] = {}
            StandbyCapacitance[currentCapacitance].update({'Value': valueCapacitance})

            if (StandbyCapacitance[currentCapacitance].get('Value') == ""):
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText('Enter Capacitance')
                # msg.setInformativeText()
                msg.setWindowTitle("Error")
                msg.exec_()

            #print(StandbyCapacitance)

    def setTimeValues(self):

        supplyText = self.label_6.text()
        supplyValue = self.lineEdit_7.text()
        stoptimeText = self.label_9.text()
        stoptimeValue = self.lineEdit_8.text()
        timestepText = self.label_7.text()
        timestepValue = self.lineEdit_9.text()
        #print(supplyValue)
        pattern1 = '^\d+(\.(\d+))?$'
        res1 = re.match(pattern1, supplyValue)
        pattern2 = '^\d+(\.(\d+))?[dcmunpfazy]'
        res2 = re.match(pattern2, stoptimeValue)
        res3 = re.match(pattern2, timestepValue)

        if not res1 or not res2 or not res3 :
            msg1 = QtWidgets.QMessageBox()
            msg1.setIcon(QtWidgets.QMessageBox.Critical)
            msg1.setText('Check entered parameters!')
            msg1.setWindowTitle("Error")
            msg1.exec_()

        else:



            TimeValues['Supply'] = supplyValue
            TimeValues['Stop_Time'] = stoptimeValue
            TimeValues['Time_Step'] = timestepValue

            if (TimeValues['Supply'] == '' or TimeValues['Stop_Time'] == '' or TimeValues['Time_Step'] == ''):
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText('Enter all Values')
                # msg.setInformativeText()
                msg.setWindowTitle("Error")
                msg.exec_()
            else :

                #print(TimeValues)
                self.setOutputText()

    def setStandbyTimeValues(self):
        supplyValue = self.lineEdit_66.text()
        stoptimeValue = self.lineEdit_67.text()
        timestepValue = self.lineEdit_68.text()
        pattern1 = '^\d+(\.(\d+))?$'
        res1 = re.match(pattern1, supplyValue)
        pattern2 = '^\d+(\.(\d+))?[dcmunpfazy]'
        res2 = re.match(pattern2, stoptimeValue)
        res3 = re.match(pattern2, timestepValue)

        if not res1 or not res2 or not res3 :
            msg1 = QtWidgets.QMessageBox()
            msg1.setIcon(QtWidgets.QMessageBox.Critical)
            msg1.setText('Check entered parameters!')
            #msg1.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No )
            # msg.setInformativeText()
            msg1.setWindowTitle("Error")
            msg1.exec_()

        else :

            StandbyTimeValues['Supply'] = supplyValue
            StandbyTimeValues['Stop_Time'] = stoptimeValue
            StandbyTimeValues['Time_Step'] = timestepValue


            if (StandbyTimeValues['Supply'] == '' or StandbyTimeValues['Stop_Time'] == '' or StandbyTimeValues['Time_Step'] == ''):
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText('Enter all Values')
                # msg.setInformativeText()
                msg.setWindowTitle("Error")
                msg.exec_()
            else :

                #print(StandbyTimeValues)
                self.setStandbyOutputText()


    def setOutputText(self):
        OutputText = 'Supply ' + TimeValues['Supply'] + '\n' + 'Stop Time ' + TimeValues[
            'Stop_Time'] + '\n' + 'Step Size ' + TimeValues['Time_Step'] + '\n'
        OutputText = OutputText
        keys10 = DictDCValues.keys()
        for i in keys10 :
            OutputText = OutputText + '\n' + 'Input DC ' + i +' ' + DictDCValues.get(i) + 'V'

        keys1 = DictPulse.keys()
        for i in keys1:
            OutputText = OutputText + '\n' + 'Input Pulse ' + i + " "
            keys2 = DictPulse[i].keys()
            if DictPulse[i].get('Initial_Value') == '':
                DictPulse[i].update({'Initial_Value':'0'})
            if DictPulse[i].get('Pulsed_Value') == '':
                DictPulse[i].update({'Pulsed_Value':TimeValues['Supply']})

            for j in keys2:
                OutputText = OutputText + j + ' '
                temp = DictPulse[i].get(j)
                #temp = temp.replace('_', ' ')
                OutputText = OutputText + ' ' + temp + ' '
            # OutputText = OutputText + '\n'

        keys3 = CapacitanceValue.keys()
        for i in keys3:
            OutputText = OutputText + '\n' + 'Load ' + i + ' '
            keys4 = CapacitanceValue[i].keys()
            for j in keys4:
                # OutputText = OutputText + j +' '
                OutputText = OutputText + CapacitanceValue[i].get(j)
            # OutputText = OutputText + '\n'

        #print(OutputText)
        self.textBrowser.clear()
        self.textBrowser.append(OutputText)

    def setStandbyOutputText(self):
        OutputText = 'Supply ' + StandbyTimeValues['Supply'] + '\n' + 'Stop Time ' + StandbyTimeValues[
            'Stop_Time'] + '\n' + 'Step Size ' + StandbyTimeValues['Time_Step'] + '\n'
        for i in StandbyValues :
            OutputText = OutputText + 'Input DC ' + i + ' ' + StandbyValues.get(i) + '\n'

        keys3 = StandbyCapacitance.keys()
        for i in keys3:

            OutputText = OutputText + '\n' + 'Load ' + i + ' '
            keys4 = StandbyCapacitance[i].keys()
            for j in keys4:

                # OutputText = OutputText + j +' '
                OutputText = OutputText + StandbyCapacitance[i].get(j)


        #print(OutputText)
        self.textBrowser_3.clear()
        self.textBrowser_3.append(OutputText)

    def saveFile(self):
        # newDialog = QInputDialog()

        # newDialog.setModal(True)
        # newDialog.exec()
        ProjectName, ok = QInputDialog.getText(None, "Input", "Enter file name")

        if ProjectName in os.listdir() :
            msg1 = QtWidgets.QMessageBox()
            msg1.setIcon(QtWidgets.QMessageBox.Critical)
            msg1.setText('The entered file name already exists. Do you wish to overwrite?')
            msg1.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No )
            # msg.setInformativeText()
            msg1.setWindowTitle("Error")
            retval = msg1.exec_()
            if retval == 16384 :
                self.saveAndWrite(ProjectName)

        else :
            self.saveAndWrite(ProjectName)

        

    def saveAndWrite(self, ProjectName):
        inputFile = open("./EmpowerSOC/sim_parameters/"+ProjectName+"_ActivePwr_param.txt", "w")
        #inputFile = open("hellloo","w")

        #print(TimeValues)

        OutputText1 = 'Supply ' + TimeValues['Supply'] + '\n' + 'Stop Time ' + TimeValues[
            'Stop_Time'] + '\n' + 'Step Size ' + TimeValues['Time_Step'] + '\n'
        OutputText1 = OutputText1
        keys10 = DictDCValues.keys()
        for i in keys10 :
            OutputText1 = OutputText1 + '\n' + 'Input DC ' + i +' ' + DictDCValues.get(i)+"V"

        keys1 = DictPulse.keys()
        for i in keys1:
            OutputText1 = OutputText1 + '\n' + 'Input Pulse ' + i + ' '
            keys2 = DictPulse[i].keys()
            for j in keys2:
                OutputText1 = OutputText1 + j + ' '
                temp = DictPulse[i].get(j)
                temp = temp.replace('_', ' ')
                OutputText1 = OutputText1 + ' ' + temp + ' '
            # OutputText = OutputText + '\n'

        keys3 = CapacitanceValue.keys()
        for i in keys3:
            OutputText1 = OutputText1 + '\n' + 'Load ' + i + ' '
            keys4 = CapacitanceValue[i].keys()
            for j in keys4:
                # OutputText = OutputText + j +' '
                OutputText1 = OutputText1 + CapacitanceValue[i].get(j)
            # OutputText = OutputText + '\n'

        inputFile.write(OutputText1)
        inputFile.close()
        moduleName = self.getModuleName() # JUGAAD
        modelFileLoc = self.lineEdit_10.text()
        #print("bash "+ScriptLoc+"/RunSim.sh "+ProjectName+"_param_active.txt"+" ActivePwr "+moduleName + " "+ modelFileLoc)
        read = os.popen( "bash "+ScriptLoc+"/RunSim.sh "+ProjectName+" ActivePwr "+moduleName +" "+ modelFileLoc)
        self.textBrowser.clear()
        self.textBrowser.append("Power has been saved.")


    def saveStandbyFile(self):
        ProjectName, ok = QInputDialog.getText(None, "Input", "Enter file name")

        if ProjectName in os.listdir():
            msg1 = QtWidgets.QMessageBox()
            msg1.setIcon(QtWidgets.QMessageBox.Critical)
            msg1.setText('The entered file name already exists. Do you wish to overwrite?')
            msg1.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No )
            # msg.setInformativeText()
            msg1.setWindowTitle("Error")
            retval = msg1.exec_()
            if retval == 16384 :
                self.saveAndWriteStandby(ProjectName)
        else :
            self.saveAndWriteStandby(ProjectName)

    def saveAndWriteStandby(self,ProjectName):

        #inputFile = open("./EmpowerSOC/sim_parameters/"+ProjectName+"_param.txt", "w")
        inputFile = open("./EmpowerSOC/sim_parameters/"+ProjectName+"_StandbyPwr_param.txt","w")

        OutputText = 'Supply ' + StandbyTimeValues['Supply'] + '\n' + 'Stop Time ' + StandbyTimeValues[
            'Stop_Time'] + '\n' + 'Step Size ' + StandbyTimeValues['Time_Step'] + '\n'
        for i in StandbyValues :

            OutputText = OutputText + 'Input DC ' + i + ' ' + StandbyValues.get(i) + '\n'

        keys3 = StandbyCapacitance.keys()
        for i in keys3:

            OutputText = OutputText + '\n' + 'Load ' + i + ' '
            keys4 = StandbyCapacitance[i].keys()
            for j in keys4:

                # OutputText = OutputText + j +' '
                OutputText = OutputText + StandbyCapacitance[i].get(j)


        inputFile.write(OutputText)
        inputFile.close()
        moduleName = self.getModuleName() # JUGAAD
        modelFileLoc = self.lineEdit_11.text()
        read = os.popen( "bash "+ScriptLoc+"/RunSim.sh "+ProjectName+" StandbyPwr "+moduleName +" "+ modelFileLoc)
        self.textBrowser_3.clear()
        self.textBrowser_3.append("Power has been saved.")

    def getInputOutput(self):
        os.system('cd ./synthesis')
        stream1 = os.popen('ls ./synthesis/*.blif')
        blifFile = stream1.read()
        #input_file = open("new.txt.txt", "r")
        input_file = open(blifFile.rstrip(), "r")
        data = input_file.read()
        data = data.split("\n\n")
        # print(data)
        data = data[1]
        inputStr = data.split("\n")
        str1= next(s for s in inputStr if '.inputs' in s)
        #print(str1)
        inputArr = str1.split(' ')
        inputArr = inputArr[1:]

        str2 = next(s1 for s1 in inputStr if '.outputs' in s1)
        #print(str2)
        outputArr = str2.split(' ')
        outputArr = outputArr[1:]

        str3 = next(s1 for s1 in inputStr if '.model' in s1)

        return inputArr,outputArr

    def getModuleName(self):
        os.system('cd ./synthesis')
        stream1 = os.popen('ls ./synthesis/*.blif')
        blifFile = stream1.read()
        #input_file = open("new.txt.txt", "r")
        input_file = open(blifFile.rstrip(), "r")
        data = input_file.read()
        data = data.split("\n\n")
        # print(data)
        data = data[1]
        inputStr = data.split("\n")
        str3 = next(s1 for s1 in inputStr if '.model' in s1)
        #print(str3)
        moduleName = str3.split(' ')[1]
        #print(moduleName)
        return moduleName

    def openFiles(self):
        #print("ok")
        dlg = QtWidgets.QFileDialog()
        dlg.setFileMode(QtWidgets.QFileDialog().AnyFile)
        filenames2 = []
        if dlg.exec_():
            filenames2 = dlg.selectedFiles()

        location = filenames2[0]


        #print(location)
        self.readFile(location)

    def readFile(self,location):
        '''TimeValues={}
        InputPulse = {}
        InputDC ={}
        Capacitance = {}'''
        print(location)
        with open(location,"r") as file:
            if location.find('_Active') != -1:
                for line in file :
                    #print(line)
                    line = line.split(" ")
                    if line[0] == "Supply":
                        temp = line[1].replace("\n","")

                        TimeValues['Supply'] = temp
                    if line[0]== "Stop" and line[1] == "Time":
                        temp1 = line[2].replace("\n","")

                        TimeValues['Stop_Time'] = temp1
                    if line[0]== "Step" and line[1] == "Size":
                        temp2 = line[2].replace("\n","")

                        TimeValues['Time_Step'] = temp2
                    if line[0] == "Input" and line[1] == "Pulse" :
                        DictPulse[line[2]] = {}
                        DictPulse[line[2]].update({"Initial_Value": (line[5])})
                        DictPulse[line[2]].update({'Pulsed_Value':(line[8])})
                        DictPulse[line[2]].update({'Delay':(line[11])})
                        DictPulse[line[2]].update({'Rise_Time':(line[14])})
                        DictPulse[line[2]].update({'Fall_Time':(line[17])})
                        DictPulse[line[2]].update({'Pulse_Width':(line[20])})
                        DictPulse[line[2]].update({'Period':(line[23].replace("\n",""))})
                    if line[0] == "Input" and line[1] == "DC" :
                        DictDCValues[line[2]] = (line[3].replace("V\n",""))
                    if line[0]=="Load":
                        CapacitanceValue[line[1]] = {}
                        CapacitanceValue[line[1]].update({"Value" : line[2].replace("\n","")})

                self.lineEdit_7.setText(TimeValues['Supply'])
                self.lineEdit_8.setText(TimeValues['Stop_Time'])
                self.lineEdit_9.setText(TimeValues['Time_Step'])

            if location.find('_Standby') != -1 :
                print("FOUND")
                for line in file :
                    #print(line)
                    line = line.split(" ")
                    if line[0] == "Supply":
                        StandbyTimeValues['Supply'] = line[1].replace("\n","")
                    if line[0]== "Stop" and line[1] == "Time":
                        StandbyTimeValues['Stop_Time'] = line[2].replace("\n","")
                    if line[0]== "Step" and line[1] == "Size":
                        StandbyTimeValues['Time_Step'] = line[2].replace("\n","")
                    if line[0] == "Input" and line[1] == "DC" :
                        StandbyValues[line[2]] = line[3]
                    if line[0]=="Load":
                        StandbyCapacitance[line[1]] = {}
                        StandbyCapacitance[line[1]].update({"Value" : line[2].replace("\n","")})
                self.lineEdit_66.setText(StandbyTimeValues['Supply'])
                self.lineEdit_67.setText(StandbyTimeValues['Stop_Time'])
                self.lineEdit_68.setText(StandbyTimeValues['Time_Step'])



        file.close()

        self.inputSelectionChange()
        self.inputCapacitanceSelectionChange()
        self.standbyCapacitanceChange()
        self.inputSelectionChangeStandby()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

