from PyQt5.QtWidgets import QWidget
from PyQt5 import uic
from utils.login import Login
import models.login_model as LogModel

class CadLogin():
    def __init__(self, janela):
        self.janela = janela

        self.lista_usuarios = []
        self.carregaDados()

        self.janela.c_btn.clicked.connect(self.salvarCadastro)

    def carregaDados(self):
        self.lista_usuarios = LogModel.getLogins()


    def salvarCadastro(self):
        novo = self.verificaCadastro()
        if novo != None:
            self.add(novo)
            self.limpaCampos()   

           

    def verificaCadastro(self):
        nome = self.janela.nome.text()
        usuario = self.janela.usuario.text()
        senha = self.janela.senha.text()


        if ((nome != "") and (usuario != "") and (senha != "")):
            return Login(-1, nome, usuario, senha)
        return None
 

    def add(self, login):
        LogModel.addLogin(login)
        self.carregaDados()


    def excluir(self, login):
        LogModel.delLogin(login.id)
        self.carregaDados()

    def limpaCampos(self):
        self.janela.nome.setText("")
        self.janela.usuario.setText("")
        self.janela.senha.setText("")




