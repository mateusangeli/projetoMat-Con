class Cliente:
    def __init__(self, id, nome, cpf, telefone, email, endereco):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        
    def print(self):
        print("ID: ", self.id)
        print("Nome: ", self.nome)
        print("CPF: ", self.cpf)
        print("Telefone: ", self.telefone)
        print("Email: ", self.email)
        print("Endereço :", self.endereco)

