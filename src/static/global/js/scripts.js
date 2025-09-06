const reference = document.querySelector('.reference');
const espacamento = document.querySelector('.espacamento');

const larg = reference.offsetWidth;
const altura = reference.offsetHeight;

espacamento.style.width = larg + 'px';
espacamento.style.height = altura + 'px';

window.addEventListener('resize', () => {
    const larg = reference.offsetWidth;
    const altura = reference.offsetHeight;
    espacamento.style.width = larg + 'px';
    espacamento.style.height = altura + 'px';
});
