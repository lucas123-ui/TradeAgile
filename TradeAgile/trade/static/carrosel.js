const carouselImages = document.querySelector('.carousel-images'); // Contêiner das imagens
const images = document.querySelectorAll('.carousel img'); // Lista de imagens
const prev = document.querySelector('.prev'); // Botão para imagem anterior
const next = document.querySelector('.next'); // Botão para imagem seguinte
let counter = 0; // Índice da imagem atual
const size = images[0].clientWidth; // Largura de uma imagem

// Move para a próxima imagem do carrusel
function moveToNextImage() {
    if (counter >= images.length - 1) {
        counter = -1; // Reinicia no início
    }
    carouselImages.style.transform = 'translateX(' + (-size * (counter + 1)) + 'px)';
    counter++;
}

// Move para a imagem anterior do carrusel
function moveToPrevImage() {
    if (counter <= 0) {
        counter = images.length; // Vai para o final
    }
    carouselImages.style.transform = 'translateX(' + (-size * (counter - 1)) + 'px)';
    counter--;
}

// Configura eventos de clique nos botões
next.addEventListener('click', moveToNextImage);
prev.addEventListener('click', moveToPrevImage);

// Muda automaticamente para a próxima imagem a cada 3 segundos
setInterval(moveToNextImage, 3000);
