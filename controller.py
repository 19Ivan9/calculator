from calculator_interface import Ui_MainWindow

class Controller:
    def __init__(self,window):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(window)
        self.ui.pushButton.clicked.connect(self.press_button('1'))
        self.ui.pushButton_2.clicked.connect(self.press_button('2'))
        self.ui.pushButton_3.clicked.connect(self.press_button('3'))
        self.ui.pushButton_4.clicked.connect(self.press_button('4'))
        self.ui.pushButton_5.clicked.connect(self.press_button('5'))
        self.ui.pushButton_6.clicked.connect(self.press_button('6'))
        self.ui.pushButton_7.clicked.connect(self.press_button('7'))
        self.ui.pushButton_8.clicked.connect(self.press_button('8'))
        self.ui.pushButton_9.clicked.connect(self.press_button('9'))
        self.ui.pushButton_10.clicked.connect(self.press_button('0'))
        self.ui.pushButton_11.clicked.connect(self.press_button('+'))
        self.ui.pushButton_12.clicked.connect(self.press_button('-'))
        self.ui.pushButton_13.clicked.connect(self.equal)
        self.ui.pushButton_14.clicked.connect(self.press_button('/'))
        self.ui.pushButton_15.clicked.connect(self.press_button('*'))
        self.ui.pushButton_16.clicked.connect(self.clear_console)
        self.ui.pushButton_17.clicked.connect(self.calc_exit)
        self.ui.pushButton_18.clicked.connect(self.press_button('('))
        self.ui.pushButton_19.clicked.connect(self.press_button(')'))
        self.ui.pushButton_20.clicked.connect(self.press_button('%'))
        self.ui.pushButton_21.clicked.connect(self.press_button('.'))
        self.display_text = '0'
        window.show()

    def intro(self):
        text = self.ui.lineEdit.setText('0')
        return text

    def err_control(self):
        if self.ui.lineEdit.text() == 'ERROR':
            self.clear_console()

    def zero_control(self):
        if self.ui.lineEdit.text() == self.display_text:
            self.clear_console()

    def clear_console(self):
        self.ui.lineEdit.clear()


    def press_button(self, symbol):
        self.display_text = self.intro()
        def click(*args, **kwargs):
            self.err_control()
            self.zero_control()
            text = self.ui.lineEdit.text() + symbol
            if text == '.' and self.ui.lineEdit.text() == '':
                text = '0.'
            self.ui.lineEdit.setText(text)
        return click


    def equal(self):
        txt = self.ui.lineEdit.text()
        try:
            result = str(eval(txt))
        except SyntaxError:
            result = 'ERROR'
        self.ui.lineEdit.setText(result)

    def calc_exit(self):
        exit()