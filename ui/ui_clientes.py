from PyQt5.QtWidgets import QWidget
from PyQt5 import uic
from utils.cliente import Cliente
from ui.tabel_clientes import TabelaClientes

class CadClientes(QWidget):
    def __init__(self):
        super().__init__()
        # carrega os componentes (Widgets) para dentro da classe
        uic.loadUi("ui/ui_clientes.ui", self)
        self.table = TabelaClientes(self)
        self.verticalLayout.addWidget(self.table)

        self.clienteAtual = None
        self.setEventos()

        # definindo os eventos dos botões
    def setEventos(self):
        self.b_salvar.clicked.connect(self.salvarCliente)
        self.b_excluir.clicked.connect(self.excluirCliente)
        self.b_limpar.clicked.connect(self.limparCampos)
    
    def salvarCliente(self):
        novo = self.getCliente()
        if novo != None:
            if self.clienteAtual == None:
                self.table.add(novo)
            else:
                novo.id = self.clienteAtual.id
                self.table.atualizar(novo)
            self.limparCampos()

    def getCliente(self):
        nome = self.nome.text()
        cpf = self.cpf.text()
        telefone = self.telefone.text()
        email = self.email.text()
        endereco = self.endereco.text()
    
        if ((nome != "") and (cpf != "") and (telefone != "") and (email != "") and (endereco != "")):
            return Cliente(-1,nome,cpf,telefone,email,endereco)
        return None

    

    def insereInfo(self, cliente):
        self.clienteAtual = cliente
        self.nome.setText(cliente.nome)
        self.cpf.setText(cliente.cpf)
        self.telefone.setText(cliente.telefone)
        self.email.setText(cliente.email)
        self.endereco.setText(cliente.endereco)
        
        self.b_salvar.setText("Atualizar")
        self.b_excluir.setEnabled(True)

    def excluirCliente(self):
        self.table.excluir(self.clienteAtual)
        self.limparCampos

    def limparCampos(self):
        self.nome.setText("")
        self.cpf.setText("")
        self.telefone.setText("")
        self.email.setText("")
        self.endereco.setText("")
        self.b_salvar.setText("Salvar")
        self.b_excluir.setEnabled(False)
