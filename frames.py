import sys
from PySide6.QtWidgets import *

app = QApplication(sys.argv)

tela = QMainWindow()
tela.setWindowTitle('Título')
central_widget = QWidget()
main_layout = QVBoxLayout(central_widget)
# o QMainWindow precisa ter apenas 1 widget filho, que este sim pode ter vários filhos
# cada widget que possui vários filhos precisa de um layout
# o widget filho aqui é o central_widget
# o central_widget aqui é o widget pai do main_layout, mas pode ser adicionado dps pelo método "setLayout" dos widgets
# métodos: setSpacing, setAlignment, setStretch

myFrame = QFrame()
myFrame.setStyleSheet("background-color: gray")
t1 = QLineEdit(myFrame)

myFrame2 = QFrame()
myFrame2.setStyleSheet("background-color: gray")
frame2_layout = QVBoxLayout(myFrame2)
#myFrame2.setContentsMargins(5, 5, 5, 5)
spinbox1 = QSpinBox()
spinbox1.setRange(0, 10)
spinbox1.setWrapping(True)
spinbox2 = QComboBox()
spinbox2.addItems(['a', 'b', 'c', 'd'])
label = QLabel('Texto')
frame2_layout.addWidget(spinbox1) ; frame2_layout.addWidget(spinbox2)
frame2_layout.addWidget(label)
label.setText('Novo texto')


main_layout.addWidget(myFrame)
main_layout.addWidget(myFrame2)
main_layout.setContentsMargins(0, 0, 0, 0)
#tela.setCentralWidget(central_widget)
central_widget.show()



app.exec()
