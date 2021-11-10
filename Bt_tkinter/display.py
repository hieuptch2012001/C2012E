import tkinter as tk
from tkinter import ttk


class Display():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tkinter")

        # Make the app responsive
        self.root.columnconfigure(index=0, weight=1)
        self.root.columnconfigure(index=1, weight=1)
        self.root.columnconfigure(index=2, weight=1)
        self.root.rowconfigure(index=0, weight=1)
        self.root.rowconfigure(index=1, weight=1)
        self.root.rowconfigure(index=2, weight=1)

        # Create a style
        style = ttk.Style(self.root)

        # Import the tcl file
        self.root.tk.call("source", "forest-light.tcl")

        # Set the theme with the theme_use method
        style.theme_use("forest-light")

        self.Create_frame()
        self.Crete_label_entry()
        self.Create_button()

    # Create a Frame for input widgets
    def Create_frame(self):
        self.widgets_frame = ttk.Frame(self.root, padding=(0, 0, 0, 10))
        self.widgets_frame.grid(row=0, column=1, padx=10, pady=(
            30, 10), sticky="nsew", rowspan=3)
        self.widgets_frame.columnconfigure(index=0, weight=1)

    # Create Label Entry
    def Crete_label_entry(self):
        # Entry Id
        label_id = ttk.Label(self.widgets_frame, text="ID")
        label_id.grid(row=0, column=0, padx=5, sticky="ew")
        entry_id = ttk.Entry(self.widgets_frame)
        entry_id.grid(row=0, column=1, padx=5, pady=(0, 10), sticky="ew")

        # Entry Password
        label_password = ttk.Label(self.widgets_frame, text="Password")
        label_password.grid(row=1, column=0, padx=5, sticky="ew")
        entry_password = ttk.Entry(self.widgets_frame)
        entry_password.grid(row=1, column=1, padx=5, pady=(0, 10), sticky="ew")

    # Button
    def Create_button(self):
        # Button B1
        self.button_b1 = ttk.Button(self.widgets_frame, text="B1")
        self.button_b1.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")

        # Button B2
        self.button_b2 = ttk.Button(self.widgets_frame, text="B2")
        self.button_b2.grid(row=2, column=1, padx=5, pady=10, sticky="nsew")

        # Button B3
        self.button_b3 = ttk.Button(self.widgets_frame, text="B3")
        self.button_b3.grid(row=2, column=2, padx=5, pady=10, sticky="nsew")

        # Button Sent
        self.button_sent = ttk.Button(self.widgets_frame, text="Sent")
        self.button_sent.grid(row=2, column=3, padx=5, pady=10, sticky="nsew")

    # Start the main loop
    def run(self):
        self.root.mainloop()


def main():
    Start = Display()
    Start.run()


if __name__ == '__main__':
    main()
