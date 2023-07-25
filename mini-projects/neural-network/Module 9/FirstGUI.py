from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QPushButton

# # O primeiro passo para cada GUI é criar um aplicativo. Este é um contêiner
# # para armazenar todos os nossos widgets.
# my_app = QApplication([])
#
# # Se quiser apenas imprimir algum texto em nosso aplicativo
# my_label = QLabel('Hello Foothill!')
#
# # E, finalmente, dizemos ao Python para colocar esse rótulo na tela com:
# my_label.show()
#
# """
# We really have a complete program now, that you can run.
# The label will appear and disappear from the screen so fast you probably
# won't even notice it, so we want a way to make our app persistent.
# We do that with:
# """
#
# my_app.exec()

my_app = QApplication([])
# O objeto QGridLayout nos dá algumas bordas ao redor do rótulo
layout = QGridLayout()
win = QWidget()
win.setLayout(layout)

my_label = QLabel('Hello Foothill!')
layout.addWidget(my_label)
win.show()
my_app.exec()