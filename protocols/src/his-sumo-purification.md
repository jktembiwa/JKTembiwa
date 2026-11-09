title: His-SUMO-tagged protein purification (Ni-NTA, dialysis, SEC), example CwlM
category: Protein biochemistry
tags: protein purification, His-SUMO, Ni-NTA, FPLC, SEC, CwlM
summary: Express in BL21, lyse by sonication, purify on Ni-NTA by FPLC, dialyze, polish by size-exclusion chromatography. Example: His-SUMO-CwlM (~56 kDa).
source: Written by K. Tembiwa, developed for His-SUMO-CwlM.
version: Version 1.0
status: reviewed
related: ni-his-tag-purification-overview | General His-tag workflow from cloning to concentrated, frozen protein. || gst-purification-econofit-profinity | GST-tagged proteins on EconoFit Profinity GST columns. || magstrep-xt-bead-purification | Strep-tag II / Twin-Strep-tag proteins on MagStrep XT magnetic beads.
---
## Overview

Plasmid: pET His-SUMO-CwlM, stored in a cloning strain. Miniprep the vector, then transform into chemically competent *E. coli* BL21 (Codon Plus) each time and use a single colony for the starter. Select with ampicillin (140 µg/mL) in LB.

## 1. Expression

1. Induce 1L of culture with **1.3 mM IPTG at 18 °C overnight with shaking (220 rpm, in 4L flask)**. 
2. Pellet at 5,000 [rpm] for 20 min and store pellets at –20 °C. 
3. Record OD₆₀₀ before and after induction and keep 50–100 µL of each in Laemmli buffer to confirm induction on a gel.

## 2. Lysis (sonication)

Wash buffer: 50 mM Tris pH 8, 350 mM NaCl, 10 mM imidazole, 10% glycerol, 1 mM DTT (add fresh).

1. Thaw pellets on ice and resuspend in 20–50 mL wash buffer. Add a pinch of lysozyme; 30 min on ice.
2. Sonicate 35 s at 40% amplitude, 30 s rests, 15 cycles.
3. Spin 13,000 rpm, 25 min. Keep samples of supernatant and (resuspended) pellet in Laemmli.

## 3. Ni-NTA by FPLC

Use filtered, degassed buffers. If the supernatant is cloudy, syringe-filter it before loading.

- Equilibrate: 1.25 CV wash buffer
- Wash: 3 CV wash buffer, then a 1.25 CV gradient 0–100% elution buffer
- Elute: 3 CV elution buffer (wash buffer with 250 mM imidazole)

## 4. Check fractions

Run flow-through, wash and elution fractions with supernatant and pellet samples on a 12% SDS gel. His-SUMO-CwlM runs at ~56 kDa.

<figure class="proto-fig" style="max-width:560px"><img src="images/fplc-ni-run.jpg" alt="FPLC software screen during the Ni-NTA elution, showing the A280 trace, collected fractions and the flow-path schematic with pressure and UV readings" width="1300" height="975" loading="lazy"><figcaption>Ni-NTA elution on the FPLC: UV trace with collected fractions, and the flow path with pressure and detector readings.</figcaption></figure>

<figure class="proto-fig" style="max-width:480px"><img src="images/gel-post-ni.jpg" alt="Coomassie-stained gel of fractions after the Ni column with heavily overloaded lanes" width="1000" height="750" loading="lazy"><figcaption>Gel after the Ni column (lanes overloaded).</figcaption></figure>

## 5. Dialysis

Dialyze the eluate overnight against wash/elution buffer with no imidazole.

## 6. Size-exclusion chromatography (SEC)

1. NanoDrop the dialyzed protein (blank: dialysis buffer) and keep a gel sample. 
2. Load on SEC (column should be on SEC buffer: 50 mM Tris pH 8, 350 mM NaCl, 10% glycerol, 1 mM DTT); equilibrate 1.25 CV; elute 1.25 CV. 
3. Run fractions on a gel, pool the clean ones, concentrate to 1 mg/mL at least, NanoDrop to confirm , adjust glycerol to 10% final, re-measure, flash freeze 10-100 µL aliquots in liquid nitrogen and store at –80 °C.

<figure class="proto-fig" style="max-width:520px"><img src="images/sec-trace.jpg" alt="Size-exclusion chromatogram with a small early peak and a larger main peak, with fraction ranges along the top" width="1200" height="657" loading="lazy"><figcaption>Example SEC trace: a small early peak and the main peak; fractions are marked along the top.</figcaption></figure>

<figure class="proto-fig" style="max-width:480px"><img src="images/gel-post-sec.jpg" alt="Coomassie-stained gel of fractions after size-exclusion with cleaner bands" width="1000" height="750" loading="lazy"><figcaption>Gel after SEC: cleaner bands.</figcaption></figure>

