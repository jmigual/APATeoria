import md from '../dist/pandoc.html';

import './base.scss';
import './code.scss';

import renderMath from './math';

function wrapTables() {
  // Wrap all tables in div, this allows the tables to be scrolled horizontally in a phone screen
  let tableList = document.querySelectorAll(":not(div) > table");

  for (let table of tableList) {
    let wrapper = document.createElement("div");
    wrapper.classList.add("table");

    table.parentNode.insertBefore(wrapper, table);
    wrapper.appendChild(table);
  }
}

function addCaptions() {
  // Search for all the elements with a caption attribute
  let captionList = document.querySelectorAll("*[caption]");

  for (let element of captionList) {
    let text = element.getAttribute("caption");

    // Ignore empty elements
    if (text === null || text === "") continue;

    let par = document.createElement('p');
    par.innerHTML = text;
    par.classList.add("caption");

    element.appendChild(par);
  }
}

function createElements() {
  document.body.innerHTML = md;

  renderMath();
  wrapTables();
  addCaptions();
}

document.addEventListener('DOMContentLoaded', createElements);