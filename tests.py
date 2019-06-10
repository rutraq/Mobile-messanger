from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.config import Config
import vk_api
from random import randint


# Config.set("graphics", "width", "300")
# Config.set("graphics", "height", "200")
Config.set("graphics", "resizable", "0")
count = 0


class Login(BoxLayout):
    def __init__(self, **kwargs):
        super(Login, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.grid = GridLayout(
            cols=2,
            size_hint=[1, .63]
        )
        self.lbl = Label(
            text='Login',
            size_hint=[.8, 1]
        )
        self.grid.add_widget(self.lbl)
        self.txt = TextInput(
            write_tab=False,
            multiline=False
        )
        self.grid.add_widget(self.txt)
        self.lbl2 = Label(
            text='Password',
            size_hint=[.8, 1]
        )
        self.txt2 = TextInput(
            write_tab=False,
            multiline=False,
            password=True,
            on_text_validate=self.login
        )
        self.grid.add_widget(self.lbl2)
        self.grid.add_widget(self.txt2)
        self.lay = AnchorLayout(
            anchor_x="center",
            anchor_y="bottom"
        )
        self.lay.add_widget(self.grid)
        self.add_widget(self.lay)
        self.btn = Button(
            text="Sign in",
            size_hint=[.3, .3]
        )
        self.lay2 = AnchorLayout(
            anchor_x="center",
            anchor_y="center"
        )
        self.lay2.add_widget(self.btn)
        self.add_widget(self.lay2)

    def login(self, obj):
        vk_login = self.txt.text
        pass_login = self.txt2.text
        vk_session = vk_api.VkApi(vk_login, pass_login)
        vk_session.auth()
        vk = vk_session.get_api()
        vk.messages.send(message="provirka", domain='genek_orlov', random_id=randint(1, 1000000000000))


class MyFirstProgram(App):
    def build(self):
        return Login()


if __name__ == "__main__":
    MyFirstProgram().run()
