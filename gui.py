from tkinter import ttk
from tkinter import *
from tkinter import messagebox
class AppGUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Auto Clicker")

        #styles
        style = ttk.Style()
        style.configure("TLabel", font=("courier", 13))
        style.configure("TButton", font=("courier", 15))
        style.configure("TEntry", font=("courier", 13))
        style.configure("TCombobox", font=("courier", 13))
        style.configure("TRadiobutton", font=("courier", 13))

        
        self.root = ttk.Frame(self.window)
        self.root.grid(row=0,column=0,sticky="nswe")


        # Add grid weights for dynamic resizing
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_rowconfigure(3, weight=1)


        # Click Interval Group
        self.click_interval_frame = ttk.LabelFrame(self.root, text="Click Interval", padding=(10, 5))
        self.click_interval_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

        self.hours_label = ttk.Label(self.click_interval_frame, text="hours")
        self.hours_label.grid(row=0, column=1)
        self.hours_entry = ttk.Entry(self.click_interval_frame, width=5)
        self.hours_entry.grid(row=0, column=0, padx=5)

        self.minutes_label = ttk.Label(self.click_interval_frame, text="mins")
        self.minutes_label.grid(row=0, column=3)
        self.minutes_entry = ttk.Entry(self.click_interval_frame, width=5)
        self.minutes_entry.grid(row=0, column=2, padx=5)

        self.seconds_label = ttk.Label(self.click_interval_frame, text="secs")
        self.seconds_label.grid(row=0, column=5)
        self.seconds_entry = ttk.Entry(self.click_interval_frame, width=5)
        self.seconds_entry.grid(row=0, column=4, padx=5)

        self.milliseconds_label = ttk.Label(self.click_interval_frame, text="milliseconds")
        self.milliseconds_label.grid(row=0, column=7)
        self.milliseconds_entry = ttk.Entry(self.click_interval_frame, width=5)
        self.milliseconds_entry.grid(row=0, column=6, padx=5)

        # Click Options Group
        self.click_options_frame = ttk.LabelFrame(self.root, text="Click Options", padding=(10, 5))
        self.click_options_frame.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")

        self.mouse_button_label = ttk.Label(self.click_options_frame, text="Mouse Button:")
        self.mouse_button_label.grid(row=0, column=0, pady=5, sticky="w")
        self.mouse_button_combo = ttk.Combobox(self.click_options_frame, width=7, values=["Left", "Right", "Middle"])
        self.mouse_button_combo.grid(row=0, column=1, pady=5 ,padx=5)

        self.click_type_label = ttk.Label(self.click_options_frame, text="Click Type:")
        self.click_type_label.grid(row=1, column=0, pady=5, sticky="w")
        self.click_type_combo = ttk.Combobox(self.click_options_frame, width=7, values=["Single", "Double"])
        self.click_type_combo.grid(row=1, column=1, pady=5 ,padx=5)

        #Click repeat Group
        self.click_repeat_mode = IntVar()
        self.click_repeat_frame = ttk.LabelFrame(self.root, text="Click repeat")
        self.click_repeat_frame.grid(row=1, column=1, padx=10, pady=5, sticky="nsew")
        self.repeat_radio = ttk.Radiobutton(self.click_repeat_frame, text="Repeat", variable=self.click_repeat_mode, value=1)
        self.repeat_radio.grid(row=0, column=0, pady=5, sticky="w")
        self.num_clicks_entry = ttk.Entry(self.click_repeat_frame, width=10)
        self.num_clicks_entry.grid(row=0,column=1, pady=5, sticky="w")
        self.num_clicks_label = ttk.Label(self.click_repeat_frame, text="times")
        self.num_clicks_label.grid(row=0, column=2, pady=5, sticky="w")
        self.repeat_time_interval_radio = ttk.Radiobutton(self.click_repeat_frame, text="Use time interval", variable=self.click_repeat_mode, value=2)
        self.repeat_time_interval_radio.grid(row=1, column=0, columnspan=3, sticky="w")

        # Cursor Position Group
        self.cursor_position_frame = ttk.LabelFrame(self.root, text="Cursor Position", padding=(10, 5))
        self.cursor_position_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

        self.pick_position_button = ttk.Button(self.cursor_position_frame, text="Pick Location")
        self.pick_position_button.grid(row=0, column=0)

        self.x_label = ttk.Label(self.cursor_position_frame, text="X")
        self.x_label.grid(row=0, column=1, padx=5)
        self.x_entry = ttk.Entry(self.cursor_position_frame, width=5)
        self.x_entry.grid(row=0, column=2, padx=5)
        self.y_label = ttk.Label(self.cursor_position_frame, text="Y")
        self.y_label.grid(row=0, column=3, padx=5)
        self.y_entry = ttk.Entry(self.cursor_position_frame, width=5)
        self.y_entry.grid(row=0, column=4, padx=5)

        # Buttons
        self.buttons_frame = ttk.LabelFrame(self.root)
        self.buttons_frame.grid(row=3,column=0, columnspan=2, padx=10, pady=10, sticky="ns")

        self.start_button = ttk.Button(self.buttons_frame, text="Start")
        self.start_button.grid(row=0, column=0, padx=5, pady=5,sticky="nsew")

        self.stop_button = ttk.Button(self.buttons_frame, text="Stop")
        self.stop_button.grid(row=0, column=1, padx=5, pady=5,sticky="nsew")

        self.help_button = ttk.Button(self.buttons_frame, text="Help")
        self.help_button.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

        # Center the window after it's displayed
        self.window.update_idletasks()  # Update "requested size" from geometry manager
        self.center_window()

    def center_window(self):
        # Get the width and height of the window
        window_width = self.window.winfo_width()
        window_height = self.window.winfo_height()
        
        # Get the width and height of the screen
        monitor_width = self.window.winfo_screenwidth()
        monitor_height = self.window.winfo_screenheight()

        # Calculate x and y coordinates to center the window
        x = (monitor_width // 2) - (window_width // 2)
        y = (monitor_height // 2) - (window_height // 2)

        # Set the geometry of the window to center it
        self.window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def show_alert_message(self,alert_type,title,msg):
        if alert_type == "error":
            messagebox.showerror(title,msg)
        elif alert_type == "warning":
            messagebox.showwarning(title,msg)
        elif alert_type == "success":
            messagebox.showinfo(title,msg)

    # Helper function to validate numeric input
    def is_numeric(self, value, field_name):
        if value.strip() == "":
            self.show_alert_message("error", "Missing value", f"Please enter the number of {field_name}")
            return False
        elif not value.isnumeric():
            self.show_alert_message("error", "Invalid value", f"{field_name.capitalize()} should only contain numbers")
            return False
        return True
    
    def is_valid(self, value, allowed_values, field_name):
        if value.strip() == "":
            self.show_alert_message("error", "Missing value", f"Please choose a {field_name}")
            return False
        elif value.lower() not in allowed_values:
            self.show_alert_message("error", "Invalid value", f"{field_name.capitalize()} should be one of these {allowed_values}")
            return False
        return True

    def time_interval_is_valid(self):
        hours = self.hours_entry.get()
        minutes = self.minutes_entry.get()
        seconds = self.seconds_entry.get()
        milliseconds = self.milliseconds_entry.get()

        # Validate each input using helper function
        return (self.is_numeric(hours, "hours") and
                self.is_numeric(minutes, "minutes") and
                self.is_numeric(seconds, "seconds") and
                self.is_numeric(milliseconds, "milliseconds"))

    def picked_location_is_valid(self):
        x = self.x_entry.get()
        y = self.y_entry.get()

        if x.strip() == "" or y.strip() == "":
            self.show_alert_message("error", "Missing value", "Please pick a location")
            return False
        elif not(x.isnumeric()) or not(y.isnumeric()):
            self.show_alert_message("error", "Invalid value", "Location must be numeric")
            return False
        return True

    def click_options_is_valid(self):
        mouse_button = self.mouse_button_combo.get()
        click_type = self.click_type_combo.get()
        return (self.is_valid(mouse_button,("left","middle","right"),"mouse button")
                and self.is_valid(click_type,("single","double"),"click type"))