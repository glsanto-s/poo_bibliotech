from conexao import Conexao

class ExibirInfo:
  def __init__(self, idUsuario):
    self.idUsuario = idUsuario
    self.conn = Conexao.get_connection()
    self.cur = self.conn.cursor()
    self.usuario = False
     
  def exibir(self):
    try:
      self.cur.execute(f"""SELECT nome, cpf, email, data_nascimento, telefone FROM usuario WHERE id_usuario = '{self.idUsuario}'""")
      usuarios = self.cur.fetchall()
      self.conn.commit()
      self.usuario = usuarios
      return self.usuario
    except KeyError as e:
      print('Error' + e)
      return False

  def exibir_emprestimos(self):
    self.cur.execute(f"""select L.titulo , L.categoria, E.data_validade, E.data_emprestimo , E.data_devolucao , E.status  from emprestimo as E inner join livro as L on E.id_livro = L.id_livro  where E.id_usuario = {self.idUsuario} order by E.data_emprestimo asc""")
    emprestimos = self.cur.fetchall()
    return emprestimos

  def exibir_reservas(self):
    self.cur.execute(f"""SELECT * FROM reserva WHERE id_usuario = {self.idUsuario} ORDER BY data_reserva ASC""")
    reservas = self.cur.fetchall()
    return reservas



