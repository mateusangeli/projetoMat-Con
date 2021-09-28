import sys
from ui.ui_listavendas import ListaVendas
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

from ui.ui_produtos import CadProdutos
from ui.ui_clientes import CadClientes
from ui.ui_vendas import NovaVenda
from ui.ui_listavendas import ListaVendas

from qt_material import apply_stylesheet


'''def tema(app):
    breeze_light = 'style/light/stylesheet.qss'
    breeze_dark = 'style/dark/stylesheet.qts'
    meu_style = 'style/my_style.qss'
    with open (meu_style, 'r') as f:
        style = f.read
        app.setStyleSheet(style)'''

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("mainwindow.ui", self)
        # define os eventos dos botões
        self.listWidget.insertItem(0, "PRODUTOS")
        self.listWidget.insertItem(1, "CLIENTES")
        self.listWidget.insertItem(2, "NOVA VENDA")
        self.listWidget.insertItem(3, "LISTA DE VENDAS")

        self.listWidget.setCurrentRow(0)
        self.carregaJanelas()
        self.listWidget.currentRowChanged.connect(self.display)
        

    def carregaJanelas(self):
        self.stackedWidget.insertWidget(0, CadProdutos()) # Pág 0
        self.stackedWidget.insertWidget(1, CadClientes()) # Pág 1
        self.stackedWidget.insertWidget(2, NovaVenda()) # PAG 3
        self.stackedWidget.insertWidget(3, ListaVendas(self)) # PAG 4


    def display(self, index):
        self.carregaJanelas()
        self.stackedWidget.setCurrentIndex(index)
        self.listWidget.setCurrentRow(index)


app = QApplication(sys.argv)
#aplicar o tema no programa
apply_stylesheet(app, theme='dark_red.xml')

window = MainWindow()
window.show()

app.exec()