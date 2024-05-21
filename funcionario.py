from colorama import init, Fore, Style
from menus_func import menu_principal
import exibir
import catalogo


init(autoreset=True)

class ConfigFuncionario():
   def __init__(self):
     self.funcionario = None 

   def exibirInfo(self, idUsuario):
      self.funcionario = exibir.ExibirInfo(idUsuario).exibir()
      if(self.funcionario and len(self.funcionario) != 0):
         print('')
         print(Fore.YELLOW + "----- Funcionário -----")
         print(f"Nome: {self.funcionario[0][0]}")
         print(f"CPF: {self.funcionario[0][1]}")
         print(f"Email: {self.funcionario[0][2]}")
         print(f"Data de nascimento: {self.funcionario[0][3]}")
         print(f"Telefone: {self.funcionario[0][4]}")
         print(f"Senha: {self.funcionario[0][5]}")
      else:
         print(Fore.RED + 'Erro ao encontrar usuário.')

   
   def exibirMenu(self, idUsuario):
      while True:
         print('')
         print(Fore.BLUE + "----- Menu Principal -----")
         print('1. Minha Conta')
         print('2. Editar Livros')
         print('3. Catálogo de Livros')
         print('4. Dashboard')
         print('0. Sair')

         opcao = input("Escolha uma opção: ")

         if opcao == '1':
            while True:
               self.exibirInfo(idUsuario)
               print('0. Voltar')
               voltar = input()
               if voltar == "0":
                  break

         elif opcao == '2':
            menu_principal.main()
         elif opcao == '3':
           catalogo.Catalogo()
         elif opcao == '4':
            print(Fore.LIGHTYELLOW_EX + 'Opção ainda não configurada!')
         elif opcao == '0':
               print(Fore.BLUE + "Saindo...")
               break
         else:
            print(Fore.RED + "Opção inválida!")






