from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem, QWidget, QHBoxLayout, QPushButton
from PyQt5 import uic
from PyQt5.QtCore import Qt, QSize, QRect
import models.vendas_model as VendasModel


class ListaVendas(QWidget):
    def __init__(self, parent):
        super().__init__()
        uic.loadUi("ui/ui_listavendas.ui", self)
        self.parent = parent
        self.configTable()
        self.lista_de_vendas = []

        self.carregaVendas()
        self.nova_venda.clicked.connect(self.novaVenda)


    def configTable(self):
        self.tableWidget.verticalHeader().setVisible(False)
        # ajusta a altura das linhas
        self.tableWidget.verticalHeader().setSectionResizeMode(
            QHeaderView.ResizeToContents)
        # ajusta as colunas ao tamanho da tela
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                 QHeaderView.Stretch)

        # desabilita a edição dos campos
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        # seleciona toda a linha
        self.tableWidget.setSelectionBehavior(False)

    def novaVenda(self):
        self.parent.display(2)       


    def carregaVendas(self):
        self.lista_de_vendas = VendasModel.getVendas()
        self.tableWidget.setRowCount(0)
        for vendas in self.lista_de_vendas:
            self._addRow(vendas)

    def _addRow(self, item):
        rowCount = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowCount)
        id = QTableWidgetItem(str(item.id))
        id.setTextAlignment(Qt.AlignCenter)
        data = QTableWidgetItem(item.data)
        data.setTextAlignment(Qt.AlignCenter)
        nome = QTableWidgetItem(item.cliente.nome)
        fone = QTableWidgetItem(item.cliente.telefone)
        fone.setTextAlignment(Qt.AlignCenter)
        valor = QTableWidgetItem(str(item.valorTotal()))
        valor.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(rowCount, 1, id)
        self.tableWidget.setItem(rowCount, 2, data)
        self.tableWidget.setItem(rowCount, 3, nome)
        self.tableWidget.setItem(rowCount, 4, fone)
        self.tableWidget.setItem(rowCount, 5, valor)


    #def excluirVenda(self):
     #   self.tableWidget.delete(self.vendaAtual)
