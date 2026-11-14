(function(){
'use strict';
var INDEX_URL='search-index.json';
var index=null;
var indexLoaded=false;

// Levenshtein distance for fuzzy matching
function levenshtein(a,b){
  if(a===b) return 0;
  if(!a.length) return b.length;
  if(!b.length) return a.length;
  var prev=Array.from({length:b.length+1},(_,i)=>i);
  for(var i=1;i<=a.length;i++){
    var cur=[i];
    for(var j=1;j<=b.length;j++){
      var cost=a[i-1]===b[j-1]?0:1;
      cur[j]=Math.min(prev[j]+1,cur[j-1]+1,prev[j-1]+cost);
    }
    prev=cur;
  }
  return prev[b.length];
}

// Normalize text for search
function normalize(text){
  return (text||'').toLowerCase().replace(/ё/g,'е').replace(/[^а-яa-z0-9\s]/g,' ').replace(/\s+/g,' ').trim();
}

// Tokenize
function tokenize(text){
  return normalize(text).split(' ').filter(function(w){return w.length>1;});
}

// Score a page against query
function scorePage(page, queryTokens){
  var title=normalize(page.t);
  var desc=normalize(page.d);
  var h1=normalize(page.h);
  var text=normalize(page.x);
  var full=title+' '+h1+' '+desc+' '+text;
  var score=0;
  var matched=0;
  for(var i=0;i<queryTokens.length;i++){
    var q=queryTokens[i];
    var found=false;
    // exact match in title (high weight)
    if(title.indexOf(q)!==-1){ score+=10; found=true; }
    // exact match in h1
    if(h1.indexOf(q)!==-1){ score+=8; found=true; }
    // exact match in description
    if(desc.indexOf(q)!==-1){ score+=5; found=true; }
    // exact match in body
    if(text.indexOf(q)!==-1){ score+=2; found=true; }
    // fuzzy match (Levenshtein <= 2 for words >= 4 chars)
    if(!found && q.length>=4){
      var words=full.split(' ');
      for(var w=0;w<words.length;w++){
        if(words[w].length>=3 && levenshtein(q,words[w])<=2){
          score+=1; found=true; break;
        }
      }
    }
    if(found) matched++;
  }
  // bonus for matching all query tokens
  if(matched===queryTokens.length && queryTokens.length>1) score+=5;
  return score;
}

// Load index
function loadIndex(cb){
  if(indexLoaded){ cb(); return; }
  fetch(INDEX_URL).then(function(r){return r.json();}).then(function(data){
    index=data; indexLoaded=true; cb();
  }).catch(function(){ index=[]; indexLoaded=true; cb(); });
}

// Search
function search(query){
  if(!index || !query.trim()) return [];
  var tokens=tokenize(query);
  if(!tokens.length) return [];
  var results=[];
  for(var i=0;i<index.length;i++){
    var sc=scorePage(index[i],tokens);
    if(sc>0) results.push({page:index[i],score:sc});
  }
  results.sort(function(a,b){return b.score-a.score;});
  return results.slice(0,12);
}

// Highlight matched text
function highlight(text, query){
  if(!text) return '';
  var tokens=tokenize(query);
  var result=text;
  for(var i=0;i<tokens.length;i++){
    var re=new RegExp('('+tokens[i].replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+')','gi');
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
  var html='';
  for(var i=0;i<results.length;i++){
    var r=results[i];
    var p=r.page;
    html+='<a href="'+p.u+'" class="search__result">';
    html+='<div class="search__result-title">'+highlight(p.t,query)+'</div>';
    if(p.d) html+='<div class="search__result-desc">'+highlight(p.d,query)+'</div>';
    html+='</a>';
  }
  container.innerHTML=html;
}

// Create search UI
function createSearchUI(){
  // Find header actions
  var actions=document.querySelector('.header__actions');
  if(!actions) return;
  // Create search button
  var btn=document.createElement('button');
  btn.className='search__toggle';
  btn.setAttribute('aria-label','Поиск по сайту');
  btn.innerHTML='<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg>';
  // Insert before theme toggle
  var themeToggle=actions.querySelector('.theme-toggle');
  if(themeToggle) actions.insertBefore(btn, themeToggle);
  else actions.insertBefore(btn, actions.firstChild);

  // Create search overlay
  var overlay=document.createElement('div');
  overlay.className='search__overlay';
  overlay.innerHTML='<div class="search__modal"><div class="search__input-wrap"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg><input type="text" class="search__input" placeholder="Поиск по сайту..." autocomplete="off" aria-label="Поиск"></div><div class="search__results"></div><div class="search__hint">Esc — закрыть, ↑↓ — навигация, Enter — открыть</div></div>';
  document.body.appendChild(overlay);

  var input=overlay.querySelector('.search__input');
  var results=overlay.querySelector('.search__results');
  var selectedIdx=-1;

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
    var q=input.value.trim();
    if(q.length<2){ results.innerHTML=''; return; }
    var res=search(q);
    renderResults(res, q, results);
    selectedIdx=-1;
  });
  input.addEventListener('keydown', function(e){
    var items=results.querySelectorAll('.search__result');
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
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded', createSearchUI);
  else createSearchUI();
}
init();
})();