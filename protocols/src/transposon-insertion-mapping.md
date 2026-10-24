title: Mapping a single transposon insertion (SacII digest, ligation, pir+ E. coli)
category: Mycobacterial genetics
tags: Tn-seq, transposon mutant, insertion mapping, cloning
summary: Recover the transposon–genome junction from one mutant by digesting gDNA, self-ligating, transforming into a pir+ E. coli strain and sequencing out of the transposon.
source: Protocol from the Rego lab, itself adapted from an earlier lab protocol (Mike Chao); received through the Boutte lab. Condensed by K. Tembiwa.
version: Draft 0.1
---
For an individual mutant from a φMycoMarT7 library (see the [Tn-seq overview](tn-seq-overview.html)). The idea is that a SacII-cut, re-ligated fragment containing the transposon can replicate as a plasmid in a *pir*+ host and carry the flanking genomic sequence with it. [Presumably the transposon carries an R6K origin and kanamycin marker; confirm against the phMycoMarT7 map.]{.tbc}

1. Prepare genomic DNA with a quick prep that includes RNase (so the A₂₆₀ reading reflects DNA; see [Smash and Grab](smash-and-grab-genomic-dna.html) or the [long gDNA prep](msmeg-gdna-prep-long.html)).
2. Digest **2 µg** gDNA with 3 µL SacII in 1× CutSmart buffer (3 µL), water to 30 µL, overnight at 37 °C.
3. Heat-inactivate 20 min at 65 °C.
4. Add 4 µL T4 DNA ligase buffer and 2 µL T4 DNA ligase; incubate overnight at 16 °C.
5. Heat-inactivate 20 min at 65 °C.
6. Reduce the volume to ~15 µL (speed-vac) and dialyze the DNA for 30 min.
7. Electroporate into freshly made electrocompetent *pir*+ *E. coli* (BW25142; see [E. coli electrocompetent cells](ecoli-electrocompetent-cells.html)).
8. Pick colonies, grow in LB + kanamycin 50 µg/mL, miniprep.
9. Sequence with the transposon primer that reads out of the transposon into the genome: 5′-GTCTAGAGACCGGGGACTTATC-3′ (the same transposon primer used for [Tn-seq library PCR 1](tn-seq-library-prep.html)).

Align the resulting sequence to the genome to find the insertion site.
