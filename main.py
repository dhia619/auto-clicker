from gui import *
from pyautogui import *

class Application:
    def __init__(self):
        self.gui = AppGUI()
        self.gui.start_button.configure(command=self.start)
        self.gui.window.mainloop()

    def start(self):
        if self.gui.picked_location_is_valid() and self.gui.click_options_is_valid():
            repeat_mode = self.gui.click_repeat_mode.get()
            x_cord,y_cord = float(self.gui.x_entry.get()),float(self.gui.y_entry.get())
            mouse_button = self.gui.mouse_button_combo.get()
            click_type = self.gui.click_type_combo.get()
            if repeat_mode == 1:
                times = self.gui.num_clicks_entry.get()
                if self.gui.is_numeric(times,"times"):
                    self.start_continuous_clicking(x_cord,y_cord,int(times),mouse_button,click_type)
            elif repeat_mode == 2:
                if self.gui.time_interval_is_valid():
                    self.start_timed_clicking(x_cord,y_cord)
            else:
                self.gui.show_alert_message("error", "Empty Field", "Please select the repeat mode")

    def start_continuous_clicking(self,x_cord,y_cord,times,button,click_type):
        for t in range(times):
            self.perform_click(button,click_type,x_cord,y_cord)
        self.gui.show_alert_message("success","Finished","Clicking Task is complete")

    def start_timed_clicking(self):
        print("Starting timed clicking...")

    def perform_click(self,button,click_type,x_cord,y_cord):
        if click_type == "Single":
            click(x=x_cord, y=y_cord, button=button)
        elif click_type == "Double":
            click(x=x_cord, y=y_cord, button=button, clicks=2, interval=0.1)

if __name__ == "__main__":
    app = Application()
