title: Whole-genome sequencing analysis (assembly, annotation, variant calling)
category: Computational analysis
tags: WGS, genome assembly, variant calling, annotation, Unicycler, breseq
summary: A workflow for bacterial whole-genome data: check reads, assemble with Unicycler, annotate, and call mutations against a reference.
source: Wick et al. 2017 and the Unicycler documentation; Deatherage and Barrick 2014; Schwengers et al. 2021. Summary of published tools; not yet run in this lab.
version: Version 0.1
status: study
---
## About this page

This page outlines a typical analysis of bacterial whole-genome sequencing data. It has not yet been run in this lab, so follow each tool's documentation for the exact options. Highlighted text has not been checked against a source.

## Choose the question first

- **I need a new genome** (a clinical isolate, a new species): assemble the reads de novo.
- **I need to know how a mutant differs from its parent:** map the reads to a reference and call variants. A de novo assembly is not needed.

## De novo assembly

Unicycler is an assembly pipeline for bacterial genomes. It can assemble Illumina-only reads by optimizing a SPAdes assembly, assemble long reads (PacBio or Nanopore), or run a short-read-first hybrid assembly. It aims to produce complete, circularized replicons and an assembly graph that can be viewed in Bandage (Wick et al. 2017; Unicycler documentation).

1. [Check read quality with FastQC and trim adapters.]{.tbc}
2. Run Unicycler with the reads you have:
    - Short reads only: `unicycler -1 reads_1.fastq.gz -2 reads_2.fastq.gz -o output_dir`
    - Long reads only: `unicycler -l long_reads.fastq.gz -o output_dir`
    - Hybrid: `unicycler -1 reads_1.fastq.gz -2 reads_2.fastq.gz -l long_reads.fastq.gz -o output_dir`
3. Open the assembly graph in Bandage. A complete genome shows as circular contigs. Many small pieces suggest repeats that the reads could not span. The Unicycler author notes that long-read-first approaches are often preferable when long-read depth is high.
4. [Assess the assembly (QUAST for size and contiguity; CheckM for completeness and contamination) and compare the size with what you expect for the species.]{.tbc}

## Annotation

[Annotate the assembly with Bakta or Prokka to predict genes, rRNAs and tRNAs.]{.tbc} Bakta is described in Schwengers et al. 2021. [For a well-studied species, transfer the annotation from the closest reference genome and check the key genes by hand.]{.tbc}

## Calling mutations against a reference

1. Choose a reference that is as close as possible to the parent strain, ideally the parent's own genome.
2. Run breseq, which predicts mutations from short reads mapped to a reference (Deatherage and Barrick 2014). [Give it a GenBank-format reference so that mutations are reported with gene names.]{.tbc}
3. Read the output for single-nucleotide changes, small insertions and deletions, and new junctions (which indicate larger rearrangements or insertion sequences).
4. Compare mutant and parent. [Run the parent through the same pipeline, so that differences between the parent and the published reference are not mistaken for new mutations.]{.tbc}
5. **Confirm important variants by PCR and Sanger sequencing.** This is also the standard check after allelic exchange (see the [*S. aureus* quick-start](staphylococcus-aureus-quick-start.html)).

## Reporting

[Deposit raw reads in a public archive such as SRA and the assembly in GenBank, and record tool names, versions and settings.]{.tbc}

## Sources

- Wick RR, Judd LM, Gorrie CL, Holt KE. 2017. Unicycler: resolving bacterial genome assemblies from short and long sequencing reads. *PLoS Comput Biol* 13:e1005595. [PubMed 28594827](https://pubmed.ncbi.nlm.nih.gov/28594827/)
- Unicycler documentation: [github.com/rrwick/Unicycler](https://github.com/rrwick/Unicycler)
- Deatherage DE, Barrick JE. 2014. Identification of mutations in laboratory-evolved microbes from next-generation sequencing data using breseq. *Methods Mol Biol* 1151:165–188.
- Schwengers O, Jelonek L, Dieckmann MA, et al. 2021. Bakta: rapid and standardized annotation of bacterial genomes via alignment-free sequence identification. *Microb Genom* 7:000685.
