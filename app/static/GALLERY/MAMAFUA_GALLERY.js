// This code changes the border color of an image when it is clicked
const images = document.querySelectorAll('.image-group img');

for (let i = 0; i < images.length; i++) {
  images[i].addEventListener('click', function() {
    this.style.borderColor = 'red';
  });
}
