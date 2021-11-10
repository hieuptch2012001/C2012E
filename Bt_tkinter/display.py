import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Tkinter")

# Make the app responsive
root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)
root.columnconfigure(index=2, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=1)
root.rowconfigure(index=2, weight=1)

# Create a style
style = ttk.Style(root)

# Import the tcl file
root.tk.call("source", "forest-light.tcl")

# Set the theme with the theme_use method
style.theme_use("forest-light")

# Create a Frame for input widgets
widgets_frame = ttk.Frame(root, padding=(0, 0, 0, 10))
widgets_frame.grid(row=0, column=1, padx=10, pady=(
    30, 10), sticky="nsew", rowspan=3)
widgets_frame.columnconfigure(index=0, weight=1)

# Entry Id
label_id = ttk.Label(widgets_frame, text="ID")
label_id.grid(row=0, column=0, padx=5, sticky="ew")
entry_id = ttk.Entry(widgets_frame)
entry_id.grid(row=0, column=1, padx=5, pady=(0, 10), sticky="ew")

# Entry Password
label_password = ttk.Label(widgets_frame, text="Password")
label_password.grid(row=1, column=0, padx=5, sticky="ew")
entry_password = ttk.Entry(widgets_frame)
entry_password.grid(row=1, column=1, padx=5, pady=(0, 10), sticky="ew")

# Button B1
button_b1 = ttk.Button(widgets_frame, text="B1")
button_b1.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")

# Button B2
button_b2 = ttk.Button(widgets_frame, text="B2")
button_b2.grid(row=2, column=1, padx=5, pady=10, sticky="nsew")

# Button B3
button_b3 = ttk.Button(widgets_frame, text="B3")
button_b3.grid(row=2, column=2, padx=5, pady=10, sticky="nsew")

# Button Sent
button_b3 = ttk.Button(widgets_frame, text="Sent")
button_b3.grid(row=2, column=3, padx=5, pady=10, sticky="nsew")


# Start the main loop
root.mainloop()
