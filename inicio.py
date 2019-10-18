class Cliente:
    def __init__(self, nome, cpf, email, telefone):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone

    def setNome(self, nome):
        self.nome = nome

    def setCPF(self, cpf):
        self.cpf = cpf

    def setEmail(self, email):
        self.email = email

    def setTelefone(self, telefone):
        self.telefone = telefone

    def getCPF(self):
        return self.cpf

    def getNome(self):
        return self.nome

    def getEmail(self):
        return self.email

    def getTelefone(self):
        return self.telefone

    def __str__(self):
        return 'Cliente(name - '+ self.nome + ', CPF - ' + self.cpf + ', Email - ' + self.email + ', Telefone - ' + self.telefone

    def __repr__(self):
        return str(self)


# flag = True

print("Bem vindo ao sistema de passagem aereas, selecione uma categoria:")
print("1- Cadastrar um cliente")
print("2- Alterar dados de um cliente")
print("3- Exibir dados de um cliente")
print("4- Remover um cliente")
op = int(input("Digite sua opcap: "))
if op == 1:
    cpf = input("Digite o cpf: ")
    nome = input("Digite o nome: ")
    telefone = input("Digita telefone: ")
    email = input("Digite email")
    cliente = Cliente(cpf, nome, email, telefone)
    lista_cliente = []
    # cliente.__repr__()
    lista_cliente.append(cliente)
    cpf = input("Digite o cpf: ")
    nome = input("Digite o nome: ")
    telefone = input("Digita telefone: ")
    email = input("Digite email")
    cliente = Cliente(cpf, nome, email, telefone)
    lista_cliente.append(cliente)
    print(lista_cliente)
elif op == 2:
    print("nada")
