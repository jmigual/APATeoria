import katex from 'katex/dist/katex.mjs';
import 'katex/dist/katex.css';


function renderInlineMath() {
  // Render math
  let inlineList = document.querySelectorAll(".math.inline");

  for (let element of inlineList) {
    let text = element.textContent;
    element.innerHTML = "";

    katex.render(text, element, {
      displayMode: false,
      throwOnError: true,
      strict: false
    })
  }
}


function renderDisplayMath() {
  let displayList = document.querySelectorAll(".math.display");
  for (let element of displayList) {
    let text = element.textContent;
    element.innerHTML = "";
    katex.render(text, element, {
      displayMode: true,
      throwOnError: true,
      strict: false,
    })
  }
}

export default function renderMath() {
  renderInlineMath();
  renderDisplayMath();
}