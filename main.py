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

list_friends_buttons = []
def login_with_sql():
    global conn, cur
    try:
        conn = psycopg2.connect(
            "dbname='xhbkgwzr' user='xhbkgwzr' host='stampy.db.elephantsql.com' password='54wZQUcm0pw6CY9gXUy7Z4vQ01bP_7ee'")
        cur = conn.cursor()
    except psycopg2.OperationalError:
        msgbox(msg="Отсутствует интернет соединение", title="Login", ok_button="fuck go back")


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
        self.load()
        self.sql()

    def load(self):
        check = QPushButton('2222' + '1111', self)
        check.resize(282, 81)
        check.move(0, 79)
        # check.clicked.connect(self.choosen_dialog)
        check.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        check.setStyleSheet('QRadioButton {background-color: #17212b; color: white;}')
        list_friends_buttons.append(check)

    def sql(self):
        info = vk.account.getProfileInfo()
        name = info['first_name']
        surname = info['last_name']
        domain = info['screen_name']
        cur.execute("SELECT * FROM users WHERE DOMAIN = '" + domain + "'")
        row = cur.fetchone()
        if not row:
            cur.execute("INSERT INTO users(domain, name, surname) VALUES (%s,%s,%s)",
                        (domain, name, surname))  # Добавление информации
            conn.commit()


if __name__ == '__main__':
    app = Qt.QApplication([])
    si = Loginform()
    si.show()
    app.exec()
