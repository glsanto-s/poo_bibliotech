from django.shortcuts import render, redirect
from backend.catalogo import Catalogo
from backend.usuario import Usuario, Cliente
from backend.acoes_funcionario import Livro, LivroDigital, LivroFisico, Autor, Editora
from backend.exibir import ExibirInfo
from .forms import CadastroForm, Login, CadastroLivro, ProcurarAutor,ProcurarEditora, Excluir, EditarLivro,EditarAutorEditora,CadastroDigital,CadastroFisico, AtualizarUsuario
from django.contrib import messages
from backend.exibir import ExibirInfo


def listar_categorias(livros):
    categorias = []
    if livros == 'error':
        categorias = 'Error'
    else:
        categorias = set()
        for livro in livros:
            categorias.add(livro[2])
    return categorias

def categoria(request, categoria):
    idUser = request.session.get('idUser')
    sessaoADM = request.session.get('UserADM')
    if idUser is not None or sessaoADM is not None:
        categorias = listar_categorias(Catalogo().exibir_livros())
        livros = Catalogo().livros_por_categoria(categoria)
        return render(request, 'templates/categoria.html', {'categoria_selecionada': categoria, 'categorias': categorias, 'livros': livros, 'idUser':idUser,'userADM':sessaoADM})
    else:
        return redirect('login')


def listar_livros(request):
    idUser = request.session.get('idUser')
    sessaoADM = request.session.get('UserADM')
    if idUser is not None or sessaoADM is not None:
        livros = Catalogo().exibir_livros()
        categorias = listar_categorias(livros)
        request.session.save()
        if livros:
             return render(request, 'templates/catalogo.html', {'livros': livros['livros'], 'livros_digitais': livros['livros_digitais'], 'livros_fisicos': livros['livros_fisicos'], 'categorias': categorias, 'idUser':idUser,'userADM':sessaoADM})
        else:
            return render(request, 'templates/catalogo.html', {'livros': False, 'categorias': categorias, 'idUser':idUser,'userADM':sessaoADM})
    else:
        request.session['LoginMensagem'] = 'Você precisa estar logado para acessar a página desejada!'
        request.session.save()
        return redirect('login')
    
def logar(request):
    idUser = request.session.get('idUser')
    print(idUser)
    if idUser is None:
        mensagem = ''
        if request.method == 'POST':
            form = Login(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                senha = form.cleaned_data['senha']
                validarUser = Usuario().logar(email,senha)
                if validarUser["status"] == True:
                    if validarUser['adm'] == '0':
                        request.session['idUser'] = validarUser["id"]
                        request.session.save()
                        return redirect('catalogo')
                    else:
                        request.session['UserADM'] = validarUser['id']
                        request.session.save()
                        return redirect('catalogo')
                else:
                    request.session['LoginMensagem'] = validarUser["message"] 
                    request.session.save()
        else:
            form = Login()
    
        mensagemSession = request.session.get('LoginMensagem')
        if mensagemSession:
            mensagem = mensagemSession
            del request.session['LoginMensagem']
            request.session.save()
            
        return render(request, 'templates/login.html', {'form':form,'message':mensagem})
    else:
        return redirect('catalogo')

def registrar(request):
    mensagem = ''
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            cpf = form.cleaned_data['cpf']
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            data_nascimento = form.cleaned_data['data_nascimento']
            telefone = form.cleaned_data['telefone']

            cadastraUser = Usuario().cadastrar(nome,cpf,email,data_nascimento,telefone,senha)
            if cadastraUser != 'Usuário Cadastrado!':
                request.session['CadastroMensagem'] = cadastraUser
                request.session.save()
                return redirect('cadastro')
            else:
                request.session['LoginMensagem'] = f'{cadastraUser} Faça seu login.'
                request.session.save()
                return redirect('login')
    else:
        form = CadastroForm()
    
    mensagemSession = request.session.get('CadastroMensagem')
    if mensagemSession:
        mensagem = mensagemSession
        del request.session['CadastroMensagem']
        request.session.save()
        
    return render(request, 'templates/cadastro.html', {'form': form , 'message':mensagem})


def historico (request):
    
    iduser = request.session.get('idUser') 
    if iduser is not None:
        exibir_historico= ExibirInfo (idUsuario=iduser)
        resp= exibir_historico.exibir_emprestimos
        #del request.session['idUser']
        #request.session.save()
        return render(request, 'templates/historico.html', {'emprestimo': resp})
    else:
        request.session['LoginMensagem'] = 'Você precisa estar logado para acessar a página desejada!'
        request.session.save()
        return redirect('login')
    