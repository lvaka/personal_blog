const logo = document.querySelector('#header .logo')

const setBackground = imgSrc => {
  logo.setAttribute('style', `background-image: url('${imgSrc}')`)
}

if (logo) {
  const imgSrc = logo.dataset.bgImage
  const img = document.createElement('img')
  img.onload = setBackground(imgSrc)
  img.src = imgSrc
}
