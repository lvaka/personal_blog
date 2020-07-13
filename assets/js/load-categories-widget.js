import axios from 'axios'

const categoriesList = document.querySelector('#categories-widget .categories')

const hideLoader = () => {
  const loader = document.getElementById('category-widget-loader')
  loader.classList.add('d-none')
}

const setCategoriesList = categories => {
  for (const cat of categories) {
    const li = document.createElement('li')
    const innerHTML = `<a href="/posts/category/${cat.slug}">` +
                      `${cat.category}</a>`
    li.innerHTML = innerHTML

    categoriesList.appendChild(li)
  }
}

if (categoriesList) {
  axios.get('/posts/categories')
    .then(res => res.data.categories)
    .then(cats => setCategoriesList(cats))
    .then(() => hideLoader())
    .catch(e => console.log(e))
}
