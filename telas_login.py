from colorama import init, Fore
init(autoreset=True)

from usuario import Usuario
from cliente import Cliente
from funcionario import ConfigFuncionario


class Telas:
    def __init__(self):
       self.user = Usuario() 
       self.cliente = Cliente()
       self.func = ConfigFuncionario()
    
    def login(self):    
        print(Fore.LIGHTMAGENTA_EX+'''
------------------
Realize seu Login!
------------------
''')
        login = str(input('Email: '))
        senha = str(input('Senha: '))
        validacao_login = self.user.logar(login, senha)
        idUsuario = validacao_login["id"] 
        if  idUsuario != None:
            validacao_login = validacao_login["adm"]
            if validacao_login == "1":
                self.func.exibirMenu(idUsuario)
            elif validacao_login == "0":
                self.cliente.exibirMenu(idUsuario)
        else:
            self.tela_principal()
        
    
    def cadastro_cliente(self):
        print(Fore.LIGHTMAGENTA_EX+'''
-----------
Cadastre-se
-----------''')
        nome = str(input('Nome: '))
        cpf = str(input('CPF: '))
        email = str(input('Email: '))
        data_nascimento = str(input('Data de Nascimento: '))
        telefone = str(input('Telefone: '))
        senha = str(input('Senha: '))
        print(self.user.cadastrar(nome, cpf, email, data_nascimento, telefone, senha))

    def cadastro_funcionario(self):
        print('''
-----------------------
Cadastro de Funcionário
-----------------------''')
        nome = str(input('Nome: '))
        cpf = str(input('CPF: '))
        email = str(input('Email: '))
        data_nascimento = str(input('Data de Nascimento: '))
        telefone = str(input('Telefone: '))
        senha = str(input('Senha: '))
        print(self.user.cadastrar(nome, cpf, email, data_nascimento, telefone, senha))

    def deletar_usuário(self):
        email = str(input('Email: '))
        print(self.user.deletar(email))

    def tela_principal(self):
        print(Fore.LIGHTCYAN_EX +'''
Bibliotech
----------
''')
        print('''Digite uma opção:
                        
1. Login
2. Cadastro        
''')
        opcao = str(input('Sua Escolha: '))
        while opcao != '1' and opcao != '2':
           opcao = str(input('Digite uma opção válida: '))
        if opcao == '1':
            self.login()
            
        elif opcao == '2':
            self.cadastro_cliente()

tela = Telas()
tela.tela_principal()

