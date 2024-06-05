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
        

  def exibir_autores(self, opcaoCerta = False):
    self.cur = self.conn.cursor()
    if opcaoCerta:
      opcao = opcaoCerta
    else:
      print(Fore.YELLOW + "----- Selecionar Autores por -----")
      print("1. Nome do autor")
      print("2. Todos os autores")
      opcao = input('Escolha uma opção: ')
      
    if opcao == '1':
      try:
        nome = input('Digite o nome do autor: ')
        self.cur.execute(f"""SELECT id_autor, nome   
                         FROM autor             
                    WHERE nome LIKE '%{nome}%'""")
        autores = self.cur.fetchall()
        self.conn.commit()
        if(autores and len(autores) != 0):
          for autor in autores:
            print('')
            print('------')
            print(Fore.LIGHTCYAN_EX + f'ID: {autor[0]}')
            print(f'Nome do Autor: {autor[1]}')
          self.exibir_catalogo() 
        else:
          print(Fore.RED+'Não existe esse autor.')
          self.exibir_catalogo() 
      except KeyError as e:
         print('Error' + e)
    elif opcao == '2':
      try:
        self.cur.execute(f"""SELECT id_autor, nome   
                         FROM autor""")
        autores = self.cur.fetchall()
        self.conn.commit()
        if(autores and len(autores) != 0):
          for autor in autores:
            print('')
            print('------')
            print(Fore.LIGHTCYAN_EX + f'ID: {autor[0]}')
            print(f'Nome do Autor: {autor[1]}')
          self.exibir_catalogo() 
        else:
          print(Fore.RED+'Não existe esse autor.')
          self.exibir_catalogo() 
      except KeyError as e:
         print('Error' + e)
    else:    
      voltar = input('Escolha uma opção válida: ')
      self.exibir_autores(voltar) 

  def exibir_editoras(self, opcaoCerta = False):
    self.cur = self.conn.cursor()
    if opcaoCerta:
      opcao = opcaoCerta
    else:
      print(Fore.YELLOW + "----- Selecionar Editoras por -----")
      print("1. Nome da editora")
      print("2. Todas as editoras")
      opcao = input('Escolha uma opção: ')
      
    if opcao == '1':
      try:
        nome = input('Digite o nome da editora: ')
        self.cur.execute(f"""SELECT id_editora, nome   
                         FROM editora             
                    WHERE nome = '{nome}'""")
        editoras = self.cur.fetchall()
        self.conn.commit()
        if(editoras and len(editoras) != 0):
          for editora in editoras:
            print('')
            print('------')
            print(Fore.LIGHTCYAN_EX + f'ID: {editora[0]}')
            print(f'Nome da Editora: {editora[1]}')
          self.exibir_catalogo() 
        else:
          print(Fore.RED+'Não existe essa editora.')
          self.exibir_catalogo() 
      except KeyError as e:
         print('Error' + e)
    elif opcao == '2':
      try:
        self.cur.execute(f"""SELECT id_editora, nome   
                         FROM editora""")
        editoras = self.cur.fetchall()
        self.conn.commit()
        if(editoras and len(editoras) != 0):
          for editora in editoras:
            print('')
            print('------')
            print(Fore.LIGHTCYAN_EX + f'ID: {editora[0]}')
            print(f'Nome da Editora: {editora[1]}')
          self.exibir_catalogo() 
        else:
          print(Fore.RED+'Não existe essa editora.')
          self.exibir_catalogo() 
      except KeyError as e:
         print('Error' + e)
    else:    
      voltar = input('Escolha uma opção válida: ')
      self.exibir_editoras(voltar) 








