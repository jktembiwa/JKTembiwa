/* Notebook ruled page: snap block heights to the 32px rule grid so text stays on the lines; fill in today's date. */
(function(){
  var L=32;
  function snap(){
    if(!document.body.classList.contains('ruled'))return;
    var els=[].slice.call(document.querySelectorAll('.hero-grid,.research-teaser,.news-list li,.section>.container,.news-year,.hero-actions'));
    els.forEach(function(e){e.style.paddingBottom='';});
    els.reverse().forEach(function(e){
      var cs=getComputedStyle(e);if(cs.display==='none')return;
      var h=e.getBoundingClientRect().height, r=h%L;
      if(r>0.5&&L-r>0.5){e.style.paddingBottom=(parseFloat(cs.paddingBottom)+L-r)+'px';}
    });
  }
  function date(){
    var d=document.querySelectorAll('.entry-date');if(!d.length)return;
    var n=new Date();var s=('0'+n.getDate()).slice(-2)+' '+['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'][n.getMonth()]+' '+n.getFullYear();
    [].forEach.call(d,function(e){e.textContent='Date: '+s;});
  }
  date();
  window.addEventListener('load',snap);window.addEventListener('resize',snap);
  if(document.fonts&&document.fonts.ready)document.fonts.ready.then(snap);
})();
