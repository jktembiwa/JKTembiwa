title: ORBIT: oligo recombineering followed by Bxb1 integrase targeting
category: Mycobacterial genetics
tags: ORBIT, recombineering, Bxb1, integrase, gene tagging, mycobacteria
summary: Insert a payload plasmid at a chromosomal target using a 188 nt oligo carrying a Bxb1 attP site, in cells expressing recombinase and Bxb1 integrase.
source: ORBIT method (see Murphy et al., mBio 2018); lab adaptation, shared with the Boutte lab and adapted for this site.
version: Draft 0.1
---
## Overview

An oligo containing the Bxb1 attP site flanked by 70 bases of target sequence is recombined into the chromosome, and a payload plasmid is then integrated at the attP site by Bxb1 integrase. [Organism: the conditions (37 °C, 3 days) suggest *M. smegmatis*; confirm.]{.tbc}

## Steps

1. **Design and order the oligo.** Include the Bxb1 attP site (`GGTTTGTCTGGTCAACCACCGCGGTCTCAGTGGTGTACGGTACAAACC`, 48 nt) flanked by 70 bases of target sequence on each side. For a C-terminal tag, insert attP between the last codon and the stop codon: copy the sequence from 70 bases upstream of the insertion point to 70 bases downstream. Decide whether the oligo is the top strand or its reverse complement ([see the oligo-directionality guidance for ORBIT]{.tbc}). Order the 188 nt oligo as an Ultramer.
2. **Prepare the payload vector.** Miniprep the appropriate ORBIT vector.
3. **Grow the recipient strain.** The strain carrying the inducible recombinase and integrase plasmid is grown in 7H9 + kanamycin: 10 mL per transformation, grown to turbidity. The night before, do a calculated dilution so that the culture is at OD about 0.5 the next morning.
4. **Induce.** In the morning, measure the OD and adjust to 0.5. Induce the integrase with **500 ng/mL anhydrotetracycline (aTc)** and shake or roll for 3 hours.
5. **Make competent cells.** Wash the induced cells three times in ice-cold 10% glycerol. Cool the centrifuge, pellet the cells at 4000 rpm for 5 min, resuspend in 10 mL cold 10% glycerol, repeat twice, then pellet once more and resuspend in 500 µL cold 10% glycerol for a single transformation.
6. **Prepare cuvettes** while spinning. For one transformation you need two cuvettes, the transformation and a control with no oligo.
    - Control: pipette 0.4 µg of the ORBIT vector onto the side of the cuvette.
    - Transformation: pipette 0.4 µg of ORBIT vector and 1 µg of oligo.
7. Pipette 250 µL of the washed competent cells into each cuvette and tap to remove bubbles.
8. **Electroporate** at 2500 V, 1000 Ω, 25 µF after drying each cuvette. The time constant should be about 20 ms.
9. Transfer the cells into labeled tubes with 1 mL 7H9, tape them to a roller and roll at 37 °C for 3 hours.
10. Have at least two LB + hygromycin 50 µg/mL plates ready.
11. Spin the tubes for 1 min at maximum speed. Resuspend in 150 µL 7H9. Put beads on the plates, add the 150 µL of cells and spread.
12. Incubate at 37 °C for 3 days.
13. **PCR check** each junction: for the left flank, use an *oriE* reverse primer with a target-specific forward primer; for the right flank, use a hygromycin-cassette forward primer with a target-specific reverse primer.

## Which strand to order (oligo directionality)

Which strand you order depends on both the **position** and the **direction** of the gene on the chromosome. [The underlying reason (annealing to the lagging-strand template) is general knowledge, not from the source note; confirm.]{.tbc}

- Take the gene sequence in the 5′→3′ coding orientation (the "top" strand in a sequence file; databases such as Tuberculist always give the gene reading 5′→3′ regardless of orientation on the chromosome). Its reverse complement is the "bottom" strand.
- Insert the attP site into the sequence **before** choosing the strand (not critical for deletions, critical for fusions).
- Find the replicore:
  - *M. smegmatis*: right replicore ~0–3.4 Mb, left replicore ~3.5–6.9 Mb (the note gives 0–3.3 and 3.3–6.4 Mb in places; confirm)
  - *M. tuberculosis*: right replicore 0–2.2 Mb, left replicore 2.3–4.4 Mb
- **Rule of thumb:** if the gene reads **toward the origin**, order the sequence as it appears in your file (top strand). If it reads **away from the origin**, order the **reverse complement**.

| Replicore | Gene reads | Order |
|---|---|---|
| Right | toward origin (counterclockwise) | top strand (as in file) |
| Right | away from origin (clockwise) | reverse complement |
| Left | away from origin (counterclockwise) | reverse complement |
| Left | toward origin (clockwise) | top strand (as in file) |

[Source and author of this directionality note are not recorded in the file; add credit if known. Replicore boundaries differ between the paragraphs in the original.]{.tbc}
