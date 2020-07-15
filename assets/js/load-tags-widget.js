import axios from 'axios'
const widgetTags = document.querySelector('#tags-widget .widget-tags')

const generateTags = tags => {
  for (const tag of tags) {
    const aTag = document.createElement('a')
    aTag.href = `/posts/tag/${tag}`
    aTag.innerText = tag
    widgetTags.append(aTag)
  }
}

if (widgetTags) {
  axios.get('/posts/tags')
    .then(res => res.data.tags)
    .then(tags => generateTags(tags))
    .catch(e => console.log(e))
}
