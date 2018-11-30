from tkinter import *
from .GUI_baseUI import UI


class LoadGet_UI(UI):

    """
        The UI page to choose from get scan from email or load scan into classifier
    """

    def __init__(self, master, img):
        super().__init__(master, img)


        # ------------------MID FRAME ----------------------------------
        self.mid_frame.grid_columnconfigure(0, weight=1)
        self.mid_frame.grid_columnconfigure(2, weight=1)

        # self.mid_frame.grid_rowconfigure(1, weight=1)
        self.mid_frame.grid_rowconfigure(0, weight=1)

        self.mid_frame.grid_rowconfigure(2, weight=1)

        self.load_get_frame = Frame(self.mid_frame)
        self.load_get_frame.grid(row=1, column=1, sticky='nsew')
        self.header_label = Label(self.mid_frame, text='', font=("TkDefaultFont", 12, 'bold'))
        self.header_label.grid(row=0, column=1, pady=10)

        self.get_but = Button(self.load_get_frame, text='Get Scans', width=30, height=2)
        self.load_but = Button(self.load_get_frame, text='Load Scans', width=30, height=2)
        self.get_but.grid(row=1, column=1, pady=7)
        self.load_but.grid(row=2, column=1, pady=7)

        # -------------Bottom FRAME ---------------------------------------------
        self.botbut_frame.grid_rowconfigure(0, weight=1)
        self.botbut_frame.grid_rowconfigure(2, weight=1)

        self.botbut_frame.grid_columnconfigure(0, weight=1)
        self.botbut_frame.grid_columnconfigure(1, weight=0)

        self.can_but = Button(self.botbut_frame, text='Exit', width=10)
        self.can_but.grid(row=1, column=1, padx=30, pady=15)


if __name__ == "__main__":
    root = Tk()
    LoadGet_UI(root)
    mainloop()
