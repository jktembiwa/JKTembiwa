title: HADA / NADA pulse-chase staining of peptidoglycan (PCP)
category: Imaging and analysis
tags: HADA, NADA, microscopy, peptidoglycan, pulse-chase, M. smegmatis
summary: Label old peptidoglycan with HADA, let cells grow, label new peptidoglycan with NADA, and image.
source: Written by K. Tembiwa from the Boutte Lab pulse-chase staining protocol.
version: Draft 0.1
---
## Part 1: HADA pulse (stop here if not doing the chase)

1. Grow a 5 mL culture to log phase.
2. Pellet all 5 mL at 5,000 × g for 10 min.
3. Resuspend in 3 mL 7H9 (+ antibiotics if used).
4. Add 3 µL HADA (1:1000) and incubate 15 min.
5. Pellet 1 mL at a time in 1.5 mL tubes, 16,000 × g for 90 s.
6. Resuspend thoroughly in 3 mL 7H9, then pellet again (1 mL per tube, 16,000 × g, 90 s).

## Part 2: Outgrowth and NADA pulse

1. Resuspend cells in 1 mL 7H9 and add to 4 mL 7H9 (final 5 mL), with antibiotics if used.
2. Measure and record OD₆₀₀.
3. Incubate 90 min at 37 °C on a roller.
4. Stain 1 mL of culture with 1 µL NADA (1:1000) for 2 min at room temperature.
5. Pellet at 16,000 × g for 90 s.
6. Resuspend in 7H9. Start with 100 µL and add 50 µL at a time until the suspension is not too turbid.
7. Image (example settings below).

| Filter | Exposure | Lamp power |
|---|---|---|
| GFP (NADA) | [100 ms]{.tbc} | [30%]{.tbc} |
| DAPI (HADA) | [700 ms]{.tbc} | [40%]{.tbc} |
| DIA | [to be confirmed]{.tbc} | [50%]{.tbc} |

Settings depend on the microscope and need to be tuned for each setup.

## Notes

- Image fixed cells within 24 h of fixation.
- For a lone HADA stain, stop after Part 1.
- Measurement of old- and new-pole length from the images is done in Fiji with a segmented-line macro; a separate analysis page will be added.
