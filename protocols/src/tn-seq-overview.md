title: Tn-seq in mycobacteria: which protocol to use
category: Mycobacterial genetics
tags: Tn-seq, transposon library, phage transduction, library prep, overview
summary: Map of the Tn-seq workflow (phage, library, DNA, sequencing, analysis) and how the competing versions of each step differ.
source: Compiled from several Tn-seq and transduction protocols received from collaborating labs (Rego, Fortune, Rubin and Boutte lab versions, 2015–2024) and Murry et al. 2008.
version: Draft 0.1
---
Tn-seq protocols for mycobacteria have been passed between labs and edited many times, so several versions of each step exist and they do not always agree. They are not different methods so much as different tunings of the same method. This page shows the order of steps, which page covers each, and where the versions differ. **Pick one version per step and stay with it for a whole experiment.**

The method is the *Himar1* mariner transposon (φMycoMarT7, a temperature-sensitive phage carrying the transposon and a kanamycin marker) delivered by phage transduction (Murry et al. 2008), followed by sequencing of transposon–genome junctions.

## Workflow

| Step | What happens | Page |
|---|---|---|
| 1 | Make a high-titer, temperature-sensitive phage stock | [Phage stock preparation](tn-seq-phage-stock-prep.html) |
| 2 | Transduce, plate on kanamycin, scrape, freeze the library | [Library construction by transduction](tn-seq-library-construction.html) |
| 3 | Extract genomic DNA, shear, add adapters, amplify junctions, size-select, add Illumina ends | [Library prep and sequencing](tn-seq-library-prep.html) |
| 4 | Map reads and count insertions at TA sites | Analysis with TPP and Transit (see links below) |
| (side) | Find the insertion site of one individual mutant | [Manual insertion mapping](transposon-insertion-mapping.html) |

## Where the versions differ

| Step | Version | Key differences |
|---|---|---|
| Phage stock | Murry 2008 / Mtb-lab edits | Wash host cells in 7H9 + glycerol + ADC without Tween; 10-cm 7H10 plates; titer by spotting. |
| Phage stock | *M. smegmatis*-optimized | LB plates throughout; host washed in MP buffer; use within 3 days; fresh stock per transduction. |
| Transduction | Mtb-style (Murry/Rego) | ~100 mL culture at OD 0.6–1.0; ~2×10¹¹ phage; 37 °C overnight; 7H10 + Tween + Kan; ~3 weeks. |
| Transduction | *M. smegmatis*-optimized | 50–200 mL culture at OD 2–3; ~1×10¹¹ phage per OD unit; 4 h at 37 °C; LB + Kan + Tween; 3 days. |
| Transduction | Benchling (Fortune lab, 2022) | BSL3 Mtb: OD 1.0–1.5; ~18 h unshaken at 37 °C; optional PBS-Tween wash; ~21 days. |
| DNA shearing | Acoustic (Covaris) | Several parameter sets; see variant table on the library-prep page. |
| DNA shearing | Enzymatic (NEBNext Ultra II FS) | 500 ng input; 15–30 min at 37 °C; no instrument needed. |
| Junction PCR | KAPA HiFi or HotStart vs Q5 | Different polymerase, cycles and annealing temperature. |
| Size selection | E-gel, PippinPrep, AMPure beads, agarose gel | Same goal (~300–400 bp); different tradeoffs. |

## Analysis and published sources

- Transit and TPP documentation: <https://transit.readthedocs.io/en/latest/tpp.html>
- Murry J, Sassetti CM, Moreira J, Lane J, Rubin EJ. Transposon site hybridization in *Mycobacterium tuberculosis*. *Methods Mol Biol* 2008;416:45–59.
- Long JE, DeJesus M, Ward D, Baker RE, Ioerger T, Sassetti CM. Identifying essential genes in *Mycobacterium tuberculosis* by global phenotypic profiling. *Methods Mol Biol* 2015;1279:79–95.
- DeJesus MA, Ambadipudi C, Baker R, Sassetti C, Ioerger TR. TRANSIT: a software tool for Himar1 TnSeq analysis. *PLoS Comput Biol* 2015;11:e1004401.

[A published article on Tn-seq in *M. smegmatis* and *M. tuberculosis* was also received (library-delivered PDF without a visible citation). Add its reference here once identified.]{.tbc}
