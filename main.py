from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import time
import cv2

from filesharer import FileSharer

# Connects python file to kivy
Builder.load_file('frontend.kv')


class CameraScreen(Screen):

    def start(self):
        """ Starts camera and changes Button Text"""
        self.ids.camera.play = True
        self.ids.camera_button.text = "Stop Camera"
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        """ Stops camera and changes button text"""
        self.ids.camera.play = False
        self.ids.camera_button.text = "Start Camera"
        self.ids.camera.texture = None

    def capture(self):
        """ Creates a filename with the current time and captures and saves a photo image under that filename"""
        current_time = time.strftime('%Y%m%d-%H%M%S')
        self.filepath = f"files/{current_time}.png"
        self.ids.camera.export_to_png(self.filepath)
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = self.filepath


class ImageScreen(Screen):

    def create_link(self):
        file_path = App.get_running_app().root.ids.camera_screen.filepath
        print(file_path)


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
