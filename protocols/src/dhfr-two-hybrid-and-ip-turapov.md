title: Immunoprecipitation and mycobacterial DHFR two-hybrid (M-PFC) cloning plan
category: Protein biochemistry
tags: immunoprecipitation, two-hybrid, DHFR, M-PFC, cloning, CwlM
summary: Co-immunoprecipitation of an endogenous mycobacterial protein with an antibody-coupled resin, and a plan for cloning interaction partners into DHFR-fragment two-hybrid vectors.
source: Based on methods in Turapov et al. 2018 (Cell Reports; full citation to be verified), annotated and adapted by K. Tembiwa. Please read the original paper for the authoritative method.
version: Draft 0.1
---
## Immunoprecipitation (Turapov et al.)

1. Couple anti-CwlM antibody to CNBr-activated Sepharose 4B (a resin for immobilizing ligands containing primary amines) following the manufacturer's coupling protocol.
2. Mix 1 mL containing **100 µg protein** from a cell fraction (e.g. membrane or cytosol) with **10 µL** antibody–Sepharose. Rotate for 60 min. Spin 500 × g for 5 min. Discard supernatant and wash the resin 3× with TBS.
3. Elute with 40 µL phosphoric acid, pH 2.0. [The original method does not say how the eluate is neutralized or dried before blotting/mass spec.]{.tbc}
4. Control: the same fraction from a CwlM-depleted mutant.
5. To test candidate partners directly, mix recombinant CwlM with 10 µg of each purified candidate in phosphate buffer (20 mM KH₂PO₄ pH 7.0, 100 mM NaCl, 10 mM KCl) with 10 µL antibody–Sepharose, and process as above.

Suggested gel layout: ladder; CwlM; CwlM + resin FT; CwlM + resin eluate; partner; partner + resin FT; partner + resin eluate; partner + CwlM + resin FT; partner + CwlM + resin eluate.

## DHFR two-hybrid (M-PFC): plates and controls

M-PFC splits mycobacterial dihydrofolate reductase into fragments fused to the two proteins; if the proteins interact, DHFR is reconstituted and cells grow on trimethoprim (TMP).

| | Turapov et al. | Used here |
|---|---|---|
| Plates | 7H10 | 7H11 (clearer results than 7H10 in testing) |
| Antibiotics | Hyg 50, Kan 50, TMP 15 | Hyg 50, Kan 25, TMP 50 |

Make plates ± TMP. Streak controls on both:

- **Negative:** vectors expressing DHFR fragments with no interaction domain. Should grow on –TMP and **not** on +TMP.
- **Positive:** vectors carrying GCN4 leucine-zipper domains (which dimerize). Should grow on both.
- Test both 7H10 and 7H11. Proceed with the medium that gives the clearest separation.

## Cloning plan for the test proteins

1. Amplify each ORF from *M. tuberculosis* genomic DNA with primers designed for each vector (separate primer pairs for each of the four vectors).
2. Gel-purify the PCR products ([Gel purification](gel-purification.html)). A longer incubation of the gel slice in dissolving buffer (1–3 h at ~54 °C) can increase yield.
3. Prepare four parent vectors by miniprep and digest (40–50 µg DNA each, then column cleanup, resuspend 30–50 µL, NanoDrop): pUAB100 (BamHI + ClaI), pUAB200 (MfeI + ClaI), pUAB300 (BamHI + HpaI), pUAB400 (MfeI + HpaI).
4. Assemble by Gibson ([Gibson assembly](gibson-assembly.html)), calculating insert and vector volumes. Letting the reaction proceed overnight at room temperature can help.
5. Transform ~5 µL into *E. coli*. For electrocompetent cells, dialyze the Gibson reaction 15–20 min first and use 1–2 µL. Run the remaining ~5 µL on a TAE gel to judge success.
6. Pick 16–32 colonies per plate, patch them, and colony-PCR with check primers ([Colony PCR](colony-pcr-screening.html)).
7. Sequence 2–3 positive clones. If colony PCR is inconclusive, miniprep 8 colonies and do an analytical digest (0.5–1.5 µg).

[Strain names and primer names from the working notes have been removed. Expected band sizes were not recorded in the source.]{.tbc}
