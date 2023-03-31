// Script untuk menampilkan sub-menu pada tampilan mobile
const menuIcon = document.querySelector('.menu-icon');
const menuList = document.querySelector('nav ul');
menuIcon.addEventListener('click', () => {
    menuList.classList.toggle('show-menu');
});

// Script untuk menyalin value pada input form
new ClipboardJS('.copy-button');
