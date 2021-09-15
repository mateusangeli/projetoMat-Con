# IMPORTAR A CLASSE CLIENTE
from utils.cliente import Cliente
import models.database as db



# PEGA TODOS OS CLIENTES DO BANCO DE DADOS
def getClientes():
    # CRIO A CONEXÃO 
    conn = db.connect_db()
    # SE COMUNICAR COM O BANCO DE DADOS
    cursor = conn.cursor()
    # EXECUTA O COMANDO DE SELEÇÃO DOS CLIENTES
    cursor.execute("SELECT * FROM Clientes;")
    # IMPRIMIR O RESULTADO
    # CRIAR OS OBJETOS
    lista_clientes = []
    for l in cursor.fetchall():
        id = l[0]
        nome = l[1]
        cpf = l[2]
        telefone = l[3]
        email = l[4]
        endereco = l[5]
        novoCliente = Cliente(id, nome, cpf, telefone, email, endereco)
        lista_clientes.append(novoCliente)
    conn.close()
    return lista_clientes

# RETORNA UM CLIENTE ESPECÍFICO
def getCliente(id):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """SELECT * FROM Clientes WHERE ID = ?;""" 
    cursor.execute(sql, [id]) # lista de argumentos na mesma ordem das ?s
    # coloca o resultado em uma lista de objetos clientes
    l = cursor.fetchall()[0]
    id = l[0]
    nome = l[1]
    cpf = l[2]
    telefone = l[3]
    email = l[4]
    endereco = l[5]
    # cria o novo objeto
    novoCliente = Cliente(id, nome, cpf, telefone, email, endereco)
    # fecha a conexão
    conn.close
    # retorna a lista
    return novoCliente

  

def addCliente(cliente):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """ INSERT INTO Clientes (nome, cpf, telefone, email, endereco) VALUES (?,?,?,?,?); """
    cursor.execute(sql,[cliente.nome, cliente.cpf, cliente.telefone, cliente.email, cliente.endereco])
    # GRAVA OS DADOS NO BANCO DE DADOS
    conn.commit()
    conn.close()

def editCliente(cliente):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """ UPDATE Clientes SET nome = ?, cpf = ?, telefone = ?, email = ?, endereco = ? WHERE id = ?"""
    cursor.execute(sql,[cliente.nome, cliente.cpf, cliente.telefone, cliente.email, cliente.endereco, cliente.id])
    # GRAVA OS DADOS NO BANCO DE DADOS
    conn.commit()
    conn.close()


def delCliente(id):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """ DELETE FROM Clientes WHERE id = ?"""
    cursor.execute(sql, [id])
    # GRAVA OS DADOS NO BANCO DE DADOS
    conn.commit()
    conn.close()
    