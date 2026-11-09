title: Flow cytometry of host cells and infections
category: Flow cytometry
tags: flow cytometry, host cells, macrophages, infection, gating, panel design, quick-start
summary: Study notes on analyzing infected host cells by flow cytometry: panel and control design, a typical gating order, how to separate intracellular from extracellular bacteria, and what flow cannot tell you.
source: Study notes compiled from published guidance: Cossarizza et al. 2021 (flow cytometry guidelines), Flannagan and Heinrichs 2018, and Lee et al. 2008 (MIFlowCyt). Not yet run by the author.
version: Version 0.1
status: study
---
## About this page

This page summarizes published guidance for analyzing infected host cells by flow cytometry. It has not yet been run in this lab, so treat it as orientation. The authoritative reference for panel design and controls is the consensus guideline paper (Cossarizza et al. 2021). Highlighted text is standard practice that has not been checked against a source.

## What flow can and cannot tell you in an infection

**Can:** the fraction of host cells that carry bacteria, per-cell reporter or probe intensity, and host phenotype (surface or intracellular markers) in infected versus uninfected cells.

**Cannot (reliably): intracellular replication.** Flannagan and Heinrichs (2018) report that attempts to assess bacterial proliferation by flow cytometry failed: a macrophage can hold several phagosomes, and bacteria may replicate in only one of them, so a cell with any signal is simply scored as positive and sorting by GFP intensity can overstate replication. They used fluorescence microscopy of individual cells instead. Their microscopy assay used GFP-expressing *S. aureus* USA300 labelled with a proliferation dye, a multiplicity of infection of 10, time points at 1.5 h and 12 h, and gentamicin (100 µg/mL for 1 h after a 30 min infection) to remove extracellular bacteria.

## Panel and control design

- **Controls for every run:** unstained cells; single-stain compensation controls (cells or beads) for each fluorochrome; and [fluorescence-minus-one (FMO) controls to set gates for any marker that does not give a clean positive/negative split]{.tbc}.
- [**Titrate** every antibody on the cell type you will use, rather than relying on the datasheet amount.]{.tbc}
- [Use a **viability dye** compatible with fixation if you will fix, and exclude dead cells, which stick to antibodies non-specifically.]{.tbc}
- [Block Fc receptors before staining mouse or human immune cells.]{.tbc}
- [Match fluorochrome brightness to antigen abundance, put bright dyes on low-abundance markers, and avoid combining dyes with heavy spectral overlap.]{.tbc}
- [Keep one **reference sample** that you stain every time, so you can spot drift between days.]{.tbc}

## A typical gating order

1. [Cells (FSC-A vs SSC-A), to exclude debris.]{.tbc}
2. [Single cells (FSC-H vs FSC-A), to exclude doublets.]{.tbc}
3. [Live cells (viability dye negative).]{.tbc}
4. [Cell type (lineage markers, for example a macrophage marker).]{.tbc}
5. [Infected cells (bacterial reporter positive), compared with an uninfected control sample and with cells infected with non-fluorescent bacteria.]{.tbc}

Set gates on the controls and apply the same gates to every sample in the experiment.

## Separating intracellular from extracellular bacteria

- Kill extracellular bacteria with an antibiotic that does not enter host cells. Flannagan and Heinrichs used gentamicin. [Lysostaphin is a common alternative for *S. aureus*.]{.tbc}
- [Alternatively, stain extracellular bacteria with an antibody against a surface antigen *before* permeabilization, so only the unstained, reporter-positive fraction is intracellular.]{.tbc}
- [pH-sensitive dyes (for example pHrodo) can mark bacteria that have reached the acidic phagolysosome.]{.tbc}
- *S. aureus* caution: [protein A binds the Fc region of antibodies, so use Fc-independent reagents or proper isotype and no-primary controls]{.tbc} (see the [*S. aureus* quick-start](staphylococcus-aureus-quick-start.html)).

## Fixation and safety

[Fix infected cells (for example with paraformaldehyde) before they go on a shared cytometer, check that the fixation protocol inactivates your pathogen, and follow your institution's biosafety rules and your core facility's policy for pathogens.]{.tbc} Fixation can reduce some fluorescent-protein signals and affect some epitopes, so test it on your reporter and antibodies first.

## Reporting

Record the instrument, configuration, panel, controls and gating, and keep the raw FCS files. MIFlowCyt lists the minimum information to report (Lee et al. 2008). For bacteria on their own, see [flow cytometry of bacteria](flow-cytometry-bacteria.html).

## Sources

- Cossarizza A, Chang HD, Radbruch A, et al. 2021. Guidelines for the use of flow cytometry and cell sorting in immunological studies (third edition). *Eur J Immunol* 51:2708–3145. [Open-access copy](https://eprints.whiterose.ac.uk/id/eprint/184275/)
- Flannagan RS, Heinrichs DE. 2018. A fluorescence based-proliferation assay for the identification of replicating bacteria within host cells. *Front Microbiol* 9:3084. [doi:10.3389/fmicb.2018.03084](https://doi.org/10.3389/fmicb.2018.03084)
- Lee JA, Spidlen J, Boyce K, et al. 2008. MIFlowCyt: the minimum information about a flow cytometry experiment. *Cytometry A* 73:926–930. [PubMed 18752282](https://pubmed.ncbi.nlm.nih.gov/18752282/)
