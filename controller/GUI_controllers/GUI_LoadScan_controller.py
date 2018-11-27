from tkinter import *
from tkinter.filedialog import askopenfilename
from view import LoadScan_UI
from view import main_frame
from model import ModelClassifier
from os import path


class LoadScan_controller:

    """
        The Chequing or savings GUI controller.
        It creates the Chequing or savings UI
        Contains functions that the UI's buttons will use.

        decides which account is subjected to the option of withdraw or deposit
    """


    def __init__(self, master):
        self.master = master
        self.img = './view/BCIT_Logo.png'


        main_frame.current_frame = LoadScan_UI(self.master, self.img)
        main_frame.current_frame.Open_but.config(command=lambda: self.openFile())
        main_frame.current_frame.can_but.config(command=lambda: self.Exit())

    def openFile(self):
        filename = askopenfilename(initialdir=path.join(path.dirname(path.realpath(".")), "pyscan/model/scans"), title="Select a file")
        fname = filename.split('/')
        main_frame.current_frame.log_File_Path.set(fname[-1])
        classifier = ModelClassifier(filename)
        self.output_classifier(classifier)

    @staticmethod
    def output_classifier(classifier):
        fname = classifier.filename.split('/')
        main_frame.current_frame.Data_listbox.insert(END, "Loading file: {}".format(fname[-1]))
        main_frame.current_frame.Data_listbox.insert(END, "Processing...")
        classifier.classify()
        main_frame.current_frame.Data_listbox.insert(END, "{0} is a {1:.2f}% match!".format(classifier.results[0], classifier.results[1]))
        classifier.show_histogram(classifier.existing_data, classifier.data, classifier.results[0])


    def Exit(self):
        from .GUI_LoadGet_controller import LoadGet_controller
        LoadGet_controller(self.master)


if __name__ == "__main__":
    root = Tk()
    frame = CorS_UI(root)
    ui = LoadGet_controller(root)
    mainloop()
