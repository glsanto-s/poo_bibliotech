from colorama import init, Fore

import menus_func.menu_autor
import menus_func.menu_editora
import menus_func.menu_livro

init(autoreset=True)

def exibir_menu_principal():
    print(Fore.YELLOW + "----- Configurar Livros -----")
    print("1. Livros")
    print("2. Autores")
    print("3. Editores")
    print("0. Menu Principal")

def main():
    while True:
        exibir_menu_principal()
        opcao_principal = input("Escolha uma opção: ")

        if opcao_principal == '1':
            while True:
                menus_func.menu_livro.exibir_menu_livros()
                opcao_livros = input("Escolha uma opção: ")

                if opcao_livros == '1':
                    menus_func.menu_livro.adicionar_livro()
                elif opcao_livros == '2':
                    menus_func.menu_livro.excluir_livro()
                elif opcao_livros == '3':
                    menus_func.menu_livro.alterar_livro()
                elif opcao_livros == '0':
                    break
                else:
                    print(Fore.RED + "Opção inválida!")

        elif opcao_principal == '2':
            while True:
                menus_func.menu_autor.exibir_menu_autor()
                opcao_autor = input("Escolha uma opção: ")

                if opcao_autor == '1':
                    menus_func.menu_autor.adicionar_autor()
                elif opcao_autor == '2':
                    menus_func.menu_autor.excluir_autor()
                elif opcao_autor == '3':
                    menus_func.menu_autor.alterar_autor()
                elif opcao_autor == '0':
                    break
                else:
                    print(Fore.RED + "Opção inválida!")

        elif opcao_principal == '3':
            while True:
                menus_func.menu_editora.exibir_menu_editora()
                opcao_editora = input("Escolha uma opção: ")

                if opcao_editora == '1':
                    menus_func.menu_editora.adicionar_editora()
                elif opcao_editora == '2':
                    menus_func.menu_editora.excluir_editora()
                elif opcao_editora == '3':
                    menus_func.menu_editora.alterar_editora()
                elif opcao_editora == '0':
                    break
                else:
                    print(Fore.RED + "Opção inválida!")

        elif opcao_principal == '0':
            print(Fore.BLUE + "Saindo...")
            break

        else:
            print(Fore.RED + "Opção inválida!")

if __name__ == "__main__":
    main()
