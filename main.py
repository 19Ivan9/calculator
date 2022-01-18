from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

from controller import Controller

app = QApplication([])
window = QMainWindow()
c = Controller(window)
app.exec_()