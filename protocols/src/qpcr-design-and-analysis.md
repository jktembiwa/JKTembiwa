title: qPCR design and ΔΔCt analysis
category: Computational analysis
tags: qPCR, RT-qPCR, ΔΔCt, gene expression, primer design, analysis
summary: How to design and validate qPCR primers, which controls to include, and how to turn Ct values into fold changes with the 2^-ΔΔCt method.
source: Livak and Schmittgen 2001 (2^-ΔΔCt method); Bustin et al. 2009 (MIQE guidelines). Summary of published methods; not yet run in this lab. For RNA preparation and the one-step reaction set-up see the linked protocol.
version: Version 0.1
status: study
---
## About this page

This page summarizes the published 2^-ΔΔCt method and the MIQE reporting guidelines. It has not yet been run in this lab, so follow the cited papers for the exact procedure. Highlighted text has not been checked against a source. For RNA extraction and the reaction set-up, see [RNA extraction and one-step RT-qPCR](rna-extraction-and-qpcr-msmeg.html).

## Primer design and validation

1. Design primers for a short amplicon. The 2^-ΔΔCt paper states the method applies to amplicons under 150 bp with optimized primer and Mg²⁺ concentrations (Livak and Schmittgen 2001).
2. [Check primer specificity against the genome (for example with Primer-BLAST) and avoid primer pairs that can form dimers or hairpins.]{.tbc}
3. For SYBR Green assays, [run a melt curve for every primer pair and look for a single peak.]{.tbc}
4. Run a **validation experiment** for each target/reference pair. Make serial dilutions of cDNA, plot log dilution against ΔCt (target minus reference), and check the slope. A slope close to zero means the two efficiencies are similar. If not, use absolute quantification with standard curves or redesign the primers (Livak and Schmittgen 2001).

## Controls

- **No-template control (NTC):** water instead of template, to detect primer-dimers and contamination.
- **No-RT control:** RNA processed without reverse transcriptase, to detect genomic DNA carry-over. For a one-step reaction, [omit the RT enzyme.]{.tbc}
- **Reference gene:** it must be validated so that the experimental treatment does not change its expression (Livak and Schmittgen 2001). [In bacteria, rRNA and housekeeping genes such as *sigA* are often used, but check that your condition does not change them.]{.tbc}
- **Technical replicates:** [at least three wells per sample and gene.]{.tbc}
- **Calibrator:** usually the untreated control. For a time course, use time zero (Livak and Schmittgen 2001).

## Calculating fold change (2^-ΔΔCt)

1. Average the technical-replicate Ct values for each sample and gene.
2. For each sample, calculate **ΔCt = Ct(target) − Ct(reference)**.
3. Choose the calibrator and calculate **ΔΔCt = ΔCt(sample) − ΔCt(calibrator)**.
4. Calculate **fold change = 2^(−ΔΔCt)**. The calibrator is 1 by definition.
5. For biological replicates, calculate ΔΔCt for each replicate first, then summarize. Report the range as 2^−(ΔΔCt ± s), where s is the standard deviation of the ΔCt values. The range is asymmetric because the Ct scale is logarithmic (Livak and Schmittgen 2001).
6. [Run statistics on the ΔCt values (which are approximately normally distributed) rather than on the fold changes.]{.tbc}

**Worked example (invented numbers).** Sample: target Ct 24.0, reference Ct 18.0, so ΔCt = 6.0. Calibrator: target Ct 26.0, reference Ct 18.0, so ΔCt = 8.0. ΔΔCt = 6.0 − 8.0 = −2.0, so fold change = 2² = 4 (four-fold higher than the calibrator).

The method assumes both amplicons amplify with efficiency close to 100% (a doubling per cycle). If efficiencies differ, [use an efficiency-corrected method such as the Pfaffl method.]{.tbc}

## Reporting

The MIQE guidelines list the minimum information to report for a qPCR experiment (Bustin et al. 2009), including how RNA quality was checked, the primer sequences and the validation data.

## Sources

- Livak KJ, Schmittgen TD. 2001. Analysis of relative gene expression data using real-time quantitative PCR and the 2^−ΔΔCT method. *Methods* 25:402–408. [PubMed 11846609](https://pubmed.ncbi.nlm.nih.gov/11846609/)
- Bustin SA, Benes V, Garson JA, et al. 2009. The MIQE guidelines: minimum information for publication of quantitative real-time PCR experiments. *Clin Chem* 55:611–622. [PubMed 19246619](https://pubmed.ncbi.nlm.nih.gov/19246619/)
