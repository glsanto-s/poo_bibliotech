from poo_bibliotech.conexao import Conexao

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



