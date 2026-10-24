title: GST-tagged protein purification with EconoFit Profinity GST columns
category: Protein biochemistry
tags: GST, protein purification, affinity chromatography, FPLC, vendor manual
summary: Native purification of GST fusion proteins on prepacked 1 or 5 mL columns: buffers, flow rates, lysate prep, cleaning and storage.
source: Summarized from the Bio-Rad EconoFit Profinity GST Columns, 1 and 5 ml, Instruction Manual (catalog 12009295, 12009296, 12009297). Full manual: [Bio-Rad instruction manual (PDF)](https://www.bio-rad.com/webroot/web/pdf/lsr/literature/10000105057.pdf). The manual is authoritative; this is a condensed summary.
version: Draft 0.1
---
These columns are for **native** purification only. They connect to any low-pressure chromatography system with 10-32 fittings. Maximum pressure 72 psi; not autoclavable; storage in 20% ethanol or 2% benzyl alcohol at 4 °C.

## Buffers (manufacturer's recommendations)

| Solution | Composition |
|---|---|
| Lysis / wash | 150 mM NaCl, 10 mM Na₂HPO₄, 5 mM EDTA, pH 7.4 |
| Elution | 20 mM glutathione, 100 mM Tris, 5 mM EDTA, pH 8.0 |
| Desalting | 137 mM NaCl, 2.7 mM KCl, 4.3 mM Na₂HPO₄, 8.1 mM KH₂PO₄, pH 7.4 |
| Cleaning 1 | 500 mM NaCl, 50 mM Tris, pH 8.0 |
| Cleaning 2 | 500 mM NaCl, 100 mM sodium acetate, pH 4.5 |
| Storage | 2% benzyl alcohol or 20% ethanol |

Compatible additives include up to 5 mM DTT, 30 mM β-mercaptoethanol, 5% non-ionic detergents, 20% glycerol and 2 M NaCl (see the manual's compatibility table).

## Quick solubility screen

1. Pellet ~2 mL *E. coli* culture (4,000 × g, 10 min, 4 °C). Resuspend in 500 µL PBS, sonicate 60 s on ice in 10 s pulses. Keep 50 µL as **Total**.
2. Spin 12,000 × g, 10 min, 4 °C. Keep 50 µL of the supernatant as **Soluble**.
3. Resuspend the pellet in 500 µL 6 M urea in PBS, sonicate, spin, and keep 50 µL as **Insoluble**.
4. Add 150 µL Laemmli to each, boil 5 min, and load 10 µL on a gel.

## Lysate preparation

1. Harvest at 8,000 × g for 10 min, 4 °C. Weigh the pellet and resuspend in 10 volumes lysis/wash buffer (200 mL of culture gives ~0.8–1 g; 200 mL suits a 1 mL column and 1 L a 5 mL column for highly expressed protein).
2. Optional: DNase (100 U/mL) or Benzonase (25 U/mL), 10 min at room temperature, to reduce viscosity.
3. Sonicate on ice (25% output) 4 × 1 min.
4. Spin 16,000 × g, 20 min, 4 °C. Filter the supernatant (0.45 µm). Freezing once at –20 °C is possible but can allow proteolysis; re-filter after thawing.

## Purification (1 mL column; scale flow rates for a 5 mL column)

| Step | Volume | 1 mL column | 5 mL column |
|---|---|---|---|
| Flush storage solution | 2 CV water or buffer | 2 mL/min | 10 mL/min |
| Equilibrate | 5 CV | 2 mL/min | 10 mL/min |
| Load lysate | 5–10 CV | 0.5–1 mL/min | 2.5–5 mL/min |
| Wash | 12 CV | 2 mL/min | 10 mL/min |
| Elute | 3 CV | 0.5 mL/min | 2.5 mL/min |

Collect fractions, run an SDS-PAGE gel, and pool the clean ones.

## Cleaning and storage

5 CV cleaning solution 1 and 5 CV cleaning solution 2 at 2 mL/min; rinse with 5 CV water; 5 CV storage solution at 1 mL/min. Seal and store at 4 °C.

## Dynamic binding capacity

More than 11 mg per mL of resin (for a 51 kDa GST fusion at 0.5 mL/min; depends on pH, flow rate and temperature).

Also see [His-tag purification overview](ni-his-tag-purification-overview.html) and [Test inductions](test-induction-protein-expression.html).
