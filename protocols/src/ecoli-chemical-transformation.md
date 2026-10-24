title: Chemical transformation of E. coli, with efficiency test
category: Transformation
tags: transformation, E. coli, competent cells, heat shock
summary: Heat-shock transformation of chemically competent E. coli, tips for toxic constructs, and how to measure competent-cell efficiency.
source: Adapted by K. Tembiwa from the Boutte Lab Beginner's Manual (v2.0, 2021).
version: Draft 0.1
---
## Purpose

Introduce a plasmid or assembly reaction (for example a Gibson or ligation product) into chemically competent *E. coli*, and test how competent a new batch of cells is.

## Transformation

Competent cells (DH5α, Mach1, TOP10 or XL1-Blue) are stored in 100 µL aliquots at −80 °C. Split one tube between two or three transformations if you are doing several at a time.

1. Thaw competent cells on ice.
2. Add 5–10 µL of assembly or ligation reaction.
3. Incubate on ice 15–20 min.
4. Heat shock at 42 °C for 45–60 seconds.
5. Return to ice for 2 min.
6. Add 1 mL LB and incubate at 37 °C for 45–60 min.
7. Spin the tube and remove the LB. Resuspend the pellet in 100 µL LB and spread on an LB plate with the appropriate antibiotic. Incubate at 37 °C overnight.

## If your gene may be toxic

Grow the recovery at 30 °C for about 1.5 hours and incubate the plate at 30 °C overnight. Colonies take 24+ hours but are often correct, with little background. TOP10 and XL1-Blue (which carries a tet repressor) tend to suit toxic cloning, but both grow more slowly than DH5α.

## Testing transformation efficiency

Use a control plasmid with a known concentration, aliquoted at 100 ng.

1. Transform 100 ng of plasmid into chemically competent cells with the heat-shock protocol above.
2. Add 200 µL LB and recover for 45 min at 37 °C.
3. Make a 10-fold dilution series (tubes labeled 10⁻¹ to 10⁻⁶), each with 270 µL LB. Move 30 µL from the transformation into the 10⁻¹ tube, mix by pipetting, and continue down the series with a fresh tip each time.
4. Plate about 270 µL of the remaining undiluted transformation and of each dilution on separate selection plates.
5. Count colonies on the lowest-dilution plate with individual, countable colonies.
6. Colonies per aliquot = colonies × 10^(dilution). For example, 57 colonies on the 10⁻⁵ plate gives 57 × 10⁵. This ignores the fraction of the transformation plated: if the total volume after recovery is about 310 µL (100 µL cells + 10 µL plasmid + 200 µL LB) and you plate 270 µL, multiply by about 1.15 for an exact value. [The correction is small relative to the order-of-magnitude efficiency usually reported.]{.tbc}
7. Transformants per µg = total colonies × 10 (because 100 ng was used).

Good competent cells give about 10⁶ colonies per µg or higher.

## Where it usually fails

- **No or very few colonies.** Test the efficiency of your competent cells with a control plasmid (above).
- **Suspected toxic gene.** Use the 30 °C recovery and incubation above, and a strain such as TOP10 or XL1-Blue.
