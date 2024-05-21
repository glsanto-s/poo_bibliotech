from acoes_funcionario import Autor
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
    idAutor_res = addAutor.procurar(addAutor.nome)
    
    if idAutor_res == "sem cadastro":
        print(Fore.GREEN + "\nAdicionando um novo autor...")
        res = addAutor.adicionar(addAutor.nome)
    else:
        res = "Autor já cadastrado!"
    print(res)
    


def excluir_autor():
    id = input('Id do autor: ')

    excluirAutor = Autor(
        id=id,
        nome = None
    )

    print(Fore.GREEN + "\nExcluindo autor...")
    res = excluirAutor.excluir(excluirAutor.id)
    print(res)
    
def alterar_autor():

    id = input('Id do autor: ')
    autor = input('Nome: ')

    alterarAutor = Autor(
        id=id,
        nome = autor
    )

    print(Fore.GREEN + "\nAlterando autor...")
    res = alterarAutor.alterar(id, nome= alterarAutor.nome)
    print(res)