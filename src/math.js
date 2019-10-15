import '../submodules/KaTeX/dist/katex.css'
import renderMathInElement from '../submodules/KaTeX/dist/contrib/auto-render';


// function renderInlineMath() {
//   // Render math
//   let inlineList = document.querySelectorAll(".math.inline");

//   for (let element of inlineList) {
//     let text = element.textContent;
//     element.innerHTML = "";
//     console.log("Text", text);

//     katex.render(text, element, {
//       displayMode: false,
//       throwOnError: true,
//       strict: false
//     })
//   }
// }


// function renderDisplayMath() {
//   let displayList = document.querySelectorAll(".math.display");
//   for (let element of displayList) {
//     let text = element.textContent;
//     element.innerHTML = "";
//     katex.render(text, element, {
//       displayMode: true,
//       throwOnError: true,
//       strict: false,
//     })
//   }
// }

export default function renderMath() {
  renderMathInElement(document.body, {
    "output": "html" // Disables mathML output
    // "preProcess": x => {
    //   console.log(x);
    //   return x;
    // }
  });
  // console.log("Rendering inline math");
  // renderInlineMath();

  // console.log("Rendering display math");
  // renderDisplayMath();
}