from conexao import Conexao
from psycopg2 import sql
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
                         WHERE email = '{self.email}'
                         """)
        rows = self.cur.fetchall()
        self.conn.commit()
        return rows
    
    def atualizar_usuario(self, campos_para_atualizar, valores):
        self.campos_para_atualizar = campos_para_atualizar
        self.valores = valores

        query = sql.SQL("UPDATE usuario SET {} WHERE id_usuario = %s").format(
            sql.SQL(", ").join(map(sql.SQL, campos_para_atualizar))
        )
        self.cur.execute(query, valores)

        self.conn.commit()
        return "Dados Atualizados!"
    ####################################### Reservas / Empréstimos #######################################
    def criar_reserva(self, idusuario, idlivro):
        self.cur.execute(f"""SELECT * from reserva WHERE id_usuario = {idusuario} AND id_livro = {idlivro}""")
        rows = self.cur.fetchall()
        if rows == []:
            self.cur.execute(f"""WITH posicao_nova AS (
    SELECT COALESCE(MAX(posicao), 0) + 1 AS posicao_nova
    FROM reserva 
    WHERE id_livro = {idlivro}
)
INSERT INTO reserva (id_usuario, id_livro, posicao)
VALUES ({idusuario}, {idlivro}, (SELECT posicao_nova FROM posicao_nova))""")
            self.conn.commit()
            return "Livro reservado!"
        else:
            self.conn.commit()
            return "Este livro já foi reservado!"
        
    def cancelar_reserva(self, idusuario, idlivro):
        self.cur.execute(f"""DELETE FROM reserva WHERE id_usuario = {idusuario} AND id_livro = {idlivro}""")
        self.conn.commit()
        return "Reserva Cancelada!"
        