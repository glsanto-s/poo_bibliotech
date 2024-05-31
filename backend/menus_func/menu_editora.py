from acoes_funcionario import Editora

def response(metodo):
    res = {
        200 : f'Editora {metodo} com sucesso!',
        404 : f'Não encontramos essa editora!',
        422 : f'Editora já cadastrada no sistema!'
    }
    return res

def adicionar_editora(nomeEditora):
    addEditora = Editora(
        id=None,
        nome = nomeEditora
    )
    idEditora_res = addEditora.procurar('nome', addEditora.nome)
    
    retorno = response('cadastrada')
    if idEditora_res == "sem registro":
        addEditora.adicionar(addEditora.nome)
        res = retorno[200] 
    else:
        res = retorno[422] 
    return res


def excluir_editora(idEditora):
    excluirEditora = Editora(
        id=idEditora,
        nome = None
    )
    
    retorno = response('excluída')
    pesquisa = excluirEditora.procurar('id_editora',excluirEditora.id)
    if pesquisa != "sem registro": 
        excluirEditora.excluir(excluirEditora.id)
        res = retorno[200] 
    else:
        res = retorno[404]
    return res

    
def alterar_editora(idEditora, nomeEditora):
    alterarEditora = Editora(
        id=idEditora,
        nome = nomeEditora
    )
    
    retorno = response('alterada')
    pesquisa = alterarEditora.procurar('id_editora',alterarEditora.id)
    if pesquisa != "sem registro": 
        alterarEditora.alterar(alterarEditora.id, nome = alterarEditora.nome)
        res = retorno[200] 
    else:
        res = retorno[404]
    return res
    