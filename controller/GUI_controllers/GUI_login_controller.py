
from tkinter import *
import os
import sys

from tkinter import messagebox

# from model.GUI_model.GUI_login_model import login_model
from view import login_UI
from view import main_frame

# from .GUI_option_controller import option_controller

from model import MailParser

class login_controller:

    """
        The login GUI controller.
        Contains functionalities for the login UI
        Connects to the MailParser.py
    """

    def __init__(self, master):
        self.master = master
        self.img = './view/BCIT_Logo.png'

        main_frame.current_frame = login_UI(self.master, self.img)

        main_frame.current_frame.login_but.config(command=self._login)
        main_frame.current_frame.can_but.config(command=lambda: self.exit())
        main_frame.current_frame.get_but.config(command=lambda: self.select_models())
        # main_frame.current_frame.radio_but_new.config(command=lambda: main_frame.current_frame.var.set(0))
        # main_frame.current_frame.radio_but_all.config(command=lambda: main_frame.current_frame.var.set(1))

    def _login(self):
        """
            Gets the input for mail login and logs in
            Displays error based on returned mail parser functions

            Inserts fetched models from email into the listbox
        """
        user_email = str(main_frame.current_frame.account_entry.get())
        user_pass = str(main_frame.current_frame.pin_entry.get())
        # scan_type = str(main_frame.current_frame.var.get())
        
        if user_email == "" or user_pass == "":
            messagebox.showinfo("Error", "Please Enter Email or Password")
        else:
            try:
                self.mail = MailParser(user_email, user_pass)
                mail_list = self.mail.get_scan()
                self.mail_message = mail_list[2]
                self.mail_box = mail_list[-1]
                if len(mail_list[1]) == 0:
                    messagebox.showinfo("Success", 'There are no scans to fetch')
                else:
                    for models in mail_list[1]:
                        main_frame.current_frame.model_list.insert(END, models)
                    messagebox.showinfo("Success", 'Scans have been fetched')
            except:
                if self.mail.error == "Please use an Outlook email or Gmail":
                    messagebox.showinfo("Error", "Please use an Outlook email or Gmail")
                elif self.mail.error == 'Invalid Host Address':
                    messagebox.showinfo("Error", 'Invalid Host Address')
                elif self.mail.error == 'Incorrect Email or Password':
                    messagebox.showinfo("Error", 'Incorrect Email or Password')
                elif self.mail.error == "Unable to connect to Email service":
                    messagebox.showinfo("Error", "Unable to connect to Email service")



    def exit(self):
        """
            goes back to LoadGet UI
            Logs out of email if connected
        """
        from .GUI_LoadGet_controller import LoadGet_controller
        LoadGet_controller(self.master)
        self.mail.logout(self.mail_box)

    def select_models(self):
        """
            Stores a list of selected models in the list box.
            The Get Scans button will fetch all scans selected/saved in the list
            Message will show the root directory of pyscan file as well as /model/scans
                this is where the files are saved to
        """
        selected_models =[]
        val = main_frame.current_frame.model_list.curselection()
        for i, v in enumerate(val):
            selected_models.append(main_frame.current_frame.model_list.get(val[i]))
        self.mail.downloadAttachments(self.mail_message, selected_models)
        messagebox.showinfo("Success", 'Scans are saved in ' + os.path.dirname(sys.modules['__main__'].__file__) + "/model/scans")
        self.mail.logout(self.mail_box)


if __name__ == "__main__":
    # root = Tk()
    frame = login_UI()
    # ui = login_controller(root, frame)
    mainloop()