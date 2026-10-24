title: Gibson assembly cloning
category: Cloning
tags: Gibson assembly, cloning, primer design, PCR, restriction digest
summary: Primer design, PCR, vector preparation, purification and assembly for Gibson cloning, including multi-insert strategies.
source: Original protocol by Jeff Wagner (May 2015), adapted by K. Tembiwa from the Boutte Lab Beginner's Manual (v2.0, 2021). Reference: Gibson et al. (2009) Nat Methods 6:343–345.
version: Draft 0.1
---
## Overview

1. PCR and gel purification of the insert.
2. Restriction digest and column purification of the vector.
3. Add insert and vector to a 5 µL Gibson master-mix aliquot for a final volume of 10 µL.
4. Incubate at 50 °C for 1 hour.
5. Transform 5 µL of the reaction into chemically competent *E. coli* ([protocol](ecoli-chemical-transformation.html)).
6. Plate and screen colonies ([colony PCR](colony-pcr-screening.html)).

Gibson assembly uses an exonuclease to create long, thermodynamically stable single-stranded overhangs at 50 °C. It is **not** a homologous recombination method.

## Primer design

The overlap between fragments must be long enough that its melting temperature is above 50 °C. As a fast rule, use 60 nt primers: 20 nt that anneal to the template and 40 nt (including any restriction site) that overlap the vector. This is overkill but works at a very high rate. If you need to add something (an epitope tag, a restriction site), subtract the required bases from the overhang, keeping the overhang melting temperature above 50 °C. Overlaps of about 30 nt work, and some people routinely use about 20 nt. Primers under 60 nt allow the smallest IDT order size; longer primers (up to 90 nt) have also worked.

For several fragments, design primers so adjacent fragments overlap with a melting temperature above 50 °C; about 40 nt is a good default.

## PCR (Q5 polymerase example)

| Ingredient | Amount (µL) |
|---|---|
| ddH₂O | 25.5 |
| Primer 1 (100 µM) | 1 |
| Primer 2 (100 µM) | 1 |
| dNTPs (10 mM each) | 1 |
| Q5 reaction buffer | 10 |
| Q5 GC enhancer | 10 |
| Template | 1 |
| Q5 polymerase | 0.5 |

Primer amounts can be reduced substantially; extra does no harm. Program: 98 °C 0:30; 35 cycles of 98 °C 0:30, 60 °C 0:30, 72 °C 0:30 per kb of product; 72 °C 2:00; hold at 4 °C.

## Vector restriction digest

Use standard methods with any suitable enzyme(s). A single-enzyme digest works for Gibson without phosphatase treatment. Overnight digestion is preferred; a couple of hours has worked in a pinch.

## Purification

Column-purify the vector with a standard PCR/enzyme clean-up kit. Gel-purify the PCR product, or see [gel purification](gel-purification.html).

## Gibson reaction

The reaction tolerates a wide range of vector and insert amounts. Aliquot the Gibson reagent (NEB) into 5 µL 2X reactions in PCR tubes. A typical reaction adds 2 µL vector and 3 µL insert for 10 µL total. The nominal ideal is 100 ng vector with a 3:1 insert:vector ratio, but measuring this exactly is usually unnecessary. Include a negative control with vector only (water in place of insert) to control for residual restriction and ligation.

Incubate 1 hour at 50 °C. Transform 5 µL of the raw reaction directly into chemically competent *E. coli*, recover and plate. There should be several-fold more colonies with insert than in the negative control. Pick about 3 colonies and screen by restriction digest or colony PCR.

## Multiple inserts

Efficiency falls with each additional insert. Up to three inserts at once has worked, though one or two is best. With more inserts (or after a failed multi-insert reaction), first do a Gibson reaction with all inserts but no vector. Add 1 µL of the raw reaction to a new PCR with the two terminal primers to make a single pre-assembled fragment, purify it as for a single insert, then use it in the final Gibson reaction with vector.

## Where it usually fails

- **PCR fails.** Run a gradient PCR with 8 tubes (one strip) across annealing temperatures of 50–70 °C.
- **Few or no colonies with more than two fragments.** Pre-assemble the inserts as described above.
- [**Insert and vector-only control have similar colony counts.** The vector may not be fully cut or purified; check the digest.]{.tbc}
