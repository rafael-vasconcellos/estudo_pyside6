import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import *

app = QApplication(sys.argv)

tela = QMainWindow()
tela.setWindowTitle('Título')
tela.setGeometry(200, 200, 500, 250)
tela.showMaximized()  # showMinimized()
nova_janela = QWidget(tela)
# tela.setMinimumSize(250, 250)
# tela.setWindowIcon()
# tela.width()

button = QPushButton('Botão', tela)
button.setFixedSize(100, 50)
button.move(10, 10)
button.show()

check_box = QCheckBox('Label do input', tela)
check_box.move(10, 40)
check_box.show()

spin_box = QSpinBox(tela)
spin_box.setRange(0, 10)
spin_box.move(10, 70)
spin_box.show()


slide = QSlider(Qt.Horizontal, tela)
slide.setRange(0, 100)
slide.setSingleStep(0.5)
slide.move(10, 100)
slide.show()

label1 = QLabel('Label', tela)
label1.setText('Novo label')
label1.move(10, 130)
label1.show()

spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
# (width, height, vertical, horizontal)

# command= Função
# fg: cor do texto
# bg: cor de fundo
# width: em pxs, height: em linhas
# font= 'Arial 20 bold'
# bd= n, relief='solid'
# anchor: Rosa dos ventos: variáveis WENS ou strings 'wens'
# padx: padding
# justify
# image= QImage('caminho relativo')


sys.exit(app.exec())
# o argumento aqui é o ultimo código a ser executado antes da finalização
