const copyButtons = document.querySelectorAll('.copy-code-button')

const copyCode = codeId => {
  const codeText = document.getElementById(codeId)
  codeText.hidden = false
  codeText.select()
  document.execCommand('copy')
  codeText.hidden = true
}

const registerButton = button => {
  const codeId = button.dataset.codeid
  button.addEventListener('click', () => copyCode(codeId))
}

for (const button of copyButtons) {
  registerButton(button)
}
