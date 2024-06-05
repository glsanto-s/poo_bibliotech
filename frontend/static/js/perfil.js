const btnAlterar = document.querySelector('.btn_alterar');
const formPerfil = document.querySelector('.perfil_form');

function handleClick() {
  btnAlterar.classList.toggle('ativo');
  formPerfil.classList.toggle('ativo');

  if (btnAlterar.classList.contains('ativo')) {
    btnAlterar.innerText = 'Alterar dados -';
    window.scrollTo({ top: 400, behavior: 'smooth' });
  } else {
    btnAlterar.innerText = 'Alterar dados +';
  }
}

btnAlterar.addEventListener('click', handleClick);
