from utils.venda import Venda
from PyQt5.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem

class TebelaItens(QTableWidget):
    def __init__(self,janela_pai):
        super().__init__(0,4)
        self.janela_pai = janela_pai

        headers = ["ID DO PRODUTO", "PREÇO", "QUANTIDADE", "PREÇO TOTAL"]
        self.setHorizontalHeaderLabels(headers)