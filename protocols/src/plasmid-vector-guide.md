title: Plasmid and vector guide (mycobacteria and E. coli)
category: Reference
tags: plasmids, vectors, integrating, episomal, reference
summary: A guide to commonly used episomal, integrating, recombineering and E. coli vectors, with promoters, markers and cautions.
source: Adapted by K. Tembiwa from the Boutte Lab Beginner's Manual (v2.0, 2021). Vector credits are given where known.
version: Draft 0.1
---
## Episomal mycobacterial vectors

Carry a mycobacterial origin, usually about 5–10 copies per cell.

| Vector | Promoter | Features | Marker |
|---|---|---|---|
| pSE100 / pTetO | Tet-inducible | No TetR on the plasmid; promoter lacks a ribosome binding site. | Usually hygromycin |
| pTetOR / pUV15TetOR | Tet-inducible | TetR expressed from an intermediate-strength promoter. A Gateway form exists (pTetSG). | Usually hygromycin |
| pMV762 / pMV261 | Constitutive, intermediate (Mtb GroEL2) | Promoter includes a ribosome binding site. **pMV261 is toxic in mycobacteria; avoid.** | Usually hygromycin (zeocin forms used for complementation) |
| pNIT | Nitrile-inducible | Includes the NitA activator (positive feedback). | Usually kanamycin |

## Integrating vectors

Carry a mycobacteriophage integrase that integrates at a specific tRNA locus.

| Vector | Integrase / site | Promoter | Marker |
|---|---|---|---|
| pJeb402 | L5, attB at a glycine tRNA | Mycobacterial optimized promoter (MOP), constitutive; no RBS | Usually kanamycin |
| pMC1 | L5 | Expresses TetR (strong in pMC1s, intermediate in pMC1O) | Usually kanamycin |
| pKK216 | L5 | UV15 (*rpsA*) promoter with tet operator; no TetR, so expression is constitutive unless TetR is present elsewhere. Versions with other markers and fusions exist. Made by Karen Kieser. | Kanamycin (KK158 is a nourseothricin version) |
| pTweety | Tweety integrase, a lysine tRNA locus | No promoter | Kanamycin or hygromycin |
| pGH | Giles integrase, a proline tRNA locus in *M. smegmatis* | No promoter | Kanamycin or hygromycin (a zeocin form exists) |

## Recombination and recombineering vectors

| Vector | Purpose |
|---|---|
| pJM1 | Suicide vector (no mycobacterial origin) for clean knockouts by homologous recombination; hygromycin marked; carries *sacB* for sucrose counter-selection. Made by Jeff Murry. |
| pKM342 | Recombineering vector: hygromycin cassette flanked by lox sites; no mycobacterial origin; homologous sequence must be placed around the cassette. A zeocin form exists. |
| pUC57 | Backbone for synthesized homologous flanks; ampicillin resistance for *E. coli*. Used for PCR only; **do not transform into mycobacteria.** |
| pNIT-ET | Inducible vector expressing phage RecE/RecT homologues for recombineering; episomal with an unstable origin (lost without selection); kanamycin or zeocin forms. The host strain for recombineering transformations. |
| pJV53 | Acetamide-inducible recombinase plasmid, kanamycin marked. [Origin credit to be confirmed.]{.tbc} |

## E. coli vectors

| Vector | Use | Marker and features |
|---|---|---|
| pBluescript (+), pUC19, pUC57 | Subcloning, difficult cloning reactions | Ampicillin/carbenicillin; *lacZα* for blue/white screening. A pUC57 "Simple" form has no multiple cloning site. |
| pET41a | GST fusion (N-terminal) expression | Kanamycin; IPTG-inducible |
| pGEX 4T-1 | GST fusion (N-terminal) expression | Ampicillin/carbenicillin; IPTG-inducible |
| pBAD24 | Arabinose-inducible expression | Ampicillin/carbenicillin; strong induction |
| pET28 | His-tag (N- or C-terminal) expression | Kanamycin; strong IPTG induction |
