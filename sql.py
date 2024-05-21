from conexao import conn

class SQL_COMMANDS:
    def __init__(self):
        self.cur = conn.cursor()

    def create_user(self, nome, cpf, email, data_nascimento, telefone, senha, adm):
        self.cur.execute(f"""SELECT email from usuario WHERE email = '{email}'""")
        rows = self.cur.fetchall()
        if rows == []:
            self.cur.execute(f"""INSERT INTO usuario (nome, cpf, email, data_nascimento, telefone, senha, adm)
                        VALUES ('{nome}', '{cpf}', '{email}', '{data_nascimento}', '{telefone}', '{senha}', '{adm}')""")
            conn.commit()
            return 'Usuário Cadastrado!'
        else:
            return 'Usuário já existente!'
        

    def delete_user(self, email):
        self.cur.execute(f"""SELECT email from usuario WHERE email = '{email}'""")
        rows = self.cur.fetchall()
        if rows == []:
            return "Usuário não encontrado!"
        else:
            self.cur.execute(f""" DELETE FROM usuario
                         WHERE email = '{email}'
                         """)
            conn.commit()
            return "Usuário Removido!"
        
    def validacao_login(self, email, senha):
        self.email = email
        self.senha = senha
        self.cur.execute(f""" SELECT senha, adm, nome, id_usuario FROM usuario
                         WHERE email = '{email}'
                         """)
        rows = self.cur.fetchall()
        conn.commit()
        return rows
        