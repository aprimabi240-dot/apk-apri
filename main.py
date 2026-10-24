from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Label(text='APK Apri Jadi! Dari Medan!', font_size=24))
        btn = Button(text='Klik Gue', size_hint=(1, 0.3))
        btn.bind(on_press=self.klik)
        self.add_widget(btn)
        self.label = Label(text='Menunggu klik...')
        self.add_widget(self.label)

    def klik(self, instance):
        self.label.text = 'GOKIL! Dari pagi sampe jam 01.21 akhirnya jadi!'

class MyApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    MyApp().run()
