from colorama import init, Fore, Style
import exibir

# Inicializar colorama para suportar cores no terminal
init(autoreset=True)

class Cliente():
   def __init__(self):
     self.cliente =  None

   def exibirInfo(self, idUsuario):
      self.cliente = exibir.ExibirInfo(idUsuario).exibir()
      if(self.cliente and len(self.cliente) != 0):
         print(Fore.YELLOW + "----- Usuário -----")
         print(f"Nome: {self.cliente[0][0]}")
         print(f"CPF: {self.cliente[0][1]}")
         print(f"Email: {self.cliente[0][2]}")
         print(f"Data de nascimento: {self.cliente[0][3]}")
         print(f"Telefone: {self.cliente[0][4]}")
      else:
         print(Fore.RED + 'Erro ao encontrar usuário.')


   def exibirMenu(self, idUsuario):

      while True:
         print(Fore.BLUE + "----- Menu Principal -----")
         print('1. Minha Conta')
         print('2. Catálogo de Livros')
         print('3. Contato')
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
            print('')
         #   exibirLivros
         
         elif opcao == '3':
             print(Fore.LIGHTYELLOW_EX + 'Opção ainda não configurada!')

         elif opcao == '0':
               print(Fore.BLUE + "Saindo...")
               break
         else:
            print(Fore.RED + "Opção inválida!")
        
        

