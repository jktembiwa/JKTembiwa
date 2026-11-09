title: Escherichia coli quick-start (strains, deletion collections, λ Red)
category: Organism quick-starts
tags: E. coli, Keio, lambda Red, gene deletion, recombineering, quick-start
summary: Orientation for E. coli genetics: the Keio deletion collection and its caveats, and the one-step λ Red method for making your own deletions.
source: Baba et al. 2006 (Keio collection); Datsenko and Wanner 2000 (λ Red); the Keio Collection summary. Summary of published methods; not yet run in this lab.
version: Version 0.1
status: study
---
## About this page

This page summarizes the Keio collection and the Datsenko–Wanner deletion method for *E. coli* K-12. It has not yet been run in this lab, so follow the original papers for exact conditions. Highlighted text has not been checked against a source. Routine procedures are on other pages: [chemical transformation](ecoli-chemical-transformation.html), [electrocompetent cells](ecoli-electrocompetent-cells.html), [recombineering](recombineering.html), [colony PCR](colony-pcr-screening.html) and [antibiotic plates](antibiotic-plates.html).

## Biosafety

[Laboratory K-12 strains are normally handled at biosafety level 1. Pathogenic *E. coli* (for example enterohaemorrhagic strains) are not, so check the risk assessment.]{.tbc}

## The Keio collection

- Single-gene in-frame deletions in *E. coli* K-12 strain **BW25113**: 3,985 non-essential gene deletion mutants, from 4,288 genes targeted. About 299 open reading frames were identified as likely essential (Baba et al. 2006; Keio Collection summary).
- Each gene was replaced with a kanamycin-resistance cassette by the λ Red method (Keio Collection summary), so mutants are selected on kanamycin. [The cassette is flanked by FRT sites and can be removed with FLP recombinase.]{.tbc}
- **Caveats** (Keio Collection summary):
    - Spontaneous mutations, including frameshifts, can arise in a stock and be wrongly attributed to the deleted gene.
    - Deletions can have polar effects on downstream genes in the same operon.
    - Phenotypes can depend on growth conditions.
    - A later check found 37 strains incorrect because of gene duplications.
- **Good practice:** [verify the deletion by colony PCR, and move it into a clean background by P1 transduction before drawing conclusions. Complement with the gene on a plasmid.]{.tbc}

## One-step deletion with λ Red (Datsenko and Wanner 2000)

The method replaces a chromosomal gene with a PCR-made resistance cassette flanked by short homology arms. It uses plasmids that are described in the paper: template plasmids carrying the resistance cassettes (pKD3 and pKD4), a λ Red helper plasmid (pKD46) and an FLP plasmid (pCP20).

1. [Make a PCR product from pKD3 or pKD4 using primers with about 40 nt of homology to the target at the 5′ ends.]{.tbc}
2. [Transform the strain carrying pKD46, which has a temperature-sensitive replicon and an arabinose-inducible λ Red. Grow at 30 °C with ampicillin and induce with L-arabinose before making cells electrocompetent.]{.tbc}
3. Electroporate the PCR product (see [electrocompetent cells](ecoli-electrocompetent-cells.html)) and select recombinants on the cassette's antibiotic.
4. [Confirm the deletion by colony PCR with primers outside the target.]{.tbc}
5. [To remove the cassette, transform with pCP20 (FLP recombinase, temperature-sensitive) and cure the plasmid by growing at a higher temperature.]{.tbc}

## Sources

- Baba T, Ara T, Hasegawa M, et al. 2006. Construction of *Escherichia coli* K-12 in-frame, single-gene knockout mutants: the Keio collection. *Mol Syst Biol* 2:2006.0008. [PMC1681482](https://pmc.ncbi.nlm.nih.gov/articles/PMC1681482)
- Datsenko KA, Wanner BL. 2000. One-step inactivation of chromosomal genes in *Escherichia coli* K-12 using PCR products. *Proc Natl Acad Sci USA* 97:6640–6645. [PubMed 10829079](https://pubmed.ncbi.nlm.nih.gov/10829079/)
- [Keio Collection (summary)](https://en.wikipedia.org/wiki/Keio_Collection).
