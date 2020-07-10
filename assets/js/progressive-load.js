const progressiveLoad = () => {
  const lazyImages = document.querySelectorAll('.lazy-load')

  const loadProgressive = (image, srcset) => {
    const baseSrc = image.children[0]
    const newPicture = document.createElement('picture')
    newPicture.id = image.id
    newPicture.classList.add('lazy-load')

    for (const i in srcset) {
      const src = srcset[i].trim()
      const newSrc = document.createElement('source')

      if (i < 2) {
        newSrc.setAttribute('media', '(min-width: 501px)')
        newSrc.setAttribute('srcset', src)
      } else {
        newSrc.setAttribute('media', '(max-width: 500px)')
        newSrc.setAttribute('srcset', src)
      }
      newPicture.append(newSrc)
    }
    baseSrc.onload = () => newPicture.classList.add('loaded')
    newPicture.append(baseSrc)
    image.parentNode.replaceChild(newPicture, image)
  }

  for (const image of lazyImages) {
    if (!image.classList.contains('loaded')) {
      const srcset = image.dataset.srcset.split(',')
      loadProgressive(image, srcset)
    }
  }
}

window.progressiveLoad = progressiveLoad

export { progressiveLoad }
