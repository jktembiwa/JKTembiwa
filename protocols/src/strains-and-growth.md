title: Strains and growth characteristics (E. coli and mycobacteria)
category: Reference
tags: strains, E. coli, M. smegmatis, BCG, M. tuberculosis, reference
summary: Quick reference to common E. coli cloning and expression strains and the mycobacterial strains used in cell-envelope work, with resistance markers and growth rates.
source: Adapted by K. Tembiwa from the Boutte Lab Beginner's Manual (v2.0, 2021).
version: Draft 0.1
---
Follow your institution's biosafety rules for every organism below, and work with BSL-2 mycobacteria (BCG and auxotrophic *M. tuberculosis*) in a biosafety cabinet.

## E. coli strains

| Strain | Use | Notes |
|---|---|---|
| XL1-Blue | General cloning | Tetracycline resistant. Carries the tet repressor, which can help when cloning toxic genes under a tet-inducible promoter. Usually used as homemade chemical competent cells. |
| DH5α | General cloning | No antibiotic resistance. Some constructs (for example, certain genes in pTetO vectors) are toxic here; XL1-Blue works better for those. |
| Mach1 | General cloning | No antibiotic resistance. Grows faster than typical *E. coli*: transformations plated mid-morning give small colonies by evening, and colonies picked in the morning can be miniprepped by mid-afternoon. |
| TOP10 | General cloning | Streptomycin resistant. Can be good for toxic genes. |
| BL21 (DE3) | Recombinant protein expression | Chloramphenicol resistant. The pLysS form is selected with chloramphenicol 20 µg/mL. The Codon Plus form has extra rare tRNAs (useful for non-*E. coli* proteins) and is selected with chloramphenicol 40 µg/mL. Used for GST- and MBP-tagged proteins. |
| BW25142 | Replicating oriR6K plasmids | DH5α background carrying *pir*. Supports more oriR6K plasmids than a *pir* DH5α strain. |

## M. smegmatis mc²155

- Selected for high transformation efficiency; carries a large chromosomal duplication.
- Grown in 7H9 + ADC; plated on LB or 7H10 + ADC.
- Wild type without antibiotic doubles about every 2.5 hours.

## M. bovis BCG

- Attenuated vaccine strain (BSL-2); lacks the ESX-1 locus among other changes.
- Grown in inkwells or roller bottles with tightly closed caps.
- 7H9 + ADC; plated on 7H10 + ADC. Doubles about every 18–20 hours.

## M. tuberculosis strains

Use 7H9 with **OADC** (not ADC) for broth and plates.

- **Leucine/pantothenate auxotroph:** deletion of both leucine and pantothenate synthesis genes; virulence loci likely intact (BSL-2, biosafety cabinet); hygromycin resistant; doubles about every 24 hours. Grow in 7H9 + OADC with 50 µg/mL leucine and 24 µg/mL pantothenic acid. Grown in inkwells or roller bottles with tight caps.
- **H37Rv:** the standard virulent laboratory strain; doubles about every 24 hours; handled only in a BSL-3 facility; prone to PDIM loss and attenuation in mouse infection. Other strains seen in the literature include Erdman, CDC1551 and Beijing strains.
