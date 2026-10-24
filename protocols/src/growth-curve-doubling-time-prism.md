title: Calculating doubling times from growth curves in GraphPad Prism
category: Imaging and analysis
tags: growth curve, doubling time, Prism, statistics, ANOVA
summary: Fit log-phase data to an exponential growth equation, extract doubling times per replicate, and compare strains with one-way ANOVA.
source: Written by K. Tembiwa (Boutte Lab).
version: Draft 0.1
---
1. Enter data in Prism: X = elapsed time; Y = three replicate values in side-by-side sub-columns.
2. Make a new table with a single replicate per data set, called "singles", and copy the data and times into it.
3. Plot the singles data and set the Y axis to **log₂ scale**.
4. **Exclude the non-linear parts** (lag and stationary phase). Only log-phase measurements should be used to calculate doubling time. Look at each biological replicate separately, note which time points are linear, and exclude the rest (highlight, Cmd+E; the table must be frozen).
5. Fit each replicate: *Analyze → Nonlinear regression → Exponential growth equation*.
6. Take the doubling times from the results table into a new column table (replicates in columns; use "paste transpose" if needed). Aim for at least 3 biological replicates per strain or condition.
7. Compare strains: *Analyze → Ordinary one-way ANOVA → Multiple comparisons → compare the mean of each column with the mean of a control column* (set the control to wild type).

Use biological, not technical, replicates as *n*. See [Growth curve setup](growth-curve-setup.html) and [Manual growth curves](manual-growth-curves.html).
