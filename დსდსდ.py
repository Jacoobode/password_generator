from PyQt5 import QtCore, QtGui, QtWidgets
import random
import string


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("პაროლის გენერატორი")
        MainWindow.resize(799, 464)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 20, 171, 61))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(480, 90, 291, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(70, 70, 121, 31))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(70, 110, 141, 21))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(70, 140, 111, 31))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(70, 180, 151, 21))
        self.checkBox_4.setObjectName("checkBox_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 350, 241, 28))
        self.pushButton.setObjectName("pushButton")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(70, 280, 95, 20))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(170, 280, 95, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(610, 140, 151, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 10, 141, 16))
        self.label_2.setObjectName("label_2")
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(0, 395, 311, 21))
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        # Connect signals and slots
        self.pushButton.clicked.connect(self.generate_password)
        self.pushButton_2.clicked.connect(self.copy_password)
        self.horizontalScrollBar.valueChanged.connect(self.update_password_length)

        # Set default values
        self.horizontalScrollBar.setMinimum(6)
        self.horizontalScrollBar.setMaximum(50)
        self.horizontalScrollBar.setValue(12)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "პაროლის გენერატორი"))
        self.label.setText(_translate("MainWindow", "მიუთითეთ სიმბოლოები"))
        self.checkBox.setText(_translate("MainWindow", "დიდი ასოებით"))
        self.checkBox_2.setText(_translate("MainWindow", "პატარა ასოებით"))
        self.checkBox_3.setText(_translate("MainWindow", "ციფრებით"))
        self.checkBox_4.setText(_translate("MainWindow", "სხვა სიმბოლოებით"))
        self.pushButton.setText(_translate("MainWindow", "დააგენერირე"))
        self.radioButton.setText(_translate("MainWindow", "მარტივი"))
        self.radioButton_2.setText(_translate("MainWindow", "რთული"))
        self.pushButton_2.setText(_translate("MainWindow", "დააკოპირე პაროლი"))
        self.label_2.setText(_translate("MainWindow", "პაროლის გენერატორი"))

    def generate_password(self):
        length = self.horizontalScrollBar.value()
        characters = ""


        if self.checkBox.isChecked():
            characters += string.ascii_uppercase
        if self.checkBox_2.isChecked():
            characters += string.ascii_lowercase
        if self.checkBox_3.isChecked():
            characters += string.digits
        if self.checkBox_4.isChecked():
            characters += "!@#$%^&*()_+-=[]{}|;:,.<>?"


        if not any([self.checkBox.isChecked(),
                    self.checkBox_2.isChecked(),
                    self.checkBox_3.isChecked(),
                    self.checkBox_4.isChecked()]):
            characters = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?"


        if self.radioButton.isChecked() or not (self.radioButton.isChecked() or self.radioButton_2.isChecked()):

            password = ''.join(random.choice(characters) for _ in range(length))
        else:

            password = []
            categories = []

            if self.checkBox.isChecked():
                categories.append(string.ascii_uppercase)
            if self.checkBox_2.isChecked():
                categories.append(string.ascii_lowercase)
            if self.checkBox_3.isChecked():
                categories.append(string.digits)
            if self.checkBox_4.isChecked():
                categories.append("!@#$%^&*()_+-=[]{}|;:,.<>?")


            if not categories:
                categories = [
                    string.ascii_uppercase,
                    string.ascii_lowercase,
                    string.digits,
                    "!@#$%^&*()_+-=[]{}|;:,.<>?"
                ]

            for category in categories:
                password.append(random.choice(category))


            while len(password) < length:
                password.append(random.choice(characters))


            random.shuffle(password)
            password = ''.join(password)

        self.lineEdit.setText(password)

    def copy_password(self):
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setText(self.lineEdit.text())

    def update_password_length(self):

        length = self.horizontalScrollBar.value()
        


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())