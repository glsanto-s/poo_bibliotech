window.addEventListener('load', () => {
  const sectionLivros = document.querySelector('.livros');
  const sectionAutores = document.querySelector('.autores');
  const sectionEditoras = document.querySelector('.editoras');
  const sectionEmprestimos = document.querySelector('.emprestimos');

  const btnLivros = document.querySelector('.btnLivros');
  const btnEditoras = document.querySelector('.btnEditoras');
  const btnAutores = document.querySelector('.btnAutores');
  const btnEmprestimos = document.querySelector('.btnEmprestimos');
  const btnMultas = document.querySelector('.btnMultas');
  const buttons = document.querySelectorAll('.categorias li');
  const sections = document.querySelectorAll('.container');

  function livros() {
    sections.forEach((item) => {
      item.classList.remove('ativo');
    });
    sectionLivros.classList.add('ativo');

    buttons.forEach((btn) => {
      btn.classList.remove('ativo');
    });
    btnLivros.classList.add('ativo');
  }

  function autores() {
    sections.forEach((item) => {
      item.classList.remove('ativo');
    });
    sectionAutores.classList.add('ativo');

    buttons.forEach((btn) => {
      btn.classList.remove('ativo');
    });
    btnAutores.classList.add('ativo');
  }

  function editoras() {
    sections.forEach((item) => {
      item.classList.remove('ativo');
    });
    sectionEditoras.classList.add('ativo');

    buttons.forEach((btn) => {
      btn.classList.remove('ativo');
    });
    btnEditoras.classList.add('ativo');
  }

  function emprestimo() {
    sections.forEach((item) => {
      item.classList.remove('ativo');
    });
    sectionEmprestimos.classList.add('ativo');

    buttons.forEach((btn) => {
      btn.classList.remove('ativo');
    });
    btnEmprestimos.classList.add('ativo');

    const contentEmprestimo = document.querySelectorAll('.emprestimoContent');
    contentEmprestimo.forEach((content) => {
      const data = document.querySelector('.emprestimoData span');
      const dataValidade = new Date(data.innerText);
      const dataAtual = new Date();

      if (dataAtual > dataValidade) {
        content.classList.add('validade');
      } else {
        content.classList.remove('validade');
      }
      console.log(dataValidade);
    });
  }
  emprestimo();

  btnLivros.addEventListener('click', livros);
  btnAutores.addEventListener('click', autores);
  btnEditoras.addEventListener('click', editoras);
  btnEmprestimos.addEventListener('click', emprestimo);

  const btnListarAutores = document.querySelector('.btnListarAutores');
  const nomeAutores = document.querySelector('.nomeAutores');
  btnListarAutores.addEventListener('click', () => {
    nomeAutores.classList.toggle('ativo');
    if (nomeAutores.classList.contains('ativo')) {
      btnListarAutores.innerText = 'Listar Autores -';
    } else {
      btnListarAutores.innerText = 'Listar Autores +';
    }
  });

  const btnListarLivros = document.querySelector('.btnListarLivros');
  const nomeLivros = document.querySelector('.nomeLivros');
  btnListarLivros.addEventListener('click', () => {
    nomeLivros.classList.toggle('ativo');
    if (nomeLivros.classList.contains('ativo')) {
      btnListarLivros.innerText = 'Listar Livros -';
    } else {
      btnListarLivros.innerText = 'Listar Livros +';
    }
  });

  const btnListarEditoras = document.querySelector('.btnListarEditoras');
  const nomeEditoras = document.querySelector('.nomeEditoras');
  btnListarEditoras.addEventListener('click', () => {
    nomeEditoras.classList.toggle('ativo');
    if (nomeEditoras.classList.contains('ativo')) {
      btnListarEditoras.innerText = 'Listar Editoras -';
    } else {
      btnListarEditoras.innerText = 'Listar Editoras +';
    }
  });
});
