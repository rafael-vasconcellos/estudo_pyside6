import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt


app = QApplication(sys.argv)
tela = QMainWindow()
main_widget = QWidget()

# tela.setCentralWidget(main_widget)
main_widget.show() # ou tela.show()
app.exec()

# o método show a ser usado necessariamente precisa ser o elemento pai, aqui o main_widget.show() é usado
# note que o main_widget não usa a variável tela como argumento, desta maneira "main_widget = QWidget(tela)"
# se assim o fosse, o "tela.show()" que precisaria ser usado