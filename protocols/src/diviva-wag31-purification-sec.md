title: His-DivIVA (Wag31) purification by Ni-NTA and SEC, with oligomer observations
category: Protein biochemistry
tags: DivIVA, Wag31, protein purification, Ni-NTA, SEC, oligomerization, EDTA
summary: Lysis, Ni-NTA purification and dialysis of His6-DivIVA/Wag31, and analytical SEC showing at least two oligomeric populations that do not depend on protein concentration.
source: Condensed from a lab summary dated 12 July 2019 (unpublished internal results, generalized).
version: Version 1.0
---
## Buffers

| Buffer | Composition |
|---|---|
| Lysis | 50 mM Tris/HCl pH 8.0, 100 mM NaCl, 1 mM EDTA, 1 mM DTT, 1 mM PMSF, 0.2% Tween 20, 10 mM imidazole |
| Wash | 50 mM Tris/HCl pH 8.0, 100 mM NaCl, 1 mM DTT, 1 mM PMSF, 0.2% Tween 20, 20 mM imidazole |
| Elution | 50 mM Tris/HCl pH 8.0, 100 mM NaCl, 1 mM DTT, 1 mM PMSF, 250 mM imidazole |
| Dialysis | 50 mM Tris/HCl pH 8.0, 400 mM NaCl, 1 mM EDTA, 1 mM DTT, 0.2% Tween 20, 5% glycerol |
| Size exclusion | Same as dialysis buffer |

## Purification

1. Resuspend the cell pellet in lysis buffer with **lysozyme** and incubate 30 min.
2. Sonicate (power 4, 10 pulses of 30 s). Spin the crude lysate at 12,000 rpm for 40 min.
3. Equilibrate **Ni-NTA beads** with lysis buffer without EDTA, plus 20 mM imidazole.
4. Dilute the supernatant 1:5 with wash buffer, load on the column, wash, and elute His-DivIVA with elution buffer. Run a 12% SDS-PAGE gel of post-induction, supernatant, pellet, flow-through, wash, elution and dialysis samples.
5. **Dialyze** the elution (about 10 mL) against 1 L of dialysis buffer overnight in the cold room.
6. Concentrate the next day in a 10 kDa MWCO PES spin concentrator.

**EDTA: a trade-off.** EDTA must **not** be in the wash and elution buffers, because it chelates Ni²⁺ and reduces the free Ni available to bind DivIVA. However, DivIVA is strongly stabilized by EDTA: every attempt to dialyze it into buffer without EDTA ended in precipitation. So EDTA is in the lysis, dialysis and SEC buffers but not in the wash and elution buffers.

## Analytical SEC and oligomers

The void volume was set from a blue dextran run on the analytical SEC column, with **0.48 CV** used as the void threshold. Fractions across the A280 trace (fractions 17–40, 0.38–0.87 CV) were run on a western blot with an anti-His6 antibody and quantified with ImageJ. Protein concentrations were estimated against a BSA standard curve on Coomassie.

| Run | Sample | Concentration |
|---|---|---|
| 1 | Diluted: dialysate concentrated 10 → 5 mL; 1 mL injected | 2.8 mg/mL |
| 2 | Concentrated: further concentrated 5 → 1 mL | 5.6 mg/mL |
| 3 | Void-volume rerun: fractions before 0.48 CV from run 2 pooled, concentrated and run again | not stated |

**Observations**
- The A280 traces differ between the diluted and concentrated runs, but quantifying by western shows the **distribution between populations is not changed by concentration**.
- The void-volume rerun was done to ask whether the early-eluting species are in equilibrium with the later ones (which could indicate oligomerized unfolded protein).
- Comparing the runs, there are **at least two oligomeric populations**: one eluting around **0.46–0.48 CV** (before the void threshold) and another between **0.52 and 0.58 CV**. Band-intensity plots show two distinct peaks near 0.46 and 0.54 CV.

The source contains the SDS-PAGE, western blots, FPLC traces and the intensity plot; they are not reproduced here.

See also [His-SUMO purification](his-sumo-purification.html) and [FPLC use](fplc-ni-sec-workflow.html).
