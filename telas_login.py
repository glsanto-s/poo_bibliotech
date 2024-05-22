from colorama import init, Fore
init(autoreset=True)

from usuario import *



class Telas:
    def __init__(self):
       self.user = Usuario() 
       self.cliente = Cliente()
       self.func = Funcionario()
       self.dados_validados = {
            'nome': False,
            'cpf': False,
            'email': False,
            'data_nascimento': False,
            'telefone': False,
            'senha': False
        }
    
    def login(self):    
        print(Fore.LIGHTMAGENTA_EX+'''
------------------
Realize seu Login!
------------------
''')
        email = str(input('Email: '))
        is_valido = self.validar(email, 'email')

        if not is_valido:
            print('Email inválido. Informe um e-mail válido.')
            self.login()

        senha = str(input('Senha: '))

        validacao_login = self.user.logar(email, senha)
        idUsuario = validacao_login["id"]
        if validacao_login["status"] == True:
            self.login()
        elif validacao_login["status"] == False:
            self.tela_principal() 
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
        
        
        if not self.dados_validados['nome']:
            nome = str(input('Nome: '))
            nome = self.converter_nome(nome)

            is_valido = self.validar(nome, 'nome')

            if not is_valido:
                print('Nome inválido.')
                self.cadastro_cliente()

            self.dados_validados['nome'] = is_valido
            self.user.nome = nome
        
        if not self.dados_validados['cpf']:
            cpf = str(input('CPF: '))
            is_valido = self.validar(cpf, 'cpf')

            if not is_valido:
                print('CPF inválido. Informe um CPF válido.')
                self.cadastro_cliente()

            self.dados_validados['cpf'] = is_valido
            self.user.cpf = cpf

        if not self.dados_validados['email']:
            email = str(input('Email: '))
            is_valido = self.validar(email, 'email')

            if not is_valido:
                print('Email inválido. Informe um e-mail válido.')
                self.cadastro_cliente()

            self.dados_validados['email'] = is_valido
            self.user.email = email

        if not self.dados_validados['data_nascimento']:
            data_nascimento = str(input('Data de Nascimento: '))
            is_valido = self.validar(data_nascimento, 'data_nascimento')

            if not is_valido:
                print('Data de nascimento inválida. Informe uma data de nascimento válida.')
                self.cadastro_cliente()

            self.dados_validados['data_nascimento'] = is_valido
            data_nascimento = self.converter_data(data_nascimento)
            self.user.data_nascimento = data_nascimento

        if not self.dados_validados['telefone']:
            telefone = str(input('Telefone: '))
            is_valido = self.validar(telefone, 'telefone')

            if not is_valido:
                print('Telefone inválido. Informe um telefone válido.')
                self.cadastro_cliente()

            self.dados_validados['telefone'] = is_valido
            self.user.telefone = telefone

        if not self.dados_validados['senha']:
            senha = str(input('Senha: '))
            is_valido = self.validar(senha, 'senha')

            if not is_valido:
                print('Senha inválida. Informe uma senha válida.')
                self.cadastro_cliente()

            self.dados_validados['senha'] = is_valido
            self.user.senha = senha

        is_valido = all(self.dados_validados.values())
        
        if is_valido:    
            log = self.user.cadastrar(self.user.nome, 
                                      self.user.cpf, 
                                      self.user.email, 
                                      self.user.data_nascimento, 
                                      self.user.telefone, 
                                      self.user.senha
                                    )
            if log != 'Usuário Cadastrado!':
                print(log)
                self.tela_principal()
            else:
                print(log)
                self.login()

    def cadastro_funcionario(self):
        print('''
-----------------------
Cadastro de Funcionário
-----------------------''')
        
        if not self.dados_validados['nome']:
            nome = str(input('Nome: '))
            nome = self.converter_nome(nome)
            is_valido = self.validar(nome, 'nome')

            if not is_valido:
                print('Nome inválido.')
                self.cadastro_funcionario()

            self.dados_validados['nome'] = is_valido
            self.user.nome = nome

        if not self.dados_validados['cpf']:
            cpf = str(input('CPF: '))
            is_valido = self.validar(cpf, 'cpf')
        
            if not is_valido:
                print('CPF inválido. Informe um CPF válido')
                self.cadastro_funcionario()

            self.dados_validados['cpf'] = is_valido
            self.user.cpf = cpf

        if not self.dados_validados['email']:
            email = str(input('Email: '))
            is_valido = self.validar(email, 'email')
        
            if not is_valido:
                print('Email inválido. Informe um e-mail válido')
                self.cadastro_funcionario()
            
            self.dados_validados['email'] = is_valido
            self.user.email = email

        if not self.dados_validados['data_nascimento']:
            data_nascimento = str(input('Data de Nascimento: '))
            is_valido = self.validar(data_nascimento, 'data_nascimento')

            if not is_valido:
                print('Data de nascimento inválida. Informe uma data de nascimento válida.')
                self.cadastro_funcionario()

            self.dados_validados['data_nascimento'] = is_valido
            data_nascimento = self.converter_data(data_nascimento)
            self.user.data_nascimento = data_nascimento

        if not self.dados_validados['telefone']:
            telefone = str(input('Telefone: '))
            is_valido = self.validar(telefone, 'telefone')

            if not is_valido:
                print('Telefone inválido. Informe um telefone válido.')
                self.cadastro_funcionario()
            
            self.dados_validados['telefone'] = is_valido
            self.user.telefone = telefone
        
        if not self.dados_validados['senha']:
            senha = str(input('Senha: '))
            is_valido = self.validar(senha, 'senha')
            
            if not is_valido:
                print('Senha inválida. Informe uma senha válida.')
                self.cadastro_funcionario()

            self.dados_validados['senha'] = is_valido
            self.user.senha = senha

        is_valido = all(self.dados_validados.values())
        
        if is_valido:
            log = self.user.cadastrar(self.user.nome, 
                                      self.user.cpf, 
                                      self.user.email, 
                                      self.user.data_nascimento, 
                                      self.user.telefone, 
                                      self.user.senha
                                    )
            if log != 'Usuário Cadastrado!':
                print(log)
                self.tela_principal()
            else:
                print(log)
                self.login()

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
        while opcao not in ['1','2']:
           opcao = str(input('Digite uma opção válida: '))
        if opcao == '1':
            self.login()
            
        elif opcao == '2':
            self.cadastro_cliente()

    def validar(self, dado: str, atributo: str) -> bool:
        """Valida o dado informado.
        Args:
            dado (str): Dado a ser validado.
            atributo (str, optional): Nome do atributo à ser validado.
        Returns:
            bool: True se o dado for válido, False caso contrário.
        """

        if dado == '': return False

        match atributo:
            case 'nome':
                if any(char.isdigit() for char in dado):
                    return False
                
                if len(dado) < 3:
                    return False
                
            case 'email':
                if not '@' in dado or not '.' in dado:
                    return False
            
            case 'cpf':
                if len(dado) != 11:
                    return False
                
                if not dado.isdigit():
                    return False
            
            case 'telefone':
                if len(dado) != 11:
                    return False
                
                if not dado.isdigit():
                    return False
                
            case 'data_nascimento':
                if len(dado) != 10:
                    return False

                if not dado[2] == '/' or not dado[5] == '/':
                    return False
                
                if not dado[:2].isdigit() or not dado[3:5].isdigit() \
                or not dado[6:].isdigit():
                    return False
            
            case 'senha':
                if len(dado) < 8:
                    return False
                
        return True
    
    def converter_nome(self, nome: str) -> str:
        """Converte o nome informado para o padrão 
        Nome Sobrenome.
        Args:
            nome (str): Nome a ser tratado.
        Returns:
            str: Nome tratado.
        """

        return nome.title()
    
    def converter_data(self, data: str) -> str:
        """Converte a data informada do padrão 
        DD/MM/YYYY para YYYY-MM-DD.
        Args:
            data (str): Data a ser tratada.
        Returns:
            str: Data tratada.
        """

        return f'{data[6:]}-{data[3:5]}-{data[:2]}'

tela = Telas()
tela.tela_principal()