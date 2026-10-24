title: PCR set-ups for common polymerases
category: Cloning
tags: PCR, polymerase, cloning, GoTaq, Q5, KOD, Phusion
summary: Reaction compositions and notes for Taq, KOD Xtreme, Q5, Phusion and a Taq:Pfu mix, and when to use each.
source: Adapted by K. Tembiwa from the Boutte Lab Beginner's Manual (v2.0, 2021).
version: Draft 0.1
---
Primer stocks below are 10 µM.

## Taq-based master mix (GoTaq): checking colonies and lysates

Low fidelity. **Do not use for cloning.** Supplied as a 2X mix containing nucleotides, salts, enzyme and loading dye. See also [colony PCR](colony-pcr-screening.html).

10 µL reaction: 5 µL master mix, 0.5 µL forward primer, 0.5 µL reverse primer, 0.5 µL DMSO, 3.5 µL water (minus template volume).

## KOD Xtreme: high-fidelity, GC-rich cloning

Extension at **68 °C**, not 72 °C, at about 1 min/kb.

50 µL reaction: 0.5 µL KOD Xtreme, 1.5 µL forward primer, 1.5 µL reverse primer, 2.5 µL DMSO, 10 µL KOD Xtreme dNTPs, 25 µL 2X KOD Xtreme buffer, water, and template. [The listed components add to 41 µL plus 7.5 µL water minus template, which is 48.5 µL before template; water plus template should total 9 µL to reach 50 µL.]{.tbc}

## Q5: high fidelity, AT- or GC-rich templates

50 µL reaction: 1 µL template, 2.5 µL each primer, 1 µL dNTPs (10 mM each), 10 µL Q5 reaction buffer, 10 µL Q5 GC enhancer, 0.5 µL Q5 polymerase, and water to 50 µL (22.5 µL with these amounts). A cycling program is given in the [Gibson assembly protocol](gibson-assembly.html).

## Phusion: high fidelity and processivity

Not well optimized for GC-rich DNA. Extension about 15 s/kb. There are two buffers: HF (higher fidelity) and GC (lower fidelity, for GC-rich organisms).

## 10:1 Taq:Pfu mix

Balances the flexibility of Taq with some proofreading by Pfu. Use when Phusion has failed, especially in stitching reactions.

## Where it usually fails

When a PCR fails, the usual cause is an annealing temperature that does not suit the primers. The first thing to try is a gradient PCR across 50–70 °C (see [Gibson assembly](gibson-assembly.html)).
