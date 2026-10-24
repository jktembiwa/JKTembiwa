title: Making a transposon library by phage transduction
category: Mycobacterial genetics
tags: Tn-seq, transposon library, phage transduction, M. smegmatis, M. tuberculosis
summary: Transduce mycobacteria with φMycoMarT7, plate on kanamycin, scrape and freeze the library; three versions compared.
source: Murry et al., Methods Mol Biol 2008;416:45–59; Mtb-style edits (2015); M. smegmatis-optimized protocol for Tn-seq (12/2015); Fortune-lab Benchling protocol (2022). Condensed by K. Tembiwa.
version: Draft 0.1
---
Part of the [Tn-seq workflow](tn-seq-overview.html). Start from a titered phage stock ([phage stock preparation](tn-seq-phage-stock-prep.html)). Add **Tween 80 to the selection plates**: it inhibits the lytic cycle, so you avoid recovering mostly phage DNA. Include a no-phage control to measure kanamycin background. Aim for **at least ~200,000 independent colonies** per library; too-crowded plates lose signal from some mutants.

## Common core

1. Grow cells to the OD in the table; wash with MP buffer (50 mM Tris pH 7.5, 150 mM NaCl, 10 mM MgSO₄, 2 mM CaCl₂).
2. Resuspend in warm (37 °C) MP buffer; warm the phage to 37 °C too (the Benchling version pre-warms wash and resuspension media and the centrifuge to 37 °C so the temperature-sensitive phage does not become lytic at the 30 °C permissive temperature).
3. Mix cells and phage, incubate at 37 °C.
4. Plate on kanamycin + Tween 80, incubate, scrape, freeze in aliquots with glycerol; titer one thawed aliquot.

## Versions

| | A. Mtb-style (Murry/Rego edits) | B. *M. smegmatis*-optimized | C. Benchling (Fortune lab, 2022) |
|---|---|---|---|
| Culture | 100 mL, OD₆₀₀ 0.6–1.0, 7H9 + glycerol + OADC (ADC for smeg/BCG) + 0.05% Tween | 50 mL (up to 200 mL for bigger libraries) at OD₆₀₀ 2–3; late log/stationary is critical | 100 mL Mtb, OD 1.0–1.5, 7H9 + OADC + Tween |
| Wash | 2 × 10–25 mL MP | 3 × MP | 2 × 50 mL 7H9 + glycerol + OADC without Tween, pre-warmed to 37 °C |
| Resuspend | 10 mL warm MP | ~5 mL MP to a 6 mL final volume after phage | 5 mL medium without Tween |
| Phage | ~2×10¹¹ | 2–3×10¹² (1×10¹¹ per OD unit); ~5 mL if stock is only ~10¹¹ PFU/mL | ~2.5 mL high-titer phage |
| Incubation | 3–4 h (generic) or overnight (Mtb), 37 °C | 4 h, 37 °C, shaking | ~18 h, 37 °C, **no shaking** |
| After | Spin, resuspend, plate (or freeze and titer first) | Plate at once | Optional PBS + Tween wash, resuspend in 2 mL |
| Plates | 10 × 150 mm 7H10 + Tween + Kan 25 µg/mL, 250 µL each | ~20 × 15 cm LB + Kan + 0.1% Tween 80, 600 µL each, glass beads; square plates also work | 10 × 150 mm or 3 × 225 mm 7H10 + OADC + Tween + Kan 50 µg/mL |
| Growth | ~3 weeks, 37 °C | 3 days, 37 °C | ~21 days, agar side up, foil-wrapped |
| Harvest | scrape, prep gDNA | scrape into 7H9 + 15% glycerol, pool, aliquot at −80 °C | scrape into buffer or 7H9 + glycerol |
| Yield target | ~200,000 | ≥200,000–300,000 | dense, nearly a lawn |

Notes:
- Kanamycin differs between sources (20, 25 and 50 µg/mL). [The *M. smegmatis* source writes "20 ml/ml"; this is assumed to mean 20 µg/mL.]{.tbc}
- Phage titers above 5×10¹¹ PFU/mL are not always obtained; scale phage volume to the titer.
- "Lacy" phage plates are hard to get; test a dilution series and then scale up the best dilution to 5–10 plates.
- Mtb work is BSL3. Wrap and incubate plates for the full time.

For scraping, freezing and DNA extraction, continue with [library prep and sequencing](tn-seq-library-prep.html).
