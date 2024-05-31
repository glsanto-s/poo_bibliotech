const formCategoria = document.querySelector('#select-categoria');
const pesquisarTitulo = document.querySelector('.pesquisa input');

function handleChange() {
  formCategoria.setAttribute('disabled', '');
  pesquisarTitulo.setAttribute('disabled', '');
  if (formCategoria instanceof HTMLSelectElement) {
    if (formCategoria.value !== 'todas') {
      window.location.href = `${formCategoria.value}`;
    }
  }
}
formCategoria.addEventListener('change', handleChange);

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
