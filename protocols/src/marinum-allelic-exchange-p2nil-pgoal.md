title: Gene knockouts in Mycobacterium marinum with p2NIL / pGOAL
category: Mycobacterial genetics
tags: M. marinum, knockout, allelic exchange, p2NIL, pGOAL, electroporation
summary: Build a p2NIL–pGOAL suicide construct in E. coli, transform M. marinum (with UV-treated DNA), and select single and double crossovers using kanamycin, X-gal and sucrose.
source: Written by K. Tembiwa from a lab protocol, with context from advice from an experienced *M. marinum* laboratory and from Talaat & Trucksis, Am J Vet Res (2000). The p2NIL/pGOAL system is from Parish & Stoker. Please check these references before relying on them.
version: Draft 0.1
---
Handle *M. marinum* at the biosafety level required by your institution.

## 1. Clone the flanks into p2NIL

1. Combine 0.5 µL DpnI-treated p2NIL vector, 0.5 µL PCR upstream flank and 0.5 µL PCR downstream flank. Add 50 µL DH5α competent cells, keep on ice at least 30 min.
2. Heat shock 45 s at 42 °C; add 200 µL LB; 1 h at 37 °C. Spin 1 min, resuspend, plate on LB + kanamycin (p2NIL is KanR).
3. Pick 4–8 colonies into 5 mL LB + kanamycin overnight. Miniprep.
4. Diagnostic digest (10 µL: 1 µL 10× buffer, 2 µL DNA, 0.5 µL enzyme, 6.5 µL water; 1 h at 37 °C) with an enzyme that gives at least two bands. Check on a gel.

## 2. Add the pGOAL cassette (PacI)

1. Digest p2NIL clone with PacI (same 10 µL recipe). Dephosphorylate with Antarctic phosphatase (1.5 µL buffer, 1 µL enzyme; 37 °C 30 min; 80 °C 2 min).
2. "Cut/kill" empty pGOAL with PacI (37 °C 60 min, 65 °C 20 min, hold 25 °C).
3. Ligate: 1 µL p2NIL, 0.5 µL water, 0.5 µL ligase buffer, 2.5 µL digested pGOAL, 0.5 µL ligase; overnight at 4 °C.
4. Transform the whole ligation into 50 µL DH5α. Plate on LB + kanamycin + X-gal (to add X-gal to existing plates: warm, add beads and ~100 µL LB, 20 µL X-gal, shake, soak in at 37 °C).
5. Pick **blue** colonies (pGOAL carries *lacZ*), grow in LB + kanamycin, miniprep.
6. Check with AflII + PacI: three bands expected (two near 5 and 7 kb, one near 2 kb; use your construct map for exact sizes).

## 3. Transform *M. marinum*

1. Use **~3 µg** DNA for p2NIL/pGOAL constructs (UV-treat the DNA) and ~0.5 µg for complementation plasmids (no UV). *M. marinum* needs more DNA than *M. tuberculosis*; about 1 µg is the minimum for success.
2. Spin 500 µL competent cells (13,000 rpm, 2 min). Wash three times with glycerol buffer (80 mL water, 20 mL 50% glycerol, 500 µL 20% Tween 80). Resuspend in 500 µL, add DNA, electroporate, and immediately add to 2 mL 7H9.
3. Recover at 32 °C. Plate the next day on KO plates (7H11 + X-gal + kanamycin + OADC) (complementation constructs on 7H11 + hygromycin as appropriate).
4. Pick **blue** colonies (single crossover); grow in 3 mL 7H9.
5. Dilute 1:20 (10 µL + 190 µL 7H9) and plate 200 µL on sucrose plates (7H11 + X-gal + sucrose + OADC).
6. Pick **white** colonies (double crossover), grow in 7H9, and confirm the knockout by PCR with confirmation primers.

Advice from experienced *M. marinum* labs: p2NIL and pGOAL are obtained from Addgene (under a material transfer agreement). The **UV treatment of the DNA is critical**. Without it *M. marinum* integrates the plasmid at the wrong site, probably because of strong mismatch repair compared with *M. tuberculosis*. The glycine step in preparing competent cells improves transformation.

## Competent cell preparation

1. Grow a colony in 5 mL 7H9 for 3–5 days; expand to 25 mL for 24–48 h.
2. Add 2 mL 2 M glycine; grow 24 h.
3. Spin the whole culture 4,000 rpm, 5 min. Wash three times with the glycerol buffer above.
4. Resuspend in 5 mL buffer; freeze 500 µL aliquots at –80 °C.

Keep wild-type stocks low-passage; avoid unnecessary passaging (the strain can lose haemolytic activity).

[Temperatures (32 °C vs 30 °C), UV dose and plate recipes should be checked against the original protocol.]{.tbc}
