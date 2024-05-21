import acoes_funcionario as acoes_funcionario
from colorama import init, Fore, Style

# Inicializar colorama para suportar cores no terminal
init(autoreset=True)

def exibir_menu_livros():
    print(Fore.CYAN + "\n----- Menu Livros -----")
    print("1. Adicionar Livro")
    print("2. Excluir Livro")
    print("3. Alterar Livro")
    print("0. Voltar")
    
def adicionar_livro():
    titulo = input('Título: ')
    autor = input('Nome autor: ')
    editora = input('Nome editora: ')
    categoria = input('Categoria: ')
    isbn = input('ISBN: ')
    dataPublicacao = input('Data de publicação: ')

    idAutor = acoes_funcionario.Autor(
        id=None,
        nome = autor
    )
    idAutor_res = idAutor.procurar('nome',autor)

    idEditora = acoes_funcionario.Editora(
        id=None,
        nome = editora
    )
    idEditora_res = idEditora.procurar('nome',editora)

    addLivro = acoes_funcionario.Livro( 
        id= None, 
        titulo= titulo,
        idAutor= idAutor_res,
        idEditora= idEditora_res,
        categoria= categoria,
        isbn= isbn,
        dataPublicacao= dataPublicacao)
    
    print(Fore.GREEN + "\nAdicionando um novo livro...")
    res = addLivro.adicionar(addLivro.titulo, addLivro.idAutor, addLivro.idEditora, addLivro.categoria, addLivro.isbn, addLivro.dataPublicacao)


    print('Qual tipo de livro você está cadastrando?')
    print('1. Físico')
    print('2. Digital')
    opcao= input('Digite a opção: ')

    pkLivro = addLivro.procurar('titulo', addLivro.titulo)
    if opcao == '1':
        qtd = livro_fisico()
        livroFisico= acoes_funcionario.LivroFisico(
            quantidade = qtd,
            id = None,
            id_livro = pkLivro
        )
        rsp= livroFisico.adicionar(livroFisico.id_livro, livroFisico.quantidade)
        print (rsp)

    elif opcao == '2':
        obj = livro_digital()
        livroDigital= acoes_funcionario.LivroDigital(
            tamanho = obj['tamanho'],
            versao = obj['versao'],
            formato = obj['formato'],
            id = None,
            id_livro = pkLivro
        )
        rsp = livroDigital.adicionar(livroDigital.tamanho, livroDigital.versao, livroDigital.formato, livroDigital.id_livro)
        print  (rsp)
    else:
        print('Opção Incorreta')
        opcao= input('Digite a opção: ')

    print(res)

def excluir_livro():
    id = input('Id do livro: ')

    excluirLivro = acoes_funcionario.Livro(
        id= id, 
        titulo= None,
        idAutor= None,
        idEditora= None,
        categoria= None,
        isbn= None,
        dataPublicacao= None
    )

    print(Fore.GREEN + "\nExcluindo livro...")
    res = excluirLivro.excluir(excluirLivro.id)
    print(res)
    
def alterar_livro():
    print("Caso não queira alterar o campo, deixar vazio!")

    id = input('Id do livro: ')
    titulo = input('Título: ')
    categoria = input('Categora: ')
    isbn = input('ISBN: ')
    dataPublicacao = input('Data de publicação: ')

    alterarLivro = acoes_funcionario.Livro(
        id= id, 
        titulo= titulo,
        idAutor= None,
        idEditora= None,
        categoria= categoria,
        isbn= isbn,
        dataPublicacao= dataPublicacao
    )
    dic = {'titulo': titulo, 'categoria':categoria, 'isbn':isbn, 'dataPublicacao': dataPublicacao}
    values = remover_chaves_vazias(alterarLivro.id,dic)
    print(Fore.GREEN + "\nAlterando livro...")
    res = alterarLivro.alterar(values)

    print(res)

def remover_chaves_vazias(dicionario):
    chaves_para_remover = [chave for chave, valor in dicionario.items() if not valor]
    for chave in chaves_para_remover:
        del dicionario[chave]

def livro_fisico():
    qtd= input('Quantidade: ')
    return qtd

def livro_digital():
    tamanho= input('Tamanho: ')
    versao = input('Versao: ')
    formato= input('Formato: ')

    obj_digital = {
        "tamanho": tamanho,
        "versao": versao,
        "formato": formato
    }
    return obj_digital
