title: Pseudomonas aeruginosa quick-start (strains, PA14 library, genetics)
category: Organism quick-starts
tags: P. aeruginosa, Pseudomonas, PA14, transposon library, quick-start
summary: Orientation for P. aeruginosa work: biosafety, common strains, the PA14 non-redundant transposon library and its caveats, and what to check before starting genetics.
source: Liberati et al. 2006 (PA14 library) and the PA14 resource site; other statements are general knowledge and highlighted. Summary of published methods; not yet run in this lab.
version: Version 0.1
status: study
---
## About this page

This page is an orientation for working with *Pseudomonas aeruginosa*. It has not yet been run in this lab, so follow a published protocol for your strain. Highlighted text has not been checked against a source.

## Biosafety

[*P. aeruginosa* is normally handled at biosafety level 2. Check your institution's rules and the risk assessment for your strain.]{.tbc}

## Common strains

- **PA14** is a clinical isolate from a burn patient that is pathogenic in several model hosts and in mice (PA14 resource site).
- [**PAO1** is the other widely used reference strain. The two differ in genome content and virulence, so state which one you used and do not assume results transfer.]{.tbc}

## The PA14 non-redundant transposon library

- The PA14NR set contains **5,459** mutants (version 1.0), drawn from a parental library of 38,976 mutants, and covers **4,596** predicted PA14 genes, about 77% of the 5,962 predicted (Liberati et al. 2006).
- The main transposon is MAR2xT7, a *mariner*-family derivative of *Himar1*. Those mutants were selected on gentamicin (15 µg/mL). Some mutants carry TnphoA instead, selected on neomycin and maintained on kanamycin (Liberati et al. 2006).
- **Caveats** (Liberati et al. 2006):
    - Coverage is incomplete, with insertion-site hot spots and some genes not targeted.
    - The list of 335 candidate essential genes may include non-essential genes.
    - Insertions near the 5′ end of a gene can give functional fusion proteins, and insertions can affect downstream genes.
    - About 2.8% of mutants are expected to be mislabeled. In a test of 109 mutants, 106 had the expected insertion.
    - Small colony variants arose under static growth, so culture conditions were adjusted.
- **Good practice:** verify the insertion by PCR before relying on a mutant, and complement it. See also [Tn-seq data analysis](tn-seq-data-analysis.html) for pooled screens with *mariner*-type transposons.

## Culture and genetics

1. [Grow on LB at 37 °C. *P. aeruginosa* grows quickly and is often recognized by its smell and by green pigment.]{.tbc}
2. [*P. aeruginosa* is intrinsically resistant to many antibiotics, so antibiotic concentrations used for *E. coli* will not necessarily work. Check published concentrations for your strain and marker.]{.tbc}
3. [Gene deletions are commonly made by conjugation from an *E. coli* donor with a suicide plasmid and *sacB* sucrose counter-selection. Use a published protocol for your strain.]{.tbc} The [bi-parental conjugation page](bi-parental-conjugation.html) is a model for the donor/counter-selection design only, since it was written for a different recipient.

## Sources

- Liberati NT, Urbach JM, Miyata S, et al. 2006. An ordered, nonredundant library of *Pseudomonas aeruginosa* strain PA14 transposon insertion mutants. *Proc Natl Acad Sci USA* 103:2833–2838. [PMC1413827](https://pmc.ncbi.nlm.nih.gov/articles/PMC1413827)
- [PA14 resource site](https://pa14.mgh.harvard.edu/cgi-bin/pa14/home.cgi) (Massachusetts General Hospital and Harvard Medical School).
