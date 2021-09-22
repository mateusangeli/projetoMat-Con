from utils.venda import Venda
import models.database as db


def addVenda(self):
    sql_addVenda = "INSERT INTO Vendas (id_cliente, valor_total) VALUES (?, ?)"

    sql_id_venda = "SELECT LAST_INSERT_ROWID() AS id;"

    #for item in venda.lista_de_itens:
        #pass

