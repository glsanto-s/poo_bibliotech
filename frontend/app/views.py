from django.shortcuts import render
from backend.catalogo import Catalogo

# Create your views here.
def listar_livros(request):
    livros = Catalogo().exibir_livros()  # Chame sua função procurar para buscar todos os livros
    return render(request, 'templates/home.html', {'livros': livros})
