title: Setting up a 96-well growth curve (dilution calculator)
category: Growth and assays
tags: growth curve, plate reader, OD600, dilution, 7H9, assays
summary: Calculate culture and medium volumes to start every well at the same OD, with a fillable template.
source: Template by K. Tembiwa.
version: Draft 0.1
---
## Purpose

Start every well of a plate-reader growth curve at the same initial OD₆₀₀ by diluting each culture into medium. The calculator below gives the volumes of culture and 7H9 for each strain. The default is 200 µL final volume and an initial OD of 0.1.

## Calculator

<div class="gc-calc">
<p><label>Final volume per well (µL) <input id="gc-vf" type="number" value="200" min="1" step="1"></label>
<label>Initial OD₆₀₀ <input id="gc-od0" type="number" value="0.1" min="0.001" step="0.01"></label></p>
<table class="gc-table">
<thead><tr><th>#</th><th>Strain / genotype</th><th>Culture OD₆₀₀</th><th>Culture (µL)</th><th>7H9 (µL)</th></tr></thead>
<tbody id="gc-body"></tbody>
</table>
</div>
<script>
(function(){
  var body=document.getElementById('gc-body'),vf=document.getElementById('gc-vf'),od0=document.getElementById('gc-od0'),rows=[];
  for(var i=1;i<=18;i++){
    var tr=document.createElement('tr');
    tr.innerHTML='<td>'+i+'</td><td><input type="text" aria-label="Strain '+i+'"></td><td><input type="number" min="0" step="0.01" aria-label="Culture OD '+i+'"></td><td class="c">–</td><td class="m">–</td>';
    body.appendChild(tr);rows.push(tr);
  }
  function calc(){
    var V=parseFloat(vf.value),O=parseFloat(od0.value);
    rows.forEach(function(tr){
      var od=parseFloat(tr.children[2].firstChild.value),c=tr.querySelector('.c'),m=tr.querySelector('.m');
      if(!(od>0)||!(V>0)||!(O>0)){c.textContent='–';m.textContent='–';return;}
      var cv=O*V/od;
      if(cv>V){c.textContent='OD too low';m.textContent='–';return;}
      c.textContent=cv.toFixed(1);m.textContent=(V-cv).toFixed(1);
    });
  }
  [].slice.call(document.querySelectorAll('.gc-calc input')).forEach(function(el){el.addEventListener('input',calc);});
})();
</script>

Culture volume = (initial OD × final volume) ÷ culture OD. Medium volume = final volume − culture volume. If a culture's OD is below the target, it cannot be diluted to the target and the row shows "OD too low".

[Plate reader settings (temperature, shaking, reading interval, duration) and plate layout notes to be added.]{.tbc}
