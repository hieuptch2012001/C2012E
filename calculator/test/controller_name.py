from view_name import Button


class Run:
    def __init__(self):
        self.gui = Button()

    def run_window(self):
        self.gui.mainloop()

    def button_action(self, text):
        print(text)
        self.a = self.a + str(text)
        if text == "=":
            print(eval(self.a[:-1]), "\n")
            self.a = ""


def main():
    run = Run()
    run.run_window()


if __name__ == '__main__':
    main()
