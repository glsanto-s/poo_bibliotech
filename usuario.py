from sql import SQL_COMMANDS
from funcionario import ConfigFuncionario
from colorama import init, Fore
init(autoreset=True)

class Usuario:
    def __init__(self):
        self.sql_commands = SQL_COMMANDS()
        self.func = ConfigFuncionario()

    def logar(self, email, senha):
        self.email = email
        self.senha = senha
        rows = self.sql_commands.validacao_login(email, senha)
        error_message1 = Fore.RED+'\nUsuário Não Existe!'
        error_message2 = Fore.RED+'\nCredenciais Inválidas!'
        validate_message = Fore.GREEN+"\nLogin Realizado com Sucesso!"
        if rows == []:
            id_message = {
                "id" : None,
                "Message": error_message1
            }
            print(id_message["Message"])
            return id_message
        elif rows[0][0] == senha:
            validacao_user = rows[0][1]
            id_message = {
                    "id" : f"{rows[0][3]}",
                    "message": validate_message,
                    "adm": f"{validacao_user}"
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
                "adm": None
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
             super().__init__()
        
        def cadastrar_funcionario(self, nome, cpf, email, data_nascimento, telefone, senha):
            self.nome = nome
            self.cpf = cpf
            self.email = email
            self.data_nascimento = data_nascimento
            self.telefone = telefone
            self.senha = senha
            validacao = self.sql_commands.create_user(nome, cpf, email, data_nascimento, telefone, senha, '1')
            return validacao