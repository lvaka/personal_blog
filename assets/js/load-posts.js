import axios from 'axios'
import { progressiveLoad } from './progressive-load'

window.page = 1

const hideLoadmoreButton = () => {
  const loadButton = document.getElementById('load-more')
  loadButton.classList.add('d-none')
}

const hideLoader = () => {
  const loader = document.getElementById('posts-loader')
  loader.classList.add('d-none')
}

const showLoader = () => {
  const loader = document.getElementById('posts-loader')
  loader.classList.remove('d-none')
}

const loadposts = () => {
  let posts, nextpage
  const postsContainer = document.getElementById('posts')
  if (window.page) {
    showLoader()
    axios.get(`/posts?page=${window.page}`)
      .then(res => {
        posts = res.data.posts.trim()
        nextpage = res.data.next_page
        const domparser = new DOMParser()
        const parsedText = domparser.parseFromString(posts, 'text/html')
        const postElems = parsedText.querySelectorAll('.post-prev')
        for (const post of postElems) {
          postsContainer.appendChild(post)
        }
        window.page = nextpage
        if (!window.page) {
          hideLoadmoreButton()
        }
      })
      .then(() => hideLoader())
      .then(() => progressiveLoad())
      .catch(e => console.log(e))
  }
}

window.loadposts = loadposts
