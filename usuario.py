from sql import SQL_COMMANDS
from colorama import init, Fore
import exibir
import catalogo 
from menus_func import menu_principal


init(autoreset=True)

class Usuario:
    def __init__(self):
        self.sql_commands = SQL_COMMANDS()

    def logar(self, email, senha):
        self.email = email
        self.senha = senha
        rows = self.sql_commands.validacao_login(email, senha)
        error_message1 = Fore.RED+'\nUsuário Não Existe!'
        error_message2 = Fore.RED+'\nSenha Incorreta!'
        validate_message = Fore.GREEN+"\nLogin Realizado com Sucesso!"
        if rows == []:
            id_message = {
                "id" : None,
                "message": error_message1,
                "adm": None,
                "status": False
            }
            print(id_message["Message"])
            return id_message
        elif rows[0][0] == senha:
            validacao_user = rows[0][1]
            id_message = {
                    "id" : f"{rows[0][3]}",
                    "message": validate_message,
                    "adm": f"{validacao_user}",
                    "status": None
                }
            if validacao_user == '1':
                print(id_message["message"])
                return id_message
            else:
                print(id_message["message"])
                return id_message
        elif rows[0][0] != senha:
            id_message = {
                "id" : f"{rows[0][3]}",
                "message": error_message2,
                "adm": None,
                "status": True
            }
            print(id_message["message"])
            return id_message

    def cadastrar(self, nome, cpf, email, data_nascimento, telefone, senha):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.data_nascimento = data_nascimento
        self.telefone = telefone
        self.senha = senha
        validacao = self.sql_commands.create_user(nome, cpf, email, data_nascimento, telefone, senha, '0')
        return validacao
    
    def deletar(self, email):
        self.email = email
        validacao = self.sql_commands.delete_user(email)
        return validacao
    
class Funcionario(Usuario)  :   
        def __init__(self):
            self.funcionario = None 
            super().__init__()
        
        def cadastrar_funcionario(self):
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
            self.nome = nome
            self.cpf = cpf
            self.email = email
            self.data_nascimento = data_nascimento
            self.telefone = telefone
            self.senha = senha
            validacao = self.sql_commands.create_user(nome, cpf, email, data_nascimento, telefone, senha, '1')
            return validacao
        
        def exibirInfo(self, idUsuario):
            self.funcionario = exibir.ExibirInfo(idUsuario).exibir()
            if(self.funcionario and len(self.funcionario) != 0):
                print('')
                print(Fore.YELLOW + "----- Funcionário -----")
                print(f"Nome: {self.funcionario[0][0]}")
                print(f"CPF: {self.funcionario[0][1]}")
                print(f"Email: {self.funcionario[0][2]}")
                print(f"Data de nascimento: {self.funcionario[0][3]}")
                print(f"Telefone: {self.funcionario[0][4]}")
            else:
                print(Fore.RED + 'Erro ao encontrar usuário.')

   
        def exibirMenu(self, idUsuario):
            while True:
                print('')
                print(Fore.BLUE + "----- Menu Principal -----")
                print('1. Minha Conta')
                print('2. Configurar Livros')
                print('3. Catálogo de Livros')
                print('4. Cadastro de Funcionários')
                print('5. Dashboard')
                print('0. Sair')

                opcao = input("Escolha uma opção: ")

                if opcao == '1':
                    while True:
                        self.exibirInfo(idUsuario)
                        print('0. Voltar')
                        voltar = input()
                        if voltar == "0":
                            break

                elif opcao == '2':
                    menu_principal.main()
                elif opcao == '3':
                    catalogo.Catalogo()
                elif opcao == '4':
                    print('')
                    self.cadastrar_funcionario()
                elif opcao == '5':
                    print(Fore.LIGHTYELLOW_EX + 'Opção ainda não configurada!')
                elif opcao == '0':
                    print(Fore.BLUE + "Saindo...")
                    break
                else:
                    print(Fore.RED + "Opção inválida!")

class Cliente(Usuario):
   def __init__(self):
     super().__init__()
     self.cliente =  None

   def exibirInfo(self, idUsuario):
      self.cliente = exibir.ExibirInfo(idUsuario).exibir()
      if(self.cliente and len(self.cliente) != 0):
         print(Fore.YELLOW + "----- Usuário -----")
         print(f"Nome: {self.cliente[0][0]}")
         print(f"CPF: {self.cliente[0][1]}")
         print(f"Email: {self.cliente[0][2]}")
         print(f"Data de nascimento: {self.cliente[0][3]}")
         print(f"Telefone: {self.cliente[0][4]}")
      else:
         print(Fore.RED + 'Erro ao encontrar usuário.')


   def exibirMenu(self, idUsuario):

      while True:
         print(Fore.BLUE + "----- Menu Principal -----")
         print('1. Minha Conta')
         print('2. Catálogo de Livros')
         print('3. Contato')
         print('0. Sair')

         opcao = input("Escolha uma opção: ")

         if opcao == '1':
            while True:
               self.exibirInfo(idUsuario)
               print('0. Voltar')
               voltar = input()
               if voltar == "0":
                  break
               
         elif opcao == '2':
            catalogo.Catalogo()

         
         elif opcao == '3':
             print(Fore.LIGHTYELLOW_EX + 'Opção ainda não configurada!')

         elif opcao == '0':
               print(Fore.BLUE + "Saindo...")
               break
         else:
            print(Fore.RED + "Opção inválida!")
        