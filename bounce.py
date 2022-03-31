from tkinter import *


class App:
    def __init__(self):
        self.master = Tk()
        self.master.title("Error")

        self.WINDOW_W = 360
        self.WINDOW_H = 180
        self.x_limit = self.master.winfo_screenwidth() - self.WINDOW_W
        self.y_limit = self.master.winfo_screenheight() - self.WINDOW_H

        self.GRAVITY = 10  # px/20ms^2
        self.BOUNCE_FACTOR = 0.7  # percentage of velocity remaining right after bounce
        self.curr_vel = 0  # px/20ms

        self.held = False
        self.master.geometry(f"{self.WINDOW_W}x{self.WINDOW_H}+"
                             f"{int(self.x_limit / 2)}+{int(self.y_limit / 2)}")

        self.master.bind("<Button-1>", lambda e: self.under_hold())
        self.master.bind("<ButtonRelease-1>", lambda e: self.released())

        self.master.after(1000, self.move)

        self.master.mainloop()

    def under_hold(self):
        self.curr_vel = 0
        self.held = True

    def released(self):
        self.held = False

    def ypos(self):
        return self.master.winfo_y()

    def move(self, event=None):  # moves the window
        if not self.held:
            if self.ypos() < self.y_limit:
                self.curr_vel += self.GRAVITY
                self.master.geometry(f"+{self.master.winfo_x()}+{self.ypos()+self.curr_vel}")
            else:
                self.master.geometry(f"+{self.master.winfo_x()}+{self.y_limit}")
                if self.curr_vel != 0:
                    self.curr_vel = int((-1)*(self.curr_vel * self.BOUNCE_FACTOR))
                    self.master.geometry(f"+{self.master.winfo_x()}+{self.ypos() + self.curr_vel}")

        self.master.after(20, self.move)


if __name__ == '__main__':
    App()
