title: Strep-tag II / Twin-Strep-tag purification with MagStrep "type3" XT magnetic beads
category: Protein biochemistry
tags: Strep-tag, Strep-Tactin, magnetic beads, protein purification, vendor manual
summary: Batch purification in tubes or 96-well plates, with native elution by biotin.
source: Summarized from IBA Lifesciences protocol PR83-0011 (March 2022), "MagStrep type3 XT bead-based protein purification" (catalog 2-4090-002 and 2-4090-010). IBA documents are available from the [IBA Lifesciences download area](https://www.iba-lifesciences.com/download-area-protein.html). The vendor protocol is authoritative.
version: Draft 0.1
---
**Beads:** ferrimagnetic spheres coated with 6% agarose and Strep-Tactin XT, supplied as a 5% (v/v) suspension (20 µL = 1 µL beads). Capacity: up to 0.85 nmol tagged protein per µL beads (25.5 µg of a 30 kDa protein). The beads are not meant to be reused.

**Buffers (10× stocks; dilute 1:9 with water):**

- Buffer W: 1 M Tris-Cl, 1.5 M NaCl, 10 mM EDTA, pH 8 (10×)
- Buffer BXT: Buffer W with 500 mM biotin (10×)

## Batch purification in tubes

- Cleared extract volume should not exceed 2.5 mL per µL beads, and the tagged protein should be above 1 mg/mL. If below this, the vendor recommends gravity-flow Strep-Tactin columns instead. 100 mM biotin can give a more concentrated eluate.

1. Calculate beads: 1 µL beads per 0.85 nmol protein.
2. Place the bead suspension in a tube, collect on a magnet, remove the supernatant.
3. Equilibrate with 200 µL 1× Buffer W per µL beads, 3 times.
4. Clear the sample (20 min at 10,000 × g, or 4,000 × g for small volumes).
5. Resuspend the beads in the cleared sample. Incubate 30 min on ice, vortexing 3–4 times.
6. Collect beads on the magnet; remove the supernatant (save the flow-through).
7. Wash 3× with 100 µL 1× Buffer W per µL beads.
8. **Elute.**
   - *Native:* 25 µL 1× Buffer BXT per µL beads, 10 min with 2–3 vortexes; transfer the supernatant to a new tube; repeat once. The first elution gives the highest concentration.
   - *Denaturing:* SDS sample buffer, 95 °C for 2 min. Strep-Tactin XT also denatures and appears as an extra band at ~13.5 kDa.
9. Check purity by SDS-PAGE (Coomassie or silver) and quantify by Bradford with BSA as standard.

## Batch purification in 96-well plates

For targets up to 90 kDa, at least 0.425 nmol per 200 µL sample. Use at least 40 µL of the 5% suspension per well (2 µL beads), equilibrate with 100 µL 1× Buffer W per µL beads, bind 60 min at room temperature on a plate shaker at 700 rpm, wash 3×, elute with 50 µL 1× Buffer BXT per µL beads (400 rpm, 10 min, twice).

## Troubleshooting (vendor)

- No or weak binding: add protease inhibitors and work at 2–8 °C; use a protease-deficient expression strain; move the tag to the other terminus or use a longer linker or Twin-Strep-tag.
- Contaminants: reduce with reducing agents (disulfide-linked), add salt (up to 5 M NaCl) or mild detergents (up to 2% Triton X-100 or Tween 20) for non-covalent ones, and use biotin blocking solution or avidin for biotinylated proteins.

See also the [Strep-Tactin pulldown](strep-tactin-pulldown-crosslinking.html).
