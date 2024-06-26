from django.shortcuts import render, redirect
from backend.catalogo import Catalogo
from backend.usuario import Usuario, Cliente
from backend.acoes_funcionario import Livro, LivroDigital, LivroFisico, Autor, Editora, Base
from .forms import CadastroForm, Login, CadastroLivro, ProcurarAutor,ProcurarEditora, Excluir, EditarLivro,EditarAutorEditora,CadastroDigital,CadastroFisico, AtualizarUsuario
from django.contrib import messages
from backend.exibir import ExibirInfo
from backend.dashboard import Dashboard


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
        livroCategoria = Catalogo().exibir_livros()
        categorias = listar_categorias(livroCategoria['livros'])
        livros = Catalogo().livros_por_categoria(categoria)
        print(livros['avaliacao'])
        return render(request, 'templates/categoria.html', {'categoria_selecionada': categoria, 'categorias': categorias, 'livros': livros['livros'],'livros_digitais': livros['livros_digitais'], 'livros_fisicos': livros['livros_fisicos'], 'idUser':idUser,'userADM':sessaoADM, 'avaliacao': livros['avaliacao']})
    else:
        return redirect('login')

def listar_livros(request):
    idUser = request.session.get('idUser')
    sessaoADM = request.session.get('UserADM')
    if idUser is not None or sessaoADM is not None:
        livros = Catalogo().exibir_livros()
        categorias = listar_categorias(livros['livros'])
        request.session.save()
        if livros:
             print(livros['avaliacao'])
             return render(request, 'templates/catalogo.html', {'livros': livros['livros'], 'livros_digitais': livros['livros_digitais'], 'livros_fisicos': livros['livros_fisicos'], 'categorias': categorias, 'idUser':idUser,'userADM':sessaoADM, 'avaliacao': livros['avaliacao']})
        else:
            return render(request, 'templates/catalogo.html', {'livros': False, 'categorias': categorias, 'idUser':idUser,'userADM':sessaoADM,  'avaliacao': livros['avaliacao']})
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

def acoes(request):
    sessaoADM = request.session.get('UserADM')
    if sessaoADM is not None:
        resAutor = ''
        resEditora = ''
        mensagemLivro = ''
        idLivro = ''
        ediAutErro = ''
        livros = Catalogo().exibir_livros()
        if request.method == 'POST':
            form_cadLivro = CadastroLivro(request.POST)
            form_cadLivroD = CadastroDigital(request.POST)
            form_cadLivroF = CadastroFisico(request.POST)
            formEditora = ProcurarEditora(request.POST)
            formAutor = ProcurarAutor(request.POST)
            excluir = Excluir(request.POST)
            editarLivro = EditarLivro(request.POST)
            editarAutorEditora = EditarAutorEditora(request.POST)
            
            if form_cadLivro.is_valid():
                autor = form_cadLivro.cleaned_data['autor']
                editora = form_cadLivro.cleaned_data['editora']
                categoria = form_cadLivro.cleaned_data['categoria']
                isbn = form_cadLivro.cleaned_data['isbn']
                dataPublicacao = form_cadLivro.cleaned_data['dataPublicacao']
                titulo = form_cadLivro.cleaned_data['titulo']
                
                addLivro = Livro(
                    titulo=titulo,
                    idAutor=autor,
                    idEditora=editora,
                    categoria=categoria,
                    isbn=isbn,
                    dataPublicacao=dataPublicacao,
                    id=None
                    )
                pesquisaLivro = addLivro.procurar('isbn', addLivro.isbn)
                if pesquisaLivro != "sem registro":
                    request.session['LivroMensagem'] = 'Livro já cadastrado no sistema!'
                    request.session.save()
                    return redirect('acoes')
                else:
                    addLivro.adicionar(addLivro.titulo,addLivro.idAutor,addLivro.idEditora,addLivro.categoria,addLivro.isbn,addLivro.dataPublicacao)
                    getIdLivro = addLivro.procurar('isbn', addLivro.isbn)
                    request.session['idCadastroLivro'] = getIdLivro[0]
                    request.session.save()
                    return redirect('acoes')
            elif form_cadLivroD.is_valid():
                idLivro = form_cadLivroD.cleaned_data['idLivroD']
                tamanho = form_cadLivroD.cleaned_data['tamanho']
                versao = form_cadLivroD.cleaned_data['versao']
                formato = form_cadLivroD.cleaned_data['formato']
                
                addLivroDigital = LivroDigital(
                    id_livro= idLivro,
                    tamanho= tamanho,
                    versao=versao,
                    formato=formato,
                    id=None
                )
                
                res = addLivroDigital.procurar('id_livro',idLivro)
                if res != 'sem registro':
                    addLivroDigital.adicionar(  addLivroDigital.id_livro,
                                            addLivroDigital.tamanho, 
                                            addLivroDigital.versao, 
                                            addLivroDigital.formato)
                    request.session['LivroMensagem'] = 'Livro digital cadastrado com sucesso!'
                    request.session.save()
                    return redirect('acoes')
                else:
                    request.session['LivroMensagem'] = 'Livro não encontrado no sistema!'
                    request.session.save()
                    return redirect('acoes')                         
            elif form_cadLivroF.is_valid():
                idLivro = form_cadLivroF.cleaned_data['idLivroF']
                quantidade = form_cadLivroF.cleaned_data['quantidade']
                
                addLivroFisico = LivroFisico(
                    id_livro= idLivro,
                    quantidade=quantidade,
                    id=None
                )
                
                res = addLivroFisico.procurar('id_livro',idLivro)
                if res != 'sem registro':
                    addLivroFisico.adicionar(addLivroFisico.id_livro,addLivroFisico.quantidade)
                    request.session['LivroMensagem'] = 'Quantidade cadastrado com sucesso!'
                    request.session.save()
                    return redirect('acoes')
                else:
                    request.session['LivroMensagem'] = 'Livro não encontrado no sistema!'
                    request.session.save()
                    return redirect('acoes') 
            elif formAutor.is_valid():
                nome = formAutor.cleaned_data['nomeAutor']
                idAutor = Autor(
                    id=None,
                    nome=nome
                )
                if 'procurar' in request.POST:
                    idAutor_res = idAutor.procurar('nome',idAutor.nome)
                    if idAutor_res == "sem registro":
                        request.session['ediAutErro'] = 'Autor não encontrado no sistema!'
                        request.session.save()
                        return redirect('acoes')
                    else:
                        request.session['autorSucesso'] = idAutor_res
                        request.session.save()
                        return redirect('acoes')
                elif 'cadastrar' in request.POST:
                    idAutor_res = idAutor.procurar('nome',idAutor.nome)
                    if idAutor_res == "sem registro":
                        idAutor.adicionar(idAutor.nome)
                        request.session['LivroMensagem'] = "Autor cadastrado com sucesso!"
                        request.session.save()
                        return redirect('acoes')
                    else:
                        request.session['LivroMensagem'] = 'Autor já cadastrado no sistema!'
                        request.session.save()
                        return redirect('acoes')
            elif formEditora.is_valid():
                nome = formEditora.cleaned_data['nomeEditora']
                
                idEditora = Editora(
                    id=None,
                    nome=nome
                )
                if 'procurar' in request.POST:
                    idEditora_res = idEditora.procurar('nome',idEditora.nome)
                    if idEditora_res == "sem registro":
                        request.session['ediAutErro'] = 'Editora não encontrada no sistema!'
                        request.session.save()
                        return redirect('acoes')
                    else:
                        request.session['editoraSucesso'] = idEditora_res
                        request.session.save()
                        return redirect('acoes') 
                elif 'cadastrar' in request.POST:
                    idEditora_res = idEditora.procurar('nome',idEditora.nome)
                    if idEditora_res == "sem registro":
                        idEditora.adicionar(idEditora.nome)
                        request.session['LivroMensagem'] = "Editora cadastrada com sucesso!"
                        request.session.save()
                        return redirect('acoes')
                    else:
                        request.session['LivroMensagem'] = 'Editora já cadastrada no sistema!'
                        request.session.save()
                        return redirect('acoes') 
            elif excluir.is_valid():
                idDeletar = excluir.cleaned_data['idDeletar']
                
                exLivro = Livro( id= idDeletar, 
                                titulo= None,
                                idAutor= None,
                                idEditora= None,
                                categoria= None,
                                isbn= None,
                                dataPublicacao= None)
                idLivroDigital = LivroDigital(
                    id_livro= idDeletar,
                    tamanho=None,
                    versao=None,
                    formato=None,
                    id=None
                )
                idLivroFisico = LivroFisico(
                    id_livro=idDeletar,
                    quantidade=None,
                    id=None
                )
                
                exAutor = Autor(
                    id= idDeletar,
                    nome=None
                )
                exEditora = Editora(
                    id= idDeletar,
                    nome=None
                )
                
                if 'delLivro' in request.POST:
                    
                    pesquisaDigital = idLivroDigital.procurar('id_livro', idLivroDigital.id_livro)
                    if pesquisaDigital != "sem registro": 
                        idLivroDigital.excluir(pesquisaDigital[0])
                        
                    pesquisaFisico = idLivroFisico.procurar('id_livro', idLivroFisico.id_livro)
                    if pesquisaFisico != "sem registro": 
                        idLivroFisico.excluir(pesquisaFisico[0])
                        
                    pesquisa = exLivro.procurar('id_livro',exLivro.id)
                    if pesquisa != "sem registro": 
                        exLivro.excluir(exLivro.id)
                        request.session['LivroMensagem'] = 'Livro excluido do sistema!'
                        request.session.save()
                        return redirect('acoes')
                    else:
                        request.session['LivroMensagem'] = 'Livro não encontrado no sistema!'
                        request.session.save()
                        return redirect('acoes')
            elif editarAutorEditora.is_valid():
                idAlterar = editarAutorEditora.cleaned_data['idAlterar']
                nomeAlterar = editarAutorEditora.cleaned_data['nomeAlterar']
                
                altAutor = Autor(
                    id=idAlterar,
                    nome=nomeAlterar
                )
                altEditora = Editora(
                    id=idAlterar,
                    nome=nomeAlterar
                )
                
                if 'editAutor' in request.POST:
                    idAutor_res = altAutor.procurar('id_autor',altAutor.id)
                    if idAutor_res == "sem registro":
                        request.session['LivroMensagem'] = "Autor não encontrado no sistema"
                        request.session.save()
                        return redirect('acoes')
                    else:
                        altAutor.alterar(altAutor.id, nome = altAutor.nome)
                        request.session['LivroMensagem'] = 'Autor alterado com sucesso!'
                        request.session.save()
                        return redirect('acoes')
                elif 'editEditora' in request.POST:
                    idEditora_res = altEditora.procurar('id_editora',altEditora.id)
                    if idEditora_res == "sem registro":
                        request.session['LivroMensagem'] = "Editora não encontrada no sistema"
                        request.session.save()
                        return redirect('acoes')
                    else:
                        altEditora.alterar(altEditora.id, nome = altEditora.nome)
                        request.session['LivroMensagem'] = 'Editora alterada com sucesso!'
                        request.session.save()
                        return redirect('acoes')
            elif editarLivro.is_valid():
                idLivro = editarLivro.cleaned_data['altIdLivro']
                titulo = editarLivro.cleaned_data['altTitulo']
                autor = editarLivro.cleaned_data['altAutor']
                editora = editarLivro.cleaned_data['altEditora']
                categoria = editarLivro.cleaned_data['altCategoria']
                isbn = editarLivro.cleaned_data['altIsbn']
                dataPublicacao = editarLivro.cleaned_data['altDataPublicacao']
                
                altLivro = Livro(
                    id= idLivro, 
                    titulo= titulo,
                    idAutor= autor,
                    idEditora= editora,
                    categoria= categoria,
                    isbn= isbn,
                    dataPublicacao= dataPublicacao
                )
                
                dic = {'titulo': titulo, 'categoria':categoria, 'isbn':isbn, 'dataPublicacao': dataPublicacao,'autor': autor, 'editora': editora}
                
                values = _remover_chaves_vazias(altLivro.id,dic)
                
                pesquisa = altLivro.procurar('id_livro',altLivro.id)
                if pesquisa != "sem registro": 
                    altLivro.alterar(altLivro.id,values)
                    request.session['LivroMensagem'] = "Livro alterado com sucesso!"
                    request.session.save()
                    return redirect('acoes')
                else:
                    request.session['LivroMensagem'] = "Livro não encontrado no sistema"
                    request.session.save()
                    return redirect('acoes')
        
        else:
            form_cadLivro = CadastroLivro()
            form_cadLivroD = CadastroDigital()
            form_cadLivroF = CadastroFisico()
            formEditora = ProcurarEditora()
            formAutor = ProcurarAutor()
            excluir = Excluir()
            editarLivro = EditarLivro()
            editarAutorEditora = EditarAutorEditora()
        mensagemSession = request.session.get('LivroMensagem')
        if mensagemSession:
            mensagemLivro = mensagemSession
            del request.session['LivroMensagem']
            request.session.save()
        idLivroSession = request.session.get('idCadastroLivro')
        if idLivroSession:
            idLivro = idLivroSession
        ediAutErroSession = request.session.get('ediAutErro')
        if ediAutErroSession:
            ediAutErro = ediAutErroSession
            del request.session['ediAutErro']
            request.session.save()
        idEditoraSession = request.session.get('editoraSucesso')
        if idEditoraSession:
            resEditora = idEditoraSession
            del request.session['editoraSucesso']
            request.session.save()
        idAutorSession = request.session.get('autorSucesso')
        if idAutorSession:
            resAutor = idAutorSession
            del request.session['autorSucesso']
            request.session.save()
        params = {
            'livros': livros['livros'],
            'form_cadLivro':form_cadLivro,
            'form_cadLivroD':form_cadLivroD,
            'form_cadLivroF':form_cadLivroF,
            'formEditora':formEditora,
            'formAutor':formAutor,
            'mensagemLivro': mensagemLivro,
            'idCadastroLivro':idLivro,
            'ediAutErro':ediAutErro,
            'resAutor':resAutor,
            'resEditora':resEditora,
            'excluir': excluir,
            'editarLivro':editarLivro,
            'editarAutorEditora':editarAutorEditora,
            'userADM': sessaoADM
        }
        return render(request, 'templates/acoes.html', params)
    else:
        request.session['LoginMensagem'] = 'Você precisa estar logado para acessar a página desejada!'
        request.session.save()
        return redirect('login')
        
def _remover_chaves_vazias(dicionario):
    chaves_para_remover = [chave for chave, valor in dicionario.items() if not valor]
    for chave in chaves_para_remover:
        del dicionario[chave]

def reservar(request, idlivro):
    idUser = request.session.get('idUser')
    sessaoADM = request.session.get('UserADM')
    if idUser is not None:
        idGeral  = idUser
    else:
        idGeral = sessaoADM
    if request.method == 'POST':
        message = Cliente().reservar(idGeral, idlivro)
        messages.info(request, message)
        print(message)
        return redirect('catalogo')
    
def atualizar_usuario(request):
    idUser = request.session.get('idUser')
    sessaoADM = request.session.get('UserADM')
    if idUser is not None or sessaoADM is not None:
        request.session.save()
        if idUser is not None:
            idGeral  = idUser
        else:
            idGeral = sessaoADM

        usuario = ExibirInfo(idGeral).exibir
        if request.method == 'POST':
            form = AtualizarUsuario(request.POST)
            if form.is_valid():
                nome = form.cleaned_data['nome']
                cpf = form.cleaned_data['cpf']
                email = form.cleaned_data['email']
                data_nascimento = form.cleaned_data['data_nascimento']
                telefone = form.cleaned_data['telefone']
                senha = form.cleaned_data['senha']
            message = Usuario().atualizar_dados(
                idusuario=idGeral,
                nome=nome,
                cpf=cpf,
                email=email,
                data_nascimento=data_nascimento,
                telefone=telefone,
                senha=senha
            )
            print(message)
        else:
            form = AtualizarUsuario(request.POST)
        if usuario:
            return render(request, 'templates/perfil.html', {'form': form, 'usuario': usuario, 'idUser':idUser,'userADM':sessaoADM})
        else:
            return render(request, 'templates/perfil.html', {'form': form, 'usuario': False, 'idUser':idUser,'userADM':sessaoADM})
    else:
       return redirect('login')

def emprestar(request, idlivro, tipolivro):
    idUser = request.session.get('idUser')
    sessaoADM = request.session.get('UserADM')
    if idUser is not None:
        idGeral  = idUser
    else:
        idGeral = sessaoADM
    if request.method == 'POST':
        message = Cliente().emprestar(idGeral, idlivro, tipolivro)
        messages.info(request, message)
        print(message)
        return redirect('catalogo')

def sair_login(request):
    request.session.flush()
    return redirect('login')

def dashboard(request):
    sessaoADM = request.session.get('UserADM')
    if sessaoADM is not None:
        livros = Dashboard().totalTabela('livro')
        editora = Dashboard().totalTabela('editora')
        autor = Dashboard().totalTabela('autor')
        emprestimos = Dashboard().infoValidade()
        multas = Dashboard().infoMultas()

        return render(request, 'templates/dashboard.html', {'userADM':sessaoADM, 'livros': livros, 'editora': editora, 'autor': autor, 'emprestimos': emprestimos, 'multas': multas})
    else:
        redirect('login')

def devolucao(request, idemprestimo):
    sessaoADM = request.session.get('UserADM')

    if sessaoADM is not None:
        devolvido = Base('o','o').devolucao(idemprestimo)
        if devolvido:
            message = 'Livro devolvido com sucesso!'
        else:
            message = 'Erro ao devolver o livro.'
        storage = messages.get_messages(request)
        for m in storage:
            pass
        messages.success(request, message)
        return redirect('dashboard')
        
    else:
        redirect('login')

def multar(request):
    sessaoADM = request.session.get('UserADM')

    if sessaoADM is not None:
        message = Base('o','o').multar()
        storage = messages.get_messages(request)
        for m in storage:
            pass
        messages.success(request, message)
        return redirect('dashboard')
    else:
        redirect('login')

def historico (request):
    
    iduser = request.session.get('idUser') 
    if iduser is not None:
        exibir_historico= ExibirInfo (idUsuario=iduser)
        resp= exibir_historico.exibir_emprestimos
        return render(request, 'templates/historico.html', {'emprestimo': resp, 'idUser': iduser})
    else:
        request.session['LoginMensagem'] = 'Você precisa estar logado para acessar a página desejada!'
        request.session.save()
        return redirect('login')

def avaliar(request, idlivro, idusuario, valor):
    iduser = request.session.get('idUser')
    if iduser is not None:
        avaliacao = Cliente().avaliar(idlivro, idusuario, valor)
        return redirect('catalogo')
    else:
        redirect ('login')