"""
This file contains all code for the extractors GUI. GUI consists of a central class (ExtractGUI) with several other
supporting classes that each contain the code for different types of widgets. All widget classes are instantiated by
the primary classes' constructor.
"""

import tkinter as tk
from vc_extractor import Extractor
from vc_approval import Approval
from vc_update import Updater


class ExtractGUI:

    # Constructor, builds the GUI object and the widgets. Also sets GUI root parameters, and begins the main event
    # loop.
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('400x225')
        self.root.title('VC Extract 2 - Extraction Mode')
        self.root.resizable(width=False, height=False)
        self.main_menu = MenuBar(self)
        self.frame = ExtractFrame(self)
        self.entry_boxes = ExtractEntryBox(self)
        self.labels = ExtractLabels(self)
        self.buttons = ExtractButtons(self)
        self.listbox = None
        self.root.mainloop()


class MenuBar:

    def __init__(self, gui_obj):
        self.gui_obj = gui_obj
        self.menu_bar = tk.Menu(self.gui_obj.root)
        self.file = tk.Menu(self.menu_bar, tearoff=0)
        self.file.add_command(label='Approval Mode', command=self.click_approval)
        self.file.add_command(label='Extraction Mode', command=self.click_extraction)
        self.file.add_command(label='Update Mode', command=self.click_update)
        self.menu_bar.add_cascade(label='File', menu=self.file)
        self.menu_bar.add_cascade(label='Error Log')
        self.gui_obj.root.config(menu=self.menu_bar)

    def click_extraction(self):
        self.gui_obj.root.title('VC Extract 2 - Extraction Mode')
        self.gui_obj.frame = ExtractFrame(self.gui_obj)
        self.gui_obj.entry_boxes = ExtractEntryBox(self.gui_obj)
        self.gui_obj.labels = ExtractLabels(self.gui_obj)
        self.gui_obj.buttons = ExtractButtons(self.gui_obj)
        self.gui_obj.root.update()

    def click_approval(self):
        self.gui_obj.root.title('VC Extract 2 - Approval Mode')
        self.gui_obj.frame = ApproveFrame(self.gui_obj)
        self.gui_obj.listbox = ApproveListBox(self.gui_obj)
        self.gui_obj.buttons = ApproveButtons(self.gui_obj)
        self.gui_obj.root.update()

    def click_update(self):
        self.gui_obj.root.title('VC Extract 2 - Update Mode')
        self.gui_obj.frame = UpdateFrame(self.gui_obj)
        self.gui_obj.labels = UpdateLabels(self.gui_obj)
        self.gui_obj.entry_boxes = UpdateEntryBox(self.gui_obj)
        self.gui_obj.buttons = UpdateButtons(self.gui_obj)
        self.gui_obj.root.update()


class ExtractFrame:

    # Constructor builds the extraction frame object and places it in the GUI root.
    def __init__(self, gui_obj):
        self.gui_obj = gui_obj
        self.main_frame = tk.Frame(self.gui_obj.root, bd=5)
        self.main_frame.place(anchor='nw', width=400, height=225)


class ApproveFrame:

    # Constructor builds the approval frame object and places it in the GUI root.
    def __init__(self, gui_obj):
        self.gui_obj = gui_obj
        self.main_frame = tk.Frame(self.gui_obj.root, bd=5)
        self.main_frame.place(anchor='nw', width=400, height=225)


class UpdateFrame:

    # Constructor builds the approval frame object and places it in the GUI root.
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


class UpdateEntryBox:

    # Constructor builds the entry box objects and places them in the GUI root.
    def __init__(self, gui_obj):
        self.gui_obj = gui_obj
        self.pass_box = tk.Entry(self.gui_obj.frame.main_frame, width=25, show='*')
        self.pass_box.place(anchor='nw', x=200, y=25)
        self.count_box = tk.Entry(self.gui_obj.frame.main_frame, width=25)
        self.count_box.place(anchor='nw', x=200, y=75)


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


class UpdateLabels:

    def __init__(self, gui_obj):
        self.gui_obj = gui_obj
        self.pass_label = tk.Label(self.gui_obj.frame.main_frame, text='Vcommerce Password:')
        self.pass_label.place(anchor='nw', x=40, y=25)
        self.count_label = tk.Label(self.gui_obj.frame.main_frame, text='Update Count:')
        self.count_label.place(anchor='nw', x=40, y=75)
        

class ApproveListBox:

    def __init__(self, gui_obj):
        self.gui_obj = gui_obj
        self.approval_list = tk.Listbox(self.gui_obj.frame.main_frame, height=9, width=60)
        self.approval_list.place(anchor='nw', x=10, y=10)


class ExtractButtons:

    # Constructor builds the button objects and places them in the GUI root.
    def __init__(self, gui_obj):
        self.extractor_obj = None
        self.gui_obj = gui_obj
        self.new_extract_button = tk.Button(self.gui_obj.frame.main_frame, text="New Extract", width=12,
                                            command=self.press_new_extract)
        self.new_extract_button.place(anchor="nw", x=25, y=175)
        self.existing_extract_button = tk.Button(self.gui_obj.frame.main_frame, text="Existing Extract", width=12,
                                                 command=self.press_exist_extract)
        self.existing_extract_button.place(anchor='nw', x=150, y=175)
        self.quit_button = tk.Button(self.gui_obj.frame.main_frame, text='Quit', width=12, command=self.press_quit)
        self.quit_button.place(anchor="nw", x=275, y=175)

    # Closes the webdriver and then the GUI
    def press_quit(self):
        self.gui_obj.root.destroy()

    # Takes the data from the password and vc_number entry boxes and uses them as the arguments to build the
    # extractor object. Once build, the extract() method is called, and then the webdriver is closed again.
    def press_new_extract(self):
        # noinspection PyBroadException
        try:
            vc_password = self.gui_obj.entry_boxes.pass_box.get()
            vc_number = self.gui_obj.entry_boxes.vc_num_box.get()
            self.gui_obj.labels.status_label.config(text="Extracting...")
            self.gui_obj.root.update()
            self.extractor_obj = Extractor(vc_password, vc_number)
            self.extractor_obj.extract_new()
            self.extractor_obj.chromedriver_close()
            self.gui_obj.entry_boxes.vc_num_box.delete(0, 'end')
            self.gui_obj.labels.status_label.config(text="Extract Completed")
            self.gui_obj.root.update()
        except Exception:
            self.gui_obj.labels.status_label.config(text="Error Detected")
            self.gui_obj.root.update()

    def press_exist_extract(self):
        # noinspection PyBroadException
        try:
            vc_password = self.gui_obj.entry_boxes.pass_box.get()
            vc_number = self.gui_obj.entry_boxes.vc_num_box.get()
            self.gui_obj.labels.status_label.config(text="Extracting...")
            self.gui_obj.root.update()
            self.extractor_obj = Extractor(vc_password, vc_number)
            self.extractor_obj.extract_existing()
            self.extractor_obj.chromedriver_close()
            self.gui_obj.entry_boxes.vc_num_box.delete(0, 'end')
            self.gui_obj.labels.status_label.config(text="Extract Completed")
            self.gui_obj.root.update()
        except Exception:
            self.gui_obj.labels.status_label.config(text="Error Detected")
            self.gui_obj.root.update()


class ApproveButtons:

    def __init__(self, gui_obj):
        self.gui_obj = gui_obj
        self.approval_obj = None
        self.previous_approval_names = []
        self.confirm_update_button = tk.Button(self.gui_obj.frame.main_frame, text="Confirm Vendors Approved",
                                               command=self.press_confirm, state="disabled")
        self.confirm_update_button.place(anchor='nw', x=10, y=175)
        self.load_export_button = tk.Button(self.gui_obj.frame.main_frame, text="Load Export", command=self.press_load)
        self.load_export_button.place(anchor="nw", x=182, y=175)
        self.quit_button = tk.Button(self.gui_obj.frame.main_frame, text='Quit', width=12, command=self.press_quit)
        self.quit_button.place(anchor="nw", x=275, y=175)

    # Closes the webdriver and then the GUI
    def press_quit(self):
        self.gui_obj.root.destroy()

    def press_load(self):
        self.approval_obj = Approval()
        self.approval_obj.get_approval_list()
        for row in self.approval_obj.approval_worksheet:
            approved_vendor_name = row[1].value
            self.previous_approval_names.append(approved_vendor_name)
        for count, item in enumerate(self.approval_obj.approved_vendor_list):
            vc_number, vendor_name = item
            if vendor_name not in self.previous_approval_names:
                self.gui_obj.listbox.approval_list.insert(count, vendor_name)
        self.confirm_update_button.config(state="normal")

    def press_confirm(self):
        self.approval_obj.confirm_approval()
        self.approval_obj.format_and_save_excel()
        self.gui_obj.listbox.approval_list.delete(0, 'end')
        self.confirm_update_button.config(state="disabled")


class UpdateButtons:

    def __init__(self, gui_obj):
        self.gui_obj = gui_obj
        self.quit_button = tk.Button(self.gui_obj.frame.main_frame, text='Quit', width=12, command=self.press_quit)
        self.quit_button.place(anchor='nw', x=275, y=175)
        self.pull_button = tk.Button(self.gui_obj.frame.main_frame, text='Pull Updates', width=12, command=self.press_update)
        self.pull_button.place(anchor='nw', x=25, y=175)

    def press_quit(self):
        self.gui_obj.root.destroy()

    def press_update(self):
        vc_password = self.gui_obj.entry_boxes.pass_box.get()
        update_count = self.gui_obj.entry_boxes.count_box.get()
        updater = Updater(vc_password, update_count)
        updater.prep_update()
        updater.process_update()
        updater.chromedriver_close()
        self.gui_obj.entry_boxes.count_box.delete(0, 'end')


