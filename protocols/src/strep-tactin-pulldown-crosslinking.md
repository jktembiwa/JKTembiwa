title: Strep-Tactin pulldown of cross-linked interactors (for mass spectrometry)
category: Protein biochemistry
tags: pulldown, Strep-tag, cross-linking, formaldehyde, mass spectrometry, interactors
summary: Cross-link cells with formaldehyde, capture a Strep-tagged protein on magnetic Strep-Tactin beads, elute, and prepare samples for analytical and preparative gels.
source: Boutte Lab protocol (as received), adapted by K. Tembiwa.
version: Draft 0.1
---
Use a tagged strain and an **untagged control strain** processed in parallel. Formaldehyde and PFA are toxic; work in a hood.

## Cross-link and lyse

1. Grow 500 mL of each strain to OD₆₀₀ ~0.8.
2. Pellet and resuspend in 100 mL PBS-Tween 80 + 800 µL 16% PFA. Keep on ice. (The first exposure and wash is to scavenge amine groups.)
3. Pellet and resuspend again in 100 mL PBS-Tween 80 + 800 µL 16% PFA; incubate 1 h at 37 °C.
4. Pellet and resuspend in 30 mL Buffer W (100 mM Tris pH 8.0, 150 mM NaCl, 1 mM EDTA) + 0.1% DDM + protease inhibitor tablets.
5. Lyse with a French press, 2× at up to 1,400 [psi]{.tbc}.
6. Spin in Oakridge tubes at 15,000 × g for 15 min.

## Beads

For each sample vortex the bead stock, move 600 µL to a tube, collect on a magnet, remove the supernatant, wash with 1 mL Buffer W, and resuspend in 400 µL Buffer W.

## Capture

1. Pour the supernatant into 50 mL conicals. Save 200 µL as **lysate**.
2. Dissolve the pellet in 30 mL denaturing wash buffer (8 M urea) to recover protein still in the membrane. Save 200 µL as **pellet**.
3. Add 400 µL beads per sample (optimize for your protein and lysate). Rock for 2 h in the cold room.
4. Spin 5,000 rpm, 5 min. Save 200 µL of supernatant as **flow-through**.
5. Move the beads to microcentrifuge tubes. Wash 3× with Buffer W (magnet); save 100 µL of the first wash as **wash**.

## Elute and precipitate

1. Add 160 µL PBS + 40 µL 5× Buffer BX. Vortex; incubate 10 min at room temperature; collect on the magnet and move the eluate to a new tube. Repeat once and combine.
2. Add 100 µL 100% TCA to the eluate; keep in the fridge overnight. Add 25 µL 1× Laemmli to the beads ("beads" sample) and keep overnight.
3. Spin the precipitate 15 min at 15,000 × g in the cold. Remove the supernatant. Wash with 1 mL acetone for 30–60 min in the fridge. Spin again 15 min. Remove the acetone (leave a little to protect the pellet), short spin, remove the rest, and air-dry 20–30 min.
4. Resuspend in 25 µL 1× Laemmli. Add NaOH a microliter at a time until the dye is solid blue (orange or brown means too acidic). To reverse the cross-links, heat the sample at [temperature and time per your protocol]{.tbc}.

## Gels and mass spectrometry

1. **Analytical gel first:** 5–10 µL of lysate, pellet, flow-through and wash per strain, plus ~0.5 µL concentrated eluate diluted into 10–15 µL buffer. If the pulldown worked, continue.
2. **Preparative gel:** run the remaining eluates for the tagged and control strains, stain with Coomassie and look for bands unique to the tagged strain. Cut out the whole region around your protein for each sample and send for mass spectrometry.
3. Keep only proteins more abundant in the pulldown than in the control in **multiple independent pulldowns**.

See also [MagStrep XT purification](magstrep-xt-bead-purification.html) for the manufacturer's bead protocol.
