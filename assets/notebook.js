/* Notebook ruled page: snap block heights to the 32px rule grid so text stays on the lines; fill in today's date. */
(function(){
  var L=32;
  function snap(){
    if(!document.body.classList.contains('ruled'))return;
    var pad='.hero-grid,.research-teaser,.news-list li,.section>.container,.news-year,.hero-actions,.card,.grid-2,.grid-3,.page-hero>.container,.news-fig,.publication,.faq,.proto-foot,.chips,.proto-group';
    var mar='figure.proto-fig,figure.research-fig,table,.which-box,pre,.profile-photo,.tag-row,.search';
    var els=[].slice.call(document.querySelectorAll(pad+','+mar));
    els.forEach(function(e){e.style.paddingBottom='';e.style.marginBottom='';});
    els.reverse().forEach(function(e){
      if(!e.offsetParent&&getComputedStyle(e).position!=='fixed')return;
      var cs=getComputedStyle(e),useMargin=e.matches(mar)&&!e.matches(pad);
      var h=(cs.transform==='none'?e.getBoundingClientRect().height:e.offsetHeight)+(useMargin?parseFloat(cs.marginTop)+parseFloat(cs.marginBottom):0), r=h%L;
      if(r>0.5&&L-r>0.5){
        if(useMargin)e.style.marginBottom=(parseFloat(cs.marginBottom)+L-r)+'px';
        else e.style.paddingBottom=(parseFloat(cs.paddingBottom)+L-r)+'px';
      }
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
