from tkinter import *


def customise_window(master):
    master.title("Error")
    master.resizable(False, False)
    WINDOW_W = 300
    WINDOW_H = 150

    y_limit = master.winfo_screenheight() - WINDOW_H
    x_limit = master.winfo_screenwidth() - WINDOW_W

    master.geometry(f"{WINDOW_W}x{WINDOW_H}+"
                    f"{int(x_limit / 2)}+{int(y_limit / 4)}")

    master.rowconfigure(1, weight=1)
    master.columnconfigure(0, weight=1)

    frame = Frame(master)

    Frame(master, height=20).grid(row=0, column=0, sticky=EW)

    frame.grid(row=1, column=0, sticky=NSEW, padx=2, pady=2)

    frame.columnconfigure(1, weight=1)
    frame.rowconfigure(0, weight=1)

    gravity_button = Label(frame, text="  !", font=('Arial', 26, "bold"), fg="red")
    gravity_button.grid(row=0, column=0, sticky=W)

    message = Label(frame,
                    text="ERROR 9806:\nGravity detected.",
                    justify=LEFT
                    )
    message.grid(row=0, column=1, sticky=EW)

    ok_button = Button(frame, text="OK", command=master.destroy, width=6, relief=RIDGE,
                       overrelief=GROOVE)
    ok_button.grid(row=1, column=1, sticky=E, padx=10, pady=5)

    master.update()


class Gravity:
    def __init__(self, master, gravity=3, bounce_factor=0.6, *args, **kwargs):
        if type(bounce_factor) is int:
            bounce_factor = float(bounce_factor)
        if 'tkinter.Tk' not in str(type(master)):
            raise TypeError("'master' parameter only accepts 'Tk' or 'Toplevel' object types.")
        elif type(gravity) is not int:
            raise TypeError("'gravity' parameter only accepts 'int' values.")
        elif not 0 <= gravity < 100000:
            raise ValueError("'gravity' value must be positive and below 100000")
        elif type(bounce_factor) is not float:
            raise TypeError("'bounce_factor' parameter only accepts 'int' or 'float' values.")
        elif not 0.0 <= bounce_factor <= 1.0:
            raise ValueError("'bounce_factor' value must be in range 0 to 1 only")
        self.master = master
        self.master.bind("<Escape>", lambda e: self.master.destroy())
        self.master.update()

        self.GRAVITY = gravity  # px/ms^2
        self.TIME_FACTOR = 10  # ms
        self.BOUNCE_FACTOR = bounce_factor  # percentage of velocity remaining right after bounce
        self.curr_vel = 0  # px/ms

        self.y_limit = self.master.winfo_screenheight() - self.master.winfo_height() - 69

        if gravity != 0:
            self.master.after(1000, self.fally)
        self.master.mainloop()

    def xpos(self):
        return self.master.winfo_x()

    def ypos(self):
        return self.master.winfo_y()

    def fally(self):  # moves the window
        if self.curr_vel >= 0:
            if self.curr_vel == 0 and self.ypos() == self.y_limit:
                pass
            if self.ypos() < self.y_limit:
                self.curr_vel += self.GRAVITY
                self.master.geometry(f"+{self.xpos()}+{self.ypos() + self.curr_vel}")
            else:
                if self.curr_vel >= self.GRAVITY:
                    self.curr_vel = int(self.curr_vel * (-1) * self.BOUNCE_FACTOR)
                else:
                    self.curr_vel = 0
                    self.master.geometry(f"+{self.xpos()}+{self.y_limit}")

        else:
            self.master.geometry(f"+{self.xpos()}+{self.ypos() + self.curr_vel}")
            self.curr_vel += self.GRAVITY

        self.master.after(self.TIME_FACTOR, self.fally)


if __name__ == '__main__':
    root = Tk()
    customise_window(root)
    Gravity(master=root)  # gravity = 3 and bounce_factor = 0.6 by default
    # parameters also include gravity and bounce_factor
