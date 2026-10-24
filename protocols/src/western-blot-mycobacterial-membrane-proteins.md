title: Western blot of membrane proteins from M. smegmatis (bead-beating lysis)
category: Protein biochemistry
tags: western blot, M. smegmatis, membrane proteins, lysis, SDS-PAGE
summary: Bead-beating lysis of M. smegmatis, SDS-PAGE, wet transfer to PVDF and chemiluminescent detection, with variants for PgfA and an HA/GFP-tagged PonA1.
source: Written by K. Tembiwa from lab protocols used for PgfA and PonA1-tagged western blots (Boutte Lab).
version: Draft 0.1
---
## 1. Lysis (about 1.5 h)

1. Grow a 10 mL *M. smegmatis* culture to late log (OD₆₀₀ 0.6–0.9).
2. Pellet 5 min at 4 °C. Resuspend in 500 µL PBS + 1 mM PMSF (add PMSF from a 100 mM stock, 10 µL per mL of PBS). **No Tween in the lysis PBS.**
3. Transfer to a bead-beating tube pre-filled with beads (to the bevel at the bottom of the tube).
4. Bead-beat 2 min (balance the tubes symmetrically), then 5 min on ice. Repeat for 4 rounds in total.
5. Spin 10 min at 16,000 [rpm]{.tbc} in the cold.
6. Measure A₂₈₀ of a few µL of supernatant by NanoDrop (blank: PBS + PMSF). Record the concentration.
7. Vortex supernatant and pellet back together. Add Laemmli to 1× (100 µL if the pellet was in 500 µL PBS).
   - **PgfA variant:** also add 30 µL fresh 1 M DTT, heat 95 °C for **20 min**.
   - **PonA1 variant:** heat 95 °C for **10 min**.
8. Spin 1 min at 16,000 × g, room temperature. Move supernatants to new labeled tubes.
9. Normalize all samples to the lowest concentration with PBS + Laemmli. The target is at least [10 mg/mL]{.tbc}.
10. Store at –20 °C.

## 2. Gel and transfer (about 3 h)

1. Load at least 50–100 µg total protein in 15 µL (PgfA: precast NuPAGE-type gel; PonA1: [homemade gel]{.tbc}).
2. Run at 35 mA for 45–60 min in 1× Tris-glycine-SDS buffer.
3. Assemble the transfer sandwich, bottom to top: two sponges (pre-wet in transfer buffer), filter paper, gel, PVDF membrane, filter paper, 2–3 sponges.
   - Wet PVDF in methanol until it is no longer glossy; handle only with tweezers.
   - Cut off the stacking gel and the bottom ridge. Remove all bubbles (a little transfer buffer helps).
   - For a tight pack use a third sponge or thick filter paper.
4. Fill the tank with transfer buffer (below the screws) and the outer chamber with cold water. **Put the whole unit in an ice bucket.**
5. Run at about 25 V for 60 min for one mini gel. Larger proteins need longer time or more voltage.

## 3. Blocking and antibodies (about 2.5 h)

1. Disassemble, keeping track of lane order. Cut the top right corner off the membrane on the side that touched the gel, so you know which side to image.
2. Block 30 min at room temperature in 10 mL TTBS + 5% milk (use a box that never held Coomassie).
3. Wash 3 × 5 min with plain TTBS.
4. Primary antibody in 10 mL TTBS:
   - **PgfA:** [2 µL]{.tbc} rabbit anti-PgfA, 1 h at room temperature (or overnight at 4 °C). Used dilutions can be saved at –20 °C and re-used.
   - **PonA1-tagged:** cut the membrane so the upper part can be probed for a loading control (RpoB). Anti-GFP polyclonal at [33.3 µL per 10 mL]{.tbc}; anti-RpoB re-used from a previous dilution. Save primary dilutions in labeled tubes at –20 °C.
5. Wash 3 × 5 min with TTBS; leave 10 mL plain TTBS on the blot.
6. Add [3 µL]{.tbc} of secondary antibody (rabbit for the target, mouse for RpoB), 1 h at room temperature.
7. Wash 3–5 × 5 min with TTBS.

## 4. Detection

1. Add chemiluminescent reagent (PgfA: 500 µL of each component; PonA1: 250 µL of each in ~1 mL TTBS) and image **immediately**.
2. Image the ladder with the colorimetric setting (auto exposure), then the bands with the chemiluminescence setting (auto or manual exposure).
3. Save the raw chemiluminescence and ladder images separately. Merged images are not used for publication; keep raw files.
4. If background is high, wash 3 × more in TTBS and re-image.

[Antibody dilutions are as written in the original notes. Confirm and express as ratios (e.g. 1:5000) for the public version. The two source protocols differ in details (heat time, DTT, reagent volume), as listed above.]{.tbc}
