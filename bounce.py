from tkinter import *


class App:
    def __init__(self):
        self.master = Tk()
        self.master.title("Error")

        self.window_width = 360
        self.window_height = 180
        self.x_limit = self.master.winfo_screenwidth() - self.window_width
        self.y_limit = self.master.winfo_screenheight() - self.window_height
        self.window_coord_x = int(self.x_limit/2)
        self.window_coord_y = int(self.y_limit/2)

        self.bounce_factor = 0.4

        self.master.geometry(f"{self.window_width}x{self.window_height}+"
                             f"{self.window_coord_x}+{self.window_coord_y}")

        

        self.gravity = 10

        self.master.mainloop()

    def fall(self):
        pass


if __name__ == '__main__':
    App()
