from django import forms

class CadastroForm(forms.Form):
    nome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Nome'}))
    cpf = forms.CharField(max_length=11, widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'CPF'}),label='CPF')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input-field', 'placeholder': 'Email'}))
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-field', 'placeholder': 'Senha'}))
    data_nascimento = forms.DateField(widget=forms.DateInput(attrs={'class': 'input-field', 'type': 'date', 'placeholder': 'Data de Nascimento'}),label='Data de Nascimento')
    telefone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Telefone'}))

class Login(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input-field', 'placeholder': 'Email'}))
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-field', 'placeholder': 'Senha'}))
    
class CadastroLivro(forms.Form):
    titulo = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder':'Título'}),label='Título') 
    autor = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'input-field', 'placeholder':'Id do Autor'}))
    editora = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'input-field', 'placeholder':'Id da Editora'}))
    categoria = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder':'Categoria'}))
    isbn = forms.CharField(max_length=13,min_length=13, widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder':'ISBN'}),label='ISBN')
    dataPublicacao = forms.DateField(widget=forms.DateInput(attrs={'class': 'input-field', 'type':'date','placeholder':'Data de Publicação'}),label='Data Publicação')

class CadastroDigital(forms.Form):
    idLivroD = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'input-field', 'placeholder':'Id do Livro'}),label='Id do Livro')
    tamanho = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder':'Tamanho do Livro'}),required=False)
    versao = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'input-field', 'placeholder':'Versão do Livro'}),required=False)
    formato = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder':'Versão do Livro'}),required=False)

class CadastroFisico(forms.Form):
    idLivroF = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'input-field', 'placeholder':'Id do Livro'}), label='Id do Livro')
    quantidade = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'input-field', 'placeholder':'Quantidade em Estoque'}),required=False)

    
class ProcurarAutor(forms.Form):
    nomeAutor = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder':'Nome do Autor'}),
                                label= 'Nome') 
        
class ProcurarEditora(forms.Form):
    nomeEditora = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder':'Nome da Editora'}),
                                  label= 'Nome') 
    
class Excluir(forms.Form):
    idDeletar = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'input-field', 'placeholder':'Id'}), label='Id')
    
class EditarLivro(forms.Form):
    altIdLivro = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'input-field', 'placeholder':'Id do Livro'}),required=True,label='Id do Livro')
    altTitulo = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder':'Título'}),required=False,label='Título') 
    altAutor = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'input-field', 'placeholder':'Id do Autor'}),required=False)
    altEditora = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'input-field', 'placeholder':'Id da Editora'}),required=False)
    altCategoria = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder':'Categoria'}),required=False)
    altIsbn = forms.CharField(max_length=13,min_length=13, widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder':'ISBN'}),label='ISBN',required=False)
    altDataPublicacao = forms.DateField(widget=forms.DateInput(attrs={'class': 'input-field', 'type':'date','placeholder':'Data de Publicação'}),label='Data Publicação',required=False)
    
class EditarAutorEditora(forms.Form):
    idAlterar = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'input-field', 'placeholder':'Id'}), label='Id')
    nomeAlterar = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder':'Nome'}),
                                  label= 'Nome')
    
class AtualizarUsuario(forms.Form):
    nome = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Nome'}))
    cpf = forms.CharField(max_length=11, required=False, widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'CPF'}))
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'class': 'input-field', 'placeholder': 'Email'}))
    senha = forms.CharField(min_length=8, required=False, widget=forms.PasswordInput(attrs={'class': 'input-field', 'placeholder': 'Senha'}))
    data_nascimento = forms.DateField(required=False, widget=forms.DateInput(attrs={'class': 'input-field', 'type': 'date', 'placeholder': 'Data de Nascimento'}))
    telefone = forms.CharField(max_length=15, required=False, widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Telefone'}))   