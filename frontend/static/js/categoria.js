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

  const inputAvaliar = document.querySelectorAll('.avaliar input');

  function handleAvaliar(e) {
    const valor = e.target.value;
    const elementoPai = e.target.parentElement;
    const idUsuario = elementoPai.querySelector('.livro_usuario h1');
    const idLivro = elementoPai.querySelector('.livro_usuario p');
    const urlLocal = window.location.href.replace(/\/catalogo\/.*/, '');

    window.location.assign(
      `${urlLocal}/avaliar/${idLivro.innerText}/${idUsuario.innerText}/${valor}`,
    );
  }

  inputAvaliar.forEach((input) => {
    input.addEventListener('click', handleAvaliar);
  });
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
