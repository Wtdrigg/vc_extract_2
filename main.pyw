"""
The purpose of this program is to automate some common data entry tasks associated with new vendor registration.
In order for this file to work you simply need to copy the vendors Vcommerce number into your clipboard and then run
the python file (or a packaged .exe created by pyinstaller)
"""

from main_GUI import ExtractGUI

# This is the main script, it will call the ExtractGUI method from main_GUI.py. All program controls
# are handled by the GUI
if __name__ == '__main__':

    ExtractGUI()
