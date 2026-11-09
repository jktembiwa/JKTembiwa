title: Tn-seq data analysis (TPP and TRANSIT)
category: Computational analysis
tags: Tn-seq, TRANSIT, TPP, essentiality, Himar1, analysis
summary: From sequencing reads to insertion counts at TA sites, and the TRANSIT methods for calling essential genes and comparing conditions.
source: TRANSIT documentation and DeJesus et al. 2015. Summary of published tools; not yet run in this lab. Library construction and sequencing are covered on the linked Tn-seq pages.
version: Version 0.1
status: study
---
## About this page

This page summarizes the TRANSIT analysis software for *Himar1* Tn-seq data. It has not yet been run in this lab, so follow the TRANSIT documentation for the exact commands. Highlighted text has not been checked against a source. The library and sequencing steps are in the [Tn-seq overview](tn-seq-overview.html).

## What the data look like

*Himar1* inserts at TA dinucleotides. For *Himar1* libraries TRANSIT uses read counts at every TA site, and for Tn5 libraries it uses counts at every nucleotide (TRANSIT documentation).

## Workflow

1. **Map reads and count insertions** with the TRANSIT preprocessor (TPP), linked from the [overview](tn-seq-overview.html). [TPP also reports quality metrics for each library, which you should check before going further.]{.tbc}
2. **Prepare the inputs.** TRANSIT takes `.wig` files with counts for every possible insertion site, including sites with zero reads, and an annotation file (`.prot_table`) that matches the genome used for mapping (TRANSIT documentation).
3. **Normalize** the datasets. TRANSIT has a normalization method with its own tutorial. [Check the documentation for which method suits your libraries.]{.tbc}
4. **Call essential genes in a single condition** with one of two methods (TRANSIT documentation):
    - **Gumbel**, which finds stretches of TA sites without insertions.
    - **HMM**, which finds regions with locally suppressed or increased counts, including growth-defect and growth-advantaged regions.
5. **Compare two conditions** with **Resampling** (a permutation-style test) or the **Mann-Whitney U-test**. For several conditions use **ZINB** (zero-inflated negative binomial regression, which can include covariates) or **ANOVA** (TRANSIT documentation).
6. **Correct for multiple testing.** TRANSIT often converts p-values to q-values with the Benjamini–Hochberg correction, and a q-value below 0.05 is the typical threshold (TRANSIT documentation).
7. **Replicates.** TRANSIT supports replicates and most methods use them (TRANSIT documentation).

## Reading the results

- A gene with no insertions is *consistent with* being essential in that condition, not proof. [Short genes and genes with few TA sites can look essential by chance.]{.tbc}
- Follow up important hits with an individual mutant or a knockdown, as for any screen.

## Sources

- TRANSIT documentation. [Overview](https://transit.readthedocs.io/en/latest/transit_overview.html).
- DeJesus MA, Ambadipudi C, Baker R, Sassetti C, Ioerger TR. 2015. TRANSIT: a software tool for *Himar1* TnSeq analysis. *PLoS Comput Biol* 11:e1004401.
