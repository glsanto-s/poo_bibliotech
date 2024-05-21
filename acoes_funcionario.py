from conexao import conn 
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
            if isinstance(item, str):
                try:
                    data = datetime.strptime(item, "%d/%m/%Y")
                    valores_convertidos.append(f"'{data.strftime('%Y-%m-%d')}'")
                except ValueError:
                    valores_convertidos.append(f"'{item}'")
            else:
                valores_convertidos.append(str(item))
        valores = ', '.join(valores_convertidos)
        campos = ', '.join(self.campos)

        conection = None
        cursor = None
        try:
            conection = conn
            cursor = conection.cursor()
            query = f"INSERT INTO {self.tabela} ({campos}) VALUES ({valores})"
            cursor.execute(query)
            conection.commit()
            
            linhas_afetadas = cursor.rowcount
            return f'Linhas adicionadas: {linhas_afetadas}'
        except KeyError as e:
            conection.rollback()
            print("Erro ao executar a consulta:", e)
        finally:
            cursor.close()
            conection.close()
    
    def alterar(self, id, **dic):
        for chave in dic.keys():
            if chave not in self.campos:
                return 'Campos não válidos!'
            
            campoId = f"id_{self.tabela}"
            campos_valores= ','.join([f"{campo}='{valor}'" for campo, valor in dic.items()])

            conection = None
            cursor = None
            try:
                conection = conn
                cursor = conection.cursor()
                query = f"UPDATE {self.tabela} SET {campos_valores} WHERE {campoId} = {id}"
                cursor.execute(query)
                conection.commit()

                linhas_afetadas = cursor.rowcount
                return f'Linhas afetadas: {linhas_afetadas}'
            
            except KeyError as e:
                conection.rollback()
                print("Erro ao executar a consulta:", e)

            finally:
                cursor.close()
                conection.close()
    
    def excluir(self, id):
        campoId = f'id_{self.tabela}'

        conection = None
        cursor = None
        try:
            conection = conn
            cursor = conection.cursor()
            query = f"DELETE FROM {self.tabela} WHERE {campoId} = {id}"
            cursor.execute(query)
            conection.commit()

            linhas_afetadas = cursor.rowcount
            return f'Linhas afetadas: {linhas_afetadas}'
        
        except KeyError as e:
            conection.rollback()
            print("Erro ao executar a consulta:", e)

        finally:
            cursor.close()
            conection.close()


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
    def __init__(self, tamanho, versao, formato, id_livro,id):
        self.id = id
        self.tamanho = tamanho
        self.versao = versao
        self.formato = formato
        self.id_livro = id_livro

        super().__init__('livro_digital', ['id_livro','tamanho','versao','formato'])

class LivroFisico(Base):
    def __init__(self, quantidade, id_livro):
        self.quantidade = quantidade
        self.id_livro = id_livro

        super().__init__('livro_fisico', ['id_livro','quantidade'])

class Editora(Base):
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        super().__init__('editora',['nome'])

    def procurar(self, nome):
        conection = None
        cursor = None
        try:
            conection = conn
            cursor = conection.cursor()
            query = f"SELECT id_editora FROM {self.tabela} WHERE nome LIKE '%{nome}%'"
            cursor.execute(query)

            res = cursor.fetchone()
            if res:
                print("Consulta bem-sucedida!")
                id = res[0]
            else:
                print("Nenhum resultado encontrado para o nome:", nome)
                id = "sem cadastro"

            conection.commit()
            return id
        except KeyError as e:
            conection.rollback()
            print("Erro ao executar a consulta:", e)
        finally:
            cursor.close()
            conection.close()

class Autor(Base):
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        super().__init__('autor',['nome'])
    
    def procurar(self, nome):
        conection = None
        cursor = None
        try:
            conection = conn
            cursor = conection.cursor()
            query = f"SELECT * FROM {self.tabela} WHERE nome LIKE '%{nome}%'"
            cursor.execute(query)

            res = cursor.fetchone()
            if res:
                print("Consulta bem-sucedida!")
                id = res[0]
            else:
                print("Nenhum resultado encontrado para o nome:", nome)
                id = "sem cadastro"

            conection.commit()
            return id
        except KeyError as e:
            conection.rollback()
            print("Erro ao executar a consulta:", e)
        finally:
            cursor.close()
            conection.close()

