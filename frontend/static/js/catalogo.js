const formCategoria = document.querySelector('#select-categoria');
const pesquisarTitulo = document.querySelector('.pesquisa input');
const btnLivroFisico = document.querySelector('.btn_livro_fisico');
const btnLivroDigital = document.querySelector('.btn_livro_digital');
const sectionLivroFisico = document.querySelector('.livros_fisicos');
const sectionLivroDigital = document.querySelector('.livros_digitais');

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
  const cardsFisicos = Array.from(
    document.querySelectorAll('#livros_fisico .card'),
  );
  const cardsDigitais = Array.from(
    document.querySelectorAll('#livros_digitais .card'),
  );
  function handleTitle(e) {
    const cards = sectionLivroFisico.classList.contains('ativo')
      ? cardsFisicos
      : cardsDigitais;
    const titulo = e.target.value.toLowerCase();
    const cardsFiltrados = cards.filter((card) => {
      card = card.querySelector('.titulo_livro');
      return card.innerText.toLowerCase().includes(titulo);
    });
    const container = sectionLivroFisico.classList.contains('ativo')
      ? document.querySelector('#livros_fisico')
      : document.querySelector('#livros_digitais');
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

function handleDigital() {
  sectionLivroDigital.classList.add('ativo');
  sectionLivroFisico.classList.remove('ativo');
  btnLivroDigital.classList.add('ativo');
  btnLivroFisico.classList.remove('ativo');
}

function handleFisico() {
  sectionLivroFisico.classList.add('ativo');
  sectionLivroDigital.classList.remove('ativo');
  btnLivroFisico.classList.add('ativo');
  btnLivroDigital.classList.remove('ativo');
}

btnLivroDigital.addEventListener('click', handleDigital);
btnLivroFisico.addEventListener('click', handleFisico);
