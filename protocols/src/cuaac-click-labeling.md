title: Azide metabolic labeling and CuAAC "click" staining in M. smegmatis
category: Imaging and analysis
tags: click chemistry, CuAAC, metabolic labeling, trehalose, fluorescence, M. smegmatis
summary: Pulse-label cells with an azide-modified metabolite (e.g. 6-azido-trehalose or D-Ala-azide), then attach a fluorescent alkyne by copper-catalyzed click chemistry.
source: Based on the revised Buonomo Lab SOP (azide metabolic engineering and CuAAC, non-infection protocol), modified by K. Tembiwa. Credit: Buonomo Lab; follow the original SOP for the authoritative version.
version: Draft 0.1
---
*M. smegmatis* doubles in about 2.75 h, so pulses range from 10 min (short) to 90 min (long). Do the whole workflow in one day.

## Reagents

- Sterile 7H9 (+ Tween 80 + glycerol) with OADC or ADC
- Azide reagent (6-azido-trehalose, D-Ala-azide)
- Alkyne dye (AZDye 555 Alkyne for copper-catalyzed; AZDye 568 DBCO for copper-free)
- 1× PBS; DMSO
- Cu(II)SO₄·5H₂O, BTTP (**use BTTP for live cells**), sodium ascorbate (**fresh each day**)
- Optional: 4% PFA in PBS; PBS + 0.05% Tween 80

## Stock solutions

- Alkyne dye: 10 mM in DMSO, –20 °C
- 1000× BTTP: 400 mM in DMSO (172.22 mg/mL), –20 °C
- 1000× Cu(II)SO₄·5H₂O: 200 mM in PBS (49.92 mg/mL)
- 100× sodium ascorbate: 120 mM in PBS (23.77 mg/mL); make only a small volume, good for one day
- **100× catalyst:** mix BTTP and Cu(II) 1:1 at least 20 min before use and dilute with PBS (e.g. 20 µL 1000× Cu + 20 µL 1000× BTTP + 60 µL PBS = 100 µL). Stable at –20 °C for at least 1 month.

## Labeling (1 mL cultures)

1. Start with mid-log cells (OD₆₀₀ 0.3–0.6). Spin 2 mL and resuspend in 1 mL fresh 7H9 + Tween to concentrate.
2. Put 1 mL in each of two tubes. Add azide reagent (typically 100 µM–10 mM; here 1 mM 6-azido-trehalose from a 100 mM stock, 10 µL) to the experimental tube and 10 µL DMSO to the control.
3. Incubate for the chosen pulse at 37 °C, 200 rpm.
4. Spin 5,000 × g, 5 min (be consistent about hinge orientation). Sterile technique is no longer needed.
5. Wash twice with 500 µL PBS + 0.05% Tween 80 (5,000 × g, 3 min).
6. Resuspend in PBS + 0.05% Tween 80 so each reaction has 100 µL of cells (e.g. 300 µL for three samples). Keep OD₆₀₀ below 1.0 to avoid clumping.

## CuAAC reaction (100 µL)

Prepare every reagent first. **Order and timing matter.**

1. Cells in 100 µL PBS (± Tween).
2. Add 0.25 µL alkyne dye (25 µM final).
3. Add 1 µL premixed 100× catalyst (200 µM Cu(II), 400 µM BTTP final).
4. Add 1 µL fresh sodium ascorbate (1.2 mM final), as soon as possible after the copper. Leave caps open.
5. Mix with a brief flick; the dye should be evenly distributed.
6. Stir/shake at 25 °C, ~500 rpm, 15 min.
7. Spin 5,000 × g, 5 min. Wash three times with 500 µL PBS. If pellets are visibly dye-colored or controls are bright (non-specific staining), use PBS + 0.05% Tween 80 for the washes.

## Optional fixation

Resuspend in 1.6% PFA, 10 min at room temperature, spin, wash once with PBS + 0.05% Tween 80.

## Downstream

- **Microscopy:** image as for other labeled cells.
- **Flow cytometry:** resuspend in 100 µL PBS + 0.05% Tween 80 + 0.5% FBS in a V-bottom 96-well plate.
- **Plate reader:** resuspend in 100 µL PBS in a U-bottom 96-well plate.

Always include a DMSO-only (no azide) control and a no-dye control.
