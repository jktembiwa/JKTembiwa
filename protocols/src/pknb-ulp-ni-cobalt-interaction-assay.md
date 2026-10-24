title: Kinase / protease reaction and Ni or cobalt interaction (pull-down) assay
category: Protein biochemistry
tags: pull-down, interaction assay, kinase, ULP, Ni-NTA, cobalt, CwlM
summary: Phosphorylate a His-SUMO substrate with a kinase, remove the tag with ULP, and test binding to a second His-SUMO protein on Ni or cobalt resin (gravity column or magnetic beads).
source: Written by K. Tembiwa (Boutte Lab), from published CwlM/MurJ interaction work; three lab versions combined.
version: Draft 0.1
---
## Idea

Immobilize a His-SUMO "bait" (e.g. His-SUMO-MurJ ICD) on resin. Pass the untagged "prey" (e.g. CwlM, phosphorylated by PknB or not) over it. Prey that is retained in the elution but not on a bait-free control column interacts with the bait.

*Use cobalt resin for the kinase/ULP stage and a 20 mM imidazole wash with no elution buffer when you want only to remove uncleaved tagged protein; use nickel for the pull-down.*

## Part 1: Kinase and protease reactions

1. Thaw His-SUMO-CwlM and PknB. NanoDrop with the kinase buffer as blank. Example: CwlM 0.48 mg/mL; PknB 1.80 mg/mL.
2. Use a **1:10 kinase:substrate** mass ratio. Example: 144 µg CwlM in 300 µL needs 14 µg PknB (7.8 µL).
3. Set up two tubes, **CwlM~P** (phosphorylated) and **NPC** (no-phosphorylation control): 300 µL CwlM each, PknB in both, MnCl₂ to 1 mM from a 25 mM stock (14 µL in 350 µL), and 0.5 mM ATP (7 µL from 25 mM) **only in CwlM~P**. Keep ATP at –80 °C until needed.
4. Incubate 40 min at 25 °C.
5. Meanwhile prepare Ni (or cobalt) columns: place a frit at the bottom using a pipette tip, add 500 µL resin slurry (bed ~250 µL), drain, wash with a column of nanopure water, then 3 CV of 20 mM-imidazole wash buffer (50 mM Tris pH 7.5, 350 mM NaCl, 20 mM imidazole, 10% glycerol), pipetting on the side.
6. Add **ULP** (SUMO protease) at 1:10 by mass (e.g. 14.4 µg, 16 µL of 0.968 mg/mL) plus 34 µL 10× protease buffer to each tube (400 µL final) **after** the 40 min kinase step. Incubate [time and temperature to be added]{.tbc}.
7. Load each reaction onto its column. Collect flow-through; wash twice with 250 µL wash buffer; elute with 250 µL elution buffer (same as wash but with 250 mM imidazole). Cleaved CwlM is in the **flow-through and first wash**; the tag and uncleaved protein stay on the resin.
8. Run 25 µL of each fraction + 5 µL warmed 6× Laemmli (95 °C) on a gel (10 µL per lane) with PknB, ULP and the kinase reaction. Pool the flow-through and wash 1 once the gel confirms cleavage.
9. NanoDrop. High imidazole can distort readings; if so assume ~90% yield of the cleavage reaction.
10. Clean columns: run elution buffer, then water twice, then 20% ethanol (half through); close the column, shake, and pour the resin into a labeled "used resin" container at 4 °C. Do not discard resin.

## Part 2: Interaction assay (gravity columns)

1. Four small columns: NPC experiment, NPC control, CwlM~P experiment, CwlM~P control. Each prey sample is split in two (one bait, one no-bait control).
2. Thaw His-SUMO-MurJ ICD (example 1.082 mg/mL); use a **1:1 molar/mass ratio** with the prey in the column.
3. Prepare 250 µL-bed columns, wash with 750 µL water and 750 µL 20 mM imidazole wash buffer.
4. Control column: load 250 µL wash buffer (tube A). Experimental column: load bait in wash buffer (tube 1).
5. Wash with 250 µL wash buffer twice (tubes 2 and 3).
6. Load 250 µL prey (CwlM~P or NPC) (tube 4).
7. Elute with 500 µL elution buffer (50 mM Tris pH 7.4, 350 mM NaCl, 10% glycerol, 250 mM imidazole) (tube 5).
8. Mix 50 µL of each fraction with 10 µL pre-warmed 6× Laemmli, heat 95 °C for 10 min, run on a gel.

Fractions: flow-through, wash 1, prey load, wash 2, elution.

## Part 2 (alternative): Magnetic beads

1. Pipette 40 µL HisPur Ni-NTA magnetic beads into a tube, add 160 µL wash buffer, vortex 10 s, collect beads on a magnetic stand, discard supernatant. Wash once more in 400 µL.
2. Bait: dilute His-SUMO bait to 400 µL in SEC buffer (aim for 1:1 with the prey: e.g. if 190 µg prey is recovered, use 95 µg bait), add to the beads, vortex, and keep on ice for ~15 min with gentle flicking every 5 min.
3. Collect beads; save the supernatant (fraction 1, flow-through). Wash with 400 µL wash buffer (fraction 2).
4. Add the prey (flow-through and washes from the cobalt step, ~710 µL diluted to 800 µL; split between control and experiment, 400 µL each). Mix, incubate with periodic mixing for 15 min. Save the supernatant (fraction 3).
5. Wash with 400 µL wash buffer (fraction 4).
6. Resuspend beads in 400 µL buffer, add 80 µL 6× Laemmli, heat 95 °C for 10 min (fraction 5, elution). Run all fractions on a gel.

[Some volumes and incubation times were left blank in the source drafts. They are marked above and need to be filled in from lab notes.]{.tbc}
