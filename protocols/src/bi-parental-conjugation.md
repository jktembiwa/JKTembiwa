title: Bi-parental conjugation (E. coli donor to recipient, solid mating)
category: Transformation
tags: conjugation, plasmid transfer, E. coli, mating
summary: Transfer a plasmid from a DAP-auxotroph E. coli donor into a recipient strain by spot-mating, then select and verify transconjugants.
source: Written by K. Tembiwa.
version: Draft 0.1
---
## Purpose

Move a plasmid from a diaminopimelic acid (DAP) auxotroph *E. coli* donor into a recipient strain by mating cells on solid medium, then select recipients that received the plasmid. Because the donor cannot grow without DAP, plating the mating mixture on medium lacking DAP counter-selects the donor.

## Before you start

- **Donor:** *E. coli* DAP auxotroph carrying the plasmid to be transferred (kanamycin-marked in this example). Grow with DAP.
- **Recipient:** the strain that will receive the plasmid. Grow without antibiotic.
- **Media and reagents:** [YG]{.tbc} broth and agar, LB broth, DAP stock ([60 mM]{.tbc}), kanamycin, 1X PBS.
- **Plates:** YG + DAP (mating plates) and YG + kanamycin 30 µg/mL (selection plates).
- Set up every donor × recipient combination you want. This example uses 2 donors × 2 recipients = 4 combinations.

## Day 1: overnight cultures

1. **Recipient:** 10 mL YG broth, no antibiotic, in a 125 mL flask. Shake at 225 rpm, 28 °C.
2. **Donor:** 10 mL LB + kanamycin 50 µg/mL + DAP ([50 µL of 60 mM stock]{.tbc}, about [0.3 mM]{.tbc} final). Grow in a roller drum at 37 °C.

## Day 2: mating

1. In the afternoon, transfer 1 mL of each overnight culture to a separate microcentrifuge tube.
2. Wash each pellet twice with 1X PBS: spin [3000 rpm]{.tbc} for 5 min, resuspend in 500 µL PBS each time.
3. After the second wash, resuspend in 500 µL 1X PBS.
4. In new tubes, combine donor and recipient to a total of 100 µL. **Mix by pipetting, not vortexing.** Volumes used:
    - 50 µL donor + 50 µL recipient (1:1)
    - 10 µL donor + 90 µL recipient (a 1:9 donor:recipient ratio by volume)
    - 1 µL donor + 99 µL recipient (a 1:99 donor:recipient ratio by volume)
5. **Spot** the entire 100 µL onto a YG + DAP plate. **Do not spread.** Use one plate per donor × recipient combination, with the three ratios spotted on the same plate.
6. Let the spots dry, then incubate at 28 °C overnight.

## Day 3 onward: recover transconjugants

1. Check for growth in the spots the next morning. If none, check again later that day, then the following morning.
2. When growth appears, scrape the spot and suspend in 1 mL 1X PBS. Spin and wash twice more in 1 mL PBS (same spin as above).
3. Resuspend the final pellet in 100 µL PBS and spread the entire volume on a YG + kanamycin 30 µg/mL plate (no DAP). Incubate overnight at 28 °C.
4. When colonies appear, screen by colony PCR with primers specific to the transferred plasmid. See the [colony PCR protocol](colony-pcr-screening.html). **If you see a lawn rather than single colonies**, take a small amount and streak for single colonies first, then screen.
5. Pick 3 single colonies per donor × recipient combination, grow in YG + kanamycin 30 µg/mL, and make freezer stocks.

## Where it usually fails

- **No growth in the mating spot.** Check again later the same day, then the next morning. [Confirm DAP was in the mating plates.]{.tbc}
- **A lawn on the selection plate.** Streak out for single colonies before colony PCR, so you do not screen a mixed population.
- [**Donor carry-over.** If donor growth appears on selection plates, confirm they contain no DAP and that the post-mating washes were done twice.]{.tbc}
