import axios from 'axios'

const recentPostsWidget = document.querySelector('#recent-posts-widget .widget-content-container')

const hideLoader = () => {
  const loader = document.getElementById('recentposts-widget-loader')
  loader.classList.add('d-none')
}

const embedPosts = posts => {
  recentPostsWidget.innerHTML = posts
}

if (recentPostsWidget) {
  axios.get('/posts/recent')
    .then(res => res.data.post_ajax)
    .then(posts => embedPosts(posts))
    .then(() => hideLoader())
    .catch(e => console.log(e))
}
