const hamburger = document.querySelector('#header .main-nav')

const toggleMenu = () => {
  if (hamburger.classList.contains('show-menu')) {
    hamburger.classList.remove('show-menu')
  } else {
    hamburger.classList.add('show-menu')
  }
}

hamburger.onclick = () => {
  toggleMenu()
}
