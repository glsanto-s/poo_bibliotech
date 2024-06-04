from conexao import Conexao

class Dashboard:
    def __init__(self):
        self.cur = Conexao.get_connection().cursor()
        self.conn = Conexao.get_connection()
        
    def totalTabela(self, tabela):
        try:
            self.cur.execute(f"""SELECT COUNT(*) FROM {tabela}""")
            total = self.cur.fetchall()
            self.conn.commit()
            
            return total
        except Exception as e:
            print('Error' + e)
            return False
    
    def infoValidade(self):
        try:
            self.cur.execute(f"""SELECT * FROM emprestimo ORDER BY data_emprestimo ASC""")
            emprestimos = self.cur.fetchall()
            self.conn.commit()
            
            return emprestimos
        except Exception as e:
            print('Error' + e)
            return False

    
    def infoMultas(self):
        try:
            self.cur.execute(f"""SELECT  U.nome, U.telefone, U.email, M.valor, E.data_validade  
                             FROM multa as M 
                             INNER JOIN emprestimo as E on M.id_emprestimo = E.id_emprestimo 
                             INNER JOIN usuario as U on E.id_usuario = U.id_usuario""")
            res_info = self.cur.fetchall()
            self.conn.commit()
            
            return res_info
        except Exception as e:
            print('Error' + e)
            return False
