title: Oligo-mediated recombineering (point mutations in mycobacteria)
category: Mycobacterial genetics
tags: recombineering, oligo, point mutation, MAMA-PCR, rpsL, M. smegmatis, M. tuberculosis
summary: Make one or a few base-pair changes with single-stranded oligos in Ptet-RecT strains, with a control oligo and a co-transformation screening strategy.
source: Protocol by Kenan Murphy, based on van Kessel and Hatfull (2008) Mol Microbiol 67:1094–1107. Co-transformation and MAMA-PCR section by Marte Dragset (2012). Adapted for this site.
version: Draft 0.1
---
The method for pKM402 (Ptet-RecT)-promoted oligo recombineering in *M. smegmatis* and *M. tuberculosis* follows the same procedures as [dsDNA recombineering](recombineering.html) for growing and preparing cells for electroporation, with the exceptions below.

## Differences from dsDNA recombineering

1. Induce the culture with **50 ng/mL anhydrotetracycline (aTc)**, starting at OD₆₀₀ = 0.5, for 3 hours.
2. Electroporate about 1 µg of oligo.
3. Resuspend the electroporated cells in 10 mL 7H9 and grow out at 37 °C for 4–7 days (*M. tuberculosis*) or overnight (*M. smegmatis*). If there is more than one chromosome copy per cell at electroporation and only one is modified, the culture must be grown out so the modified chromosome segregates. For *M. tuberculosis* about a week is used.
4. Plate on selective medium that you expect to select for the mutation. If you cannot select for your mutation, use the co-transformation strategy below.

## Oligo substrate

- The oligo should be 70 bases, with the mutation(s) in the middle.
- Order the oligo that targets the **lagging-strand template** of the replication fork. Because this is often hard to know, order both the top strand and the bottom strand (each with the change). In most cases one works much better than the other (the lagging-strand oligo); the other often does not work at all, like the no-DNA control.
- Resuspend the oligo to 0.5 µg/µL in 10 mM Tris-HCl, pH 8.0.
- Add 2 µL oligo (1 µg) to 400 µL of electrocompetent *M. smegmatis* carrying pKM402.

## Control oligo

This oligo makes a 1 bp change in the *rpsL* locus and confers streptomycin resistance. It is specific to *M. smegmatis*; a different oligo is needed for *M. tuberculosis*.

`CGCGCGCGACCTTCCGGAGGGCCGAGTTCGGCTTCCTCGGAGTGGTGGTGTAAACGCGCGTGCACACGCC`

Plate 200 µL of undiluted, 10⁻¹ and 10⁻² dilutions on plates containing [20 µg/mL]{.tbc} streptomycin after overnight growth (*M. smegmatis*) or one week (*M. tuberculosis*). Plate 200 µL of the 10⁻⁵ and 10⁻⁶ dilutions for a total cell count. Expect about 10⁴–10⁵ recombinants per 10⁸ total cells for *rpsL* (the change you want may or may not be in this range). Also do a no-DNA control.

## Co-transformation with the rpsL oligo (when you cannot select for your mutation)

Co-transform the oligo that makes your mutation together with the *rpsL* oligo and select on streptomycin. Then screen the streptomycin-resistant colonies for your mutation by MAMA-PCR. The idea is that a cell that took up and recombined one oligo is more likely than a random cell to have done so with a second.

1. Transform 1 µg of each oligo into the pKM402 strain as above and select on plates with streptomycin.
2. Make a plasmid or PCR product containing your desired point mutation (for example by stitch PCR, with the mutation in the middle of the primers). This is needed to optimize the MAMA-PCR. Also have a wild-type version ready.
3. Design primers for **MAMA-PCR (mismatch amplification mutation assay)**: primer F upstream of the mutation, primer mutR whose very 3′ end matches only the mutant sequence (a single 3′ mismatch is fine), and primer R downstream of the mutation as a control for the reaction and template.

| | Primer F + mutR | Primer F + R |
|---|---|---|
| Mutant DNA | product | product |
| Wild-type DNA | no product | product |

4. Optimize the MAMA-PCR by gradient PCR using mutant and wild-type DNA, finding an annealing temperature at which F + mutR gives product only on mutant template.
5. Pick 96 streptomycin-resistant colonies into a 96-well PCR plate with 10 µL DMSO per well, and patch the colonies on an agar plate. Boil at 95 °C for 1 hour. Pool 12 samples at a time, giving 8 pooled samples per plate. Run MAMA-PCR on the pools, replacing the DMSO in the PCR mix with DMSO from the samples. Choose one or two pools giving a product with F + mutR and repeat un-pooled. Depending on the target, expect about 5–20% of streptomycin-resistant colonies to carry the second mutation.
6. Sequence PCR-positive mutants. Sequence the PCR product from primers F and R, **not** mutR.

[The source gives streptomycin as "20 mg/mL"; this is read as 20 µg/mL.]{.tbc}
