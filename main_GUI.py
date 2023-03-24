"""
This file contains all code for the extractors GUI. GUI consists of a central class (ExtractGUI) with several other
supporting classes that each contain the code for different types of widgets. All widget classes are instantiated by
the primary classes' constructor and each element can access the elements of every other widget class. This is made using
the tkinter module included with the Python Standard Library.
"""

import pickle
import tkinter as tk
from vendor_info import VendorInfo
from vc_extract_mode import Extract
from vc_approve_mode import Approve
from vc_update_mode import Update


class ExtractGUI:

    # Constructor, builds the GUI object and the widgets. Also sets GUI root parameters, and begins the main event
    # loop.
    def __init__(self):
        self.load_vendor_info()
        self.root = tk.Tk()
        self.root.geometry('400x225')
        self.root.title('VC Extract 2 - Extract Mode')
        self.root.resizable(width=False, height=False)
        self.main_menu = MenuBar(self)
        self.frame = Frame(self)
        self.entry_boxes = ExtractEntryBox(self)
        self.labels = ExtractLabels(self)
        self.buttons = ExtractButtons(self)
        self.listbox = None
        self.root.mainloop()

    def load_vendor_info(self):
        try:
            with open('J:/VC_Extract_Files/vendor_info.pkl', 'rb') as file:
                vendor_info_object = pickle.load(file)
                return vendor_info_object
        except FileNotFoundError:
            vendor_info_object = self.save_vendor_info()
            return vendor_info_object
        
    def save_vendor_info(self):
        vi = VendorInfo()
        with open('J:/VC_Extract_Files/vendor_info.pkl', 'wb') as file:
            pickle.dump(vi, file)
        return vi


class MenuBar:

    def __init__(self, gui_obj):
        self.gui_obj = gui_obj
        self.menu_bar = tk.Menu(self.gui_obj.root)
        self.file = tk.Menu(self.menu_bar, tearoff=0)
        self.info = tk.Menu(self.menu_bar, tearoff=0)
        self.file.add_command(label='Extract Mode', command=self.click_extract)
        self.file.add_command(label='Update Mode', command=self.click_update)
        self.file.add_command(label='Approve Mode', command=self.click_approve)
        self.info.add_command(label='States and Post Owners', command=self.click_states)
        self.menu_bar.add_cascade(label='File', menu=self.file)
        self.menu_bar.add_cascade(label='Vendor Info', menu=self.info)
        self.gui_obj.root.config(menu=self.menu_bar)

    def click_extract(self):
        self.gui_obj.root.title('VC Extract 2 - Extract Mode')
        self.gui_obj.frame = Frame(self.gui_obj)
        self.gui_obj.entry_boxes = ExtractEntryBox(self.gui_obj)
        self.gui_obj.labels = ExtractLabels(self.gui_obj)
        self.gui_obj.buttons = ExtractButtons(self.gui_obj)
        self.gui_obj.root.update()

    def click_update(self):
        self.gui_obj.root.title('VC Extract 2 - Update Mode')
        self.gui_obj.frame = Frame(self.gui_obj)
        self.gui_obj.labels = UpdateLabels(self.gui_obj)
        self.gui_obj.entry_boxes = UpdateEntryBox(self.gui_obj)
        self.gui_obj.buttons = UpdateButtons(self.gui_obj)
        self.gui_obj.root.update()

    def click_approve(self):
        self.gui_obj.root.title('VC Extract 2 - Approve Mode')
        self.gui_obj.frame = Frame(self.gui_obj)
        self.gui_obj.listbox = ApproveListBox(self.gui_obj)
        self.gui_obj.buttons = ApproveButtons(self.gui_obj)
        self.gui_obj.root.update()

    def click_states(self):
        self.gui_obj.root.title('VC Extract 2 - Edit States')
        self.gui_obj.frame = Frame(self.gui_obj)
        self.gui_obj.listbox = EditListBox(self.gui_obj)
        self.gui_obj.entrybox = EditEntryBox(self.gui_obj)
        self.gui_obj.labels = EditLabels(self.gui_obj)
        self.gui_obj.buttons = EditButtons(self.gui_obj)
        self.vendor_info = self.load_vendor_info()
        self.display_vendor_info()
        self.gui_obj.root.update()

    def load_vendor_info(self):
        with open('J:/VC_Extract_Files/vendor_info.pkl', 'rb') as file:
            vendor_info_object = pickle.load(file)
            return vendor_info_object
        
    def display_vendor_info(self):
        for count, item in enumerate(self.vendor_info.post_info.keys()):
            self.gui_obj.listbox.edit_list.insert(count, item)


class Frame:

    # Constructor builds the extraction frame object and places it in the GUI root.
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

class EditEntryBox:

    # Constructor builds the entry box objects and places them in the GUI root.
    def __init__(self, gui_obj):
        self.gui_obj = gui_obj
        self.edit_box = tk.Entry(self.gui_obj.frame.main_frame, width=25)
        self.edit_box.place(anchor='nw', x=200, y=75)
        self.division_edit_box = tk.Entry(self.gui_obj.frame.main_frame, width=25)
        self.division_edit_box.place(anchor='nw', x=200, y=125)


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
        self.status_label2 = tk.Label(self.gui_obj.frame.main_frame, text='Please make sure you can access the J Drive before using.')
        self.status_label2.place(anchor='nw', x=50, y=130)
        self.load_label = tk.Label(self.gui_obj.frame.main_frame, text='')
        self.load_label.place(anchor='nw', x=125, y=110)


class UpdateLabels:

    def __init__(self, gui_obj):
        self.gui_obj = gui_obj
        self.pass_label = tk.Label(self.gui_obj.frame.main_frame, text='Vcommerce Password:')
        self.pass_label.place(anchor='nw', x=40, y=25)
        self.count_label = tk.Label(self.gui_obj.frame.main_frame, text='Update Count:')
        self.count_label.place(anchor='nw', x=40, y=75)

class EditLabels:

    def __init__(self, gui_obj):
        self.gui_obj = gui_obj
        self.edit_label = tk.Label(self.gui_obj.frame.main_frame, text='...')
        self.edit_label.place(anchor='nw', x=200, y=0)

        self.division_label = tk.Label(self.gui_obj.frame.main_frame, text='...')
        self.division_label.place(anchor='nw', x=200, y=25)

        self.update_division_label = tk.Label(self.gui_obj.frame.main_frame, text='-Update Division-')
        self.update_division_label.place(anchor='nw', x=200, y=100)

        self.update_post_label = tk.Label(self.gui_obj.frame.main_frame, text='-Update Post Owner-')
        self.update_post_label.place(anchor='nw', x=200, y=50)
        

class ApproveListBox:

    def __init__(self, gui_obj):
        self.gui_obj = gui_obj
        self.approval_list = tk.Listbox(self.gui_obj.frame.main_frame, height=9, width=60)
        self.approval_list.place(anchor='nw', x=10, y=10)

class EditListBox:

    def __init__(self, gui_obj):
        self.gui_obj = gui_obj
        self.edit_list = tk.Listbox(self.gui_obj.frame.main_frame, height=9, width=30)
        self.edit_list.place(anchor='nw', x=10, y=10)


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
            self.extractor_obj = Extract(vc_password, vc_number)
            self.extractor_obj.extract_new()
            self.extractor_obj.chromedriver_close()
            self.gui_obj.entry_boxes.vc_num_box.delete(0, 'end')
            self.gui_obj.labels.status_label.config(text="Extract Completed")
            self.gui_obj.root.update()
        except Exception:
            self.gui_obj.labels.status_label.config(text="Error Detected - Manual Entry Required")
            self.gui_obj.root.update()

    def press_exist_extract(self):
        # noinspection PyBroadException
        try:
            vc_password = self.gui_obj.entry_boxes.pass_box.get()
            vc_number = self.gui_obj.entry_boxes.vc_num_box.get()
            self.gui_obj.labels.status_label.config(text="Extracting...")
            self.gui_obj.root.update()
            self.extractor_obj = Extract(vc_password, vc_number)
            self.extractor_obj.extract_existing()
            self.extractor_obj.chromedriver_close()
            self.gui_obj.entry_boxes.vc_num_box.delete(0, 'end')
            self.gui_obj.labels.status_label.config(text="Extract Completed")
            self.gui_obj.root.update()
        except Exception:
            self.gui_obj.labels.status_label.config(text="Error Detected - Manual Entry Required")
            self.gui_obj.root.update()


class ApproveButtons:

    def __init__(self, gui_obj):
        self.gui_obj = gui_obj
        self.approval_obj = None
        self.csv_names = []
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
        self.approval_obj = Approve()
        self.approval_obj.get_approval_list()
        for row in self.approval_obj.approval_csv_worksheet:
            if row[1].row != 1:
                approved_vendor_name = row[1].value
                self.csv_names.append(approved_vendor_name)
        for count, item in enumerate(self.csv_names):
            if item not in self.approval_obj.approved_vendor_list:
                self.gui_obj.listbox.approval_list.insert(count, item)
        self.confirm_update_button.config(state="normal")

    def press_confirm(self):
        self.approval_obj.confirm_approval()
        self.gui_obj.listbox.approval_list.delete(0, 'end')
        self.confirm_update_button.config(state="disabled")


class UpdateButtons:

    def __init__(self, gui_obj):
        self.gui_obj = gui_obj
        self.quit_button = tk.Button(self.gui_obj.frame.main_frame, text='Quit', width=12, command=self.press_quit)
        self.quit_button.place(anchor='nw', x=275, y=175)
        self.pull_button = tk.Button(self.gui_obj.frame.main_frame, text='Pull Updates', width=12,
                                     command=self.press_update)
        self.pull_button.place(anchor='nw', x=25, y=175)

    def press_quit(self):
        self.gui_obj.root.destroy()

    def press_update(self):
        vc_password = self.gui_obj.entry_boxes.pass_box.get()
        update_count = self.gui_obj.entry_boxes.count_box.get()
        updater = Update(vc_password, update_count)
        updater.prep_update()
        updater.process_update()
        updater.chromedriver_close()
        self.gui_obj.entry_boxes.count_box.delete(0, 'end')

class EditButtons:

    def __init__(self, gui_obj):
        self.state = ''
        self.gui_obj = gui_obj
        self.submit_edit_button = tk.Button(self.gui_obj.frame.main_frame, text='Update Post', width=12, command=self.press_submit)
        self.submit_edit_button.place(anchor='nw', x=275, y=175)
        self.submit_division_button = tk.Button(self.gui_obj.frame.main_frame, text='Update Division', width=12, command=self.press_submit_division)
        self.submit_division_button.place(anchor='nw', x=175, y=175)
        self.get_info_button = tk.Button(self.gui_obj.frame.main_frame, text='Open Selected', width=12, command=self.press_get)
        self.get_info_button.place(anchor='nw', x=75, y=175)

    def press_submit(self):
        try:
            post_name = self.gui_obj.entrybox.edit_box.get()
            info_entry =  self.gui_obj.main_menu.vendor_info.post_info[self.state]
            info_entry[2] = post_name
            with open('J:/VC_Extract_Files/vendor_info.pkl', 'wb') as file:
                pickle.dump(self.gui_obj.main_menu.vendor_info, file)
            self.press_get()
            self.gui_obj.entrybox.edit_box.delete(0, 'end')
            self.gui_obj.root.update()
        except KeyError:
            self.gui_obj.labels.edit_label.configure(text='No State Selected')
            self.gui_obj.labels.division_label.configure(text='No State Selected')

    def press_submit_division(self):
        try:
            post_name = self.gui_obj.entrybox.division_edit_box.get()
            info_entry =  self.gui_obj.main_menu.vendor_info.post_info[self.state]
            info_entry[1] = post_name
            with open('J:/VC_Extract_Files/vendor_info.pkl', 'wb') as file:
                pickle.dump(self.gui_obj.main_menu.vendor_info, file)
            self.press_get()
            self.gui_obj.entrybox.division_edit_box.delete(0, 'end')
            self.gui_obj.root.update()
        except KeyError:
            self.gui_obj.labels.edit_label.configure(text='No State Selected')
            self.gui_obj.labels.division_label.configure(text='No State Selected')

    def press_get(self):
        selection = self.gui_obj.listbox.edit_list.curselection()
        try:
            self.state = self.gui_obj.listbox.edit_list.get(selection[0])
            info = self.gui_obj.main_menu.vendor_info.post_info[self.state]
            self.gui_obj.labels.edit_label.configure(text=str(info[2]))
            self.gui_obj.labels.division_label.configure(text=str(info[1]))
        except IndexError:
            self.gui_obj.labels.edit_label.configure(text='No State Selected')
            self.gui_obj.labels.division_label.configure(text='No State Selected')
        
