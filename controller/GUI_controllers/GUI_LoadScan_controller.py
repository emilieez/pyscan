from tkinter import *
from tkinter.filedialog import askopenfilename
from view import LoadScan_UI
from view import main_frame
from model import ModelClassifier
from os import path
from _thread import start_new_thread
from tkinter import messagebox


class LoadScan_controller:

    """
        Sets the Main controller to LoadScan
        contains functionalities for LoadScan.py
        Connects to the ModelClassifier.py
    """


    def __init__(self, master):
        self.master = master
        self.img = './view/BCIT_Logo.png'
        self.classifier = ''


        main_frame.current_frame = LoadScan_UI(self.master, self.img)
        main_frame.current_frame.Open_but.config(command=lambda: self.openFile())
        main_frame.current_frame.classify_but.config(command=lambda: start_new_thread(self.output_classifier,()))
        main_frame.current_frame.show_but.config(command=lambda: self.show_mesh())
        main_frame.current_frame.hist_but.config(command=lambda: self.show_histogram())
        main_frame.current_frame.can_but.config(command=lambda: self.Exit())

    def openFile(self):
        """
            Opens file explorer for user to input the desired scan for classification
        """

        filename = askopenfilename(initialdir=path.join(path.dirname(path.realpath(__file__)), "scans"), title="Select a file")
        if filename.split('.')[-1] == "ply" or filename.split('.')[-1] == 'obj':
            fname = filename.split('/')
            main_frame.current_frame.log_File_Path.set(fname[-1])
            main_frame.current_frame.Data_listbox.insert(END, "Loaded file: {}".format(fname[-1]))
            self.classifier = ModelClassifier(filename)
            main_frame.current_frame.hist_but.config(state=DISABLED)
            main_frame.current_frame.show_but.config(state=NORMAL)
        else:
            messagebox.showinfo("Error", "Please select a ply or obj file")

    def output_classifier(self):
        """
            Calls the classifier to process the input model
        """
        try:
            if self.classifier.mesh_object != "":
                main_frame.current_frame.Data_listbox.insert(END, "Processing...")
                self.classifier.classify()

                for idx in range(len(self.classifier.results[0])):
                    main_frame.current_frame.Data_listbox.insert(
                        END, "{0}: {1:.2f}%".format(
                            self.classifier.results[0][idx], self.classifier.results[1][idx]))
                main_frame.current_frame.Data_listbox.insert(END, "Match Results:")
                main_frame.current_frame.Data_listbox.insert(END, "It is a {}!".format(self.classifier.matching_shape))
                messagebox.showinfo("Success", "It is a {}!".format(self.classifier.matching_shape))
                main_frame.current_frame.hist_but.config(state = NORMAL)

        except:
            messagebox.showinfo("Error", "Please load a scan")

    def show_histogram(self):
        """
            Asynch does not work here for some reason
        """
        main_frame.current_frame.Data_listbox.insert(END, "Generating Histogram...")
        self.classifier.show_histogram(self.classifier.existing_data, self.classifier.data, self.classifier.matching_shape)


    def show_mesh(self):
        """
            Displays the model
        """
        self.classifier.mesh_object.show()

    def Exit(self):
        """
            Goes back to the LoadGet UI
        """
        from .GUI_LoadGet_controller import LoadGet_controller
        LoadGet_controller(self.master)


if __name__ == "__main__":
    root = Tk()
    frame = CorS_UI(root)
    ui = LoadGet_controller(root)
    mainloop()
