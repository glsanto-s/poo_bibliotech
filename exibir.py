from cliente import Cliente
from funcionario import Funcionario
from conexao import conn


class ExibirInfo:
  def __init__(self, usuario):
    self.usuario = usuario
    self.cur = conn.cursor()
     
  def exibir(self):
    idUsuario = self.usuario['id']
    try:
      self.cur.execute(f"""SELECT nome, cpf, email, data_nascimento, telefone, senha, adm FROM usuario WHERE id_usuario = '{idUsuario}'""")
      usuario = self.cur.fetchall()
      conn.commit()
      return usuario
    except KeyError as e:
      print('Error' + e)
    finally:
      self.cur.close()
      conn.close()


rows = ExibirInfo({'id': '2', 'Message': 'Login Realizado com Sucesso! Funcionário: Rogerin-ADM'}).exibir()

if rows[0][6] == '0':
  usuario = Cliente(rows)
  usuario.exibir()
else:
  usuario = Funcionario(rows)
  usuario.exibir()


