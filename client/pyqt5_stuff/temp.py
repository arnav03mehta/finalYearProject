# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainPage_temp.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(460, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(460, 800))
        MainWindow.setMaximumSize(QtCore.QSize(460, 800))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../assets/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setDocumentMode(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Timer = QtWidgets.QLabel(self.centralwidget)
        self.Timer.setGeometry(QtCore.QRect(20, 10, 111, 31))
        self.Timer.setAlignment(QtCore.Qt.AlignCenter)
        self.Timer.setObjectName("Timer")
        self.top_divider = QtWidgets.QFrame(self.centralwidget)
        self.top_divider.setGeometry(QtCore.QRect(20, 40, 421, 20))
        self.top_divider.setFrameShape(QtWidgets.QFrame.HLine)
        self.top_divider.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.top_divider.setObjectName("top_divider")
        self.Mode = QtWidgets.QLabel(self.centralwidget)
        self.Mode.setGeometry(QtCore.QRect(230, 10, 211, 31))
        self.Mode.setAlignment(QtCore.Qt.AlignCenter)
        self.Mode.setObjectName("Mode")
        self.Task = QtWidgets.QLabel(self.centralwidget)
        self.Task.setGeometry(QtCore.QRect(20, 80, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.Task.setFont(font)
        self.Task.setObjectName("Task")
        self.Examples = QtWidgets.QLabel(self.centralwidget)
        self.Examples.setGeometry(QtCore.QRect(20, 325, 111, 31))
        self.Examples.setObjectName("Examples")
        self.top_divider_2 = QtWidgets.QFrame(self.centralwidget)
        self.top_divider_2.setGeometry(QtCore.QRect(20, 512, 421, 20))
        self.top_divider_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.top_divider_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.top_divider_2.setObjectName("top_divider_2")
        self.top_divider_3 = QtWidgets.QFrame(self.centralwidget)
        self.top_divider_3.setGeometry(QtCore.QRect(20, 592, 421, 20))
        self.top_divider_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.top_divider_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.top_divider_3.setObjectName("top_divider_3")
        self.file = QtWidgets.QLineEdit(self.centralwidget)
        self.file.setGeometry(QtCore.QRect(20, 560, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.file.setFont(font)
        self.file.setObjectName("file")
        self.Select_file = QtWidgets.QLabel(self.centralwidget)
        self.Select_file.setGeometry(QtCore.QRect(20, 533, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Select_file.setFont(font)
        self.Select_file.setObjectName("Select_file")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 560, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 560, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.players_area = QtWidgets.QScrollArea(self.centralwidget)
        self.players_area.setGeometry(QtCore.QRect(20, 620, 421, 161))
        self.players_area.setWidgetResizable(True)
        self.players_area.setObjectName("players_area")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 419, 159))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.players = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.players.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.players.setObjectName("players")
        self.verticalLayout.addWidget(self.players)
        self.players_area.setWidget(self.scrollAreaWidgetContents_3)

        self.task_container = QtWidgets.QScrollArea(self.centralwidget)
        self.task_container.setGeometry(QtCore.QRect(20, 110, 421, 201))
        self.task_container.setWidgetResizable(True)
        self.task_container.setObjectName("task_container")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 419, 199))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.task_desc = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.task_desc.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.task_desc.setWordWrap(True)
        self.task_desc.setObjectName("label")
        self.verticalLayout_3.addWidget(self.task_desc)
        self.task_container.setWidget(self.scrollAreaWidgetContents_5)

        self.example_container = QtWidgets.QScrollArea(self.centralwidget)
        self.example_container.setGeometry(QtCore.QRect(20, 360, 421, 131))
        self.example_container.setWidgetResizable(True)
        self.example_container.setObjectName("example_container")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 419, 129))
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.examples = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.examples.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.examples.setObjectName("examples")
        self.verticalLayout_2.addWidget(self.examples)
        self.example_container.setWidget(self.scrollAreaWidgetContents_6)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Clash of Code"))
        self.Timer.setText(_translate("MainWindow", "15:00"))
        self.Mode.setText(_translate("MainWindow", "Mode : Shortest"))
        self.Task.setText(_translate("MainWindow", "Task"))
        self.Examples.setText(_translate("MainWindow", "Examples"))
        self.Select_file.setText(_translate("MainWindow", "Select File"))
        self.pushButton.setText(_translate("MainWindow", "Finish"))
        self.pushButton_2.setText(_translate("MainWindow", "Select"))
        self.players.setText(_translate("MainWindow", " TextLabel"))
        self.label.setText(_translate("MainWindow", " TextLabel"))
        self.examples.setText(_translate("MainWindow", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
