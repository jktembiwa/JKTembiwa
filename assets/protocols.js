(function(){
  var q=document.getElementById('q'),cards=[].slice.call(document.querySelectorAll('.proto-card')),
      chips=[].slice.call(document.querySelectorAll('.chip')),empty=document.getElementById('empty'),active={},body={};
  // lowercase and drop accents one character at a time, so positions still line up with the original text
  function norm(s){
    var out='';
    for(var i=0;i<s.length;i++){
      var ch=s[i],n=ch.normalize?ch.normalize('NFKD').replace(/[̀-ͯ]/g,'').toLowerCase():ch.toLowerCase();
      out+=n.length===1?n:(ch.toLowerCase().length===1?ch.toLowerCase():ch);
    }
    return out;
  }
  function count(hay,t){var n=0,i=hay.indexOf(t);while(i>-1&&n<5){n++;i=hay.indexOf(t,i+t.length);}return n;}
  cards.forEach(function(c,i){
    c._slug=c.querySelector('h3 a').getAttribute('href').replace(/\.html$/,'');
    c._head=norm(c.dataset.text);c._order=i;
    c._snip=document.createElement('p');c._snip.className='proto-snippet';c._snip.hidden=true;
    c.insertBefore(c._snip,c.querySelector('.meta'));
  });
  // Show the passage around the first match, with every search word marked.
  function snippet(c,terms){
    var b=body[c._slug];c._snip.textContent='';c._snip.hidden=true;
    if(!b||!terms.length)return;
    var pos=-1;
    terms.forEach(function(t){var i=b.n.indexOf(t);if(i>-1&&(pos<0||i<pos))pos=i;});
    if(pos<0)return;
    var start=Math.max(0,pos-70),end=Math.min(b.raw.length,pos+150);
    if(start>0){var s=b.raw.indexOf(' ',start);if(s>-1&&s<pos)start=s+1;}
    if(end<b.raw.length){var e=b.raw.lastIndexOf(' ',end);if(e>pos)end=e;}
    var seg=b.n.slice(start,end),marks=[];
    terms.forEach(function(t){var i=seg.indexOf(t);while(i>-1){marks.push([i,i+t.length]);i=seg.indexOf(t,i+t.length);}});
    marks.sort(function(x,y){return x[0]-y[0];});
    var at=0,raw=b.raw.slice(start,end);
    if(start>0)c._snip.appendChild(document.createTextNode('…'));
    marks.forEach(function(m){
      if(m[1]<=at)return;
      var from=Math.max(m[0],at);
      c._snip.appendChild(document.createTextNode(raw.slice(at,from)));
      var mk=document.createElement('mark');mk.textContent=raw.slice(from,m[1]);c._snip.appendChild(mk);at=m[1];
    });
    c._snip.appendChild(document.createTextNode(raw.slice(at)+(end<b.raw.length?'…':'')));
    c._snip.hidden=false;
  }
  function apply(){
    // the whole query is one phrase, matched exactly (spacing, case and accents aside)
    var phrase=norm(q.value||'').trim().replace(/\s+/g,' '),terms=phrase?[phrase]:[],tags=Object.keys(active).filter(function(k){return active[k]}),shown=0;
    cards.forEach(function(c){
      var b=body[c._slug],text=b?b.n:'';
      var ok=terms.every(function(t){return c._head.indexOf(t)>-1||text.indexOf(t)>-1})&&tags.every(function(t){return c.dataset.tags.split('|').indexOf(t)>-1});
      // rank within each group: title, summary and tag matches count most, then how often the words appear in the text
      c._score=terms.reduce(function(s,t){return s+(c._head.indexOf(t)>-1?10:0)+count(text,t);},0);
      c.hidden=!ok; if(ok) shown++;
      snippet(c,ok?terms:[]);
    });
    [].slice.call(document.querySelectorAll('.proto-group .grid-2')).forEach(function(g){
      [].slice.call(g.children).sort(function(x,y){return terms.length?(y._score-x._score)||(x._order-y._order):x._order-y._order;})
        .forEach(function(c){g.appendChild(c);});
    });
    empty.hidden=shown>0;
    [].slice.call(document.querySelectorAll('.proto-group')).forEach(function(g){g.hidden=!g.querySelector('.proto-card:not([hidden])');});
  }
  q.addEventListener('input',apply);
  chips.forEach(function(b){b.setAttribute('aria-pressed','false');b.addEventListener('click',function(){
    var t=b.dataset.tag;active[t]=!active[t];b.setAttribute('aria-pressed',active[t]?'true':'false');apply();});});
  fetch('search.json').then(function(r){return r.json();}).then(function(d){
    d.forEach(function(x){body[x.slug]={raw:x.text,n:norm(x.text)};});
    if(q.value)apply();
  }).catch(function(){});  // without the data, search still covers titles, summaries and tags
})();
