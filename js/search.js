(function(){
'use strict';
let INDEX_URL='search-index.json';
let index=null;
let indexLoaded=false;
let worker=null;
let workerReady=false;

// Normalize text for search
function normalize(text){
  return (text||'').toLowerCase().replace(/ё/g,'е').replace(/[^а-яa-z0-9\s]/g,' ').replace(/\s+/g,' ').trim();
}

// Tokenize
function tokenize(text){
  return normalize(text).split(' ').filter(function(w){return w.length>1;});
}

// Initialize Web Worker for fuzzy search
function initWorker(){
  if(worker) return;
  try {
    worker=new Worker('js/search-worker.js');
    workerReady=true;
  } catch(e){
    workerReady=false;
  }
}

// Load index
function loadIndex(cb){
  if(indexLoaded){ cb(); return; }
  fetch(INDEX_URL).then(function(r){return r.json();}).then(function(data){
    index=data; indexLoaded=true; cb();
  }).catch(function(){ index=[]; indexLoaded=true; cb(); });
}

// Search (delegates scoring to Web Worker when available)
function search(query, cb){
  if(!index || !query.trim()){ cb([]); return; }
  let tokens=tokenize(query);
  if(!tokens.length){ cb([]); return; }

  if(workerReady && worker){
    // Use Web Worker for CPU-intensive scoring
    let handler=function(e){
      worker.removeEventListener('message', handler);
      cb(e.data.results || []);
    };
    worker.addEventListener('message', handler);
    worker.postMessage({type:'search', index:index, query:query});
  } else {
    // Fallback: inline scoring (no worker available)
    let results=[];
    for(let i=0;i<index.length;i++){
      // Basic scoring without Levenshtein (simplified)
      let page=index[i];
      let title=normalize(page.t);
      let desc=normalize(page.d);
      let h1=normalize(page.h);
      let text=normalize(page.x);
      let full=title+' '+h1+' '+desc+' '+text;
      let score=0; let matched=0;
      for(let j=0;j<tokens.length;j++){
        let q=tokens[j]; let found=false;
        if(title.indexOf(q)!==-1){score+=10;found=true;}
        if(h1.indexOf(q)!==-1){score+=8;found=true;}
        if(desc.indexOf(q)!==-1){score+=5;found=true;}
        if(text.indexOf(q)!==-1){score+=2;found=true;}
        if(found) matched++;
      }
      if(matched===tokens.length && tokens.length>1) score+=5;
      if(score>0) results.push({page:page,score:score});
    }
    results.sort(function(a,b){return b.score-a.score;});
    cb(results.slice(0,12));
  }
}

// Highlight matched text
function highlight(text, query){
  if(!text) return '';
  let tokens=tokenize(query);
  let result=text;
  for(let i=0;i<tokens.length;i++){
    let re=new RegExp('('+tokens[i].replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+')','gi');
    result=result.replace(re,'<mark>$1</mark>');
  }
  return result;
}

// Render search results
function renderResults(results, query, container){
  if(!results.length){
    container.innerHTML='<div class="search__empty">Ничего не найдено. Попробуйте другой запрос.</div>';
    return;
  }
  let html='';
  for(let i=0;i<results.length;i++){
    let r=results[i];
    let p=r.page;
    html+='<a href="'+p.u+'" class="search__result">';
    html+='<div class="search__result-title">'+highlight(p.t,query)+'</div>';
    if(p.d) html+='<div class="search__result-desc">'+highlight(p.d,query)+'</div>';
    html+='</a>';
  }
  container.innerHTML=html;
}

// Create search UI
function createSearchUI(){
  let actions=document.querySelector('.header__actions');
  if(!actions) return;
  let btn=document.createElement('button');
  btn.className='search__toggle';
  btn.setAttribute('aria-label','Поиск по сайту');
  btn.innerHTML='<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg>';
  let themeToggle=actions.querySelector('.theme-toggle');
  if(themeToggle) actions.insertBefore(btn, themeToggle);
  else actions.insertBefore(btn, actions.firstChild);

  let overlay=document.createElement('div');
  overlay.className='search__overlay';
  overlay.innerHTML='<div class="search__modal"><div class="search__input-wrap"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg><input type="text" class="search__input" placeholder="Поиск по сайту..." autocomplete="off" aria-label="Поиск"></div><div class="search__results"></div><div class="search__hint">Esc — закрыть, ↑↓ — навигация, Enter — открыть</div></div>';
  document.body.appendChild(overlay);

  let input=overlay.querySelector('.search__input');
  let results=overlay.querySelector('.search__results');
  let selectedIdx=-1;

  function openSearch(){
    overlay.classList.add('is-open');
    document.body.style.overflow='hidden';
    input.value='';
    results.innerHTML='';
    selectedIdx=-1;
    setTimeout(function(){ input.focus(); }, 50);
    loadIndex(function(){});
  }
  function closeSearch(){
    overlay.classList.remove('is-open');
    document.body.style.overflow='';
  }

  btn.addEventListener('click', openSearch);
  overlay.addEventListener('click', function(e){
    if(e.target===overlay) closeSearch();
  });
  document.addEventListener('keydown', function(e){
    if((e.ctrlKey||e.metaKey) && e.key==='k'){ e.preventDefault(); openSearch(); }
    if(e.key==='Escape' && overlay.classList.contains('is-open')) closeSearch();
  });
  input.addEventListener('input', function(){
    let q=input.value.trim();
    if(q.length<2){ results.innerHTML=''; return; }
    // Show skeleton while loading
    results.innerHTML='<div class="search__skeleton"><div class="search__skeleton-line"></div><div class="search__skeleton-line search__skeleton-line--short"></div><div class="search__skeleton-line"></div></div>';
    loadIndex(function(){
      search(q, function(res){
        renderResults(res, q, results);
        selectedIdx=-1;
      });
    });
  });
  input.addEventListener('keydown', function(e){
    let items=results.querySelectorAll('.search__result');
    if(e.key==='ArrowDown'){
      e.preventDefault();
      selectedIdx=Math.min(selectedIdx+1, items.length-1);
      updateSelection(items);
    } else if(e.key==='ArrowUp'){
      e.preventDefault();
      selectedIdx=Math.max(selectedIdx-1, -1);
      updateSelection(items);
    } else if(e.key==='Enter' && selectedIdx>=0 && items[selectedIdx]){
      window.location.href=items[selectedIdx].getAttribute('href');
    }
  });
  function updateSelection(items){
    items.forEach(function(el,i){ el.classList.toggle('is-selected', i===selectedIdx); });
    if(selectedIdx>=0 && items[selectedIdx]) items[selectedIdx].scrollIntoView({block:'nearest'});
  }
}

function init(){
  initWorker();
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded', function(){ createSearchUI(); loadIndex(function(){}); });
  else { createSearchUI(); loadIndex(function(){}); }
}
init();
})();