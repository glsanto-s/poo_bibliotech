from conexao import Conexao 
from datetime import datetime 

class Base():
    def __init__(self, tabela, campos):
        self.tabela = tabela
        self.campos = campos

    def adicionar(self, *dados):
        if len(dados) != len(self.campos):
            return 'Número incorreto de argumentos'
        
        valores_convertidos = []
        for item in dados:
            if isinstance(item, str) and len(item) == 10 and item[4] == '-' and item[7] == '-':
                valores_convertidos.append(f"DATE('{item}')")
            else:
                valores_convertidos.append(f"'{item}'")
        valores = ', '.join(valores_convertidos)
        campos = ', '.join(self.campos)

        conection = None
        cursor = None
        try:
            conection = Conexao.get_connection()
            cursor = conection.cursor()
            query = f"INSERT INTO {self.tabela} ({campos}) VALUES ({valores})"

            cursor.execute(query)
            conection.commit()
            return f'Sucesso'
        except KeyError as e:
            conection.rollback()
            print("Erro ao executar a consulta:", e)
    
    def alterar(self, id, **dic):
        for chave in dic.keys():
            if chave not in self.campos:
                return 'Campos não válidos!'
            
            campoId = f"id_{self.tabela}"
            campos_valores= ','.join([f"{campo}='{valor}'" for campo, valor in dic.items()])

            conection = None
            cursor = None
            try:
                conection = Conexao.get_connection()
                cursor = conection.cursor()
                query = f"UPDATE {self.tabela} SET {campos_valores} WHERE {campoId} = {id}"
                cursor.execute(query)
                conection.commit()

                linhas_afetadas = cursor.rowcount
                return f'Linhas afetadas: {linhas_afetadas}'
            
            except KeyError as e:
                conection.rollback()
                print("Erro ao executar a consulta:", e)
    
    def excluir(self, id):
        campoId = f'id_{self.tabela}'

        conection = None
        cursor = None
        try:
            conection = Conexao.get_connection()
            cursor = conection.cursor()
            query = f"DELETE FROM {self.tabela} WHERE {campoId} = {id}"
            cursor.execute(query)
            conection.commit()

            linhas_afetadas = cursor.rowcount
            return f'Linhas afetadas: {linhas_afetadas}'
        
        except KeyError as e:
            conection.rollback()
            print("Erro ao executar a consulta:", e)

    def procurar(self, campo, valor):  
        conection = None
        cursor = None
        try:
            conection = Conexao.get_connection()
            cursor = conection.cursor()
            if isinstance(valor, (int, float, complex)):
                query = f"SELECT * FROM {self.tabela} WHERE {campo} = {valor}"
            else:
                query = f"SELECT * FROM {self.tabela} WHERE {campo} LIKE '%{valor}%'"

            cursor.execute(query)

            res = cursor.fetchone()
            if res:
                retorno = res
            else:
                retorno = "sem registro"

            conection.commit()
            return retorno
        except KeyError as e:
            conection.rollback()
            print("Erro ao executar a consulta:", e)


class Livro(Base):
    def __init__(self, titulo, idAutor, idEditora, categoria, isbn, dataPublicacao, id):
        self.id = id
        self.titulo = titulo
        self.idAutor = idAutor
        self.idEditora = idEditora
        self.categoria = categoria
        self.isbn = isbn
        self.dataPublicacao = dataPublicacao
        super().__init__('livro',['titulo','id_autor', 'id_editora','categoria','isbn','data_publicacao'])

class LivroDigital(Base):
    def __init__(self, id_livro,tamanho, versao, formato, id):
        self.id = id
        self.tamanho = tamanho
        self.versao = versao
        self.formato = formato
        self.id_livro = id_livro

        super().__init__('livro_digital', ['id_livro','tamanho','versao','formato'])

class LivroFisico(Base):
    def __init__(self, id_livro, quantidade, id):
        self.id = id
        self.quantidade = quantidade
        self.id_livro = id_livro

        super().__init__('livro_fisico', ['id_livro','quantidade'])

class Editora(Base):
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        super().__init__('editora',['nome'])

class Autor(Base):
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        super().__init__('autor',['nome'])