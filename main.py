from kivy.app import App
from kivy.uix.image import Image
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.boxlayout import BoxLayout
from datetime import datetime as dt
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import numpy as np
import cv2
from object_det import *
from distance_estimation import *
#from OCR import *
#from say import *

kv = """
Screen:
    MDBoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title:"See with Ears"
            left_action_items: [["menu", lambda x:nav_draw.set_state()]]
        MDBoxLayout:
            adaptive_size:True
            orientation:"horizontal"
            MDRaisedButton:
            text: "Estimate Distance"
            pos_hint: {"center_y": 0.85}
        Widget:


    MDNavigationDrawer:
        id: nav_draw
        orientation: "vertical"
        padding: "8dp"
        spacing: "8dp"
        BoxLayout:
            orientation: "vertical"
            adaptive_size:True
            MDIconButton:
                icon:"information"
                icon_size: "32sp"
                on_press: nav_draw.set_state("close")
            MDLabel:
                text: "About"
                font_style: "H4"
                size_hint_y: None
                height : self.texture_size[1]
                #valign: "center"
            MDLabel:
                text: "An Assitive app for visually impaired to navigate independently"
                font_style: "Caption"
                size_hint_y: None
                height : self.texture_size[1]
                #valign: "center"
        Widget:
"""

class Cam(Image):
    camera_resolution = (640,480)
    counter = 0
    #distance = False

    def __init__(self, capture, fps, **kwargs):
        super(Cam, self).__init__(**kwargs)
        self.capture = capture
        Clock.schedule_interval(self.update, 1.0 / fps)

    def update(self,dt):
        #self.distance = set_distance()
        ret, frame = self.capture.read()
        if ret:
            # convert it to texture
            (result,boxes,class_names, data_list) = detect(frame)
            buf1 = cv2.flip(result, 0)
            buf = buf1.tobytes()
            image_texture = Texture.create(
                size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            # display image from the texture
            self.texture = image_texture



class Main(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Orange"

        self.capture = cv2.VideoCapture(0)
        self.my_camera  = Cam(capture=self.capture, fps=30)
        #boxes,class_names, data_list = Cam.update(self,dt)

        Screen = Builder.load_string(kv)
        #window.add_widget(self.my_camera)
        Screen.add_widget(self.my_camera,2)
        return Screen


Main().run()
