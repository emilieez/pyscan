from tkinter import *
from .GUI_baseUI import UI


class login_UI(UI):

    """
        Login to Email UI
    """


    def __init__(self, master, img):
        super().__init__(master, img)


        # ------------------MID FRAME ----------------------------------
        self.mid_frame.grid_columnconfigure(0, weight=1)
        self.mid_frame.grid_columnconfigure(3, weight=1)
        # self.mid_frame.config(background='green')


        self.mid_frame.grid_rowconfigure(1, weight=1)

        self.header_label = Label(self.mid_frame, text='Enter Email', font=("TkDefaultFont", 12))
        self.header_label.grid(row=0, column=1, pady=10, columnspan=2)
        # self.model_list_frame.config(background='green')


        # #----------------ENTRY FRAME---------------------------------
        # makes boarders to center the input frame
        self.var = IntVar()
        self.var.set(0)

        self.account_frame = Frame(self.mid_frame)
        self.account_frame.grid(row=1, column=1, sticky='ns')
        # self.account_frame.config(background='red')
        self.account_frame.grid_rowconfigure(0, weight=1)
        self.account_frame.grid_rowconfigure(5, weight=1)

        self.account_label = Label(self.account_frame, text='Email :')
        self.account_entry = Entry(self.account_frame, width=30)
        self.pin_label = Label(self.account_frame, text='Password :')
        self.pin_entry = Entry(self.account_frame, width=30, show="*")
        self.login_but = Button(self.account_frame, text='Login', width=10)

        self.account_label.grid(row=1, column=0, sticky=E, padx=5, pady=5)
        self.account_entry.grid(row=1, column=1, sticky=E, padx=5, pady=5)
        self.pin_label.grid(row=2, column=0, sticky=E, padx=5, pady=5)
        self.pin_entry.grid(row=2, column=1, sticky=E, padx=5, pady=5)
        self.login_but.grid(row=3, column=1, padx=30, pady=5)

        self.model_list_frame = Frame(self.mid_frame)
        self.model_list_frame.grid(row=1, column=2, sticky='nsew')

        # self.model_list_frame.grid_rowconfigure(0, weight=1)
        self.model_list_frame.grid_rowconfigure(2, weight=2)
        # self.model_list_frame.grid_rowconfigure(3, weight=1)


        self.model_list_label = Label(self.model_list_frame, text='Model List')
        self.model_list = Listbox(self.model_list_frame, width=30, selectmode='multiple')
        self.model_list_scrollbar = Scrollbar(self.model_list_frame, orient='vertical')
        self.model_list.config(yscrollcommand=self.model_list_scrollbar.set)
        self.model_list_scrollbar.config(command=self.model_list.yview)

        self.model_list_label.grid(row=1, padx=5)
        self.model_list.grid(row=2, pady=5, sticky='ns')
        self.model_list_scrollbar.grid(row=2, column=1, sticky='ns')

        # self.radio_but_new = Radiobutton(self.account_frame, text="New Scans", variable=self.var, value=0, indicatoron=1)
        # self.radio_but_all = Radiobutton(self.account_frame, text="All Scans", variable=self.var, value=1, indicatoron=1)
        # self.radio_but_new.select()

        # self.radio_but_all.grid(row=4, column=3, sticky=E, padx=5, pady=10)
        # self.radio_but_new.grid(row=4, column=4, sticky=E, padx=5, pady=10)


        # -------------Bottom FRAME ---------------------------------------------
        self.botbut_frame.grid_rowconfigure(0, weight=1)
        self.botbut_frame.grid_rowconfigure(2, weight=1)

        self.botbut_frame.grid_columnconfigure(1, weight=1)

        self.can_but = Button(self.botbut_frame, text='Cancel', width=10)
        self.can_but.grid(row=1, column=0, padx=30, pady=15)

        self.get_but = Button(self.botbut_frame, text='Get Scans', width=10)
        self.get_but.grid(row=1, column=2, padx=30, pady=15)



if __name__ == "__main__":
    root = Tk()
    img = ""
    login_UI(root, img)
    mainloop()
