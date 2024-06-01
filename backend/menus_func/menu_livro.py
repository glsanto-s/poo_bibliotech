import acoes_funcionario as acoes_funcionario

def response(metodo):
    res = {
        200 : f'Livro {metodo} com sucesso!',
        404 : f'Não encontramos esse livro!',
        422 : f'Livro já cadastrado no sistema!'
    }
    return res
    
def adicionar_livro(titulo, idAutor, idEditora, categoria, isbn, dataPublicacao, quantidade, tamanho, versao, formato):
    retorno = response('adicionado')
    # idAutor = acoes_funcionario.Autor(
    #     id=None,
    #     nome = autor
    # )
    # idAutor_res = idAutor.procurar('nome',autor)
    # idEditora = acoes_funcionario.Editora(
    #     id=None,
    #     nome = editora
    # )
    # idEditora_res = idEditora.procurar('nome',editora)

    # if idAutor_res == "sem registro":
    #     return 'Não encontramos o autor! Registre-o primeiro e depois tente adicionar o livro novamente.'
    # elif  idEditora_res == "sem registro":
    #     return 'Não encontramos a editora! Registre-a primeiro e depois tente adicionar o livro novamente.'
    
    addLivro = acoes_funcionario.Livro( 
        id= None, 
        titulo= titulo,
        idAutor= idAutor_res[0],
        idEditora= idEditora_res[0],
        categoria= categoria,
        isbn= isbn,
        dataPublicacao= dataPublicacao)
    
    pesquisa = addLivro.procurar('titulo', addLivro.titulo)
    if pesquisa != "sem registro":
        return retorno[422]

    addLivro.adicionar(
        addLivro.titulo, 
        addLivro.idAutor, 
        addLivro.idEditora, 
        addLivro.categoria, 
        addLivro.isbn, 
        addLivro.dataPublicacao)

    getIdLivro = addLivro.procurar('titulo', addLivro.titulo)

    qtd = quantidade
    livroFisico = acoes_funcionario.LivroFisico(
        id_livro = getIdLivro[0],
        quantidade = qtd,
        id = None
    )
    livroFisico.adicionar(livroFisico.id_livro, livroFisico.quantidade)


    livroDigital= acoes_funcionario.LivroDigital(
        id_livro = getIdLivro[0],
        tamanho = tamanho,
        versao = versao,
        formato = formato,
        id = None
    )
    livroDigital.adicionar(
        livroDigital.id_livro,
        livroDigital.tamanho, 
        livroDigital.versao, 
        livroDigital.formato)

    return retorno[200]

def excluir_livro(idLivro):

    excluirLivro = acoes_funcionario.Livro(
        id= idLivro, 
        titulo= None,
        idAutor= None,
        idEditora= None,
        categoria= None,
        isbn= None,
        dataPublicacao= None
    )
    retorno = response('excluído')
    pesquisa = excluirLivro.procurar('id_livro',excluirLivro.id)
    if pesquisa != "sem registro": 
        excluirLivro.excluir(excluirLivro.id)
        res = retorno(200)
    else:
        res = retorno(404)
    return res

    
    
def alterar_livro(idLivro,titulo, categoria, isbn, dataPublicacao, autor, editora):
    idAutor = acoes_funcionario.Autor(
        id=None,
        nome = autor
    )
    idAutor_res = idAutor.procurar('nome',autor)
    idEditora = acoes_funcionario.Editora(
        id=None,
        nome = editora
    )
    idEditora_res = idEditora.procurar('nome',editora)

    if idAutor_res == "sem registro":
        return 'Não encontramos o autor! Registre-o primeiro e depois tente alterar o livro novamente.'
    elif  idEditora_res == "sem registro":
        return 'Não encontramos a editora! Registre-a primeiro e depois tente alterar o livro novamente.'
    
    alterarLivro = acoes_funcionario.Livro(
        id= idLivro, 
        titulo= titulo,
        idAutor= idAutor_res[0],
        idEditora= idEditora_res[0],
        categoria= categoria,
        isbn= isbn,
        dataPublicacao= dataPublicacao
    )

    dic = {'titulo': titulo, 'categoria':categoria, 'isbn':isbn, 'dataPublicacao': dataPublicacao,'autor': idAutor_res[0], 'editora': idEditora_res[0]}
    values = remover_chaves_vazias(alterarLivro.id,dic)

    retorno = response('alterado')
    pesquisa = alterarLivro.procurar('id_livro',alterarLivro.id)
    if pesquisa != "sem registro": 
        alterarLivro.alterar(alterarLivro.id,values)
        res = retorno(200)
    else:
        res = retorno(404)
    return res

def remover_chaves_vazias(dicionario):
    chaves_para_remover = [chave for chave, valor in dicionario.items() if not valor]
    for chave in chaves_para_remover:
        del dicionario[chave]
