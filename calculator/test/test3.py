from view_name import Button

class Run:
    def __init__(self):
        self.gui = Button()
        
    def run_window(self):
        self.gui.mainloop()

def main():
    run = Run()
    run.run_window()

if __name__ == '__main__':
    main()