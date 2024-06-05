from conexao import Conexao
from colorama import init, Fore, Style



class Catalogo():
  def __init__(self):
    self.cur = Conexao.get_connection().cursor()
    self.conn = Conexao.get_connection()
    
    
    
  def exibir_livros(self):
    try:
      self.cur.execute(f"""SELECT L.id_livro, L.titulo, L.categoria, L.data_publicacao, E.nome AS Editora, A.nome as Autor 
                  FROM livro AS L
                  INNER JOIN editora AS E on E.id_editora = L.id_editora
                  INNER JOIN autor AS A on A.id_autor = L.id_autor""")
      livros = self.cur.fetchall()
      self.conn.commit()

      self.cur.execute(f"""SELECT L.id_livro, L.titulo, L.categoria, L.data_publicacao, E.nome AS Editora, A.nome as Autor, LF.quantidade 
              FROM livro AS L
              INNER JOIN livro_fisico AS LF on LF.id_livro = L.id_livro
              INNER JOIN editora AS E on E.id_editora = L.id_editora
              INNER JOIN autor AS A on A.id_autor = L.id_autor""")
      livros_fisicos = self.cur.fetchall()
      self.conn.commit()

      self.cur.execute(f"""SELECT L.id_livro, L.titulo, L.categoria, L.data_publicacao, E.nome AS Editora, A.nome as Autor 
              FROM livro AS L
              INNER JOIN livro_digital AS LD on LD.id_livro = L.id_livro
              INNER JOIN editora AS E on E.id_editora = L.id_editora
              INNER JOIN autor AS A on A.id_autor = L.id_autor""")
      livros_digitais = self.cur.fetchall()
      self.conn.commit()

      self.cur.execute(f"""SELECT *
        FROM avaliacao """)
      avaliacao = self.cur.fetchall()
      self.conn.commit()



      if(livros and len(livros) != 0 and livros_fisicos and len(livros_fisicos) != 0 and livros_digitais and len(livros_digitais) != 0):
        return {'livros': livros, 'livros_fisicos': livros_fisicos, 'livros_digitais': livros_digitais, 'avaliacao': avaliacao}
      else:
        return 'error' 
    except KeyError as e:
      print('Error' + e)

  def livros_por_categoria(self, nome_categoria):
    try:
      self.cur.execute(f"""SELECT L.id_livro, L.titulo, L.categoria, L.data_publicacao, E.nome AS Editora, A.nome as Autor 
                  FROM livro AS L
                  INNER JOIN editora AS E on E.id_editora = L.id_editora
                  INNER JOIN autor AS A on A.id_autor = L.id_autor
                  WHERE L.categoria = '{nome_categoria}'""")
      livros = self.cur.fetchall()

      self.cur.execute(f"""SELECT L.id_livro, L.titulo, L.categoria, L.data_publicacao, E.nome AS Editora, A.nome as Autor 
                FROM livro AS L
                INNER JOIN livro_fisico AS LF on LF.id_livro = L.id_livro
                INNER JOIN editora AS E on E.id_editora = L.id_editora
                INNER JOIN autor AS A on A.id_autor = L.id_autor
                WHERE L.categoria = '{nome_categoria}'""")
      livros_fisicos = self.cur.fetchall()
      self.conn.commit()

      self.cur.execute(f"""SELECT L.id_livro, L.titulo, L.categoria, L.data_publicacao, E.nome AS Editora, A.nome as Autor 
          FROM livro AS L
          INNER JOIN livro_digital AS LD on LD.id_livro = L.id_livro
          INNER JOIN editora AS E on E.id_editora = L.id_editora
          INNER JOIN autor AS A on A.id_autor = L.id_autor
          WHERE L.categoria = '{nome_categoria}'""")
      livros_digitais = self.cur.fetchall()
      self.conn.commit()

      self.cur.execute(f"""SELECT id_livro, avg(CAST(nota AS INT)) as Media
FROM avaliacao group by id_livro""")
      avaliacao = self.cur.fetchall()
      self.conn.commit()


      if(livros and len(livros) != 0 and livros_fisicos and len(livros_fisicos) != 0 and livros_digitais and len(livros_digitais) != 0):
        return {'livros': livros, 'livros_fisicos': livros_fisicos, 'livros_digitais': livros_digitais, 'avaliacao': avaliacao}
      else:
        return 'error' 
    except KeyError as e:
      print('Error' + e)




