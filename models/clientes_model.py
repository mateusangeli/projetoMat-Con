# IMPORTAR A CLASSE CLIENTE
from utils.clientes import Cliente
import sqlite3



# PEGA TODOS OS CLIENTES DO BANCO DE DADOS
def getClientes():
    # CRIO A CONEXÃO 
    conn = sqlite3.connect('models/banco.db')
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

def getCliente(id):
    print("Retorna um cliente especifico")

def addCliente(cliente):
    print("Novo cliente os campos do cliente")

def editCliente(cliente):
    print("Edita um cliente os campos do cliente")

def delCliente(id):
    print("Deleta um cliente especifíco")
    