from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class RootWidget(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2

        # Create widgets and store as instance variables
        self.investment_label = Label(
            text="Investment Amount", valign="middle")
        self.investment_field = TextInput(
            text="0.0", multiline=False, halign="left")
        self.years_label = Label(text="Years")
        self.years_field = TextInput(text="0", multiline=False, halign="left")
        self.annual_interest_rate_label = Label(text="Annual Interest Rate")
        self.annual_interest_rate_field = TextInput(text="0.00", multiline=False)
        self.future_value_label = Label(text="Future Value")
        self.result_label = Label(text="")
        self.calculate_button = Button(text="Calculate")
        self.calculate_button.bind(on_press=self.calculate)

        # Add widgets
        for widget in [self.investment_label, self.investment_field, self.years_label, self.years_field, self.annual_interest_rate_label, self.annual_interest_rate_field, self.future_value_label, self.result_label, self.calculate_button]:
            self.add_widget(widget)

    def calculate(self, instance):
        try:
            inv_amt = float(self.investment_field.text)
            years = float(self.years_field.text)
            mth_int_rate = float(self.annual_interest_rate_field.text) / 1200.0

            future_value = round(
                inv_amt * ((1 + mth_int_rate) ** (years * 12)), 2)

            self.result_label.text = str(future_value)

        except:
            print("Please key in valid numbers only.")


class Investment(App):

    def build(self):
        return RootWidget()


Investment().run()