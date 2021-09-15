from utils.produto import Produto
from PyQt5.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem
from PyQt5 import Qt

import models.produtos_model as ProdModel

class TabelaProdutos(QTableWidget):
    def __init__(self,janela_pai):
        super().__init__(0,6)

        self.janela_pai = janela_pai

        headers = ["ID", "NOME", "MARCA", "PREÇO DE COMPRA", "PREÇO DE VENDA", "QUANTIDADE"]
        self.setHorizontalHeaderLabels(headers)

        self.configTable()

        self.lista_produtos = []

        self.carregaDados()

    def configTable(self):
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setStretchLastSection(False)
        self.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)
        self.setEditTriggers(QTableWidget.NoEditTriggers)
        self.setSelectionBehavior(QTableWidget.SelectRows)
        self.clicked.connect(self.on_click)

    def carregaDados(self):
        self.lista_produtos = ProdModel.getProdutos()
        self.setRowCount(0)
        for produtos in self.lista_produtos:
            self._addRow(produtos)

    def _addRow(self,produto):
        rowCount = self.rowCount()
        self.insertRow(rowCount)
        id_item = QTableWidgetItem(str(produto.id))
        id_nome = QTableWidgetItem(produto.nome)
        id_marca = QTableWidgetItem(produto.marca)
        id_precocompra = QTableWidgetItem(produto.precocompra)
        id_precovenda = QTableWidgetItem(produto.precovenda)
        id_quantidade = QTableWidgetItem(produto.quantidade)
        self.setItem(rowCount, 0, id_item)
        self.setItem(rowCount, 1, id_nome)
        self.setItem(rowCount, 2, id_marca)
        self.setItem(rowCount, 3, id_precocompra)
        self.setItem(rowCount, 4, id_precovenda)
        self.setItem(rowCount, 5, id_quantidade)

    def on_click(self):
        selected_row = self.currentRow()
        id = self.item(selected_row, 0).text()
        nome = self.item(selected_row, 1).text()
        marca = self.item(selected_row, 2).text()
        precocompra = self.item(selected_row, 3).text()
        precovenda = self.item(selected_row, 4).text()
        quantidade = self.item(selected_row, 5).text()
        self.janela_pai.addProduto(Produto(id, nome, marca, precocompra, precovenda, quantidade))

    def add(self, produto):
        Produto.addProduto(produto)
        self.carregaDados()

    def atualizar(self, produto):
        Produto.editProduto(produto)
        self.carregaDados

    def excluir(self, produto):
        Produto.delProduto(produto.id)
        self.carregaDados()
        
