title: Staphylococcus aureus quick-start (strains, culture, genetics)
category: Organism quick-starts
tags: S. aureus, Staphylococcus, genetics, allelic exchange, electroporation, serine hydrolases, quick-start
summary: Study notes for starting work with S. aureus: common strains and the Nebraska mutant library, the restriction barrier, electroporation, pIMAY-Z allelic exchange, and what is known about the Fph serine hydrolases.
source: Study notes compiled from published sources (Fey et al. 2013; Monk and Foster 2012; Monk et al. 2015; Monk and Stinear 2021; Lentz et al. 2018), listed at the bottom of the page. Not yet run by the author.
version: Version 0.1
status: study
---
## About this page

This page summarizes published methods for working with *S. aureus*. It has not yet been run in this lab, so use it for orientation and follow the cited papers for the exact procedure. Numbers come from the cited papers; highlighted text has not been checked against a source.

## Biosafety

*S. aureus* (including MRSA) is [normally handled at biosafety level 2, but check your institution's rules and the strain-specific risk assessment before ordering or culturing anything]{.tbc}.

## Strains you will meet

- **USA300 JE2.** A derivative of the community-associated MRSA isolate USA300 LAC, cured of its two plasmids (p01 and p03). It is the parent of the Nebraska Transposon Mutant Library (Fey et al. 2013).
- **RN4220.** A restriction-deficient laboratory strain that has long been the usual first stop for plasmids made in *E. coli*. It accepts DNA easily but only works as a gateway for a limited set of related strains, not as a universal host (Monk and Foster 2012).
- **Nebraska Transposon Mutant Library (NTML).** 1,952 sequence-defined mutants in JE2, each with one *bursa aurealis* (a *mariner*-based transposon) insertion in a different non-essential gene, selected from 18,797 mapped insertion clones. The transposon carries an erythromycin cassette, and the mutants are maintained in medium with erythromycin at 5 µg/mL. Free to registered investigators through the NARSA/BEI strain repository (Fey et al. 2013).
- **Caveat for NTML phenotypes.** Polar effects were not tested. Confirm each phenotype by phage backcross, complementation or allelic replacement (Fey et al. 2013). Mutants with no insertion (579 ORFs) are only *potentially* essential.
- **Easy phenotypes to screen on plates:** in the original library screen, hemolysis (71 mutants altered), protease activity (62), pigment (38) and mannitol utilization (7) (Fey et al. 2013).

## Culture

- The Monk and Stinear (2021) protocol grows overnight cultures in **10 mL BHI in a 50 mL tube at 37 °C, 200 rpm**, and uses BHI agar for plates.
- [TSB is also widely used; choose the medium to match the project and the paper you are following.]{.tbc}
- [Unlike mycobacteria, *S. aureus* grows quickly in rich medium, so overnight cultures and next-day colonies are normal and no detergent is needed to disperse it.]{.tbc}

## The restriction barrier (why plasmids "don't work")

Many *S. aureus* strains resist DNA made in standard *E. coli* (Monk and Foster 2012):

1. **Type IV restriction** targets cytosine-methylated DNA. Plasmid made in a *dcm*-deficient *E. coli* strain (DC10B) avoids it.
2. **Type I restriction** is harder to bypass and depends on the strain's adenine methylation pattern.

Monk et al. (2015) built *E. coli* hosts that mimic the methylation of major lineages. **IM08B** (CC8 methylation) and **IM01B** (CC1) are derived from DC10B. In the paper, plasmids from IM08B transformed the CC8 strain NRS384 about 100-fold better (pRAB11) and about 500-fold better (pIMAY-Z) than plasmids from DC10B. IM01B was tested on the CC1 strain MW2. Pick the IMxxB strain that matches the lineage of your target strain, and note that a plasmid from IM01B is not suitable for CC8 targets.

## Electroporation (summary of Monk and Stinear 2021)

**Electrocompetent cells**

1. Grow an overnight culture in 10 mL [BHI](media-recipes.html) in a 50 mL tube at 37 °C, 200 rpm.
2. Dilute to OD₆₀₀ 0.5 in fresh pre-warmed BHI and grow 40 min more.
3. From here keep everything at 4 °C. Spin at 7,000 *g* for 5 min and wash twice with an equal volume of ice-cold water.
4. Wash twice in 1/5 volume of ice-cold [10% glycerol](buffers-and-solutions.html).
5. Resuspend in 1/200 volume of ice-cold 10% glycerol.
6. Freeze 50 µL aliquots at −70 °C.

**Electroporation**

1. Thaw an aliquot on ice for 5 min, then spin at 5,000 *g* for 3 min.
2. Resuspend the pellet in 80 µL of [10% glycerol + 500 mM sucrose](buffers-and-solutions.html).
3. Add 0.5–1 µg plasmid in up to 10 µL.
4. Transfer to a 1 mm cuvette and pulse at room temperature: 21 kV/cm, 100 Ω, 25 µF.
5. Immediately add 1 mL BHIS ([BHI + 500 mM sucrose](media-recipes.html)) and recover, tilted, at 30 °C for 1 h at 200 rpm.
6. Plate on BHI agar with chloramphenicol (10 µg/mL) and X-gal (100 µg/mL) ([plate recipe](media-recipes.html)). Incubate at 30 °C for 48 h, or at 37 °C overnight for integrants.

## Allelic exchange with pIMAY-Z (summary of Monk and Stinear 2021)

The plasmid's replicon is temperature-sensitive and cannot replicate in Gram-positive hosts at 37 °C.

1. **Integration.** Select integrants at 37 °C on BHI agar + chloramphenicol (10 µg/mL) + X-gal (100 µg/mL). Blue colonies are integrants. For strains that do not integrate directly, a "slow" route is described in the paper.
2. **Excision.** Grow an integrant in BHI at 30 °C to saturation ([about 8 h or overnight]{.tbc}). Plate 2 × 10⁻⁵ and 1 × 10⁻⁶ dilutions on BHI agar + X-gal and incubate at 37 °C overnight. White colonies are candidate excision events.
3. **Screen** white colonies by colony PCR, re-streak to purify, and confirm by PCR on genomic DNA and by whole-genome sequencing.

Notes:
- The original pIMAY (Monk et al. 2012) used anhydrotetracycline induction of an antisense *secY* for counter-selection. pIMAY-Z uses *lacZ* blue/white screening instead (Monk and Stinear 2021).
- The Addgene page for pIMAY (#68939) lists two different chloramphenicol concentrations (10 and 25 µg/mL), so verify which applies. The depositor advises checking that the plasmid is still temperature-sensitive in *S. aureus* before starting. It is available to academic and non-profit users under a UBMTA.
- Zeden et al. (2023, *Cold Spring Harbor Protocols*) give a worked example (a *tagO* deletion in RN4220) that is a good second source.

## Complementation and expression

Monk and Foster (2012) describe shuttle plasmids, anhydrotetracycline-inducible expression vectors, and phage-integrase vectors that insert one copy into the chromosome (avoiding copy-number effects). They also warn that **low-level antibiotic selection can favour secondary mutations** (for example in the *sae* locus) and that plasmids can be lost during animal infections without selection.

## Serine hydrolases (the Fph family)

- Activity-based profiling with fluorophosphonate probes identified ten previously uncharacterized *S. aureus* serine hydrolases, named **FphA–J**, most without human homologues (Lentz et al. 2018).
- **FphB** processes short fatty-acid esters, becomes more active in response to host-cell factors, and sits on the cell surface in only a subset of cells, as well as concentrating in the division septum. A deletion has no growth defect in culture but impairs infection at distinct sites in vivo, and a selective inhibitor reduced infectivity (Lentz et al. 2018).
- A crystal structure of FphF (one of the more abundant members), alone, covalently bound and with inhibitors, shows promiscuous esterase activity toward hydrophobic lipid substrates ([PubMed 32865965](https://pubmed.ncbi.nlm.nih.gov/32865965/)).
- Single-cell readouts of probe labeling pair naturally with [flow cytometry of bacteria](flow-cytometry-bacteria.html).

## Common pitfalls

- [Protein A on the *S. aureus* surface binds the Fc region of antibodies, so antibody staining can look positive for the wrong reason. Use Fc-independent reagents (F(ab′)₂ fragments), a protein A-deficient strain, or proper isotype and no-primary controls.]{.tbc}
- Plasmid will not go in: wrong host strain for the lineage, or the plasmid was made in standard *E. coli* (see the restriction barrier above).
- A mutant phenotype that disappears after back-crossing: expect secondary mutations or polar effects (Fey et al. 2013; Monk and Foster 2012).

## Sources

- Fey PD, Endres JL, Yajjala VK, Widhelm TJ, Boissy RJ, Bose JL, Bayles KW. 2013. A genetic resource for rapid and comprehensive phenotype screening of nonessential *Staphylococcus aureus* genes. *mBio* 4:e00537-12. [doi:10.1128/mBio.00537-12](https://doi.org/10.1128/mBio.00537-12)
- Monk IR, Foster TJ. 2012. Genetic manipulation of staphylococci: breaking through the barrier. *Front Cell Infect Microbiol* 2:49. [doi:10.3389/fcimb.2012.00049](https://doi.org/10.3389/fcimb.2012.00049)
- Monk IR, Shah IM, Xu M, Tan MW, Foster TJ. 2012. Transforming the untransformable: application of direct transformation to manipulate genetically *Staphylococcus aureus* and *Staphylococcus epidermidis*. *mBio* 3:e00277-11. [Full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC3312211)
- Monk IR, Tree JJ, Howden BP, Stinear TP, Foster TJ. 2015. Complete bypass of restriction systems for major *Staphylococcus aureus* lineages. *mBio* 6:e00308-15. [doi:10.1128/mBio.00308-15](https://doi.org/10.1128/mBio.00308-15)
- Monk IR, Stinear TP. 2021. From cloning to mutant in 5 days: rapid allelic exchange in *Staphylococcus aureus*. *Access Microbiol* 3:000193. [doi:10.1099/acmi.0.000193](https://doi.org/10.1099/acmi.0.000193)
- Zeden MS, Schuster CF, Gründling A. 2023. Allelic-exchange procedure in *Staphylococcus aureus*. *Cold Spring Harb Protoc* 2023:pdb.prot107948. [doi:10.1101/pdb.prot107948](https://doi.org/10.1101/pdb.prot107948)
- Lentz CS, Sheldon JR, Crawford LA, Cooper R, Garland M, Amieva MR, Weerapana E, Skaar EP, Bogyo M. 2018. Identification of a *S. aureus* virulence factor by activity-based protein profiling (ABPP). *Nat Chem Biol* 14:609. [PubMed 29769740](https://pubmed.ncbi.nlm.nih.gov/29769740/)
- Nebraska Transposon Mutant Library: [library page](https://www.unmc.edu/pathology/csr/research/library.html). pIMAY: [Addgene #68939](https://www.addgene.org/68939/).
