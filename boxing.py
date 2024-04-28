import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt

app = QApplication(sys.argv)

main_widget = QWidget()

mainLayout = QVBoxLayout(main_widget)
mainLayout.setAlignment(Qt.AlignVCenter)  # Alinha os widgets verticalmente no centro
hLayout = QHBoxLayout()
hLayout.setAlignment(Qt.AlignRight)  # Alinha os widgets horizontalmente no início


button1 = QPushButton("Widget 1")
button1.setStyleSheet("""
    QPushButton {
        background-color: red;
        color: white;
        font-size: 16px;
        padding: 10px;
    }
    
    QPushButton:hover {
        background-color: blue;
    }
""")
button1.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
# os SizePolicy possuem um valor máximo

hLayout.addWidget(button1)
hLayout.addWidget(QPushButton("Widget 2"))
hLayout.addWidget(QPushButton("Widget 3"))

mainLayout.addLayout(hLayout)

main_widget.show()

sys.exit(app.exec())


