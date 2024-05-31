const formCategoria = document.querySelector('#select-categoria');
const pesquisarTitulo = document.querySelector('.pesquisa input');

function handleChange() {
  formCategoria.setAttribute('disabled', '');
  pesquisarTitulo.setAttribute('disabled', '');

  if (formCategoria instanceof HTMLSelectElement) {
    const url = window.location.href.replace(/\/catalogo\/.*/, '');
    if (formCategoria.value !== 'todas') {
      window.location.assign(`${url}/catalogo/${formCategoria.value}`);
    } else {
      window.location.assign(`${url}/catalogo`);
    }
  }
}

formCategoria.addEventListener('change', handleChange);

function selectOption() {
  const form = document.querySelector('#select-form');
  const categoria = form.dataset.categoria;
  const option = document.getElementById(categoria);
  option.setAttribute('selected', '');
}
selectOption();

window.addEventListener('load', () => {
  const cards = Array.from(document.querySelectorAll('.card'));
  function handleTitle(e) {
    const titulo = e.target.value.toLowerCase();
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

  pesquisarTitulo.addEventListener('keyup', handleTitle);
});
