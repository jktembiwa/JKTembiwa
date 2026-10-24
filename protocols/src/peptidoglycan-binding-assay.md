title: Peptidoglycan isolation and peptidoglycan-binding (sedimentation) assay
category: Protein biochemistry
tags: peptidoglycan, binding assay, E. coli, protein purification
summary: Purify peptidoglycan from E. coli by hot SDS and protease treatment, then test binding of a purified His-tagged protein by co-sedimentation.
source: Written by K. Tembiwa (Boutte Lab); protein-expression conditions follow the lab's His-tagged MurJ intracellular-domain purification.
version: Draft 0.1
---
## A. Isolate peptidoglycan (PG) from *E. coli*

1. Grow 500 mL *E. coli* in LB at 37 °C to OD₆₀₀ 0.6–0.8. Chill on ice 10 min. Pellet at 4,000 × g, 15 min, 4 °C. Resuspend in 20 mL PBS (pH 7.4).
2. Add dropwise to 80 mL **boiling 5% SDS** and boil 30 min with vigorous stirring. Cool to room temperature (**not on ice**; SDS precipitates). Optional: leave overnight at room temperature.
3. Pellet and wash:
   - **Ultracentrifuge:** 100,000 × g, 1 h, 25 °C. Wash 3× with water, 1 h spin each.
   - **Floor centrifuge:** 14,000 [rpm]{.tbc}, 1 h, 25 °C. Wash at least 6× with 50 mL water.
4. Resuspend in 1 mL PBS with α-chymotrypsin (100 µL of 3 mg/mL in 50% glycerol; Sigma C3142) to remove cell-wall-attached protein. Shake at 37 °C overnight, add another 100 µL, and incubate 3–4 h more.
5. Add 1% SDS and incubate 1–2 h at 95 °C. Cool to room temperature.
6. Pellet (14,000 rpm, 25 °C, 1 h) and wash at least 4× with 25 mL water to remove SDS. [A 1 mL wash was also noted as a possible alternative; not confirmed.]{.tbc}
7. Resuspend purified PG in 500 µL 0.02% sodium azide (Sigma S2002). Stable at 4 °C for up to about 1 month.

## B. Purify the His-tagged protein (example: His-SBD)

Express in *E. coli* BL21 and purify following your standard His-tag protocol (see [Test inductions](test-induction-protein-expression.html) and [His-SUMO purification](his-sumo-purification.html)).

- Buffer: 50 mM Tris pH 7.5, 150 mM NaCl, 10% glycerol, 20 mM imidazole (wash) / 250 mM imidazole (elution).
- Induction: 5–6 h at 25 °C, [220 rpm]{.tbc}.
- Size on gel for the example construct: 19.3 kDa (with TM) and 17.3 kDa (without TM).

## C. Binding assay

1. Mix **100 µg PG** with **10 µg protein** in 20 mM Tris-HCl pH 8, 500 mM NaCl, final volume 125 µL. Incubate 30 min at 4 °C with agitation.
2. Spin 10 min at 15,000 × g. Keep the supernatant (unbound/soluble). Add 6× Laemmli and heat 10 min at 95 °C.
3. Wash the pellet twice with 250 µL buffer, resuspend in 100 µL buffer (bound/insoluble fraction).
4. Analyze soluble and insoluble fractions by SDS-PAGE. Include a no-PG control (protein alone) so that any sedimentation of the protein by itself is seen.
