import tkinter as tk
from tkinter import ttk

def main():
    root = tk.Tk()

    buttons = [
            ['1/x','√','C','+'],
            ['7','8','9','-'],
            ['4','5','6','x'],
            ['1','2','3','÷'],
            ['+/-','0','.','=']
        ]
    
    # print (type(range(buttons)))
    rows = 5
    cols = 4

    for r in range(rows):
        root.rowconfigure(r, weight = 1)
    # for c in range(cols):
        if r == 4:
            break
        root.columnconfigure(r, weight = 1)

    button_text = tk.StringVar()

    for i in range(len(buttons)):
        for j in range(len(buttons[i])):
            print (buttons[i][j])
            button = ttk.Button(root, text=buttons[i][j])
            button.grid(row= i, column=j, sticky='nsew')

    root.mainloop()

if __name__ == '__main__':
    main()