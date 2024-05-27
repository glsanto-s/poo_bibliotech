from poo_bibliotech.acoes_funcionario import Editora
from colorama import init, Fore, Style

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
    idEditora_res = addEditora.procurar('nome', addEditora.nome)
    
    if idEditora_res == "sem registro":
        print(Fore.GREEN + "\nAdicionando um nova editora...")
        res = addEditora.adicionar(addEditora.nome)
    else:
        res = Fore.YELLOW +"Editora já cadastrada!"
    print(res)


def excluir_editora():
    id = int(input('Id da editora: '))

    excluirEditora = Editora(
        id=id,
        nome = None
    )
    
    pesquisa = excluirEditora.procurar('id_editora',excluirEditora.id)
    if pesquisa != "sem registro": 
        print(f'Editora prestes a excluir: {pesquisa[1]}')
        op = input("Confirmar (S/N)? ")
        if op == 'S':
            print(Fore.GREEN + "\nExcluindo editora...")
            res = excluirEditora.excluir(excluirEditora.id)
            print(res)
        else:
            print(Fore.BLUE + "\nVoltando...")
    else:
        print(Fore.RED +'Não foi encontrada nenhuma editora com esse id!')

    
def alterar_editora():

    id = int(input('Id da editora: '))
    editora = input('Nome: ')

    alterarEditora = Editora(
        id=id,
        nome = editora
    )
    pesquisa = alterarEditora.procurar('id_editora',alterarEditora.id)
    if pesquisa != "sem registro": 
        print(f'Editora prestes a editar: {pesquisa[1]} para {alterarEditora.nome}')
        op = input("Confirmar (S/N)? ")
        if op == 'S':
            print(Fore.GREEN + "\nAlterando editora...")
            res = alterarEditora.alterar(alterarEditora.id, nome = alterarEditora.nome)
            print(res)
        else:
            print(Fore.BLUE + "\nVoltando...")
    else:
        print(Fore.RED +'Não foi encontrada nenhuma editora com esse id!')

    