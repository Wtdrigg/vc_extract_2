"""
The purpose of this program is to automate some common data entry tasks associated with new vendor registration.
This file has a .pyw extension which hides the console, which is useful when using the GUI. In order to display 
the console run Main.py instead. See INSTRUCTIONS.txt for more info on how to run.
"""

from main_GUI import ExtractGUI

# This is the main script, it will call the ExtractGUI method from main_GUI.py. All program controls
# are handled by the GUI
if __name__ == '__main__':
    ExtractGUI()
