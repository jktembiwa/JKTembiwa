title: His-SUMO-tagged protein purification (Ni-NTA, dialysis, SEC), example CwlM
category: Protein biochemistry
tags: protein purification, His-SUMO, Ni-NTA, FPLC, SEC, CwlM
summary: Express in BL21, lyse by sonication, purify on Ni-NTA by FPLC, dialyze, polish by size-exclusion chromatography. Example: His-SUMO-CwlM (~56 kDa).
source: Written by K. Tembiwa (Boutte Lab), developed for His-SUMO-CwlM.
version: Draft 0.1
---
## Overview

Plasmid: pET His-SUMO-CwlM, stored in a cloning strain. Miniprep the vector, then transform into chemically competent *E. coli* BL21 (Codon Plus) each time and use a single colony for the starter. Select with ampicillin ([140 µg/mL]{.tbc}) in LB.

## 1. Expression

Induce with **1.3 mM IPTG at 18 °C overnight**. Pellet at 5,000 [rpm]{.tbc} for 20 min and store pellets at –20 °C. Record OD₆₀₀ before and after induction and keep 50–100 µL of each in Laemmli buffer to confirm induction on a gel.

## 2. Lysis (sonication)

Wash buffer: 50 mM Tris pH 8, 350 mM NaCl, 10 mM imidazole, 10% glycerol, 1 mM DTT (add fresh).

1. Thaw pellets on ice and resuspend in 20–50 mL wash buffer. Add a pinch of lysozyme; 30 min on ice.
2. Sonicate 35 s [at 40% amplitude]{.tbc}, 30 s rests, 15 cycles.
3. Spin 13,000 [rpm]{.tbc}, 25 min. Keep samples of supernatant and (resuspended) pellet in Laemmli.

## 3. Ni-NTA by FPLC

Use filtered, degassed buffers. If the supernatant is cloudy, syringe-filter it before loading.

- Equilibrate: 1.25 CV wash buffer
- Wash: 3 CV wash buffer, then a 1.25 CV gradient 0–100% elution buffer
- Elute: 3 CV elution buffer (wash buffer with 250 mM imidazole)

## 4. Check fractions

Run flow-through, wash and elution fractions with supernatant and pellet samples on a 12% SDS gel. His-SUMO-CwlM runs at ~56 kDa.

## 5. Dialysis

Dialyze the eluate overnight against wash/elution buffer with no imidazole.

## 6. Size-exclusion chromatography (SEC)

NanoDrop the dialyzed protein (blank: dialysis buffer) and keep a gel sample. Load on SEC in 50 mM Tris pH 8, 350 mM NaCl, 10% glycerol, 1 mM DTT (equilibrate 1.25 CV; elute 1.25 CV). Run fractions on a gel, pool the clean ones, concentrate, NanoDrop, adjust glycerol to 10% final, re-measure, and freeze aliquots at –80 °C.

[Amplitude of sonication, centrifuge speeds as rpm and the aliquot/freezing step need confirmation.]{.tbc}
