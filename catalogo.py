from conexao import conn
from colorama import init, Fore, Style

class Catalogo():
  def __init__(self):
    self.cur = conn.cursor()
    self.exibir_catalogo()
       
  def exibir_catalogo(self, opcaoCerta = False):

    if opcaoCerta:
      opcao = opcaoCerta
    else:
      print(Fore.YELLOW + "----- Catálogo -----")
      print('1. Livros')
      print('2. Editoras')
      print('3. Autores')
      print('0. Voltar')
      opcao = input('Escolha uma opção: ')

    if opcao == '1' :
      self.exibir_livros()
    elif opcao == '2' :
      self.exibir_editoras()
    elif opcao == '3' :
      self.exibir_autores()
    elif opcao == '0':
      return
    else:
      voltar = input('Escolha uma opção válida: ')
      self.exibir_catalogo(voltar) 
       
  def exibir_livros(self, opcaoCerta = False):
    self.cur = conn.cursor()
    if opcaoCerta:
      opcao = opcaoCerta
    else:
      print(Fore.YELLOW + "----- Selecionar Livros por -----")
      print("1. Titulo do livro")
      print("2. Categoria do livro")
      print("3. Todos os livros")
      opcao = input('Escolha uma opção: ')
      
    if opcao == '1':
      try:
        titulo = input('Digite o titulo do livro: ')
        self.cur.execute(f"""SELECT L.id_livro, L.titulo, L.categoria, L.data_publicacao, E.nome AS Editora, A.nome as Autor 
                    FROM livro AS L
                    INNER JOIN editora AS E on E.id_editora = L.id_editora
                    INNER JOIN autor AS A on A.id_autor = L.id_autor
                    WHERE L.titulo LIKE '%{titulo}%'""")
        livros = self.cur.fetchall()
        conn.commit()
        if(livros and len(livros) != 0):
          for livro in livros:
            print('')
            print('------')
            print(Fore.LIGHTCYAN_EX + f'ID: {livro[0]}')
            print(f'Título: {livro[1]}')
            print(f'Categoria: {livro[2]}')
            print(f'Data de publicação: {livro[3]}')
            print(f'Editora: {livro[4]}')
            print(f'Autor: {livro[5]}')
          self.exibir_catalogo() 
        else:
          print(Fore.RED+'Não existe esse livro.')
          self.exibir_catalogo() 
      except KeyError as e:
         print(Fore.RED+'Error' + e)

    elif opcao == '2':
      try:
        categoria = input('Digite a categoria do livro: ')
        self.cur.execute(f"""SELECT L.id_livro, L.titulo, L.categoria, L.data_publicacao, E.nome AS Editora, A.nome as Autor 
                    FROM livro AS L
                    INNER JOIN editora AS E on E.id_editora = L.id_editora
                    INNER JOIN autor AS A on A.id_autor = L.id_autor
                    WHERE L.categoria LIKE '%{categoria}%'""")
        livros = self.cur.fetchall()
        conn.commit()
        if(livros and len(livros) != 0):
          for livro in livros:
            print('')
            print('------')
            print(f'Categoria: {livro[2]}')
            print(Fore.LIGHTCYAN_EX +f'ID: {livro[0]}')
            print(f'Título: {livro[1]}')
            print(f'Data de publicação: {livro[3]}')
            print(f'Editora: {livro[4]}')
            print(f'Autor: {livro[5]}')
          self.exibir_catalogo() 
        else:
          print(Fore.RED+'Não existe essa categoria.')
          self.exibir_catalogo() 
      except KeyError as e:
         print('Error' + e)

    elif opcao == '3':
      try:
        self.cur.execute(f"""SELECT L.id_livro, L.titulo, L.categoria, L.data_publicacao, E.nome AS Editora, A.nome as Autor 
                    FROM livro AS L
                    INNER JOIN editora AS E on E.id_editora = L.id_editora
                    INNER JOIN autor AS A on A.id_autor = L.id_autor""")
        livros = self.cur.fetchall()
        conn.commit()
        if(livros and len(livros) != 0):
          for livro in livros:
            print('')
            print('------')
            print(Fore.LIGHTCYAN_EX +f'ID: {livro[0]}')
            print(f'Título: {livro[1]}')
            print(f'Categoria: {livro[2]}')
            print(f'Data de publicação: {livro[3]}')
            print(f'Editora: {livro[4]}')
            print(f'Autor: {livro[5]}')
          self.exibir_catalogo() 
        else:
          print(Fore.RED+'Não existem livros.')
          self.exibir_catalogo() 
      except KeyError as e:
         print('Error' + e)

    else:
      voltar = input('Escolha uma opção válida: ')
      self.exibir_livros(voltar)
        
  def exibir_autores(self, opcaoCerta = False):
    self.cur = conn.cursor()
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
        conn.commit()
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
        conn.commit()
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
    self.cur = conn.cursor()
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
        conn.commit()
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
        conn.commit()
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








