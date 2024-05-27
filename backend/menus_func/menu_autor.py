from poo_bibliotech.acoes_funcionario import Autor
from colorama import init, Fore, Style

# Inicializar colorama para suportar cores no terminal
init(autoreset=True)

def exibir_menu_autor():
    print(Fore.CYAN + "\n----- Menu Autores -----")
    print("1. Adicionar Autor")
    print("2. Excluir Autor")
    print("3. Alterar Autor")
    print("0. Voltar")

def adicionar_autor():
    autor = input('Nome autor: ')

    addAutor = Autor(
        id=None,
        nome = autor
    )
    pesquisa = addAutor.procurar('nome',addAutor.nome)
    if pesquisa == "sem registro": 
        print(Fore.GREEN + "\nAdicionando um novo autor...")
        addAutor.adicionar(addAutor.nome)
    else:
        print(Fore.BLUE + "\nAutor já cadastrado!")

def excluir_autor():
    id = int(input('Id do autor: '))

    excluirAutor = Autor(
        id=id,
        nome = None
    )
    pesquisa = excluirAutor.procurar('id_autor',excluirAutor.id)
    if pesquisa != "sem registro": 
        print(f'Autor prestes a excluir: {pesquisa[1]}')
        op = input("Confirmar (S/N)? ")
        if op == 'S':
            print(Fore.GREEN + "\nExcluindo autor...")
            excluirAutor.excluir(excluirAutor.id)
        else:
            print(Fore.BLUE + "\nVoltando...")
    else:
        print(Fore.RED +'Não foi encontrada nenhum autor com esse id!')

    
def alterar_autor():

    id = int(input('Id do autor: '))
    autor = input('Nome: ')

    alterarAutor = Autor(
        id=id,
        nome = autor
    )
    
    pesquisa = alterarAutor.procurar('id_autor',alterarAutor.id)
    if pesquisa != "sem registro": 
        print(f'Autor prestes a alterar: {pesquisa[1]} para {alterarAutor.nome}')
        op = input("Confirmar (S/N)? ")
        if op == 'S':
            print(Fore.GREEN + "\nAlterando autor...")
            alterarAutor.alterar(alterarAutor.id, nome= alterarAutor.nome)
        else:
            print(Fore.BLUE + "\nVoltando...")
    else:
        print(Fore.RED +'Não foi encontrada nenhum autor com esse id!')