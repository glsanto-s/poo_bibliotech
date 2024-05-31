from acoes_funcionario import Autor

def response(metodo):
    res = {
        200 : f'Autor {metodo} com sucesso!',
        404 : f'Não encontramos esse autor!',
        422 : f'Autor já cadastrado no sistema!'
    }
    return res

def adicionar_autor(nomeAutor):
    addAutor = Autor(
        id=None,
        nome = nomeAutor
    )
    
    retorno = response('cadastrado')
    pesquisa = addAutor.procurar('nome',addAutor.nome)
    if pesquisa == "sem registro": 
        addAutor.adicionar(addAutor.nome)
        res = retorno[200]
    else:
        res = retorno[422]
    return res

def excluir_autor(idAutor):
    excluirAutor = Autor(
        id=idAutor,
        nome = None
    )
    
    retorno = response('excluído')
    pesquisa = excluirAutor.procurar('id_autor',excluirAutor.id)
    if pesquisa != "sem registro": 
        excluirAutor.excluir(excluirAutor.id)
        res = retorno[200]
    else:
        res = retorno[404]
    return res
    
def alterar_autor(idAutor, nomeAutor):
    alterarAutor = Autor(
        id=idAutor,
        nome = nomeAutor
    )
    
    retorno = response('alterado')
    pesquisa = alterarAutor.procurar('id_autor',alterarAutor.id)
    if pesquisa != "sem registro": 
        alterarAutor.alterar(alterarAutor.id, nome= alterarAutor.nome)
        res = retorno[200]
    else:
        res = retorno[404]
    return res