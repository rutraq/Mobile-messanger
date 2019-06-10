from kivy.app import App
from kivy.uix.widget import Widget
from kivy.config import Config


Config.set("graphics", "width", "300")
Config.set("graphics", "height", "200")


class Register(Widget):
    pass


class Messenger(App):
    def build(self):
        application = Register()
        return application


if __name__ == '__main__':
    Messenger().run()
