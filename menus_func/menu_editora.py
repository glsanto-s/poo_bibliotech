from acoes_funcionario import Editora
from colorama import init, Fore, Style

# Inicializar colorama para suportar cores no terminal
init(autoreset=True)

def exibir_menu_editora():
    print(Fore.CYAN + "\n----- Menu Editoras -----")
    print("1. Adicionar Editora")
    print("2. Excluir Editora")
    print("3. Alterar Editora")
    print("0. Voltar")


def adicionar_editora():
    editora = input('Nome editora: ')

    addEditora = Editora(
        id=None,
        nome = editora
    )
    idEditora_res = addEditora.procurar(addEditora.nome)
    
    if idEditora_res == "sem cadastro":
        print(Fore.GREEN + "\nAdicionando um novo autor...")
        res = addEditora.adicionar(addEditora.nome)
    else:
        res = "Editora já cadastrada!"
    print(res)
    


def excluir_editora():
    id = input('Id da editora: ')

    excluirEditora = Editora(
        id=id,
        nome = None
    )
    
    # TO DO: PROCURAR ANTES DE EXCLUIR?

    print(Fore.GREEN + "\nExcluindo editora...")
    res = excluirEditora.excluir(excluirEditora.id)
    print(res)
    
def alterar_editora():

    id = input('Id do autor: ')
    editora = input('Nome: ')

    alterarEditora = Editora(
        id=id,
        nome = editora
    )

    print(Fore.GREEN + "\nAlterando autor...")
    res = alterarEditora.alterar(id, nome = alterarEditora.nome)
    print(res)