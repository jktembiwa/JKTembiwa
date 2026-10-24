title: Mycobacteriophage stock preparation for Tn-seq (φMycoMarT7)
category: Mycobacterial genetics
tags: Tn-seq, phage, transduction, M. smegmatis, plaque assay
summary: Isolate a temperature-sensitive plaque, amplify it on plates and titer it; two versions (Murry 2008-based and M. smegmatis-optimized).
source: Murry et al., Methods Mol Biol 2008;416:45–59, as adapted in protocols from the Rego and Rubin lab lineage and later optimized for M. smegmatis (2015). Received through the Boutte lab. Condensed and reorganized by K. Tembiwa.
version: Draft 0.1
---
Part of the [Tn-seq workflow](tn-seq-overview.html). The phage stock for a library must come from a **single temperature-sensitive clone** (forms plaques at 30 °C, not at 37 °C). Work with phage in a tissue-culture hood; wipe everything with bleach and ethanol, and put waste in biohazard bags.

**MP buffer:** 50 mM Tris pH 7.5, 150 mM NaCl, 10 mM MgSO₄, 2 mM CaCl₂.
**Top agar(ose):** 0.6% agarose; add 2 mM CaCl₂ after autoclaving; hold at 38–42 °C.

## Steps

1. **Plaque isolation.** Wash stationary *M. smegmatis* (OD 0.5–6 all work) three times in MP buffer (6,000 × g, 2 min), resuspend in ~1/4 of the volume. Make 10-fold dilutions (10⁻¹–10⁻⁵) of the phage in MP buffer. Mix 4 mL top agar, 50 µL cells and 100 µL phage dilution, pour onto LB plates, incubate at 30 °C for 36–48 h. (Skip to step 3 if a temperature-sensitive isolate was prepared within the last two weeks.)
2. **Identify temperature-sensitive plaques.** Make a cell lawn (4 mL top agar + 50 µL washed cells) on two LB plates; let dry ≥30 min (do not over-dry). Pick 8 plaques into 100 µL MP buffer each, spot 10–20 µL of each on both plates (one quadrant per plaque). Incubate one plate at 30 °C and one at 37 °C for 2 days. Use a plaque that grew **only at 30 °C**.
3. **Prepare the clone.** Crush the agar plug of a temperature-sensitive plaque in 400 µL MP buffer, spin 5 min at high speed (parafilm the tube before taking it out of the hood), and pass the supernatant through a 0.2 µm filter. This is the new phage stock. Make 10-fold dilutions (10⁻¹–10⁻⁸), plate as in step 1 and incubate 2 days at 30 °C.
4. **Amplify.** Choose the dilution that gives "lacy" (nearly confluent) plates. Pour 5 plates at that dilution; incubate 2 days at 30 °C. Because stocks degrade, it is safer to pour 10 plates: five at the lacy dilution and five at a 5-fold higher dilution.
5. **Collect.** Flood each plate with 3 mL MP buffer and rock overnight at 4 °C. Collect, spin at high speed in the cold, and filter through 0.2 µm (change filters when they clog).
6. **Titer.** Make 10-fold dilutions (10⁻¹–10⁻¹³). Spot 2 × 5 µL of each on lawn plates, let dry at least 30 min, incubate 2 days at 30 °C.
7. **Calculate.** PFU/mL = average plaques per spot × 200 × 10^(dilution factor). For transduction you want about **5×10¹⁰ to 2×10¹¹ PFU/mL**.

Use amplified phage within about 3 days; make a fresh stock for each transduction.

## Versions

| | Murry 2008-based | *M. smegmatis*-optimized |
|---|---|---|
| Host wash | 7H9 + glycerol + ADC, no Tween | MP buffer |
| Plates | 7H10 (amplification, 10 cm) or LB | LB throughout |
| Amplification plates | 5 × 10 cm 7H10, ~2 days at 30 °C | 5–10 plates, 2 days at 30 °C |
| Collection | 3 mL MP per plate, 0.2 µm filter | same, overnight at 4 °C |
| Shelf life | not stated | use within 3 days |

The Fortune-lab Benchling version (2022) differs in detail: host *M. smegmatis* mc²155, 3.5 mL top agarose with 200 µL washed cells and 50 µL phage dilution on 7H10 + glycerol + ADC (no Tween), 2 mL MP buffer per plate rocked ~4 h at room temperature, 10 µL spots for titering; "a good stock is >5×10¹⁰ PFU/mL". Dry lawn plates well before spotting or the spots run together.

[Centrifuge speeds are given as rpm in some sources and ×g in others; convert for your rotor.]{.tbc}
