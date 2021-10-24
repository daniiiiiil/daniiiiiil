# напиши модуль для работы с анимацией
from kivy.properties import NumericProperty
from kivy.uix.button import Button
from kivy.animation import Animation

from kiv.uix.boxlayout import BoxLayout

class Runner(BoxLayout):
    value = NumericPropery(0)
    finished = BoolearnProperty(False)

    def __init__(self, total=10, steptime=1, autorepiat=True, bcolor=(0.73, 0.15, 0.96, 1), btext_inprogress='Приседание', **kwargs):
        super().__init__(**kwargs)

        self.total = total
        self.autorepiat = autorepiat
        self.bext_inprogress = btext_inprogress
        self.animation = (Animation(pos_hint={'top': 0.1}, duration=steptime/2)
                        + Animation(pos_hint={'top': 1.0}, duration=steptime/2))
        self.animation.on_progres = self.next
        self.bt = Button(size_hint=(1, 0.1), pos_hint={'top': 1.0}, backgraund_color=bcolor)
        self.add_widget(self.btn)
    def start(self):
        pass

    def next(self, widget, step):
        pass