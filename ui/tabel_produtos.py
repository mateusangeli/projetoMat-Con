from utils.produto import Produto
from PyQt5.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem
from PyQt5 import Qt

import models.produtos_model as ProdModel

class TabelaProdutos(QTableWidget):
    def __init__(self,janela_pai):
        super().__init__(0,7)

        self.janela_pai = janela_pai

        headers = ["ID", "NOME", "MARCA", "DESCRIÇÃO", "PREÇO DE COMPRA", "PREÇO DE VENDA", "QUANTIDADE"]
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
        id_nomeP = QTableWidgetItem(produto.nomeP)
        id_marca = QTableWidgetItem(produto.marca)
        id_descricao = QTableWidgetItem(produto.descricao)
        id_precocompra = QTableWidgetItem(str(produto.precocompra))
        id_precovenda = QTableWidgetItem(str(produto.precovenda))
        id_quantidade = QTableWidgetItem(str(produto.quantidade))
        self.setItem(rowCount, 0, id_item)
        self.setItem(rowCount, 1, id_nomeP)
        self.setItem(rowCount, 2, id_marca)
        self.setItem(rowCount,3, id_descricao)
        self.setItem(rowCount, 4, id_precocompra)
        self.setItem(rowCount, 5, id_precovenda)
        self.setItem(rowCount, 6, id_quantidade)

    def on_click(self):
        selected_row = self.currentRow()
        id = self.item(selected_row, 0).text()
        nomeP = self.item(selected_row, 1).text()
        marca = self.item(selected_row, 2).text()
        descricao = self.item(selected_row, 3).text()
        precocompra = self.item(selected_row, 4).text()
        precovenda = self.item(selected_row, 5).text()
        quantidade = self.item(selected_row, 6).text()
        self.janela_pai.insereInfo(Produto(id, nomeP, marca, descricao, precocompra, precovenda, quantidade))

    def add(self, produto):
        ProdModel.addProduto(produto)
        self.carregaDados()

    def atualizar(self, produto):
        ProdModel.editProduto(produto)
        self.carregaDados()

    def excluir(self, produto):
        ProdModel.delProduto(produto.id)
        self.carregaDados()
        
