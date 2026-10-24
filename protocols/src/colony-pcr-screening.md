title: Colony PCR screening (E. coli and mycobacteria)
category: Cloning
tags: PCR, colony PCR, screening, E. coli, mycobacteria
summary: Quickly check colonies for an insert or plasmid with a Taq master mix, including template prep for E. coli and for mycobacteria.
source: Adapted by K. Tembiwa from the Boutte Lab Beginner's Manual (v2.0, 2021).
version: Draft 0.1
---
## Purpose

Screen colonies for an insert, plasmid or integration using a Taq-based master mix. Taq has low fidelity, so use this for checking only, never for cloning.

## Reaction (10 µL)

For a Taq master mix that is supplied as a 2X mix with salts, dNTPs and loading dye (for example GoTaq):

| Component | Volume |
|---|---|
| 2X Taq master mix | 5 µL |
| Forward primer, 10 µM | 0.5 µL |
| Reverse primer, 10 µM | 0.5 µL |
| DMSO | 0.5 µL |
| Water | 3.5 µL, minus the volume of template added |

Make a master mix for the number of colonies **plus 2** to allow for pipetting error, and aliquot 10 µL per PCR tube. **Number the tubes.**

## E. coli

1. Use a sterile tip to pick a colony.
2. Patch the colony onto a numbered spot on a plate with the correct antibiotic, then put the same tip into the PCR tube with the matching number.
3. Run the colony PCR program on the thermocycler.

## Mycobacteria

1. Pick a colony onto a plate to keep it, then transfer some into **10 µL water**. Do not boil. Use 1 µL of this per reaction.
2. An older approach is to suspend the colony in 10 µL DMSO and heat in a thermocycler for an hour to lyse the cells. This can release too much DNA and inhibit the reaction, so water without boiling is preferred.
3. Add 1 µL of lysate to the reaction and run as for *E. coli*.

## Where it usually fails

- **No band from mycobacterial colonies, but a positive control works.** Try a few colonies with a high-fidelity polymerase (Phusion) with a 5–10 min initial step at 98 °C to lyse cells.
- **Lysate seems to inhibit the reaction.** DMSO-boiled lysates can carry over too much DNA. Switch to a water suspension without boiling.
- **Mixed or lawn growth.** Re-streak to single colonies before screening.
