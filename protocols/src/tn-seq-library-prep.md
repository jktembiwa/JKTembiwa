title: Tn-seq library prep and sequencing (gDNA to Illumina library)
category: Mycobacterial genetics
tags: Tn-seq, library prep, Illumina, Covaris, AMPure, PCR
summary: Extract gDNA from the scraped library, fragment, ligate barcoded adapters, amplify transposon junctions by two PCRs, size-select and submit for paired-end sequencing; enzymatic and acoustic variants compared.
source: Tn-seq library prep protocols from the Rego/Fortune/Rubin lineage (v8, 2015), a revised enzymatic version (2019–2020), the Fortune-lab Benchling protocol (2024 export) and later lab edits. Condensed by K. Tembiwa. Assembled from several versions; see tables for where they disagree.
version: Draft 0.1
---
Part of the [Tn-seq workflow](tn-seq-overview.html). Start from the frozen library from [library construction](tn-seq-library-construction.html).

**Overall design.** Genomic DNA is fragmented, ends are repaired and A-tailed, and an annealed adapter carrying a **random barcode** is ligated. Adapter 1 carries a 3′ amine so it cannot be extended. PCR 1 amplifies from a transposon-specific primer to the adapter, so only transposon-containing fragments amplify. After size selection, PCR 2 adds Illumina flow-cell and index sequences. The random barcode lets you collapse PCR duplicates to unique templates during analysis.

## 1. Scrape and freeze the library

Per sample: 5 mL 7H9 + OADC + Tween and 5 mL 50% glycerol in a 50 mL tube. Scrape each plate vertically then horizontally into the corner, pour into the tube, pool all plates of one sample, vortex, aliquot ~2 mL into ~6 cryovials, store at −80 °C, and titer one aliquot after thaw. (Scraping 30 plates takes 8–9 h; 36 plates took 2.5–3 h in one report.)

## 2. Genomic DNA (bead beating and phenol–chloroform)

1. Thaw 4 mL library (2 vials), spin at 5,000 × g, 10 min; resuspend in 2 mL TE pH 8.0.
2. Add 750 µL to each of 3 bead-beating tubes containing 600 µL phenol:chloroform:isoamyl alcohol (25:24:1, pH 8.0). Bead beat at max speed 45 s, rest on ice 45 s (let the instrument cool 1 min between samples); 4 rounds total.
3. Spin 21,000 × g, 10 min; move the aqueous layer to a 15 mL tube with 1 volume of phenol:chloroform. Rock 1 h at room temperature (all in a fume hood, double-bagged).
4. Transfer to a phase-lock tube, spin 1,500 × g, 5 min, 4 °C. Add ½ volume chloroform, spin again. Move the aqueous phase to a new phase-lock tube.
5. Add RNase A to 25 µg/mL, 1 h at 37 °C with shaking. Repeat the phenol:chloroform then chloroform extraction.
6. Add 1/10 volume 3 M sodium acetate pH 5.2 and 1 volume isopropanol; invert; precipitate at −20 °C overnight.
7. Spin ~5,000 × g, 10 min, 4 °C; wash 3 × with 5 mL 70% ethanol; dry ~5 min (do not over-dry); resuspend in 500 µL–1 mL nuclease-free water (warm to 37–56 °C if needed).
8. Quantify by Qubit BR.


## 3. Fragment the DNA (choose one)

Goal: fragments of **200–500 bp, peak ~300 bp**. Check ~5 µL on a 2% TBE gel; a smear from ~100 bp to ~1 kb with a peak at 300–400 bp is expected. Elute in water (warm to 50–65 °C) after clean-up.

| Option | Input | Settings | Notes |
|---|---|---|---|
| Acoustic, Covaris v8 (2015) | 5 µg in 130 µL TE in Covaris tube (part 520045), pipette through the slit in the lid | duty 10%, intensity 5, 200 cycles/burst, 180 s | Cool the instrument first (~2 h). Clean up with a spin column (Qiagen), elute 50 µL. |
| Acoustic, other instrument/model (MRS version) | 5 µg in 130 µL | 140 W peak incident power, duty 10%, 200 cycles/burst, 80 s; or duty 10%, intensity 4, 200 cycles/burst, 80 s | Settings depend on the instrument; calibrate. |
| Acoustic, Benchling | as above | 5%, intensity 3, 200 cycles/burst, 110 s | Covaris calibration can drift; always check size on a gel. |
| Enzymatic, NEBNext Ultra II FS | 500 ng gDNA (up to 2 µg if you need 1 µg downstream) in 26 µL 1× TE | 26 µL DNA + 7 µL reaction buffer + 2 µL enzyme mix; 37 °C for 15–30 min (20 min typical), 65 °C 30 min, 4 °C hold; heated lid 75 °C | Time sets size: 30 min gave a peak near 150 bp in one trial, so try 15–20 min. Clean up with a spin column (3 × 30 s PE washes, elute 50 µL water at 65 °C). |

Spin-column notes (shared by all versions): a Qiagen PCR column binds up to ~10–15 µg; do 3 × 30 s PE washes instead of one 1-min wash; elute in warm water or buffer, let it sit ~1 min.

Kit reference: NEBNext Ultra II FS DNA Library Prep Kit for Illumina (NEB E7805) <https://www.neb.com/en-us/products/e7805-nebnext-ultra-ii-fs-dna-library-prep-kit-for-illumina>

## 4. Anneal adapters

Adapter 1 (short, 3′-NH₂): 5′-TAC CAC GAC CA-NH₂-3′. Adapter 2 (barcoded): 5′-ATG ATG GCC GGT GGA TTT GTG NNA NNA NNN TGG TCG TGG TAT-3′. (The different sources name these 1.1/1.2 and 2.1/2.2/3.1; the sequences are the same.)

2 µL 2 mM MgCl₂ + 24 µL adapter 1 (100 µM) + 24 µL adapter 2 (100 µM). Anneal: 95 °C 4–5 min, then −1 °C/min to 20 °C, hold at 20 °C. Do not let annealed adapters warm up again (keep at 20 °C or on ice). Aliquot and freeze at −20 °C; thaw on ice and discard leftovers. Dilute to ~20 µM in 10 mM Tris + 10 mM NaCl before ligation if your ligase module requires 15–25 µM (e.g., 20 µL adapters + 30 µL buffer). [One version lists adapter stocks as 1 mM rather than 100 µM; the 100 µM figure is used in the two later versions.]{.tbc}

## 5. End repair/A-tail and adapter ligation

1. 1 µg fragmented DNA in 65 µL with 3 µL End Prep enzyme mix and 6.5 µL 10× buffer; 20 °C 30 min, 65 °C 30 min, hold 4 °C (NEBNext Ultra End Repair/dA-Tailing Module E7546). The Benchling version uses KAPA HyperPrep or NEB Ultra kits per insert (KAPA: 7 µL buffer + 3 µL enzyme, 50 µL total).
2. Add to the same tube: 30 µL NEBNext Ultra II Ligation Master Mix (E7595), 2.5 µL annealed adapter (diluted), 1 µL ligation enhancer. Incubate 20 °C, 30 min (heated lid off). Earlier version: 15 µL ligase mix, 60 min. Benchling/KAPA: 60 µL DNA + 4 µL adapter + 30 µL buffer + 10 µL ligase, 60 min at 20 °C.
3. Clean up with AMPure XP at **1.8×** (a lower ratio may work): add beads, mix 10×, 5 min, magnet ~3 min, two 70–80% ethanol washes (fresh), elute in ~40 µL water, transfer ~36 µL. Expect ~700–800 ng from 1 µg; quantifying here is not needed. Alternatively use a spin column.

## 6. PCR 1 (transposon junction amplification)

Primers: transposon primer (anneals in the transposon) 5′-GTCTAGAGACCGGGGACTTATC-3′; adapter primer 5′-ATGATGGCCGGTGGATTTGTG-3′.

| | v8 (2015) | Revised enzymatic (2019–20) | Benchling (2024) |
|---|---|---|---|
| Polymerase | KAPA HiFi HotStart + GC buffer | KAPA HotStart ready mix + DMSO | NEB Q5 master mix |
| Template | ~800 ng total (32.5 µL), 50 µL | 4 × 50 µL reactions, ~90 ng each (<100 ng or Mg²⁺ is chelated) | ½ of ligated DNA (~300–400 ng) in 50 µL |
| Cycling | 98 °C 5 min; 15 × (98 °C 60 s, 65 °C 30 s, 72 °C 30 s); 72 °C 10 min | 98 °C 5 min; 15 × (98 °C 1 min, 65 °C 30 s, 72 °C 15 s); 72 °C 3 min | 98 °C 5 min; 14 × (98 °C 60 s, 65 °C 30 s, 72 °C 30 s); 72 °C 10 min |
| Clean-up | Qiagen, elute 35 µL, normalize to 30 ng/µL | pool, Qiagen (3 PE washes), elute 35 µL; Qubit; 30 ng/µL in 50 µL | spin column or 1.8× AMPure, elute 32 µL Tris-Tween |

One later edit used 67 °C annealing in PCR 1; the others use 65 °C. Include a water-only control and check ~2 µL on a 2% gel (diffuse band, ~300–600 bp).

## 7. Size selection (to ~300–400 bp)

Illumina paired-end reads work best near 300 bp; selection must be done after PCR 1 (or after PCR 2). Recovery is very low; **10 ng or more does not bottleneck** the library.

| Method | Notes |
|---|---|
| E-gel SizeSelect II (2%) | Load ≤700 ng per lane (hence the 30 ng/µL dilution); run ~15 min, then to the 350 bp collection point; recover 25 µL. |
| PippinPrep (2% dye-free cassette) | Mix with loading dye; select 300–400 bp range or 350 bp tight; ~1 h; ~1 ng/µL in ~40 µL. Preferred in one version. |
| AMPure double selection | Optimize the ratio (≈0.6–0.8× to remove large fragments, then bind the rest); higher throughput. |
| Agarose gel (2%) | Cut and gel-extract; higher cross-contamination risk. |

Quantify with Qubit HS if needed (or skip; low-yield results are normal).

## 8. PCR 2 (Illumina ends, index)

Transposon-side primer ("Sol-Mar mix"): four versions with a 5–8 nt variable spacer to stagger the first bases and avoid single-color clusters; mix 1:1:1:1.
5′-AATGATACGGCGACCACCGAGATCTACACTCTTTCCCTACACGACGCTCTTCCGATCT-N(5–8)-CGGGGACTTATCAGCCAACC-3′
Adapter-side indexed primer (8-nt index XXXXXXXX; each sample gets a different index):
5′-CAAGCAGAAGACGGCATACGAGAT-XXXXXXXX-GTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTATGATGGCCGGTGGATTTGTG-3′
The transposon primer ends 5 bp from the junction so reads begin with **TGTTA**, a specificity check in analysis.

Typical reaction (50 µL): polymerase mix, 2.5 µL SolMar mix, 2.5 µL indexed primer, size-selected DNA (10–100 ng; one source used 300 ng), water. Use a **touchdown** program, e.g., 98 °C 5 min; 8 cycles of (98 °C 1 min, 68 °C → −0.8 °C/cycle, 68 °C 15 s); then 8 cycles of (98 °C 1 min, 62 °C 30 s, 68 °C 15 s); 68 °C 5 min. (v8: 16 cycles of the touchdown program; Benchling: Q5 with the PCR 1 program.)

Clean up with AMPure (0.8–0.9×; elute 30 µL and take 26 µL). Run on a gel: a tight band at ~300–350 bp (a second band at about double that size has been seen; cause not established). Quantify by Qubit BR and **qPCR (use qPCR molarity for loading)**. Yield >25 ng/µL is wanted (10 ng/µL workable); one report lost ~90% of the DNA in this step. Optional check of library diversity: blunt TOPO cloning of the library, M13 colony PCR of ~10 colonies, and sequencing (see [blunt TOPO cloning](topo-blunt-cloning.html)).

## 9. Pool and submit for sequencing

Pool equal volumes of each indexed library (≥10 µL total required by many cores; lo-bind tubes). Typical order: Illumina paired-end, medium kit, **Read 1 = 78 cycles, index = 10, Read 2 = 78 cycles**, 20% PhiX spike-in, at least ~130 million reads per lane; list the library as an amplicon/custom Tn-seq library, and request TapeStation and qPCR QC. Enter the **reverse complement** of the index sequence if the core asks for "Index Read 1" (the index is read in its own cycle with the Read 2 primer). The reason for 20% PhiX is not stated in the source; it is thought to offset the low-diversity and high-GC content. [Library submission details are written for one sequencing core; check your own core's form.]{.tbc}

## 10. Analysis

Decompress the facility's fastq.bz2 files, check FastQC per lane, merge lanes per sample if consistent, then run TPP (maps reads with BWA, collapses barcodes to template counts, writes .wig files) and Transit. Do not use newer Python packages than Transit's docs list. See <https://transit.readthedocs.io/en/latest/tpp.html> and <https://transit.readthedocs.io/en/latest/transit_install.html>.

## Notes

- Always run a water-only control through the PCRs.
- Keep a record of which index went to which sample.
- Qubit and qPCR disagree on library concentration; use qPCR for flow-cell loading.
