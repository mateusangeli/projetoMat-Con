import sqlite3 
URL_DATABASE = 'models/banco.db'
def connect_db():
    #CRIA CONEXÃO
    conn = sqlite3.connect(URL_DATABASE)
    return conn
