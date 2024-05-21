from conexao import conn
from colorama import init, Fore, Style



class Catalogo():
  def __init__(self):
    self.cur = conn.cursor()


    self.exibir_catalogo()
    
    
  def exibir_catalogo(self, opcaoCerta = False):
    print(Fore.YELLOW + "----- Catálogo -----")
    print('1. Livros')
    print('2. Editoras')
    print('3. Autores')
    print('0. Voltar')

    if opcaoCerta:
      opcao = opcaoCerta
    else:
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
    print(Fore.YELLOW + "----- Selecionar livros por -----")
    if opcaoCerta:
      opcao = opcaoCerta
    else:
      print("1. Titulo do livro")
      print("2. Categoria do livro")
      print("3. Todos os livros")
      opcao = input('Escolha uma opção: ')
      
    if opcao == '1':
      try:
        titulo = input('Digite o titulo do livro: ')
        self.cur.execute(f"""SELECT L.titulo, L.categoria, L.data_publicacao, E.nome AS Editora, A.nome as Autor 
                    FROM livro AS L
                    INNER JOIN editora AS E on E.id_editora = L.id_editora
                    INNER JOIN autor AS A on A.id_autor = L.id_autor
                    WHERE L.titulo = '{titulo}'""")
        livros = self.cur.fetchall()
        conn.commit()
        if(livros and len(livros) != 0):
          for livro in livros:
            print('')
            print('------')
            print(f'Título: {livro[0]}')
            print(f'Categoria: {livro[1]}')
            print(f'Data de publicação: {livro[2]}')
            print(f'Editora: {livro[3]}')
            print(f'Autor: {livro[4]}')
        else:
          print('Não existe esse livro.')
          self.exibir_catalogo() 
      except KeyError as e:
         print('Error' + e)

    elif opcao == '2':
      try:
        categoria = input('Digite a categoria do livro: ')
        self.cur.execute(f"""SELECT L.titulo, L.categoria, L.data_publicacao, E.nome AS Editora, A.nome as Autor 
                    FROM livro AS L
                    INNER JOIN editora AS E on E.id_editora = L.id_editora
                    INNER JOIN autor AS A on A.id_autor = L.id_autor
                    WHERE L.categoria = '{categoria}'""")
        livros = self.cur.fetchall()
        conn.commit()
        if(livros and len(livros) != 0):
          for livro in livros:
            print('')
            print('------')
            print(f'Categoria: {livro[1]}')
            print(f'Título: {livro[0]}')
            print(f'Data de publicação: {livro[2]}')
            print(f'Editora: {livro[3]}')
            print(f'Autor: {livro[4]}')
        else:
          print('Não existe essa categoria.')
          self.exibir_catalogo() 
      except KeyError as e:
         print('Error' + e)

    elif opcao == '3':
      try:
        self.cur.execute(f"""SELECT L.titulo, L.categoria, L.data_publicacao, E.nome AS Editora, A.nome as Autor 
                    FROM livro AS L
                    INNER JOIN editora AS E on E.id_editora = L.id_editora
                    INNER JOIN autor AS A on A.id_autor = L.id_autor""")
        livros = self.cur.fetchall()
        conn.commit()
        if(livros and len(livros) != 0):
          for livro in livros:
            print('')
            print('------')
            print(f'Título: {livro[0]}')
            print(f'Categoria: {livro[1]}')
            print(f'Data de publicação: {livro[2]}')
            print(f'Editora: {livro[3]}')
            print(f'Autor: {livro[4]}')
        else:
          print('Não existem livros.')
          self.exibir_catalogo() 
      except KeyError as e:
         print('Error' + e)

    else:
      voltar = input('Escolha uma opção válida: ')
      self.exibir_livros(voltar)
        

  def exibir_autores(self):
    print('Opção ainda não configurada!')

  def exibir_editoras(self):
    print('Opção ainda não configurada!')







