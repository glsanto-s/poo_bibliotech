from django.shortcuts import render
from backend.catalogo import Catalogo

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

def listar_livros(request):
    livros = Catalogo().exibir_livros()  # Chame sua função procurar para buscar todos os livros
    categorias = listar_categorias(livros)
    return render(request, 'templates/home.html', {'livros': livros, 'categorias': categorias})

def categoria(request, categoria):
    categorias = listar_categorias(Catalogo().exibir_livros())
    livros = Catalogo().livros_por_categoria(categoria)
    return render(request, 'templates/categoria.html', {'categoria_selecionada': categoria, 'categorias': categorias, 'livros': livros})
