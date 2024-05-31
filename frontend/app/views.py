from django.shortcuts import render, redirect
from backend.catalogo import Catalogo
from backend.usuario import Usuario 
from .forms import CadastroForm
from .forms import Login

# Create your views here.

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
    categorias = listar_categorias(Catalogo().exibir_livros())
    livros = Catalogo().livros_por_categoria(categoria)
    return render(request, 'templates/categoria.html', {'categoria_selecionada': categoria, 'categorias': categorias, 'livros': livros})


def listar_livros(request):
    idUser = request.session.get('idUser')
    if idUser is not None:
        livros = Catalogo().exibir_livros()
        categorias = listar_categorias(livros)
        return render(request, 'templates/catalogo.html', {'livros': livros, 'categorias': categorias})
    else:
        request.session['LoginMensagem'] = 'Você precisa estar logado para acessar a página de catálogo.'
        request.session.save()
        return redirect('login')
    
def logar(request):
    mensagem = ''
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']

            validarUser = Usuario().logar(email,senha)
            if validarUser["status"] == True:
                request.session['idUser'] = validarUser["id"]
                request.session.save()
                if validarUser['adm'] == 0:
                    return redirect('catalogo')
                else:
                    request.session['LoginMensagem'] = 'Tela de adm, ainda em andamento!'
                    request.session.save()
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