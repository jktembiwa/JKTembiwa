title: Mycobacterial protein fragment complementation (M-PFC, DHFR two-hybrid)
category: Protein biochemistry
tags: two-hybrid, M-PFC, DHFR, trimethoprim, protein-protein interaction, M. smegmatis
summary: Test pairwise or library-scale protein–protein interactions in M. smegmatis by reconstituting dihydrofolate reductase and selecting on trimethoprim.
source: Summarized from the M-PFC protocol and procedures document from the Steyn laboratory, and Singh A, Mai D, Kumar A, Steyn AJ. Dissecting virulence pathways of Mycobacterium tuberculosis through protein-protein association. Proc Natl Acad Sci USA 103:11346–11351 (2006). Please read the original paper for the authoritative method.
version: Draft 0.1
---
M-PFC is not a magic bullet; it may fail for a given pair of proteins. Host strain: *M. smegmatis* mc²155.

## Vectors

| Vector | Type | Marker | Contents |
|---|---|---|---|
| pUAB100 | episomal | Hyg | GCN4 homodimerization domain fused to the N-terminus of mDHFR fragment F[1,2] with a glycine linker; insert by replacing GCN4 (MscI/ClaI or BamHI/ClaI) |
| pUAB200 | integrative | Kan | GCN4 fused to mDHFR fragment F[3]; replace GCN4 with MunI/ClaI |
| pUAB300 | episomal | Hyg | mDHFR F[1,2] for in-frame fusion at its C-terminus, multiple cloning sites (preferred for libraries) |
| pUAB400 | integrative | Kan | mDHFR F[3] for in-frame fusion at its C-terminus |

Clone gene A in pUAB100 or pUAB300 and gene B in pUAB200 or pUAB400, in frame with the complementary DHFR fragment. Verify by sequencing.

## Assay

1. Prepare competent *M. smegmatis* and check efficiency (10⁴–10⁵ transformants/µg). Electroporate both constructs.
2. Recover 3 h at 37 °C in 1 mL 7H9. Plate the whole mix on 7H11 + Kan + Hyg. Incubate 3 days at 37 °C.
3. Subculture transformants on 7H11 + Kan + Hyg + **trimethoprim (30–50 µg/mL)**. Alternatively suspend a few colonies in 100 µL PBS and streak 10 µL. Incubate 4–5 days at 37 °C.
4. **Growth on trimethoprim indicates interaction.** Stronger interactions grow earlier.
5. Controls: pUAB100 + pUAB200 (GCN4 domains, strong interaction) as the positive control; any one of the clones with an unrelated partner as the negative control.

## Notes from the protocol

- Use 7H11, **not** 7H10 or 7H9 + agar. Do not change the Kan, Hyg or trimethoprim concentrations.
- For membrane proteins, use pUAB100 and pUAB200 and make sure the DHFR fragments sit in the cytoplasm.
- Some proteins need a free N- or C-terminus; test parallel and antiparallel orientations.
- Interaction strength can be measured with the Alamar Blue assay (Singh et al. 2006).
- Make fresh trimethoprim for plates; do not store trimethoprim plates long at 4 °C.

## Library screening (summary)

An *M. tuberculosis* H37Rv library (partial AciI/HpaI digests, 0.5–2 kb, cloned in pUAB300; about 5 × 10⁵ independent clones with more than 90% cloning efficiency) is transformed into *M. smegmatis* carrying the bait (in pUAB200 or pUAB400). A semi-exhaustive screen needs about 30–60 electroporations (400 µL cells and 2–5 µg DNA each), plated on 7H11 + Kan + Hyg + trimethoprim (30 µg/mL), 4–8 days at 37 °C. Many trimethoprim-resistant colonies carry the *M. tuberculosis dfrA* gene (Rv2763c) itself; remove them by colony PCR with insert-flanking and *dfrA* primers. Identify real positives by colony PCR and sequencing, and re-test with an unrelated control.

See also the [DHFR two-hybrid cloning plan](dhfr-two-hybrid-and-ip-turapov.html).
