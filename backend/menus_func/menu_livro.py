import poo_bibliotech.acoes_funcionario as acoes_funcionario
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
    idAutor = acoes_funcionario.Autor(
        id=None,
        nome = autor
    )
    idAutor_res = idAutor.procurar('nome',autor)

    editora = input('Nome editora: ')
    idEditora = acoes_funcionario.Editora(
        id=None,
        nome = editora
    )
    idEditora_res = idEditora.procurar('nome',editora)

    if idAutor_res == "sem registro":
        return print(Fore.YELLOW + 'Não encontramos o autor! Registre-o primeiro e depois tente adicionar o livro novamente.')
    elif  idEditora_res == "sem registro":
        return print(Fore.YELLOW + 'Não encontramos a editora! Registre-a primeiro e depois tente adicionar o livro novamente.')
    
    categoria = input('Categoria: ')
    isbn = input('ISBN: ')
    dataPublicacao = input('Data de publicação: ')
    
    addLivro = acoes_funcionario.Livro( 
        id= None, 
        titulo= titulo,
        idAutor= idAutor_res[0],
        idEditora= idEditora_res[0],
        categoria= categoria,
        isbn= isbn,
        dataPublicacao= dataPublicacao)
    
    pesquisa = addLivro.procurar('titulo', addLivro.titulo)
    if pesquisa != "sem registro":
        return print(Fore.RED + 'Livro já existente, verifique o catálogo!')

    print(Fore.GREEN + "\nAdicionando um novo livro...")
    addLivro.adicionar(
        addLivro.titulo, 
        addLivro.idAutor, 
        addLivro.idEditora, 
        addLivro.categoria, 
        addLivro.isbn, 
        addLivro.dataPublicacao)

    print('Qual tipo de livro você está cadastrando?')
    print('1. Físico')
    print('2. Digital')
    opcao= input('Digite a opção: ')

    livro_res = addLivro.procurar('titulo', addLivro.titulo)
    if opcao == '1':
        qtd = livro_fisico()
        livroFisico = acoes_funcionario.LivroFisico(
            id_livro = livro_res[0],
            quantidade = qtd,
            id = None
        )
        livroFisico.adicionar(livroFisico.id_livro, livroFisico.quantidade)

    elif opcao == '2':
        obj = livro_digital()
        livroDigital= acoes_funcionario.LivroDigital(
            id_livro = livro_res[0],
            tamanho = obj['tamanho'],
            versao = obj['versao'],
            formato = obj['formato'],
            id = None
        )
        livroDigital.adicionar(
            livroDigital.id_livro,
            livroDigital.tamanho, 
            livroDigital.versao, 
            livroDigital.formato)
    else:
        print('Opção Incorreta')
        opcao= input('Digite a opção: ')

    print(Fore.GREEN + 'Livro adicionado com sucesso!')

def excluir_livro():
    id = int(input('Id do livro: '))

    excluirLivro = acoes_funcionario.Livro(
        id= id, 
        titulo= None,
        idAutor= None,
        idEditora= None,
        categoria= None,
        isbn= None,
        dataPublicacao= None
    )

    pesquisa = excluirLivro.procurar('id_livro',excluirLivro.id)
    if pesquisa != "sem registro": 
        print(f'Livro prestes a excluir: {pesquisa[1]}')
        op = input("Confirmar (S/N)? ")
        if op == 'S':
            print(Fore.GREEN + "\nExcluindo livro...")
            res = excluirLivro.excluir(excluirLivro.id)
            print(res)
        else:
            print(Fore.BLUE + "\nVoltando...")
    else:
        print(Fore.RED +'Não foi encontrada nenhum livro com esse id!')

    
    
def alterar_livro():
    print("Caso não queira alterar o campo, deixar vazio!")

    id = int(input('Id do livro: '))
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

    pesquisa = alterarLivro.procurar('id_livro',alterarLivro.id)
    if pesquisa != "sem registro": 
        print(f'Livro prestes a editar: {pesquisa[1]}')
        op = input("Confirmar (S/N)? ")
        if op == 'S':
            print(Fore.GREEN + "\nAlterando livro...")
            res = alterarLivro.alterar(alterarLivro.id,values)
            print(res)
        else:
            print(Fore.BLUE + "\nVoltando...")
    else:
        print(Fore.RED +'Não foi encontrada nenhum livro com esse id!')
    

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
