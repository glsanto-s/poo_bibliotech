from conexao import conn

class ExibirInfo:
  def __init__(self, idUsuario):
    self.idUsuario = idUsuario
    self.cur = conn.cursor()
    self.usuario = False
     
  def exibir(self):
    try:
      self.cur.execute(f"""SELECT nome, cpf, email, data_nascimento, telefone, senha, adm FROM usuario WHERE id_usuario = '{self.idUsuario}'""")
      usuarios = self.cur.fetchall()
      conn.commit()
      self.usuario = usuarios
      return self.usuario
    except KeyError as e:
      print('Error' + e)
      return False



