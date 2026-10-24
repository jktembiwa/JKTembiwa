title: Culturing bacteria: E. coli, M. smegmatis and S. aureus compared
category: Growth and assays
tags: culturing, E. coli, M. smegmatis, S. aureus, 7H9, streaking, glycerol stock
summary: How to start, grow and maintain cultures, and what changes between fast growers (E. coli, S. aureus) and mycobacteria.
source: Adapted by K. Tembiwa from the Boutte Lab Beginner's Manual (v2.0, 2021) for E. coli and mycobacteria, plus general microbiology practice for S. aureus (S. aureus entries are unverified).
version: Draft 0.1
---
Follow your institution's biosafety rules. *M. smegmatis* and *E. coli* K-12 strains are BSL-1; *S. aureus*, BCG and auxotrophic *M. tuberculosis* are BSL-2 (biosafety cabinet, appropriate PPE and waste handling).

## General steps (all organisms)

1. **Streak from the frozen stock** onto an agar plate to get single colonies. Scrape the surface of the frozen stock with a sterile tip or loop; do not thaw the stock.
2. **Incubate** until colonies appear (see the table).
3. **Pick a single colony** into liquid medium with appropriate antibiotics. Keep the tube loosely capped or in a vented tube for aeration.
4. **Grow with aeration** (shaking or rolling) at 37 °C.
5. **Use at mid-log phase** (OD₆₀₀ ~0.4–0.8) for most experiments. Do not let cultures sit in stationary phase unless the experiment requires it.
6. **Make freezer stocks** from fresh cultures by mixing with sterile glycerol (final 15–25%) and freezing at –80 °C. See [Strain annotation and freezing](strain-annotation-and-freezing.html).

## Key differences

| | *E. coli* | *S. aureus* | *M. smegmatis* |
|---|---|---|---|
| Biosafety | BSL-1 (K-12) | BSL-2 | BSL-1 |
| Doubling time (rich medium) | [~20–30 min]{.tbc} | [~30–40 min]{.tbc} | about 3 h |
| Colonies on plates | overnight | [overnight (16–24 h)]{.tbc} | 3–4 days |
| Liquid medium | LB | [TSB or BHI]{.tbc} | 7H9 + ADC (or OADC) + glycerol + 0.05% Tween 80 |
| Plate medium | LB agar | [TSA]{.tbc} | 7H10/7H11 + supplements, or LB |
| Saturated culture | overnight | [overnight]{.tbc} | 2–3 days |
| Clumping | no | [clusters, grape-like]{.tbc} | yes, without detergent |
| Aeration | shake, [200–250 rpm]{.tbc} | shake, [200–250 rpm]{.tbc} | roller or shake, [~200 rpm]{.tbc} |
| Detergent | none | none | Tween 80 (0.05%) to limit clumping |
| Stationary-phase storage | 4 °C for days | [4 °C for days]{.tbc} | room temp or 4 °C; recover in fresh medium |
| Inducible systems | arabinose, IPTG | [anhydrotetracycline (Tet), cadmium]{.tbc} | anhydrotetracycline (Tet), acetamide, see [Induction systems](induction-and-depletion-systems.html) |

### Mycobacteria

- **Tween 80** (or tyloxapol) prevents clumping. It also slightly changes the cell surface, so keep the concentration constant between comparisons and use detergent-free medium only when the experiment needs it. Do not add Tween to plates.
- **Growth is slow.** Plan multi-day cultures. Starting a dense preculture the day before lets you set up experiments with log-phase cells.
- **Do not over-dilute.** Very low-density mycobacterial cultures grow poorly; inoculate at OD₆₀₀ 0.01–0.05 or more.
- **Contamination** from faster-growing bacteria is the biggest risk with long incubations. Antibiotics for the plasmid can protect against it, and cycloheximide or other additions are sometimes used.
- **Seal plates** in bags for long incubations.
- BCG and *M. tuberculosis* need OADC (not ADC) and take 3–4 weeks to form colonies. See [Strains and growth](strains-and-growth.html).

### *S. aureus*

[This column is general microbiology knowledge and has not been checked against a lab protocol.]{.tbc}

- Grows quickly in rich medium; include antibiotics for plasmid selection, e.g. erythromycin or chloramphenicol, according to the marker.
- Grows in clusters, so vortex or pipette before reading OD, and expect OD to be noisier than for rods.
- Make sure the medium is well aerated: use a flask volume at least 5× the culture volume.
- Handle as BSL-2: biosafety cabinet for open work, and decontaminate waste.

### *E. coli*

- For toxic constructs, grow at 30 °C or lower and avoid long overnights; see the FAQ.
- For plasmid preps, use a fresh overnight in antibiotic. For competent cells see [Electrocompetent cells](electrocompetent-cells-and-electroporation.html) and [chemical transformation](ecoli-chemical-transformation.html).

### *M. marinum*

Handle at the biosafety level required by your institution.

- **Wild-type strain:** buy the M strain from ATCC. Grow a first passage (P1) and make P1 stocks, then expand to a large P2 culture. Make freezer stocks from P2 and distribute these as the parental strain to lab members. **Do not passage the strain unnecessarily.** It does not lose PDIM, but it can lose its ability to lyse red blood cells, so a new P1 may be needed every few years.
- **Medium:** 7H9 with Tween 80. OADC can be added, but it is expensive and not required.
- **Plasmids:** many are derived from pMV306 (L5-integrating); L5 integrating plasmids work. Fast-cloning genes behind the MOP promoter complements well. In general, anything that works in *M. smegmatis* and *M. tuberculosis* works in *M. marinum*.
- **Transformation:** electroporation as in *Mycobacteria Protocols* (Parish and Roberts, eds.); glycine in the culture improves efficiency. *M. marinum* needs more DNA than *M. tuberculosis* (about 1 µg or more). See [Knockouts in *M. marinum*](marinum-allelic-exchange-p2nil-pgoal.html).
- **Knockouts:** p2NIL/pGOAL with a UV step for the DNA (essential; without it, plasmids integrate at the wrong site).
- **Temperature:** *M. marinum* grows best at about 30–32 °C rather than 37 °C. [Confirm growth temperature for your strain.]{.tbc}

## Cryovial labels

To print labels instead of writing on cryovials by hand, use the label template: [download the cryovial label template (.docx)](downloads/cryovial-label-template.docx). Print on the label stock your lab uses (the template is formatted for ToughTag cryovial labels), fill in strain/plasmid, date and initials before printing, and match the information to the freezer-stock database ([Strain annotation and freezing](strain-annotation-and-freezing.html)).

## Antibiotics

Use the concentrations in [Antibiotic plates](antibiotic-plates.html) for *E. coli* and mycobacteria. Concentrations for *S. aureus* are different and strain-dependent.

[Verify S. aureus antibiotic concentrations and media before use.]{.tbc}
