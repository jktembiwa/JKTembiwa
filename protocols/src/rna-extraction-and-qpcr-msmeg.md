title: RNA extraction (TRIzol, Direct-zol) and one-step RT-qPCR set-up for M. smegmatis
category: Mycobacterial genetics
tags: RNA extraction, qPCR, TRIzol, DNase, M. smegmatis
summary: Bead-beating in TRIzol, column purification, DNase treatment, a no-RT-style PCR control for DNA contamination, and a one-step SYBR RT-qPCR reaction.
source: Written by K. Tembiwa (Boutte Lab, 2023 version).
version: Draft 0.1
---
Work in an RNase-free area. Wipe benches, pipettes and gloves with an RNase-decontaminating wipe. Have everything ready first and move quickly.

## Harvest

1. Cool a centrifuge to 4 °C. Use 20–30 mL culture at OD ~0.5–1 per biological replicate. Note RNA yield against starting OD the first time you do this.
2. **Optional RNAlater** (to freeze the transcriptome and process many samples together; [steps unverified in the source]{.tbc}): add an equal volume of RNAlater, mix, wait a few minutes at room temperature, then add water or PBS equal to ¼ of the current volume so the cells pellet. Store at 4 °C short-term or –20 °C for up to a month.
3. Without RNAlater: chill cultures on ice.
4. Spin 4,000 rpm, 10 min, 4 °C (20 °C if RNAlater was used). Remove all supernatant; with RNAlater it is essential to remove all of it. If the pellet is disturbed, re-spin.

## Lysis

1. Resuspend the pellet in 750 µL TRIzol and transfer to a bead-beating tube.
2. Bead-beat 45 s, rest 5 min at room temperature (TRIzol stabilizes the sample); bead-beat 30 s, rest 5 min.
3. Spin 15,000 rpm for 1 min.

## Purification (Direct-zol RNA kit; follow the kit manual)

All at room temperature, spins 30 s at 10,000–16,000 × g.

1. Move the supernatant to an RNase-free 2 mL tube. Add an equal volume of 95–100% ethanol and mix.
2. Load 700 µL at a time on a column; spin; discard flow-through.
3. **On-column DNase** (kit DNase): wash with 400 µL RNA wash buffer; add 5 µL DNase I + 75 µL digestion buffer; 15 min at room temperature. (Skip if using DNase Turbo afterwards.)
4. Wash twice with 400 µL Direct-zol PreWash.
5. Wash with 700 µL RNA wash buffer, 2 min spin, twice.
6. Elute with 100 µL DNase/RNase-free water.

Keep RNA on ice if used the same day, –20 °C for days, –80 °C for weeks. Avoid freeze-thaw cycles.

## Quality and DNase treatment

1. NanoDrop with kit water as blank. 260/280 and 260/230 should be near 2.0–2.2.
2. If you did not use on-column DNase: add 1/10 volume DNase buffer and 1 µL DNase Turbo, 30 min at 37 °C; add 1 µL more DNase Turbo (no extra buffer), another 30 min; add 1/10 volume DNase inactivation reagent, 5 min at room temperature with occasional flicking.
3. **Control PCR:** use a few µL of each RNA as template for a normal PCR with primers you have used before (small product), plus a positive control with plasmid or genomic DNA. No product means no contaminating DNA. If there is product, repeat the DNase treatment. Do not skip this control.
4. Re-measure concentration (it commonly drops after DNase). Optionally run ~8 µL on an RNA gel.

## One-step RT-qPCR (20 µL reaction)

| Component | Volume |
|---|---|
| One-step SYBR green master mix | 10 µL |
| Forward primer (5 µM) | 1 µL |
| Reverse primer (5 µM) | 1 µL |
| Nuclease-free water | 4.5 µL |
| One-step RT enzyme | 0.5 µL |
| RNA | 3 µL |

For 8 reactions make a master mix of 80 µL master mix, 8 µL of each primer, 36 µL water, 4 µL RT enzyme; aliquot 17 µL per well and add 3 µL RNA last. Keep the plate and samples on ice. [Cycling conditions were not recorded in the source; use the master-mix manufacturer's settings.]{.tbc}
