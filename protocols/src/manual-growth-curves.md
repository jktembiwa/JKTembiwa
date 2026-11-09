title: Manual growth curves (flask or tube, OD600 over time)
category: Growth and assays
tags: growth curve, OD600, spectrophotometer, culturing, 7H9
summary: Set up and sample a growth curve by hand, with notes for M. smegmatis and S. aureus, and how to calculate doubling time.
source: General microbiology practice, written up by K. Tembiwa; the 0.1 starting OD matches the plate-reader template in this collection.
version: Version 1.0
status: reviewed
related: growth-curve-setup | 96-well plate-reader growth curve with a dilution calculator. || growth-curve-doubling-time-prism | Analyze either type of growth curve for doubling time in GraphPad Prism.
---
## Purpose

Measure growth of a strain over time by sampling a culture and reading OD₆₀₀ by hand. Use this when you need to sample the culture itself (CFU, protein, RNA, microscopy), when volumes are too large for a plate, or to check a plate-reader result. For many strains in parallel, see [Setting up a 96-well growth curve](growth-curve-setup.html).

## Materials

- Starter culture in mid-log phase (see [Culturing](culturing-bacteria.html))
- Fresh pre-warmed medium: 7H9 (+ supplements, + Tween 80) for mycobacteria; TSB or LB for *S. aureus*; LB for *E. coli*
- Flasks (about 5–10× the culture volume) or culture tubes
- Spectrophotometer and cuvettes; medium for blanking
- Antibiotics or inducers as the experiment requires

## Procedure

1. **Prepare the starter.** Grow an overnight (or, for slow mycobacteria, multi-day) culture to mid-log. Check that it is not clumped or contaminated.
2. **Choose the starting OD.** Dilute into fresh medium to OD₆₀₀ 0.05–0.1 (0.1 is used for the plate-reader template). Culture volume to add = (target OD × final volume) ÷ starter OD.
3. **Blank** the spectrophotometer with sterile medium (same batch, same Tween/supplements).
4. **Read time zero** immediately after inoculating. Keep the same cuvette type throughout.
5. **Incubate** at 37 °C with shaking (see the table for rates).
6. **Sample at regular intervals** (table below). Mix the culture, remove about 1 mL aseptically, read OD₆₀₀.
7. **Dilute samples above OD 0.6–0.8** in medium and multiply the reading by the dilution factor, because the spectrophotometer is not linear at high density.
8. Continue until the culture plateaus (stationary phase).
9. For replicate curves, inoculate each flask from the same starter at the same OD and run at least three biological replicates.

## Suggested sampling by organism

| | *E. coli* | *S. aureus* | *M. smegmatis* |
|---|---|---|---|
| Typical doubling time | ~20–30 min | ~30–40 min | about 3 h |
| Sampling interval | every 60 min | every 60 min | every 3 h |
| Total length | 8 h | 10 h | 24–30 h |
| Medium | LB | TSB | 7H9 + ADC + 0.05% Tween 80 |
| Shaking | 200–250 rpm | 200–250 rpm | ~200 rpm, or roller |

BCG and *M. tuberculosis* double about every 18–24 h (see [Strains and growth](strains-and-growth.html)), so sample once or twice daily over one to two weeks. Work with BSL-2 organisms in a biosafety cabinet.

## Calculations

Doubling time from two points in exponential phase:

$$t_d = \frac{(t_2 - t_1)\,\ln 2}{\ln(\mathrm{OD}_2/\mathrm{OD}_1)}$$

Better: plot ln(OD) against time and fit a line through the exponential portion. Growth rate μ = slope; doubling time = ln 2 ÷ μ.

## Tips

- Plot on a log scale: exponential growth is then a straight line.
- Keep the flask:medium ratio and shaking speed the same between strains; aeration changes growth rate.
- Mycobacteria clump. Pipette the culture up and down (or vortex briefly with beads) before reading, and keep Tween 80 in the medium so that OD reflects cell number.
- When a drug or inducer is added, record the time and OD at the addition.
- Correct for OD if reading in a plate reader, since the path length differs from a 1 cm cuvette.
- OD does not distinguish live from dead cells. Plate for CFU ([Serial dilution](serial-dilution-cfu.html)) when viability matters.

Reading intervals, flask size and shaking speed are general guidelines and should be replaced with your lab's usual values.

- **Take CFU samples alongside OD readings** so you can convert OD to CFU later (OD → CFU calculation).

<figure class="proto-fig" style="max-width:360px"><img src="images/postit-cfu-tip.jpg" alt="Yellow Post-it with handwritten C1V1 = C2V2 working and a reminder to check OD alongside taking CFU samples" width="700" height="680" loading="lazy"><figcaption>A Post-it reminder from the bench: do the C₁V₁ = C₂V₂ dilution, and check OD alongside taking CFU samples.</figcaption></figure>

