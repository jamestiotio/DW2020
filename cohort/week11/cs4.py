from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App


class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout()
        self.settings_button = Button(text="Settings")
        self.settings_button.bind(on_press=self.change_to_setting)
        self.quit_button = Button(text="Quit")
        self.quit_button.bind(on_press=self.quit_app)
        self.layout.add_widget(self.settings_button)
        self.layout.add_widget(self.quit_button)
        self.add_widget(self.layout)

    def change_to_setting(self, value):
        self.manager.transition.direction = "left"
        self.manager.current = "settings"

    def quit_app(self, value):
        App.get_running_app().stop()


class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout()
        self.settings_label = Label(text="Settings Screen")
        self.menu_button = Button(text="Back to Menu")
        self.menu_button.bind(on_press=self.change_to_menu)
        self.layout.add_widget(self.settings_label)
        self.layout.add_widget(self.menu_button)
        self.add_widget(self.layout)

    def change_to_menu(self, value):
        self.manager.transition.direction = "right"
        self.manager.current = "menu"


class SwitchScreenApp(App):
    def build(self):
        sm = ScreenManager()
        ms = MenuScreen(name="menu")
        st = SettingsScreen(name="settings")
        sm.add_widget(ms)
        sm.add_widget(st)
        sm.current = "menu"
        return sm


if __name__ == "__main__":
    SwitchScreenApp().run()