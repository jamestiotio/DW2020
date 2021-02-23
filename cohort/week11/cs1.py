from kivy.app import App
from kivy.uix.label import Label


class AlternateApp(App):

    def build(self):
        self.state = 0
        self.label = Label(text="Programming is fun")
        self.label.bind(on_touch_down=self.alternate)
        return self.label

    def alternate(self, instance, touch):
        messages = ["Programming is fun", "It is fun to program"]
        self.state = (self.state + 1) % 2
        self.label.text = messages[self.state]


myapp = AlternateApp()
myapp.run()