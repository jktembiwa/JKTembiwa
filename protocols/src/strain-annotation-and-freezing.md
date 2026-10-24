title: Strain annotation and freezing down strains
category: Reference
tags: strains, nomenclature, annotation, glycerol stocks, reference
summary: A consistent way to name genetically modified strains, and how to make freezer stocks.
source: Adapted by K. Tembiwa from the Boutte Lab Beginner's Manual (v2.0, 2021).
version: Draft 0.1
---
## Naming strains

Write the background strain first, then the modifications in the order they would appear in the genotype.

| Symbol | Meaning |
|---|---|
| *gene*K122P | A point mutation: gene name, then the amino-acid change (lysine 122 to proline). |
| Δ | A deletion. |
| :: | An insertion into the chromosome, written site::insert. |
| / | An episomal vector; name the vector after the slash. |

For a non-coding mutation, give it a mutant number and list that number after the strain name, then describe the mutation elsewhere (for example in your strain database).

**Examples**

1. Deletion by recombineering: mc²155 Δ*phoP*::zeoR means *phoP* is deleted and a zeocin-resistance cassette sits at the locus. If the cassette is later removed by Cre: mc²155 Δ*phoP*::loxP.
2. A tag added by recombineering: H37Rv *phoP*::FLAG-zeoR.
3. An integrating vector: H37Rv L5::pKK216-*phoP*-FLAG means that vector is integrated at the L5 site. Vectors can be named for the person who made them or by a descriptive code. pKK216 was made by Karen Kieser and here was modified to add a C-terminal FLAG tag to *phoP*.
4. An episomal vector: mc²155 / pUV15tetOR-*phoP*. The name carries information: a UV15 promoter plus tet operator and repressor.

A strain with several modifications lists them in order, for example: mc²155 *phoP*K133P Δ*phoR*::hygR L5::pKK216-FLAG-*phoR* / pUV15tetOR-MSMEG_3717.

## Freezing down a strain

1. Record the properly annotated strain in your lab strain list.
2. In a 2 mL cryovial, mix 1 mL culture with 1 mL 50% glycerol.
3. Store at −80 °C and record the box and position.
