title: His-tagged protein purification: overview (expression strain, test induction, Ni column, SEC)
category: Protein biochemistry
tags: protein purification, His-tag, Ni-NTA, SEC, expression
summary: The overall workflow from cloning to concentrated, frozen protein, with notes on Ni columns, EDTA, and packing empty cartridges.
source: Written by K. Tembiwa (Boutte Lab).
version: Draft 0.1
---
## Workflow

1. **Clone** the gene into a vector with a His tag (e.g. pET28 or pET21).
2. **Transform** an expression strain: BL21 if the gene has no codon bias; BL21 Codon Plus if it has a GC-rich codon bias; a cold-adapted chaperone strain (e.g. Arctic Express Codon Plus) if the protein is still insoluble in BL21 Codon Plus.
3. **Test induction** ([Test inductions](test-induction-protein-expression.html)): pre-induction, post-induction, supernatant and pellet samples on a gel. Adjust conditions until most of the protein is soluble.
4. **Ni column:** large-scale expression (~1 L), lysis, and loading of the supernatant on a Ni column in low-imidazole buffer. Wash with low-imidazole buffer; elute with high imidazole. Check fractions on a gel. See [His-SUMO purification](his-sumo-purification.html) for a worked example.
5. **Size-exclusion chromatography (SEC)** to separate folded from aggregated or unfolded protein; check fractions on a gel.
6. **Concentrate**, aliquot and snap-freeze in liquid nitrogen.

## Practical notes

- **EDTA and Ni columns.** EDTA chelates Ni²⁺ and reduces binding, so leave EDTA out of the wash and elution buffers (a low level in the lysis buffer can stabilize some proteins). If a protein precipitates without EDTA after the column, add it back at the dialysis/SEC stage.
- **Filter and degas** buffers for FPLC; filter (0.45 µm) or spin lysates twice before loading.
- **Bubbles** damage columns. Prime lines whenever you change buffers and set pressure limits for every run.
- **Keep both pump lines in liquid.** Store columns in 20% ethanol and flush with water before switching to salt buffers.

## Packing an empty cartridge with Ni-NTA resin

(Example: 5 mL empty Bio-Scale Mini cartridges, Bio-Rad.)

1. Assemble the cartridge.
2. Pour up to 5 mL Ni-NTA resin into the inner cartridge. Draw the liquid through with a peristaltic pump (as vacuum at the bottom) or a vacuum. Add more resin and repeat until the cartridge is full and tightly packed.
3. Slide the outer cartridge over the packed inner cartridge, fit the ring, and invert it to connect to the chromatography system.
4. Connect "water to water": run ethanol/water at 2 mL/min, connect the top of the cartridge to the system at the column position (fluid should be dripping from the connector), then connect the bottom. The outlet should be flowing before you connect the bottom.

See the manufacturer's manual for your column and instrument.
