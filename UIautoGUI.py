# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/hn/Documents/Projects/rmc/AutoGui/autoGUI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("IIT's Robot Control Software")
        MainWindow.resize(614, 498)
        MainWindow.setStyleSheet("QPushButton {\n"
"width: 50px;\n"
"height: 50px;\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 25px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout_11.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_11.setSpacing(6)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_16.setSpacing(6)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.pushButtonConnectDisconnect = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonConnectDisconnect.setObjectName("pushButtonConnectDisconnect")
        self.horizontalLayout_16.addWidget(self.pushButtonConnectDisconnect)
        self.labelTimeLeft = QtWidgets.QLabel(self.centralWidget)
        self.labelTimeLeft.setObjectName("labelTimeLeft")
        self.horizontalLayout_16.addWidget(self.labelTimeLeft)
        self.labelBatteryLevel = QtWidgets.QLabel(self.centralWidget)
        self.labelBatteryLevel.setObjectName("labelBatteryLevel")
        self.horizontalLayout_16.addWidget(self.labelBatteryLevel)
        self.labelConnectionStatus = QtWidgets.QLabel(self.centralWidget)
        self.labelConnectionStatus.setStyleSheet("QLabel {\n"
"    width: 50px;\n"
"    height: 50px;\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 25px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"}")
        self.labelConnectionStatus.setObjectName("labelConnectionStatus")
        self.horizontalLayout_16.addWidget(self.labelConnectionStatus)
        self.pushButtonXboxToggle = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonXboxToggle.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButtonXboxToggle.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButtonXboxToggle.setStyleSheet("width: 50px;\n"
"height: 50px\n"
"")
        self.pushButtonXboxToggle.setObjectName("pushButtonXboxToggle")
        self.horizontalLayout_16.addWidget(self.pushButtonXboxToggle)
        self.pushButtonManualAutoToggle = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonManualAutoToggle.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButtonManualAutoToggle.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButtonManualAutoToggle.setStyleSheet("width: 50px;\n"
"height: 50px\n"
"")
        self.pushButtonManualAutoToggle.setObjectName("pushButtonManualAutoToggle")
        self.horizontalLayout_16.addWidget(self.pushButtonManualAutoToggle)
        self.verticalLayout_2.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_18.setSpacing(6)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.label_6 = QtWidgets.QLabel(self.centralWidget)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.verticalLayout_9.addLayout(self.verticalLayout_6)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.verticalLayout_8.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_9 = QtWidgets.QLabel(self.centralWidget)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_8.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.centralWidget)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_8.addWidget(self.label_10)
        self.verticalLayout_8.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_17.setSpacing(6)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_11 = QtWidgets.QLabel(self.centralWidget)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_17.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.centralWidget)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_17.addWidget(self.label_12)
        self.verticalLayout_8.addLayout(self.horizontalLayout_17)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_21.setSpacing(6)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_22 = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_21.addWidget(self.label_22)
        self.verticalLayout_10.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_22.setSpacing(6)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_24 = QtWidgets.QLabel(self.centralWidget)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_22.addWidget(self.label_24)
        self.label_25 = QtWidgets.QLabel(self.centralWidget)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_22.addWidget(self.label_25)
        self.verticalLayout_10.addLayout(self.horizontalLayout_22)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_23.setSpacing(6)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.label_26 = QtWidgets.QLabel(self.centralWidget)
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_23.addWidget(self.label_26)
        self.label_27 = QtWidgets.QLabel(self.centralWidget)
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_23.addWidget(self.label_27)
        self.verticalLayout_10.addLayout(self.horizontalLayout_23)
        self.verticalLayout_9.addLayout(self.verticalLayout_10)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_11.setSpacing(6)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_24.setSpacing(6)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.label_28 = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_24.addWidget(self.label_28)
        self.verticalLayout_11.addLayout(self.horizontalLayout_24)
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_25.setSpacing(6)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.label_30 = QtWidgets.QLabel(self.centralWidget)
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_25.addWidget(self.label_30)
        self.label_31 = QtWidgets.QLabel(self.centralWidget)
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.horizontalLayout_25.addWidget(self.label_31)
        self.verticalLayout_11.addLayout(self.horizontalLayout_25)
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_26.setSpacing(6)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.label_32 = QtWidgets.QLabel(self.centralWidget)
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.horizontalLayout_26.addWidget(self.label_32)
        self.label_33 = QtWidgets.QLabel(self.centralWidget)
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.horizontalLayout_26.addWidget(self.label_33)
        self.verticalLayout_11.addLayout(self.horizontalLayout_26)
        self.verticalLayout_9.addLayout(self.verticalLayout_11)
        self.horizontalLayout_18.addLayout(self.verticalLayout_9)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_13.setSpacing(6)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_12.setSpacing(6)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.textBrowserNextTasks = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowserNextTasks.setMinimumSize(QtCore.QSize(50, 50))
        self.textBrowserNextTasks.setMaximumSize(QtCore.QSize(10000, 10000))
        self.textBrowserNextTasks.setObjectName("textBrowserNextTasks")
        self.verticalLayout_12.addWidget(self.textBrowserNextTasks)
        self.labelRobotSpeed = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.labelRobotSpeed.setFont(font)
        self.labelRobotSpeed.setAlignment(QtCore.Qt.AlignCenter)
        self.labelRobotSpeed.setObjectName("labelRobotSpeed")
        self.verticalLayout_12.addWidget(self.labelRobotSpeed)
        self.verticalLayout_13.addLayout(self.verticalLayout_12)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_10.setSpacing(6)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.pushButtonForward = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonForward.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButtonForward.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButtonForward.setStyleSheet("")
        self.pushButtonForward.setObjectName("pushButtonForward")
        self.horizontalLayout_10.addWidget(self.pushButtonForward)
        self.verticalLayout_7.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_14.setSpacing(6)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.pushButtonLeft = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonLeft.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButtonLeft.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButtonLeft.setObjectName("pushButtonLeft")
        self.horizontalLayout_14.addWidget(self.pushButtonLeft)
        self.pushButtonStop = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonStop.setMinimumSize(QtCore.QSize(0, 20))
        self.pushButtonStop.setMaximumSize(QtCore.QSize(100, 40))
        self.pushButtonStop.setStyleSheet("QPushButton{\n"
"height:60px;\n"
"width: 60px;\n"
"border-radius: 30\n"
"background-color: red;\n"
"color:white;\n"
"}")
        self.pushButtonStop.setObjectName("pushButtonStop")
        self.horizontalLayout_14.addWidget(self.pushButtonStop)
        self.pushButtonRight = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonRight.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButtonRight.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButtonRight.setObjectName("pushButtonRight")
        self.horizontalLayout_14.addWidget(self.pushButtonRight)
        self.verticalLayout_7.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_15.setSpacing(6)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.pushButtonBackward = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonBackward.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButtonBackward.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButtonBackward.setObjectName("pushButtonBackward")
        self.horizontalLayout_15.addWidget(self.pushButtonBackward)
        self.verticalLayout_7.addLayout(self.horizontalLayout_15)
        self.verticalLayout_13.addLayout(self.verticalLayout_7)
        self.horizontalLayout_18.addLayout(self.verticalLayout_13)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButtonEStop = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonEStop.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButtonEStop.setMaximumSize(QtCore.QSize(16777215, 32))
        self.pushButtonEStop.setObjectName("pushButtonEStop")
        self.verticalLayout.addWidget(self.pushButtonEStop)
        self.label_15 = QtWidgets.QLabel(self.centralWidget)
        self.label_15.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.verticalLayout.addWidget(self.label_15)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButtonReadyDump = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonReadyDump.setObjectName("pushButtonReadyDump")
        self.horizontalLayout_2.addWidget(self.pushButtonReadyDump)
        self.pushButtonDump = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonDump.setObjectName("pushButtonDump")
        self.horizontalLayout_2.addWidget(self.pushButtonDump)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_14 = QtWidgets.QLabel(self.centralWidget)
        self.label_14.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayout.addWidget(self.label_14)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButtonReadyMine = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonReadyMine.setObjectName("pushButtonReadyMine")
        self.horizontalLayout_4.addWidget(self.pushButtonReadyMine)
        self.pushButtonMine = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonMine.setObjectName("pushButtonMine")
        self.horizontalLayout_4.addWidget(self.pushButtonMine)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.label_13 = QtWidgets.QLabel(self.centralWidget)
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButtonSpeedUp = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonSpeedUp.setObjectName("pushButtonSpeedUp")
        self.horizontalLayout_3.addWidget(self.pushButtonSpeedUp)
        self.pushButtonSpeedDown = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonSpeedDown.setObjectName("pushButtonSpeedDown")
        self.horizontalLayout_3.addWidget(self.pushButtonSpeedDown)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_9.addLayout(self.verticalLayout)
        self.horizontalLayout_18.addLayout(self.horizontalLayout_9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_11.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 614, 22))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButtonConnectDisconnect.setText(_translate("MainWindow", "Connect"))
        self.labelTimeLeft.setText(_translate("MainWindow", "Time Left"))
        self.labelBatteryLevel.setText(_translate("MainWindow", "Baterry level"))
        self.labelConnectionStatus.setText(_translate("MainWindow", "."))
        self.pushButtonXboxToggle.setText(_translate("MainWindow", "X"))
        self.pushButtonManualAutoToggle.setText(_translate("MainWindow", "M"))
        self.label.setText(_translate("MainWindow", "Wheels"))
        self.label_2.setText(_translate("MainWindow", "Speed 1"))
        self.label_5.setText(_translate("MainWindow", "Speed 2"))
        self.label_3.setText(_translate("MainWindow", "Speed 3"))
        self.label_6.setText(_translate("MainWindow", "Speed 4"))
        self.label_7.setText(_translate("MainWindow", "Auger"))
        self.label_9.setText(_translate("MainWindow", "Speed with dirrection"))
        self.label_10.setText(_translate("MainWindow", "Tiltness"))
        self.label_11.setText(_translate("MainWindow", "height"))
        self.label_12.setText(_translate("MainWindow", "Empty"))
        self.label_22.setText(_translate("MainWindow", "Bin"))
        self.label_24.setText(_translate("MainWindow", "Conveyor Speed"))
        self.label_25.setText(_translate("MainWindow", "Dumping distance"))
        self.label_26.setText(_translate("MainWindow", "collecting"))
        self.label_27.setText(_translate("MainWindow", "Dumping"))
        self.label_28.setText(_translate("MainWindow", "Device Status"))
        self.label_30.setText(_translate("MainWindow", "Motor Arduino"))
        self.label_31.setText(_translate("MainWindow", "Distance sensors"))
        self.label_32.setText(_translate("MainWindow", "Kinect"))
        self.label_33.setText(_translate("MainWindow", "lidar"))
        self.labelRobotSpeed.setText(_translate("MainWindow", "SPEED"))
        self.pushButtonForward.setText(_translate("MainWindow", "Forward"))
        self.pushButtonLeft.setText(_translate("MainWindow", "Left"))
        self.pushButtonStop.setText(_translate("MainWindow", "Stop"))
        self.pushButtonRight.setText(_translate("MainWindow", "Right"))
        self.pushButtonBackward.setText(_translate("MainWindow", "Backward"))
        self.pushButtonEStop.setText(_translate("MainWindow", "E-STOP"))
        self.label_15.setText(_translate("MainWindow", "Dump"))
        self.pushButtonReadyDump.setText(_translate("MainWindow", "ready"))
        self.pushButtonDump.setText(_translate("MainWindow", "dump"))
        self.label_14.setText(_translate("MainWindow", "Mine"))
        self.pushButtonReadyMine.setText(_translate("MainWindow", "ready"))
        self.pushButtonMine.setText(_translate("MainWindow", "mine"))
        self.label_13.setText(_translate("MainWindow", "Speed"))
        self.pushButtonSpeedUp.setText(_translate("MainWindow", "Up"))
        self.pushButtonSpeedDown.setText(_translate("MainWindow", "Down"))
#
#
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

