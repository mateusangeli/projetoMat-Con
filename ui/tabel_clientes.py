from utils.cliente import Cliente
from PyQt5.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem
from PyQt5 import Qt

# importa os models do banco de dados
import models.clientes_model as ClienteModel


class TabelaClientes(QTableWidget):
    def __init__(self, janela_pai):
        super().__init__(0, 6) # config inicial da tabela(qtd_linha, qtd_colunas)

        # possui a referencia do pai
        self.janela_pai = janela_pai

        # textos do cabeçalho
        headers = ["ID", "NOME", "CPF", "TELEFONE", "EMAIL", "ENDEREÇO"]
        self.setHorizontalHeaderLabels(headers)

        #Configuração da tabela
        self.configTable()

        # referência a lista de clientes
        self.lista_clientes = []

        #Carrega os dados do banco
        self.carregaDados()

    def configTable(self):
        self.verticalHeader().setVisible(False)
        # ajusta as colunas ao tamanho da tela
        self.horizontalHeader().setStretchLastSection(False)
        self.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)
        # desabilita a edição dos campos
        self.setEditTriggers(QTableWidget.NoEditTriggers)
        # seleciona toda a linha
        self.setSelectionBehavior(QTableWidget.SelectRows)
        # evento ao selecionar uma linha
        self.clicked.connect(self.on_click)
            
            
    def carregaDados(self):
        self.lista_clientes = ClienteModel.getClientes()
        self.setRowCount(0)
        for clientes in self.lista_clientes:
            self._addRow(clientes)

    def _addRow(self,cliente):
        rowCount = self.rowCount()
        self.insertRow(rowCount)
        id_item = QTableWidgetItem(str(cliente.id))
        id_nome = QTableWidgetItem(cliente.nome)
        id_cpf = QTableWidgetItem(cliente.cpf)
        id_telefone = QTableWidgetItem(cliente.telefone)
        id_email = QTableWidgetItem(cliente.email)
        id_endereco = QTableWidgetItem(cliente.endereco)
        self.setItem(rowCount, 0, id_item)
        self.setItem(rowCount, 1, id_nome)
        self.setItem(rowCount, 2, id_cpf)
        self.setItem(rowCount, 3, id_telefone)
        self.setItem(rowCount, 4, id_email)
        self.setItem(rowCount, 5, id_endereco)

    def on_click(self):
        selected_row = self.currentRow()
        id = self.item(selected_row, 0).text()
        cliente = ClienteModel.getCliente(id)
        self.janela_pai.insereInfo(cliente)

    def add(self, cliente):
        ClienteModel.addCliente(cliente)
        self.carregaDados()

    def atualizar(self, cliente):
        ClienteModel.editCliente(cliente)
        self.carregaDados()

    def excluir(self, cliente):
        ClienteModel.delCliente(cliente.id)
        self.carregaDados()



