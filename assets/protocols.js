(function(){
  var q=document.getElementById('q'),cards=[].slice.call(document.querySelectorAll('.proto-card')),
      chips=[].slice.call(document.querySelectorAll('.chip')),empty=document.getElementById('empty'),active={};
  function apply(){
    var term=(q.value||'').toLowerCase().trim(),tags=Object.keys(active).filter(function(k){return active[k]}),shown=0;
    cards.forEach(function(c){
      var ok=(!term||c.dataset.text.indexOf(term)>-1)&&tags.every(function(t){return c.dataset.tags.split('|').indexOf(t)>-1});
      c.hidden=!ok; if(ok) shown++;
    });
    empty.hidden=shown>0;
    [].slice.call(document.querySelectorAll('.proto-group')).forEach(function(g){g.hidden=!g.querySelector('.proto-card:not([hidden])');});
  }
  q.addEventListener('input',apply);
  chips.forEach(function(b){b.setAttribute('aria-pressed','false');b.addEventListener('click',function(){
    var t=b.dataset.tag;active[t]=!active[t];b.setAttribute('aria-pressed',active[t]?'true':'false');apply();});});
})();
