window.addEventListener('load', () => {
  const sectionLivros = document.querySelector('.livros');
  const sectionAutores = document.querySelector('.autores');
  const sectionEditoras = document.querySelector('.editoras');
  const sectionEmprestimos = document.querySelector('.emprestimos');
  const sectionMultas = document.querySelector('.multas');

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
      const data = content.querySelector('.emprestimoData span');
      const dataValidade = new Date(data.innerText);
      const dataAtual = new Date();
      const status = content.querySelector('.emprestimoData');

      if (dataAtual > dataValidade && status.dataset.status === '1') {
        content.classList.add('validade');
        content.classList.remove('devolucao');
      } else {
        content.classList.remove('validade');
        if (status.dataset.status === '0') {
          content.classList.add('devolucao');
        }
      }
    });
  }
  emprestimo();

  function multas() {
    sections.forEach((item) => {
      item.classList.remove('ativo');
    });
    sectionMultas.classList.add('ativo');

    buttons.forEach((btn) => {
      btn.classList.remove('ativo');
    });
    btnMultas.classList.add('ativo');

    const contentMultas = document.querySelectorAll('.multasContent');
    contentMultas.forEach((content) => {
      const valorMulta = content.querySelector('.multasValor span');
      if (valorMulta.innerText == '0') {
        content.classList.add('inativa');
      } else {
        content.classList.remove('inativa');
      }
    });
  }

  btnLivros.addEventListener('click', livros);
  btnAutores.addEventListener('click', autores);
  btnEditoras.addEventListener('click', editoras);
  btnEmprestimos.addEventListener('click', emprestimo);
  btnEmprestimos.addEventListener('click', emprestimo);
  btnMultas.addEventListener('click', multas);

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
