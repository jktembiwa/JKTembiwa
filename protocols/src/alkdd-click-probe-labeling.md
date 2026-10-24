title: Metabolic probe labeling (alkDD, Oalk-TMM, alkD-Ala) with CuAAC click detection (TBTA)
category: Imaging and analysis
tags: click chemistry, CuAAC, metabolic labeling, TMM, D-alanine, M. smegmatis, fluorescence
summary: Pulse M. smegmatis with an alkyne-modified probe, fix, and attach a fluorescent azide with a TBTA-ligand click reaction.
source: Boutte Lab protocol (as received; reagent suppliers named in the original). For a BTTP-based live-cell version see the page on azide labeling and CuAAC.
version: Draft 0.1
---
## Before you start

- Turn the benchtop shaker to 37 °C (or use an incubator).
- Prepare **PBSTB** (PBS + 0.01% BSA + 0.05% Tween 80) and chill it on ice.
- Thaw 2% PFA in PBS. Optional: 1 mg/mL glycine in PBS.
- Grow a secondary culture overnight to log phase and record the OD₆₀₀.

## Probe pulse (200 µL culture per condition)

| Probe | Stock | Final | Add per 200 µL |
|---|---|---|---|
| no probe | none | none | none |
| alkDD | 500 mM | 2.5 mM | 1 µL |
| Oalk-TMM | 2.5 mM | 50 µM | 4 µL |
| alkD-Ala | 50 mM | 500 µM | 2 µL |

1. Rotate at 37 °C for 10 min.
2. Spin 3,500 × g, 5 min. Wash 3× with cold PBSTB (spin 3,500 × g, 5 min each).
3. Fix with 2% formaldehyde, 10 min at room temperature with rotation/shaking.
4. Wash 3× with PBSTB.
5. Optional: quench in 1 mg/mL glycine in PBS for 15 min at room temperature, then wash 3× with room-temperature PBSTB.

## Click reaction (master mix for 4 samples, in 900 µL PBSTB)

Add the reagents **in this order**, mixing between additions:

| Reagent | Stock | Final | µL per reaction mix |
|---|---|---|---|
| CuSO₄ | 50 mM | 1 mM | 20 |
| TBTA | 6.4 mM | 128 µM | 20 |
| Sodium ascorbate (fresh) | 60 mM (11.9 mg/mL in water) | 1 mM | 20 |
| Azide fluorophore (e.g. picolyl azide AF488; or AF647, TAMRA, CR110) | 1 mM | 40 µM | 40 |

1. Resuspend each sample in 200 µL click master mix.
2. Incubate 30 min – 1 h at room temperature with shaking/rotation.
3. Wash 3× with PBSTB.
4. Protect from light and store at 4 °C.

TBTA and picolyl-azide dyes are available from Click Chemistry Tools; sodium ascorbate from Sigma (A7631). Green picolyl azide 488 is the usual choice; TAMRA also works when green is not available. Include a no-probe control and a no-dye control.

[Check that the picolyl azide quantity (40 µL of 1 mM into ~1 mL, 40 µM) matches the total volume used.]{.tbc}
