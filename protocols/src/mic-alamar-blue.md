title: MIC determination in 96-well plates with Alamar Blue (resazurin)
category: Growth and assays
tags: MIC, Alamar Blue, resazurin, antibiotics, 96-well, M. smegmatis
summary: Two-fold drug dilutions across a 96-well plate, inoculation at OD 0.002, and a resazurin colour readout after 48 h.
source: Written by K. Tembiwa; based on the microplate Alamar Blue assay of Franzblau et al., J. Clin. Microbiol. 36:362–366 (1998).
version: Version 1.0
status: reviewed
---
## Layout

Use rows B–G and columns 2–11. Fill the outer wells with 200 µL sterile water to limit evaporation. Column 2: highest drug concentration, **no bacteria** (drug-only control). Columns 3–10: two-fold dilution series (column 3 highest). Column 11: bacteria, no drug.

<figure class="proto-fig" style="max-width:520px"><img src="images/plate-map-example.jpg" alt="Hand-drawn plate map on a 96-well plate lid labelling columns with drug concentrations and wells with strains" width="1000" height="750" loading="lazy"><figcaption>Example plate map. Plates should be mapped at least this well before any plate-based experiment, such as an MIC or an automated growth curve.</figcaption></figure>

## Plan concentrations

1. Estimate the MIC from the literature or earlier experiments and place it in the middle of the series (column 6 or 7). Calculate two-fold steps above and below it and write the values as "actual" concentrations.
2. Antibiotic is diluted 2-fold when cells are added, and cells 2-fold when added to drug, so prepare the drug at **twice** the final concentration ("preliminary" values).

## Set-up

1. Use log-phase cultures (OD 0.1–0.6). Medium must support growth (7H9 or HdB complete; not a starvation medium).
2. Dissolve the drug in DMSO or water at a high stock concentration. Make medium containing the drug at the highest preliminary concentration.
3. Add 100 µL of this medium to column 2 and 200 µL to column 3.
4. Add 100 µL plain medium to column 2 (this completes the drug-only control, final 200 µL) and 100 µL plain medium to columns 4–11.
5. Serially transfer 100 µL from column 3 to 4, 4 to 5, and so on to column 10, mixing and changing tips each time. Discard 100 µL from column 10.
6. Measure culture OD and dilute each biological replicate to **OD 0.002**. Use three biological replicates per strain.
7. Add 100 µL diluted culture to columns 3–11 of a row (one replicate per row).
8. Seal with a breathable plate seal and cover with the lid. Incubate at 37 °C for 48 h with shaking for *M. smegmatis*.
9. Make 0.02% Alamar Blue: 0.8 mg resazurin in 4 mL water. Add 20 µL to every well except the water-filled edge wells. Reseal.
10. Re-incubate 7–18 h for *M. smegmatis*. **Blue = no growth; pink = growth.** Violet wells at 24 h usually turn pink after another day and count as growth. MIC = lowest drug concentration that stays blue.

Confirm incubation times and OD for different species; these values are for *M. smegmatis*.

<figure class="proto-fig" style="max-width:520px"><div class="fig-notes"><div class="note note-l">blue = no growth<svg width="40" height="34" viewBox="0 0 40 34" aria-hidden="true"><path d="M8 2 C 4 14, 10 22, 18 30" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/><path d="M10 24 L18 31 L19 20" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></div><div class="note note-r">pink = growth<svg width="40" height="34" viewBox="0 0 40 34" aria-hidden="true"><path d="M32 2 C 36 14, 30 22, 22 30" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/><path d="M30 24 L22 31 L21 20" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></div></div><img src="images/alamar-blue-plate.jpg" alt="96-well plate after Alamar Blue: blue wells where growth is inhibited and pink wells where bacteria grew" width="1200" height="1084" loading="lazy"><figcaption>Example read-out after Alamar Blue: blue wells are inhibited, pink wells show growth.</figcaption></figure>

