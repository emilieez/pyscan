from tkinter import *

from view import LoadGet_UI
from view import main_frame

from .GUI_login_controller import login_controller
from .GUI_LoadScan_controller import LoadScan_controller


class LoadGet_controller:

    """
        The first UI's controller.
        Contains the functions for the LoadGetUI.py buttons

        decides which option is selected:
            Fetch: fetches scans from email
            Load: loads a scan for classifications
    """


    def __init__(self, master):
        self.master = master
        self.img = './view/BCIT_Logo.png'


        main_frame.current_frame = LoadGet_UI(self.master, self.img)

        main_frame.current_frame.get_but.config(command=lambda: self.openEmail())
        main_frame.current_frame.load_but.config(command=lambda: self.openLoad())

        # main_frame.current_frame.load_but.config(command=lambda: self.To_withdraw_save(self.option))
        main_frame.current_frame.can_but.config(command=lambda: self.Exit())



    def openEmail(self):
        """
            Changes the main controller into login_controller.
            For logging into email to fetch scans
        """
        login_controller(self.master)



    def openLoad(self):
        """
            Changes the main controller into LoadScan_controller.
            For model classification
        """
        LoadScan_controller(self.master)



    def Exit(self):
        """
            closes the UI
        """
        self.master.master.destroy()

if __name__ == "__main__":
    root = Tk()
    frame = CorS_UI(root)
    ui = LoadGet_controller(root)
    mainloop()
