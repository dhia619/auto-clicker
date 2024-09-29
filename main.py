from gui import *
from pyautogui import *

class Application:
    def __init__(self):
        self.gui = AppGUI()
        self.gui.root.mainloop()

if __name__ == "__main__":
    app = Application()