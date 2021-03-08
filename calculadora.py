import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QSizePolicy
from PyQt5.QtGui import QIcon


class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculadora do Thiago')
        self.setFixedSize(400, 400)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)
        self.setWindowIcon(QIcon('icon.png'))

        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 5)
        self.display.setDisabled(True)
        self.display.setStyleSheet(
            '* {background-color: #fff; color: #000; font-size: 30px}'
        )
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        self.add_btn(QPushButton('7'), 1, 0, 1, 1)
        self.add_btn(QPushButton('8'), 1, 1, 1, 1)
        self.add_btn(QPushButton('9'), 1, 2, 1, 1)
        self.add_btn(QPushButton('+'), 1, 3, 1, 1, style='background-color: #AFAFAF')
        self.add_btn(QPushButton('C'), 1, 4, 1, 1, self.clear_all, 'background-color: #858585')

        self.add_btn(QPushButton('4'), 2, 0, 1, 1)
        self.add_btn(QPushButton('5'), 2, 1, 1, 1)
        self.add_btn(QPushButton('6'), 2, 2, 1, 1)
        self.add_btn(QPushButton('-'), 2, 3, 1, 1, style='background-color: #AFAFAF')
        self.add_btn(QPushButton('<-'), 2, 4, 1, 1, self.clear, 'background-color: #858585')

        self.add_btn(QPushButton('1'), 3, 0, 1, 1)
        self.add_btn(QPushButton('2'), 3, 1, 1, 1)
        self.add_btn(QPushButton('3'), 3, 2, 1, 1)
        self.add_btn(QPushButton('*'), 3, 3, 1, 1, style='background-color: #AFAFAF')
        self.add_btn(QPushButton('='), 3, 4, 2, 1, self.igual, 'background-color: #858585')

        self.add_btn(QPushButton('.'), 4, 0, 1, 1, style='background-color: #AFAFAF')
        self.add_btn(QPushButton('0'), 4, 1, 1, 1)
        self.add_btn(QPushButton('**'), 4, 2, 1, 1, style='background-color: #AFAFAF')
        self.add_btn(QPushButton('/'), 4, 3, 1, 1, style='background-color: #AFAFAF')
 

        self.setCentralWidget(self.cw)
    
    # Adicionar botão padrão
    def add_btn(self, btn, row, col, rowspan, colspan, funcao=None, style=None):
        self.grid.addWidget(btn, row, col, rowspan, colspan)
        style_padrao = 'font-size: 17px; border: none; background-color: #DEDEDE;'
        btn.setStyleSheet(style_padrao)

        if style is not None:
            btn.setStyleSheet(style_padrao + style)

        if funcao is None:
            btn.clicked.connect(
                lambda: self.display.setText(
                    self.display.text() + btn.text()
                )
            )
        else:
            btn.clicked.connect(funcao)
        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
    
    # Limpar tudo
    def clear_all(self):
        self.display.setText('')
    
    # Limpar 1 caracter
    def clear(self):
        self.display.setText(self.display.text()[:-1])

    # Retornar valor
    def igual(self):
        try:
            self.display.setText(str(eval(self.display.text())))
        except:
            pass



if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    qt.exec_()