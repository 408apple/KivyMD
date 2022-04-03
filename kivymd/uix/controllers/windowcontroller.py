"""
Controllers/WindowController
============================

Controlling the resizing direction of the application window
------------------------------------------------------------

.. code-block:: python

    # When resizing the application window, the direction of change will be
    # printed - 'left' or 'right'.

    from kivymd.app import MDApp
    from kivymd.uix.controllers import WindowController
    from kivymd.uix.screen import MDScreen


    class MyScreen(MDScreen, WindowController):
        def on_width(self, *args):
            print(self.get_window_width_resizing_direction())


    class Test(MDApp):
        def build(self):
            return MyScreen()


    Test().run()
"""

from kivy.core.window import Window
from kivy.core.window.window_sdl2 import WindowSDL


class WindowController:
    def __init__(self):
        self.window_resizing_direction = "unknown"
        self.__width = Window.width
        Window.bind(on_resize=self._on_resize)

    def get_window_width_resizing_direction(self) -> str:
        """Return window width resizing direction - 'left' or 'right' """

        return self.window_resizing_direction

    def _set_window_width_resizing_direction(self, width: int) -> None:
        if self.__width > width:
            self.window_resizing_direction = "left"
        elif self.__width < width:
            self.window_resizing_direction = "right"

    def _on_resize(self, window_sdl2: WindowSDL, width: int, height: int) -> None:
        self._set_window_width_resizing_direction(width)
        self.__width = width
