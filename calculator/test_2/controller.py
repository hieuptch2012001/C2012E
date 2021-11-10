
from view import View


class Controller:

    def __init__(self):
        self.display = View()
        self.setup_button()
        self.a = ""
        self.b = ""

    def setup_button(self):
        for btn in self.display.buttons:
            btn['command'] = (lambda txt=btn['text']: self.button_action(txt))

    def button_action(self, text):
        self.display.current_expression += text

    def update_label(self):
        self.display.result_label.config(
            text=self.display.current_expression[:10])

    def update_total_label(self):
        expression = self.display.total_expression
        self.display.equation_label.config(text=expression)

    def check_input(self):
        pass

    def create_expression(self, text):
        pass

    def start_app(self):
        self.display.init_display()


def main():
    controller = Controller()
    controller.start_app()


if __name__ == '__main__':
    main()
