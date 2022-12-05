"""
This file contains all code for the extractors GUI. GUI consists of a central class (ExtractGUI) with several other
supporting classes that each contain the code for different types of widgets. All widget classes are instantiated by
the primary classes' constructor.
"""

import tkinter as tk
from vc_extractor import Extractor


class ExtractGUI:

    # Constructor, builds the GUI object and the widgets. Also sets GUI root parameters, and begins the main event
    # loop.
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('400x225')
        self.root.title('VC Extract 2')
        self.root.resizable(width=False, height=False)
        self.frame = ExtractFrame(self)
        self.entry_boxes = ExtractEntryBox(self)
        self.labels = ExtractLabels(self)
        self.buttons = ExtractButtons(self)
        self.root.mainloop()


class ExtractFrame:

    # Constructor builds the frame object and places it in the GUI root.
    def __init__(self, gui_obj):
        self.gui_obj = gui_obj
        self.main_frame = tk.Frame(self.gui_obj.root, bd=5)
        self.main_frame.place(anchor='nw', width=400, height=225)


class ExtractEntryBox:

    # Constructor builds the entry box objects and places them in the GUI root.
    def __init__(self, gui_obj):
        self.gui_obj = gui_obj
        self.pass_box = tk.Entry(self.gui_obj.frame.main_frame, width=25,  show='*')
        self.pass_box.place(anchor='nw', x=200, y=25)
        self.vc_num_box = tk.Entry(self.gui_obj.frame.main_frame, width=25)
        self.vc_num_box.place(anchor='nw', x=200, y=75)


class ExtractLabels:

    # Constructor builds the label objects and places them in the GUI root.
    def __init__(self, gui_obj):
        self.gui_obj = gui_obj
        self.pass_label = tk.Label(self.gui_obj.frame.main_frame, text="Vcommerce Password:")
        self.pass_label.place(anchor='nw', x=40, y=25)
        self.vc_num_label = tk.Label(self.gui_obj.frame.main_frame, text="Vcommerce Number:")
        self.vc_num_label.place(anchor='nw', x=40, y=75)
        self.status_label = tk.Label(self.gui_obj.frame.main_frame, text='Extract Ready')
        self.status_label.place(anchor='nw', x=150, y=110)
        self.load_label = tk.Label(self.gui_obj.frame.main_frame, text='')
        self.load_label.place(anchor='nw', x=125, y=110)


class ExtractButtons:

    # Constructor builds the button objects and places them in the GUI root.
    def __init__(self, gui_obj):
        self.extractor_obj = None
        self.gui_obj = gui_obj
        self.extract_button = tk.Button(self.gui_obj.frame.main_frame, text="Extract", width=20,
                                        command=self.press_extract)
        self.extract_button.place(anchor="nw", x=25, y=175)
        self.quit_button = tk.Button(self.gui_obj.frame.main_frame, text='Quit', width=20, command=self.press_quit)
        self.quit_button.place(anchor="nw", x=200, y=175)

    # Closes the webdriver and then the GUI
    def press_quit(self):
        self.gui_obj.root.destroy()

    # Takes the data from the password and vc_number entry boxes and uses them as the arguments to build the
    # extractor object. Once build, the extract() method is called, and then the webdriver is closed again.
    def press_extract(self):
        # noinspection PyBroadException
        try:
            vc_password = self.gui_obj.entry_boxes.pass_box.get()
            vc_number = self.gui_obj.entry_boxes.vc_num_box.get()
            self.gui_obj.labels.status_label.config(text="Extracting...")
            self.gui_obj.root.update()
            self.extractor_obj = Extractor(vc_password, vc_number)
            self.extractor_obj.extract()
            self.extractor_obj.chromedriver_close()
            self.gui_obj.entry_boxes.vc_num_box.delete(0, 'end')
            self.gui_obj.labels.status_label.config(text="Extract Completed")
            self.gui_obj.root.update()
        except Exception:
            self.gui_obj.labels.status_label.config(text="Error Detected")
            self.gui_obj.root.update()
