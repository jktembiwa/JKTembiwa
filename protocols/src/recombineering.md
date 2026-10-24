title: Homologous recombination and recombineering in M. smegmatis
category: Mycobacterial genetics
tags: recombineering, homologous recombination, knockout, M. smegmatis, mycobacteria
summary: Clean knockouts by two-step homologous recombination, and gene replacement by RecE/RecT recombineering.
source: Adapted by K. Tembiwa from the Boutte Lab Beginner's Manual (v2.0, 2021).
version: Draft 0.1
---
**Other recombineering protocols on this site differ from this one**, including in the inducer, induction timing and cell handling: [an alternative M. smegmatis protocol](smeg-recombineering-sundaram.html), [oligo-mediated recombineering](oligo-recombineering.html) and [ORBIT](orbit.html). They have not been reconciled with this page.

## Homologous recombination (suicide plasmid)

Used for insertional crosses and clean knockouts. Requires at least 1 µg of suicide plasmid per transformation and at least 500 bp of identical sequence between plasmid and target. Yield is usually fewer than 10 colonies per transformation, so do multiple transformations.

- **Single insertion:** clone about 500 bp of the target gene into a suicide plasmid.
- **Clean knockout:** clone about 1 kb upstream and 1 kb downstream of the target gene into pJM1 or another *sacB*-containing vector.
  1. Transform the suicide vector into *M. smegmatis* and select on the appropriate antibiotic.
  2. Grow cells without antibiotic to allow the second recombination event.
  3. Select for loss of *sacB* on 10% sucrose. Ideally about 50% of the survivors are knockouts.

## Recombineering (RecE/RecT)

Uses mycobacteriophage RecE and RecT homologues, in a lambda-Red-like system.

1. Flank an antibiotic cassette with about 500 bp of sequence upstream and downstream of the target gene. Two cassettes with lox sites on both sides are available. Generate the linear fragment by stitch PCR or Gibson; you need about 1 µg per transformation.
2. Grow cells carrying the RecE/RecT plasmid (see [vector guide](plasmid-vector-guide.html)). Induce overnight with IVN (light sensitive) at a [10⁻⁷–10⁻⁸ dilution of the stock]{.tbc} to mid-log phase (OD 0.4–0.6). [The induction section gives 10⁻⁶–10⁻⁷; confirm.]{.tbc}
3. Make competent cells as usual ([protocol](electrocompetent-cells-and-electroporation.html)) but resuspend at [1/20 of the usual final volume]{.tbc}, and use 400 µL per transformation.
4. Transform about 1000 ng of linear DNA. Settings: 2500 V, 1000 Ω, 25 µF. The time constant should be 20–30 ms.
5. Outgrow for 2–3 hours in 7H9. If knocking out an essential gene, include aTc when a tet-inducible second copy is at the L5 site.
6. Select on the appropriate antibiotic (usually fewer than 10 colonies per transformation).
