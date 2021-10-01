import sys
from ui.ui_listavendas import ListaVendas
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

from ui.ui_produtos import CadProdutos
from ui.ui_clientes import CadClientes
from ui.ui_vendas import NovaVenda
from ui.ui_listavendas import ListaVendas
from ui.ui_login import CadLogin
import models.login_model as LogModel

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
        self.stackedWidget_geral.setCurrentIndex(0)
        self.nova_lista = []
        self.listWidget.setCurrentRow(0)
        self.listWidget.currentRowChanged.connect(self.display)
        self.entrar_btn.clicked.connect(self.verificaLogin)
        self.cad_btn.clicked.connect(self.cadastro)
        self.login_btn.clicked.connect(self.login)
        self.janela_cadLogin = CadLogin(self)
        self.nova_lista = []

    def verificaLogin(self):
        user_login = self.user_login.text()
        pass_login = self.pass_login.text()
        self.nova_lista = LogModel.getLogin(user_login, pass_login)
        if len(self.nova_lista) > 0:
            self.iniciarSistema()
        else:
            print("login e senha inválidos")


    def iniciarSistema(self):
        self.stackedWidget_geral.setCurrentIndex(1)
        self.carregaJanelas()
    
    def cadastro(self):
        self.stackedWidget_geral.setCurrentIndex(2)

    def login(self):
        self.stackedWidget_geral.setCurrentIndex(0)

        

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