from sql import SQL_COMMANDS
import exibir as exibir
import catalogo as catalogo
from datetime import datetime, timedelta

class Usuario:
    def __init__(self):
        self.sql_commands = SQL_COMMANDS()

    def logar(self, email, senha):
        self.email = email
        self.senha = senha
        rows = self.sql_commands.validacao_login(email, senha)
        error_message1 = 'Usuário Não Existe!'
        error_message2 = 'Senha Incorreta!'
        validate_message = "Login Realizado com Sucesso!"
        if rows == []:
            id_message = {
                "id" : None,
                "message": error_message1,
                "adm": None,
                "status": False
            }
            return id_message
        elif rows[0][0] == senha:
            validacao_user = rows[0][1]
            id_message = {
                    "id" : f"{rows[0][3]}",
                    "message": validate_message,
                    "adm": f"{validacao_user}",
                    "status": True
                }
            return id_message
        elif rows[0][0] != senha:
            id_message = {
                "id" : f"{rows[0][3]}",
                "message": error_message2,
                "adm": None,
                "status": False
            }
            return id_message

    def cadastrar(self, nome, cpf, email, data_nascimento, telefone, senha, adm="0"):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.data_nascimento = data_nascimento
        self.telefone = telefone
        self.senha = senha
        self.adm = adm
        validacao = self.sql_commands.create_user(nome, cpf, email, data_nascimento, telefone, senha, adm)
        return validacao
    
    def deletar(self, email):
        self.email = email
        validacao = self.sql_commands.delete_user(email)
        return validacao
    
    def atualizar_dados(self, idusuario, nome=None, cpf=None, email=None, data_nascimento=None, telefone=None, senha=None):
        self.idusuario = idusuario
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.data_nascimento = data_nascimento
        self.telefone = telefone
        self.senha = senha

        campos_para_atualizar = []
        valores = []

        if nome:
            campos_para_atualizar.append("nome = %s")
            valores.append(nome)
        if cpf:
            campos_para_atualizar.append("cpf = %s")
            valores.append(cpf)
        if email:
            campos_para_atualizar.append("email = %s")
            valores.append(email)
        if data_nascimento:
            campos_para_atualizar.append("data_nascimento = %s")
            valores.append(data_nascimento)
        if telefone:
            campos_para_atualizar.append("telefone = %s")
            valores.append(telefone)
        if senha:
            campos_para_atualizar.append("senha = %s")
            valores.append(senha)
        
        valores.append(idusuario)

        self.sql_commands.atualizar_usuario(campos_para_atualizar, valores)
        return 'Dados Atualizados!'
    
class Cliente(Usuario):
    def __init__(self):
        super().__init__()
        self.cliente =  None

    def reservar(self, idusuario, idlivro):
        self.idlivro = idlivro
        self.idusuario = idusuario
        return self.sql_commands.criar_reserva(idusuario, idlivro)
    
    def cancelar_reserva(self, idusuario, idlivro):
        self.idlivro = idlivro
        self.idusuario = idusuario
        return self.sql_commands.cancelar_reserva(idusuario, idlivro)
    
    def emprestar(self, idusuario, idlivro, tipolivro):
        self.idlivro = idlivro
        self.idusuario = idusuario
        data_emprestimo = datetime.now().date()
        data_validade = data_emprestimo + timedelta(weeks=2)
        return self.sql_commands.emprestimo(idusuario, idlivro, data_validade, tipolivro)
    
    def avaliar(self, idlivro, idusuario, valor):
        return self.sql_commands.avaliar(idlivro, idusuario, valor)