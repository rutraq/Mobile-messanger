from PyQt5 import Qt, QtGui, QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton, QRadioButton
from PyQt5.QtGui import QPixmap, QIcon
import login
import mainform
from easygui import msgbox
import vk_api
import psycopg2
import requests
import os
import rsa
from threading import Thread
from PyQt5.QtCore import QThread, pyqtSignal
import ast
import time


class Loginform(QtWidgets.QMainWindow, login.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.login)

    def login(self):
        global vk
        try:
            if (int(self.lineEdit.text().__len__()) == 0) or (int(self.lineEdit_2.text().__len__()) == 0):
                msgbox(msg="Введите данные", title="Login", ok_button="fuck go back")
            else:
                vk_session = vk_api.VkApi(self.lineEdit.text(), self.lineEdit_2.text())
                vk_session.auth()
                vk = vk_session.get_api()
                self.mainform = Mainform()
                self.mainform.show()
                self.hide()
        except vk_api.exceptions.BadPassword:
            msgbox(msg="Введён неверный логин или пароль", title="Login", ok_button="fuck go back")
            self.lineEdit.setText('')
        except requests.exceptions.ConnectionError:
            msgbox(msg="Отсутствует интернет соединение", title="Login", ok_button="fuck go back")
            self.lineEdit.setText('')


class Mainform(QtWidgets.QMainWindow, mainform.Ui_Dialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = Qt.QApplication([])
    si = Loginform()
    si.show()
    app.exec()
