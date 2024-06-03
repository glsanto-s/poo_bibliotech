const procurarTitulo = document.querySelector('.pesquisa input');
const formMetodo = document.querySelector('#select-metodo');
const formNome = document.querySelector('#select-op');

window.addEventListener('load', () => {
    const input = document.querySelector('.input-field');
    const cards = Array.from(document.querySelectorAll('.card'));
    const showcard = document.querySelector('#livros')
    function handleTitle(e) {
        const titulo = e.target.value.toLowerCase();
        if (titulo.length === 0) {
            showcard.setAttribute('hidden', true);
            return;
        } else {
            showcard.removeAttribute('hidden');
        }
      const cardsFiltrados = cards.filter((card) => {
        card = card.querySelector('.titulo_livro');
        return card.innerText.toLowerCase().includes(titulo);
      });
      const container = document.querySelector('#livros');
      container.innerHTML = '';
      if (cardsFiltrados.length === 0) {
        container.innerHTML = '<p>Não há livros com este título</p>';
      } else {
        cardsFiltrados.forEach((card) => {
          container.innerHTML += card.outerHTML;
        });
      }
    }

    function handleChange(){
      metodo = formMetodo.value;
      form = formNome.value;

      const addLivro = document.getElementById('addLivro');
      const addLivroD = document.getElementById('cadLivroD');
      const addLivroF = document.getElementById('cadLivroF');
      const addAutor = document.getElementById('cadAutor');
      const addEditora = document.getElementById('cadEditora');

      const delLivro = document.getElementById('delLivro');
      const delAutor = document.getElementById('delAutor');
      const delEditora = document.getElementById('delEditora');

      const editLivro = document.getElementById('editLivro')
      const editAutor = document.getElementById('editAutor')
      const editEditora = document.getElementById('editEditora')

      if(metodo == 'adicionar'){
        if(form == 'livro' ){
          addLivro.removeAttribute('hidden');
          addAutor.setAttribute('hidden', true);
          addEditora.setAttribute('hidden', true);
          addLivroD.setAttribute('hidden', true);
          addLivroF.setAttribute('hidden', true);

          editLivro.setAttribute('hidden', true);
          editAutor.setAttribute('hidden', true);
          editEditora.setAttribute('hidden', true);

          delLivro.setAttribute('hidden', true);
          delAutor.setAttribute('hidden', true);
          delEditora.setAttribute('hidden', true);
          return
        }
        else if(form == 'autor'){
          addAutor.removeAttribute('hidden');
          addLivro.setAttribute('hidden', true);
          addEditora.setAttribute('hidden', true);
          addLivroD.setAttribute('hidden', true);
          addLivroF.setAttribute('hidden', true);

          editLivro.setAttribute('hidden', true);
          editAutor.setAttribute('hidden', true);
          editEditora.setAttribute('hidden', true);

          delLivro.setAttribute('hidden', true);
          delAutor.setAttribute('hidden', true);
          delEditora.setAttribute('hidden', true);
          return
        }
        else if(form == 'editora'){
          addEditora.removeAttribute('hidden');
          addAutor.setAttribute('hidden', true);
          addLivro.setAttribute('hidden', true);
          addLivroD.setAttribute('hidden', true);
          addLivroF.setAttribute('hidden', true);

          editLivro.setAttribute('hidden', true);
          editAutor.setAttribute('hidden', true);
          editEditora.setAttribute('hidden', true);

          delLivro.setAttribute('hidden', true);
          delAutor.setAttribute('hidden', true);
          delEditora.setAttribute('hidden', true);
          return
        }
        else if(form == 'livroF'){
          addAutor.setAttribute('hidden', true);
          addEditora.setAttribute('hidden', true);
          addLivro.setAttribute('hidden', true);
          addLivroD.setAttribute('hidden', true);
          addLivroF.removeAttribute('hidden');

          editLivro.setAttribute('hidden', true);
          editAutor.setAttribute('hidden', true);
          editEditora.setAttribute('hidden', true);

          delLivro.setAttribute('hidden', true);
          delAutor.setAttribute('hidden', true);
          delEditora.setAttribute('hidden', true);
          return
        }
        else if(form == 'livroD'){
          addAutor.setAttribute('hidden', true);
          addEditora.setAttribute('hidden', true);
          addLivro.setAttribute('hidden', true);
          addLivroF.setAttribute('hidden', true);
          addLivroD.removeAttribute('hidden');

          editLivro.setAttribute('hidden', true);
          editAutor.setAttribute('hidden', true);
          editEditora.setAttribute('hidden', true);

          delLivro.setAttribute('hidden', true);
          delAutor.setAttribute('hidden', true);
          delEditora.setAttribute('hidden', true);
          return
        }
        else{
          addLivro.setAttribute('hidden', true);
          addAutor.setAttribute('hidden', true);
          addEditora.setAttribute('hidden', true);
          addLivroD.setAttribute('hidden', true);
          addLivroF.setAttribute('hidden', true);
  
          editLivro.setAttribute('hidden', true);
          editAutor.setAttribute('hidden', true);
          editEditora.setAttribute('hidden', true);
  
          delLivro.setAttribute('hidden', true);
          delAutor.setAttribute('hidden', true);
          delEditora.setAttribute('hidden', true);
  
          return
        }
      }
      else if(metodo == 'excluir'){
        if(form == 'livro'){
          addLivro.setAttribute('hidden',true);
          addAutor.setAttribute('hidden', true);
          addEditora.setAttribute('hidden', true);

          editLivro.setAttribute('hidden', true);
          editAutor.setAttribute('hidden', true);
          editEditora.setAttribute('hidden', true);

          delLivro.removeAttribute('hidden');
          delAutor.setAttribute('hidden', true);
          delEditora.setAttribute('hidden', true);
          return
        }
        else{
          addLivro.setAttribute('hidden', true);
          addAutor.setAttribute('hidden', true);
          addEditora.setAttribute('hidden', true);
          addLivroD.setAttribute('hidden', true);
          addLivroF.setAttribute('hidden', true);
  
          editLivro.setAttribute('hidden', true);
          editAutor.setAttribute('hidden', true);
          editEditora.setAttribute('hidden', true);
  
          delLivro.setAttribute('hidden', true);
          delAutor.setAttribute('hidden', true);
          delEditora.setAttribute('hidden', true);
  
          return
        }
      }
      else if(metodo == 'editar'){
        if(form == 'livro'){
          addLivro.setAttribute('hidden',true);
          addAutor.setAttribute('hidden', true);
          addEditora.setAttribute('hidden', true);

          editLivro.removeAttribute('hidden');
          editAutor.setAttribute('hidden', true);
          editEditora.setAttribute('hidden', true);
          
          delLivro.setAttribute('hidden', true);
          delAutor.setAttribute('hidden', true);
          delEditora.setAttribute('hidden', true);

          return
        }
        else if(form == 'autor'){
          addLivro.setAttribute('hidden',true);
          addAutor.setAttribute('hidden', true);
          addEditora.setAttribute('hidden', true);

          editAutor.removeAttribute('hidden');
          editLivro.setAttribute('hidden', true);
          editEditora.setAttribute('hidden', true);
          
          delLivro.setAttribute('hidden', true);
          delAutor.setAttribute('hidden', true);
          delEditora.setAttribute('hidden', true);

          return
        }
        else if(form == 'editora'){
          addLivro.setAttribute('hidden',true);
          addAutor.setAttribute('hidden', true);
          addEditora.setAttribute('hidden', true);
          
          editEditora.removeAttribute('hidden');
          editAutor.setAttribute('hidden', true);
          editLivro.setAttribute('hidden', true);
          
          delLivro.setAttribute('hidden', true);
          delAutor.setAttribute('hidden', true);
          delEditora.setAttribute('hidden', true);

          return
        }
        else{
          addLivro.setAttribute('hidden', true);
          addAutor.setAttribute('hidden', true);
          addEditora.setAttribute('hidden', true);
          addLivroD.setAttribute('hidden', true);
          addLivroF.setAttribute('hidden', true);
  
          editLivro.setAttribute('hidden', true);
          editAutor.setAttribute('hidden', true);
          editEditora.setAttribute('hidden', true);
  
          delLivro.setAttribute('hidden', true);
          delAutor.setAttribute('hidden', true);
          delEditora.setAttribute('hidden', true);
  
          return
        }
      }
      else{
        addLivro.removeAttribute('hidden');
        addAutor.setAttribute('hidden', true);
        addEditora.setAttribute('hidden', true);
        addLivroD.setAttribute('hidden', true);
        addLivroF.setAttribute('hidden', true);

        editLivro.setAttribute('hidden', true);
        editAutor.setAttribute('hidden', true);
        editEditora.setAttribute('hidden', true);

        delLivro.setAttribute('hidden', true);
        delAutor.setAttribute('hidden', true);
        delEditora.setAttribute('hidden', true);

        return
      }
    }

    procurarTitulo.addEventListener('keyup', handleTitle);
    formMetodo.addEventListener('change', handleChange);
    formNome.addEventListener('change', handleChange);
  });