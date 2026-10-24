title: In vitro phosphatase assay with PstP (radiolabeled substrate)
category: Protein biochemistry
tags: phosphatase assay, PstP, radioactivity, PknB, PknA, kinase
summary: Phosphorylate a substrate with its kinase and radiolabeled ATP, add PstP (wild-type or phosphomimetic variants), and follow dephosphorylation over time.
source: Boutte Lab protocol (as received) used for the PstP phosphorylation-site study; check the published paper for the authoritative version [citation to be added]{.tbc}.
version: Draft 0.1
---
**Radioactivity:** work only in an approved radioisotope area with training and monitoring. See also [In vitro kinase assay](in-vitro-kinase-assay-radioactive.html).

## Planning

Take 10 or 20 µL samples before and after ATP at several time points. You may need to load the same kinase-reaction sample (0 min, no PstP) more than once on a gel, so calculate how much substrate and total kinase-reaction volume you need to cover every sample and control. Use kinase:substrate at **1:10 (w/w)**. (5:1 substrate:kinase was used for Wag31.)

## Kinase step (examples)

| Substrate | Kinase | Conditions |
|---|---|---|
| His-SUMO-CwlM | His-MBP-PknB | 30 min, room temperature, 0.15 µCi/µL [γ-³²P]ATP, 2 mM MnCl₂, kinase buffer (50 mM Tris pH 7.5, 250 mM NaCl, 10% glycerol, 1 mM DTT) |
| His-FhaA | His-MBP-PknB | 45 min at 37 °C, 0.15 µCi/µL [γ-³²P]ATP, 5 mM MnCl₂, 25 mM Tris pH 7.5, 1 mM DTT |
| His-Wag31 | His-MBP-PknA | 2 h, room temperature, 0.2 µCi/µL [γ-³²P]ATP, 10 mM MnCl₂, 50 mM Tris pH 7.5, 20% glycerol, 150 mM NaCl |

Take a sample at the end of the kinase step (**0 min, no PstP**). Split the remainder equally into tubes: one for a **no-phosphatase control** (phosphatase buffer only) and one for each PstP variant (and each independently purified batch).

## Phosphatase step

Add PstP (catalytic domain; wild-type or phosphomimetic variants) at one-tenth the mass of substrate, in phosphatase buffer (50 mM Tris pH 7.5, 10 mM MnCl₂, 1 mM DTT). Incubate at room temperature and take samples into 6× Laemmli:

- CwlM: 1, 3, 5, 10, 20 and 40 min
- FhaA: 5, 10, 20, 40, 60 and 80 min
- Wag31: 15, 30, 45, 60, 90 and 120 s

Use two independently purified batches of each PstP variant as biological replicates.

## Gel

Heat samples 95 °C for 10 min, then **load equal amounts of substrate** in each lane. Calculate substrate per µL carefully for this. Run, dry and image as for the [kinase assay](in-vitro-kinase-assay-radioactive.html).
