from kivy.app import App
from kivy.core.window import Window
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from libdw import pyrebase

projectid = "dw1d-gui"
url = "https://" + projectid + ".firebaseio.com"
apikey = ""

config={
    "apiKey":apikey,
    "databaseURL":url,
}

class LedCollection:

    name = ['Yellow LED', 'Red LED']

    def __init__(self):
        firebase = pyrebase.initialize_app(config)
        self.db = firebase.database()
        state = self.db.child('/state').get().val()
        if state == None:
            self.state = [{'text': 'off', 'state': 'normal'},
                          {'text': 'off', 'state': 'normal'}]
        else:
            self.state = state

    def get_name(self, led):
        return self.name[led]

    def get_text(self, led):
        return self.state[led]['text']

    def get_state(self, led):
        return self.state[led]['state']

    def toggle(self, led):
        toggle = {'off': 'on', 'on': 'off',
                  'normal': 'down', 'down': 'normal'}

        temp_state = self.state[:]

        temp_state[led]['text'] = toggle[self.state[led]['text']]
        temp_state[led]['state'] = toggle[self.state[led]['state']]

        self.db.child('state').set(temp_state)

class LEDControllerApp(App):

    def build(self):
        Window.size = (500, 100)

        layout = GridLayout()
        layout.cols = 2

        self.leds = LedCollection()

        self.toggle_button = []

        # Don't know why putting this into the for-loop will
        # cause a weird bug...
        f = [lambda instance: self.toggle_led(0, instance),
             lambda instance: self.toggle_led(1, instance)]

        for i in range(2):
            layout.add_widget(Label(text=self.leds.get_name(i)))
            self.toggle_button.append( \
                    ToggleButton(text=self.leds.get_text(i),
                        state=self.leds.get_state(i),
                        on_press=f[i]))
            layout.add_widget(self.toggle_button[i])

        return layout

    def toggle_led(self, led, instance):
        self.leds.toggle(led)
        self.toggle_button[led].text = self.leds.get_text(led)
        self.toggle_button[led].state = self.leds.get_state(led)

LEDControllerApp().run()