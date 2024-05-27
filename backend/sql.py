from poo_bibliotech.conexao import Conexao

class SQL_COMMANDS:
    def __init__(self):
        self.conn = Conexao.get_connection()
        self.cur = self.conn.cursor()

    def create_user(self, nome, cpf, email, data_nascimento, telefone, senha, adm):
        self.cur.execute(f"""SELECT email from usuario WHERE email = '{email}'""")
        if self.cur.fetchone():
            return 'Email já Utilizado!'
        
        self.cur.execute(f"""SELECT cpf from usuario WHERE cpf = '{cpf}'""")
        if self.cur.fetchone():
            return 'CPF já Utilizado!'
        
        self.cur.execute(f"""INSERT INTO usuario (nome, cpf, email, data_nascimento, telefone, senha, adm)
                        VALUES ('{nome}', '{cpf}', '{email}', '{data_nascimento}', '{telefone}', '{senha}', '{adm}')""")
        self.conn.commit()
        return 'Usuário Cadastrado!'
        

    def delete_user(self, email):
        self.cur.execute(f"""SELECT email from usuario WHERE email = '{email}'""")
        rows = self.cur.fetchall()
        if rows == []:
            return "Usuário não encontrado!"
        else:
            self.cur.execute(f""" DELETE FROM usuario
                         WHERE email = '{email}'
                         """)
            self.conn.commit()
            return "Usuário Removido!"
        
    def validacao_login(self, email, senha):
        self.email = email
        self.senha = senha
        self.cur.execute(f""" SELECT senha, adm, nome, id_usuario FROM usuario
                         WHERE email = '{email}'
                         """)
        rows = self.cur.fetchall()
        self.conn.commit()
        return rows
        