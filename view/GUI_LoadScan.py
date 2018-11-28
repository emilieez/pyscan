from tkinter import *
from .GUI_baseUI import UI


class LoadScan_UI(UI):

    """
        The chequing or savigns page
        Has 2 buttons cheq or savigns
    """

    def __init__(self, master, img):
        super().__init__(master, img)


        # ------------------MID FRAME ----------------------------------
        self.mid_frame.grid_columnconfigure(0, weight=1)
        self.mid_frame.grid_columnconfigure(2, weight=1)

        self.mid_frame.grid_rowconfigure(0, weight=0)
        self.mid_frame.grid_rowconfigure(1, weight=1)

        self.header_label = Label(self.mid_frame, text='Load Scan', font=("TkDefaultFont", 12))
        self.header_label.grid(row=0, column=1, pady=10)

        self.CS_frame = Frame(self.mid_frame)
        self.CS_frame.grid(row=1, column=1)

        self.Load_frame = Frame(self.CS_frame)
        self.Load_frame.grid(row=0, column=0)
        self.Load_frame.grid_columnconfigure(1, weight=1)

        self.File_label = Label(self.Load_frame, text='File: ')
        self.File_label.grid(row=0, column=0, padx=2, pady=5)

        self.log_File_Path = StringVar()
        self.File_path = Label(self.Load_frame, textvariable=self.log_File_Path, width=40, anchor=W)
        self.File_path.grid(row=0, column=1, pady=5)

        self.Open_but = Button(self.Load_frame, text='Open', width=5)
        self.Open_but.grid(row=0, column=2, padx=10, pady=5)

        self.Data_frame = Frame(self.CS_frame)
        self.Data_frame.grid(row=1, column=0, sticky='nswe')
        self.Data_frame.grid_rowconfigure(1, weight=1)
        self.Data_frame.grid_columnconfigure(1, weight=1)


        self.Data_label = Label(self.Data_frame, text='File Data:', justify='left')
        self.Data_label.grid(row=0, column=0, padx=2, pady=5)

        self.Data_listbox = Listbox(self.Data_frame, selectmode=BROWSE)
        self.Data_listbox.grid(row=1, column=0, columnspan=2, sticky='nswe')
        self.Data_listbox_scrollbar = Scrollbar(self.Data_frame, orient='vertical')
        self.Data_listbox.config(yscrollcommand=self.Data_listbox_scrollbar.set)
        self.Data_listbox_scrollbar.config(command=self.Data_listbox.yview)
        self.Data_listbox_scrollbar.grid(row=1, column=3, sticky='ns')

        # -------------Bottom FRAME ---------------------------------------------
        self.botbut_frame.grid_rowconfigure(0, weight=1)
        self.botbut_frame.grid_rowconfigure(2, weight=1)

        self.botbut_frame.grid_columnconfigure(1, weight=1)

        self.can_but = Button(self.botbut_frame, text='Back', width=10)
        self.can_but.grid(row=1, column=0, padx=30, pady=15)

        self.classify_but = Button(self.botbut_frame, text='Classify', width=10)
        self.classify_but.grid(row=1, column=1, padx=30, pady=15)

        self.show_but = Button(self.botbut_frame, text='Show Model', width=12)
        self.show_but.grid(row=1, column=2, padx=30, pady=15)


if __name__ == "__main__":
    root = Tk()
    img = ""
    LoadScan_UI(root, img)
    mainloop()
