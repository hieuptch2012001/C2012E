import tkinter as tk
from tkinter import ttk
from os import system, name


class Button(tk.Tk):
    def __init__(self):
        super().__init__()

        self.button_count = -1
        self.buttons = []
        self.a = ""
        self.button_text = [
            '(', ')', 'C', '+',
            '7', '8', '9', '-',
            '4', '5', '6', '*',
            '1', '2', '3', '/',
            '+/-', '0', '.', '='
        ]
        self.create_button()

    def clear(self):

        # for windows
        if name == 'nt':
            _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

    def create_button(self):
        for i in range(5):
            for j in range(4):
                self.button_count += 1
                # print(self.button_count)
                self.buttons.append(tk.Button(
                    self, text=self.button_text[self.button_count], command=lambda x=self.button_count: self.print_button(x)))
                self.buttons[self.button_count].grid(row=i, column=j)

    def print_button(self, button):
        print(self.buttons[button]['text'])
        self.a = self.a + str(self.buttons[button]['text'])
        if self.buttons[button]['text'] == "=":
            print(eval(self.a[:-1]), "\n")
            self.a = ""
        elif self.buttons[button]['text'] == "C":
            self.clear()
            self.a = ""


def main():
    gui = Button()
    gui.mainloop()


if __name__ == '__main__':
    main()
