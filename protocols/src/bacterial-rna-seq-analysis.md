title: Bacterial RNA-seq analysis (reads to differential expression)
category: Computational analysis
tags: RNA-seq, differential expression, DESeq2, transcriptomics, analysis
summary: An outline of a bacterial RNA-seq workflow, from experimental design and quality control through mapping, counting and differential expression, with what the best-practice survey recommends.
source: Conesa et al. 2016 (survey of RNA-seq best practices); Love et al. 2014 (DESeq2). Summary of published guidance; not yet run in this lab.
version: Version 0.1
status: study
---
## About this page

This page outlines a typical analysis workflow for bacterial RNA-seq. It has not yet been run in this lab, so treat it as orientation and follow each tool's documentation. The general recommendations come from the Conesa et al. (2016) survey, which is written mostly around eukaryotic data, so highlighted text marks bacteria-specific points and tool settings that have not been checked against a source.

## Experimental design

- **Biological replicates:** the survey recommends a minimum of three when sample availability allows. Without biological replication, p-values are not valid and results are exploratory only (Conesa et al. 2016).
- **rRNA depletion:** bacterial mRNA lacks a poly(A) tail, so poly(A) selection does not work. The survey names ribosomal depletion as the option when poly(A) selection is not feasible (Conesa et al. 2016).
- **Strand-specific libraries:** the survey recommends strand-preserving protocols such as dUTP, which keep the information needed to analyse antisense and overlapping transcripts (Conesa et al. 2016). [This matters in bacteria, where genes overlap and antisense RNAs are common.]{.tbc}
- **Reads:** single-end reads are usually enough for gene-level expression in well-annotated organisms (Conesa et al. 2016).

## Workflow

1. **Check raw reads.** Run FastQC (or NGSQC) and check quality, GC content, adapters, k-mers and duplicates. Discard outliers and check that metrics are consistent across samples (Conesa et al. 2016).
2. **Trim.** Remove adapters and low-quality bases with Trimmomatic or FASTX-Toolkit (Conesa et al. 2016).
3. **Map** to the reference genome. [Bacterial transcripts are not spliced, so a non-splice-aware aligner such as Bowtie2 is typically used.]{.tbc}
4. **Check the alignment** for coverage uniformity, 3′ bias and strand (Conesa et al. 2016 name Picard, RSeQC and Qualimap).
5. **Count reads per gene** with featureCounts or HTSeq-count (Conesa et al. 2016), using an annotation file that matches your reference genome. [Check the strand setting so reads are assigned to the correct strand.]{.tbc}
6. **Normalize and test for differential expression** with a count-based tool. The survey recommends normalization methods robust to skewed distributions (TMM, DESeq) and lists edgeR and DESeq2 among the differential-expression tools (Conesa et al. 2016; DESeq2: Love et al. 2014).
7. **Look at the data before interpreting:** [a PCA or sample-distance plot to check that replicates cluster together and to spot batch effects.]{.tbc}
8. **Functional analysis.** The survey notes that GOseq corrects for gene-length bias in enrichment tests and that GSEA is an alternative (Conesa et al. 2016). [For bacteria, use annotation categories such as COG, KEGG or GO from your genome annotation.]{.tbc}
9. **Record** software versions and settings. The survey notes that method choice and software version can change results, and suggests repeating key analyses with more than one package (Conesa et al. 2016).

## Confirming results

[Confirm a handful of changes by RT-qPCR on independent biological samples.]{.tbc} See [qPCR design and ΔΔCt analysis](qpcr-design-and-analysis.html).

## Sources

- Conesa A, Madrigal P, Tarazona S, et al. 2016. A survey of best practices for RNA-seq data analysis. *Genome Biol* 17:13. [doi:10.1186/s13059-016-0881-8](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-016-0881-8)
- Love MI, Huber W, Anders S. 2014. Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2. *Genome Biol* 15:550.
