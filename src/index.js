import katex from 'katex';
import 'katex/dist/katex.css';

import md from '../dist/pandoc.html';

import './base.scss';
import './code.scss';

document.body.innerHTML = md;

let inlineList = document.querySelectorAll(".math.inline");
let displayList = document.querySelectorAll(".math.display");

for (let element of inlineList) {
    let text = element.textContent;
    element.innerHTML = "";

    katex.render(text, element, {
        displayMode: false,
        throwOnError: true
    })
}

for (let element of displayList) {
    let text = element.textContent;
    element.innerHTML = "";

    katex.render(text, element, {
        displayMode: true,
        throwOnError: true
    })
}