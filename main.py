from gui import *
from pyautogui import *
import time

class Application:
    def __init__(self):
        self.gui = AppGUI()
        self.gui.start_button.configure(command=self.start)
        self.gui.pick_position_button.configure(command=self.pick_location)
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
                    self.start_timed_clicking(x_cord, y_cord, mouse_button, click_type)
            else:
                self.gui.show_alert_message("error", "Empty Field", "Please select the repeat mode")

    def start_continuous_clicking(self,x_cord,y_cord,times,button,click_type):
        self.gui.window.withdraw()
        for t in range(times):
            self.perform_click(button,click_type,x_cord,y_cord)
        self.gui.show_alert_message("success","Finished","Clicking Task is complete")
        self.gui.window.deiconify()

    def start_timed_clicking(self, x_cord, y_cord, button, click_type):
        # Get time interval values
        hours = int(self.gui.hours_entry.get())
        minutes = int(self.gui.minutes_entry.get())
        seconds = int(self.gui.seconds_entry.get())
        milliseconds = int(self.gui.milliseconds_entry.get())

        total_time_in_seconds = hours * 3600 + minutes * 60 + seconds + milliseconds / 1000
        
        self.gui.window.withdraw()
        # Perform clicking until time runs out
        start_time = time.time()
        while time.time() - start_time < total_time_in_seconds:
            self.perform_click(button, click_type, x_cord, y_cord)

        self.gui.show_alert_message("success", "Finished", "Timed clicking task is complete")
        self.gui.window.deiconify()

    def perform_click(self,button,click_type,x_cord,y_cord):
        if click_type == "Single":
            click(x=x_cord, y=y_cord, button=button)
        elif click_type == "Double":
            click(x=x_cord, y=y_cord, button=button, clicks=2, interval=0.1)

    def pick_location(self):
        # Minimize the window to allow the user to pick a location on screen
        self.gui.window.withdraw()

        sleep(5)  # Wait for 5 seconds while the user positions the mouse

        # Capture the mouse position
        x, y = position()

        # Update the GUI with the captured position
        self.gui.x_entry.delete(0, END)
        self.gui.y_entry.delete(0, END)
        self.gui.x_entry.insert(0, str(x))
        self.gui.y_entry.insert(0, str(y))

        # Restore the window after capturing the position
        self.gui.window.deiconify()

if __name__ == "__main__":
    app = Application()
