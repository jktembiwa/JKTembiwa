title: Removing a lox-flanked antibiotic cassette with Cre (M. smegmatis)
category: Mycobacterial genetics
tags: Cre recombinase, lox, markerless deletion, M. smegmatis, sacB
summary: Excise a lox-flanked resistance cassette from a deletion locus using a Cre plasmid, then cure the plasmid with sucrose counter-selection.
source: Written by K. Tembiwa.
version: Draft 0.1
---
## Purpose

Cre recombinase recognizes lox sites and joins the DNA back together, removing the sequence between them. Use this to remove an antibiotic-resistance cassette that is flanked by lox sites, for example one left at a deletion locus after [recombineering](recombineering.html).

The example below assumes a strain with a lox-flanked zeocin-resistance cassette (zeoR) at the deletion site and a second, different marker elsewhere (nourseothricin resistance, nuoR, on an integrated plasmid), plus a kanamycin-marked Cre plasmid that also carries *sacB*.

## Remove the cassette

1. Miniprep the Cre-*sacB* plasmid from *E. coli* and transform it into the strain ([electroporation](electrocompetent-cells-and-electroporation.html)). Plate on kanamycin.
2. Patch colonies on both LB + nourseothricin and LB + zeocin plates. You are looking for colonies that are **nuoR and zeoS**, which have lost the cassette.

## Cure the Cre plasmid

1. Grow nuoR zeoS colonies in 7H9 + nourseothricin 20 µg/mL. **Do not passage the culture to lose the plasmid.** Passaging risks suppressor mutations in the mutants.
2. Streak the culture on 10% sucrose plates (counter-selecting *sacB*).
3. Patch colonies on both LB + kanamycin and LB + nourseothricin. You are looking for colonies that are **kanS and nuoR**.
