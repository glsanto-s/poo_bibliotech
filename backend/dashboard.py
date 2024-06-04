from conexao import Conexao

class Dashboard:
    def __init__(self):
        self.cur = Conexao.get_connection().cursor()
        self.conn = Conexao.get_connection()
        
    def totalTabela(self, tabela):
        try:
            self.cur.execute(f"""SELECT COUNT(*) AS qtd FROM {tabela}""")                
            total = self.cur.fetchall()
            self.conn.commit()

            if tabela == 'livro':
                self.cur.execute(f"""SELECT titulo AS qtd FROM {tabela}""") 
            else:
                self.cur.execute(f"""SELECT nome AS qtd FROM {tabela}""")

            nome =  self.cur.fetchall()
            self.conn.commit()
            
            return {'total': total, 'nome': nome}
        except Exception as e:
            print('Error' + e)
            return False
        
    
    
    def infoValidade(self):
        try:
            self.cur.execute(f"""SELECT E.id_emprestimo, E.data_validade, E.data_emprestimo, E.data_devolucao, E.status, U.nome, L.titulo  
                             FROM emprestimo AS E
                             INNER JOIN usuario as U on E.id_usuario = U.id_usuario
                             INNER JOIN livro as L on E.id_livro = L.id_livro
                             ORDER BY E.data_emprestimo ASC""")
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
