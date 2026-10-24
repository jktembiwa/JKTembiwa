title: CopyCutter EPI400 cells for unstable or toxic plasmids
category: Cloning
tags: CopyCutter, toxic genes, copy number, E. coli, transformation, vendor manual
summary: Using low-copy-number competent cells (and the induction solution) to clone toxic or unstable sequences, then raising copy number for plasmid preps.
source: Summarized from the Lucigen manual MA219E (12/2016), CopyCutter EPI400 Electrocompetent and Chemically Competent E. coli and CopyCutter Induction Solution (catalog C400EL10, C400CH10, CIS40025; now sold by Biosearch Technologies). The [Biosearch product page](https://www.biosearchtech.com/competent-cells-for-transformation/large-or-difficult-cloning/copycutter-epi400-competent-cells/p/COMCEL-010) lists the product; the manual accompanies the product. The manufacturer's manual is authoritative.
version: Draft 0.1
---
## What they are

*E. coli* with the plasmid-copy-number gene *pcnB* under an inducible promoter. ColE1/pMB1-origin plasmids (pUC, pET types) are kept at low copy number (about 9 copies for pUC19, versus ~216 in the parent strain) until the **CopyCutter Induction Solution** is added, which raises copy number (pUC19 ~200 copies). Genotype: *mcrA* Δ(*mrr-hsdRMS-mcrBC*) *recA1 endA1* Δ*pcnB*, T1-phage resistant, blue/white compatible.

## Cautions

- Plasmids are distributed randomly to daughter cells at low copy; 10–60% of cells can lack plasmid. Kanamycin selection gives fewer plasmid-free cells than ampicillin.
- Not recommended for vectors that need tetracycline selection.
- Store cells at –70 °C; do not refreeze chemically competent cells.

## Electroporation

1. DNA in water or low-salt buffer (e.g. TE). Prepare 1 mL antibiotic-free LB per sample; pre-chill cuvettes.
2. Thaw 50 µL cells on ice; mix gently with DNA (avoid bubbles); electroporate with your *E. coli* settings.
3. Immediately add 950 µL room-temperature LB, move to a 15 mL tube, shake at 37 °C, 220–230 rpm for 1 h.
4. Plate on LB with antibiotic. Control: 10 pg pUC19 (dilute the supplied 100 pg/µL DNA 1:10 and use 1 µL); plate on ampicillin 100 µg/mL.

## Chemical transformation

*Standard (highest efficiency):* thaw on ice; add 1–5 µL DNA/ligation; ice 5–30 min; 42 °C for 30 s; ice 2 min; add 250 µL SOC; 37 °C for 60 min with shaking (225 rpm); plate.
*Five-minute procedure (ampicillin only; ≥10-fold lower efficiency):* add 3–5 µL DNA, ice 5 min, spread the whole mix on a pre-warmed LB + ampicillin (100 µg/mL) plate.

## Inducing to high copy number

1. Grow a 5 mL overnight (LB + antibiotic) from a colony.
2. Dilute the overnight 1:10 to read OD, then dilute to OD₆₀₀ 0.2 in LB + antibiotic + **1× CopyCutter Induction Solution** (supplied at 1000×).
3. Shake vigorously at 37 °C for **4 h**. Aeration matters: use at least 15 mL tubes for 5 mL cultures and 125 mL flasks for 50 mL.
4. Isolate plasmid DNA by your usual method.

Screen clones by PCR while uninduced (few copies per cell). See also the [FAQ on toxic genes](faq.html).
