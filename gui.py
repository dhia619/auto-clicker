from tkinter import ttk
from tkinter import *

class AppGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Auto Clicker")

        #styles
        style = ttk.Style()
        style.configure("TLabel", font=("courier", 13))
        style.configure("TButton", font=("courier", 15))
        style.configure("TEntry", font=("courier", 13))
        style.configure("TCombobox", font=("courier", 13))
        style.configure("TRadiobutton", font=("courier", 13))

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
        self.click_options_frame.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

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
        self.click_repeat_frame.grid(row=1, column=1, padx=10, pady=5)
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
        self.cursor_position_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

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
        self.start_button = ttk.Button(self.root, text="Start")
        self.start_button.grid(row=3, column=0, padx=5, pady=5,sticky="ew")

        self.stop_button = ttk.Button(self.root, text="Stop")
        self.stop_button.grid(row=3, column=1, padx=5, pady=5,sticky="ew")

        self.help_button = ttk.Button(self.root, text="Help")
        self.help_button.grid(row=4, column=0, padx=5, pady=5, sticky="ew")

        # Center the window after it's displayed
        self.root.update_idletasks()  # Update "requested size" from geometry manager
        self.center_window()

        self.root.mainloop()

    def center_window(self):
        # Get the width and height of the window
        window_width = self.root.winfo_width()
        window_height = self.root.winfo_height()
        
        # Get the width and height of the screen
        monitor_width = self.root.winfo_screenwidth()
        monitor_height = self.root.winfo_screenheight()

        # Calculate x and y coordinates to center the window
        x = (monitor_width // 2) - (window_width // 2)
        y = (monitor_height // 2) - (window_height // 2)

        # Set the geometry of the window to center it
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")