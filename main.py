from kivy.app import App
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse


class ImageWidget(Widget):
    image_src = StringProperty("")

    def __init__(self, **kwargs):
        super(ImageWidget, self).__init__(**kwargs)
        self.image_src = ""
        self.ellipse_list = []

    def on_touch_down(self, touch):
        print(touch)
        print(self.size)

        if len(self.ellipse_list) >= 4:
            self.canvas.children.remove(self.ellipse_list.pop(0))

        with self.canvas:
            Color(1, 1, 0)
            d = 30
            self.ellipse_list.append(
                Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            )

    def clear_ellipse(self):
        for e in self.ellipse_list:
            self.canvas.children.remove(e)
        self.ellipse_list = []


class ImageApp(App):
    def __init__(self, **kwargs):
        super(ImageApp, self).__init__(**kwargs)
        self.title = "example"

    def _on_file_drop(self, window, file_path):
        image_src = file_path.decode("UTF-8")
        self.title = image_src

        self.widget.image_src = image_src
        self.widget.ids.image.reload()
        self.widget.clear_ellipse()

        print(self.widget.ids.image.norm_image_size)
        print(self.widget.ids.image.texture.size)

    def build(self):
        Window.bind(on_dropfile=self._on_file_drop)
        self.widget = ImageWidget()
        return self.widget


if __name__ == "__main__":
    app = ImageApp()
    app.run()
