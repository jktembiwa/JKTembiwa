title: CRISPRi gene silencing in mycobacteria (Sth1 dCas9): sgRNA design and cloning
category: Mycobacterial genetics
tags: CRISPRi, dCas9, sgRNA, gene silencing, knockdown, M. smegmatis, M. tuberculosis, Golden Gate
summary: How to design a PAM-based sgRNA, anneal and ligate oligos into a BsmBI-cut CRISPRi backbone, and extend to multiple sgRNAs by Golden Gate cloning.
source: Condensed from a shared protocol draft (v4, 3 March 2017) by Jeremy Rock; the method is published in Rock et al., Nature Microbiology (2017). Unpublished draft handout; cite the paper.
version: Version 1.0
---
**Background reading:** Qi et al., *Cell* 2013 (CRISPR as an RNA-guided platform for sequence-specific gene control). Rock et al., "Programmable transcriptional repression in mycobacteria using an orthogonal CRISPR interference platform," *Nature Microbiology* 2017 [(2:16274, doi:10.1038/nmicrobiol.2016.274)]{.tbc}.

## Overview

The system uses a catalytically inactive CRISPR1 Cas9 from *Streptococcus thermophilus* (**Sth1 dCas9**). To silence a gene you need Sth1 dCas9, an Sth1 sgRNA against the gene, and a suitably placed PAM.

- Silencing works when targeting either strand of the promoter, or the **non-template strand** of the 5′UTR and ORF. For the 5′UTR and ORF this means the PAM sits on the template strand; for the promoter the PAM can be on either strand.
- CRISPRi is **polar**: genes downstream in the same operon are silenced too. There is also recent evidence for a minor upstream polar effect (Peters et al., *Cell* 2016).

## Backbones

Backbones differ mainly in the level of Tet repressor expression, with small changes to the sgRNA and Cas9 promoters. The *M. smegmatis* backbone is **pLJR962** and the current optimum for *M. tuberculosis* is **pLJR965**. These may change over time. ATc (the TetR inhibitor) appears to act more strongly in *M. smegmatis* than in *M. tuberculosis*, so more TetR can be used in *M. smegmatis*; more TetR means less leaky expression, which matters when targeting essential genes.

## sgRNA design

Start with a gene in *M. smegmatis* to confirm that design and cloning work.

1. **Find PAMs** in the promoter, 5′UTR and ORF.
   - The published Sth1 consensus is **5′-NNAGAAW-3′**. The author tested more PAMs in vivo against a Renilla target with an identical sgRNA (a table, not reproduced here), and used 25-fold knockdown as an arbitrary cutoff. That raises the functional PAMs from 2 to 15 and gives roughly one targetable site every 50 bp of the H37Rv genome.
   - The strongest PAMs are the ones closest to the consensus. Weaker PAMs can still work well and can be used to **tune** knockdown.
   - Unlike published reports, the author sees **no bias** toward targeting near the 5′ end, so use the best PAM wherever it is in the promoter, 5′UTR or ORF.
2. **Extract about 20 nt** of targeting sequence, taking the first 20 nt 5′ of the PAM. Mycobacterial transcription starts most efficiently with A or G, so if the 20th nucleotide is not A or G, extend to 21 nt, and so on until it is.

## Cloning the sgRNA

1. **Prepare the backbone:** amplify the CRISPRi backbone in *E. coli* (kanamycin), digest with **BsmBI** (NEB), and gel purify. BsmBI is optimal at **55 °C in buffer 3.1**. Digest 2–5 µg of plasmid with 40 U for 4 h in a PCR block; overnight is fine. You cannot over-digest with BsmBI, and shorter, lower-enzyme digests led to un-cut backbone carry-through for other users.
2. **Design two oligos.** The forward oligo is the transcribed sgRNA sequence; the reverse oligo is its reverse complement. Add **5′-GGGA-3′ to the forward** oligo and **5′-AAAC-3′ to the reverse** oligo to regenerate the sgRNA promoter and dCas9 handle sequences.

   Example (*M. tuberculosis groEL1*):
   - `groEL1_F` 5′-GGGAGTCGGTAACGAAGTATGCCGA-3′
   - `groEL1_R` 5′-AAACTCGGCATACTTCGTTACCGAC-3′

   Positive control for *M. smegmatis* (*mmpL3*, Ms0250):
   - `mmpL3_F` 5′-GGGAGCGACAGACTGGCTGCCCTCGTC-3′
   - `mmpL3_R` 5′-AAACGACGAGGGCAGCCAGTCTGTCGC-3′

   Both control sgRNAs should be lethal with ATc in their respective species, so use them to check cloning and knockdown.
3. **Anneal oligos:** mix 4 µL of each oligo (100 µM in water) with 42 µL annealing buffer (50 mM Tris pH 7.5, 50 mM NaCl, 1 mM EDTA; 50 µL total) in an 8-strip PCR tube. Program: 95 °C for 2 min, ramp down at 0.1 °C/s to 25 °C, end.
4. **Ligate** (5 µL): 0.5 µL annealed oligos, ~9 ng digested and gel-purified backbone (typically ~0.25 µL), 0.5 µL T4 ligase buffer, 0.25 µL T4 DNA ligase (NEB, 2,000,000 U/mL), 3.5 µL water. Room temperature for 1–3 h, or overnight.
5. **Transform** 0.5 µL of the ligation into 5 µL of supercompetent *E. coli* and plate on LB + kanamycin. Expect 50–500 colonies.
6. **Miniprep one clone** per reaction (error-free cloning efficiency is >95% in the author's hands) and **sequence** with the backbone primer (source: primer 1834, 5′-TTCCTGTGAAGAGCCATTGATAATG-3′).

## Several sgRNAs from one plasmid

Backbones carry a **SapI-based Golden Gate site** 3′ of the first sgRNA scaffold. In principle it accepts 8 more sgRNA cassettes, for 9 sgRNAs on one plasmid. Reading: Engler and Marillonnet, *Methods Mol Biol* 2014.

1. Clone each individual sgRNA into the backbone.
2. PCR-amplify each [promoter–sgRNA–terminator] cassette with primers adding SapI sites and overhangs compatible with the Golden Gate handle.
3. Golden Gate: digest the parent sgRNA plasmid (with the first sgRNA at the usual site) and the PCR cassettes with SapI and ligate with T4 DNA ligase in one pot. If efficiency is poor, do the digests, gel purification and ligations as separate steps.
4. Sequence-confirm the insertions.

The author notes that multiplexing methods were still being optimized and that details would be added later.

See also [Recombineering](recombineering.html) and [ORBIT](orbit.html) for gene deletion and tagging approaches.
