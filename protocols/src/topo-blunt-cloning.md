title: Zero Blunt TOPO PCR cloning
category: Cloning
tags: TOPO cloning, blunt-end cloning, PCR, cloning, subcloning
summary: Clone blunt-end PCR products into pCR-Blunt II-TOPO and transform chemically competent or electrocompetent E. coli.
source: Summarized from the Zero Blunt TOPO PCR Cloning Kit user guide (Invitrogen / Thermo Fisher Scientific, publication MAN0000062, Rev B.0); see the [manufacturer's guide](https://documents.thermofisher.com/TFS-Assets/LSG/manuals/zeroblunttopo_man.pdf) for complete details and the full set of controls. Adapted by K. Tembiwa.
version: Draft 0.1
---
This is a condensed summary. The manufacturer's user guide (Thermo Fisher Scientific, [full user guide (PDF)](https://documents.thermofisher.com/TFS-Assets/LSG/manuals/zeroblunttopo_man.pdf), publication number MAN0000062) is the authoritative source and includes control reactions, vector maps and troubleshooting.

## PCR product requirements

- The kit is designed for **blunt-end PCR products** from thermostable proofreading polymerases (for example [Pfx, Phusion or Q5](pcr-polymerases.html)).
- **Do not add 5′ phosphates to your primers**; such products will not ligate into the vector.
- Use a 7–30 minute final extension to make sure products are completely extended.
- Check the product on an agarose gel for a single discrete band of the correct size, or [gel-purify it](gel-purification.html).

## TOPO cloning reaction

| Reagent | Volume |
|---|---|
| Fresh PCR product | 0.5–4 µL |
| Salt solution | 1 µL |
| Water | to a total of 5 µL |
| pCR-Blunt II-TOPO vector | 1 µL |
| **Final volume** | **6 µL** |

Mix gently and incubate for 5 minutes at room temperature (22–23 °C), then put on ice. The reaction can be stored at −20 °C overnight. For routine subcloning, 30 seconds may be enough; for products longer than 1 kb, or pools of PCR products, longer incubation gives more colonies (up to 30 minutes). The salt solution (final 200 mM NaCl, 10 mM MgCl₂ for chemical transformation) increases the number of transformants.

## Transformation

Use kanamycin (50 µg/mL) or low-salt LB with zeocin (25 µg/mL) plates, and prewarm the plates at 37 °C for 30 minutes. Use two plates per transformation.

**Chemically competent cells**

1. Add 2 µL of the TOPO reaction to a vial of competent cells and mix gently (do not pipette up and down).
2. Incubate on ice for 5–30 minutes.
3. Heat shock for 30 seconds at 42 °C without shaking, then return to ice.
4. Add 250 µL room-temperature S.O.C. medium and shake horizontally at 200 rpm and 37 °C for 1 hour.
5. Spread 10–50 µL on prewarmed selective plates (two different volumes, with 20 µL S.O.C. added to spread small volumes evenly). Incubate overnight at 37 °C.

**Electrocompetent cells.** Dilute the TOPO reaction 4-fold in water first (6 µL reaction + 18 µL water) to prevent arcing, then add 2 µL to 50 µL of cells, transfer to a chilled 0.1 cm cuvette, electroporate, and add 250 µL S.O.C. Recover for at least 1 hour at 37 °C before plating as above. If arcing is a problem, reduce the voltage by 10%, reduce the load resistance to 100 Ω, or precipitate the reaction and resuspend in water.

An efficient reaction produces several hundred colonies. Pick about 10 colonies.

## Analyzing transformants

1. Grow 2–6 colonies overnight in LB with the selective antibiotic, saving the original colony by patching to a fresh plate.
2. Isolate plasmid DNA and check by restriction digest for the insert and its orientation (use enzymes that cut once in the vector and once in the insert), or sequence with M13 forward and reverse primers.
3. Alternatively, screen colonies directly by [colony PCR](colony-pcr-screening.html) with an M13 primer and an insert-specific primer; run restriction analysis in parallel the first time.
4. For long-term storage, make a glycerol stock (0.85 mL culture + 0.15 mL sterile glycerol) at −80 °C.
