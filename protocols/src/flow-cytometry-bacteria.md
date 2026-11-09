title: Flow cytometry of bacteria (acquisition, staining and controls)
category: Flow cytometry
tags: flow cytometry, bacteria, single-cell, viability, SYTO 9, propidium iodide, quick-start
summary: Study notes on running bacteria on a flow cytometer: why bacteria are different from mammalian cells, how to set the threshold and check for swarming, viability stains, controls and reporting.
source: Study notes compiled from published guidance: Aarhus University FACS Core Facility "Analyzing Bacteria" (Bohn, 2020), the LIVE/DEAD BacLight manufacturer documentation, Stiefel et al. 2015, and Lee et al. 2008 (MIFlowCyt). Not yet run by the author.
version: Version 0.1
status: study
---
## How to use this page

These are **study notes, not a protocol**: a checklist of what to set up and test before trusting a bacterial flow experiment, to be edited as you learn your own instrument. Details that are not from a cited source are highlighted. Always check your core facility's own bacterial guidelines first, since the instrument decides which settings work.

## Why bacteria are different

Bacteria are at the lower limit of what most cytometers were built to see: they scatter little light and carry little signal, so instrument noise and debris matter much more than with mammalian cells. The practical consequences below follow from that.

## Acquisition settings (Aarhus FACS Core, "Analyzing Bacteria")

- **Use a DNA stain** to tell bacteria apart from background particles.
- **Standardize staining.** Incubation temperature and time both change the bacterial count.
- **Use height, not area,** for fluorescence and scatter, since bacteria vary less in height.
- **Use log scales** for both forward scatter (FSC) and side scatter (SSC).
- **Threshold on fluorescence** (the DNA stain) when possible. If you cannot, an SSC threshold is often better than an FSC threshold.
- **Run at the slowest speed** to start (slider fully to the left, not just "slow").

### Check for swarming (coincidence)

1. Record the median fluorescence intensity (MFI) of the bacterial population.
2. Dilute the sample and run it again.
3. The count rate should fall while the **MFI stays the same**. If the MFI changes, several cells are being read as one event ("swarming").
4. If so, run a dilution series to find a dilution where single events are detected.

[Also use filtered sheath fluid and buffers, and run a buffer-only tube so you know the background event rate before adding cells.]{.tbc}

## Viability and membrane-integrity stains

- **SYTO 9 + propidium iodide (LIVE/DEAD BacLight).** [SYTO 9 enters all cells, and propidium iodide only enters cells with damaged membranes and reduces the SYTO 9 signal, so green-only cells are read as intact and red cells as damaged.]{.tbc} Take stain concentrations and incubation times from the manufacturer's manual for your kit rather than from memory.
- **Validate before use.** Stiefel et al. (2015) discuss critical aspects of SYTO 9/PI assays, and [results can depend on the medium, growth phase and staining conditions]{.tbc}, so always include a **live control** and a **killed control** (for example heat- or isopropanol-killed cells) and a mixed sample, and confirm against plating.
- [A membrane-integrity stain does not by itself prove a cell is "dead" in the sense of unable to grow. Cultivability still needs a plating (CFU) check, such as the [serial dilution and CFU protocol](serial-dilution-cfu.html).]{.tbc}

## Fluorescent reporters and probes

- [Fluorescent proteins such as GFP need oxygen to mature, so signal can lag behind expression and be weak in dense or oxygen-poor cultures.]{.tbc}
- [Activity-based probes label the enzymes that are active in each cell, so flow cytometry can quantify per-cell probe signal and show population heterogeneity. Test whether fixation or permeabilization changes the signal before relying on it.]{.tbc} See also the [*S. aureus* quick-start](staphylococcus-aureus-quick-start.html).

## Controls checklist

- Unstained cells (autofluorescence).
- Single-stain controls for each dye or reporter.
- A strain without the reporter or probe, and (for probes) [an inhibitor- or competition-treated sample]{.tbc}.
- A dilution series (see swarming, above).
- [Calibration beads of a known size, so day-to-day instrument changes can be separated from biology.]{.tbc}
- Live, killed and mixed controls for viability stains.

## Practical notes for clumpy organisms

- [*S. aureus* grows in grape-like clusters, and mycobacteria clump without detergent. Disperse by gentle pipetting or a brief low-energy sonication, check by microscopy, and keep the same handling for every sample.]{.tbc}
- [Fix samples before running them if your facility requires it, and ask the facility about pathogen rules before bringing live cultures to a shared instrument.]{.tbc}

## Reporting

Record the instrument, configuration, settings and gating, and keep the raw FCS files. The MIFlowCyt standard lists the minimum information to report (Lee et al. 2008).

## Sources

- Bohn A. 2020. Analyzing Bacteria. FACS Core Facility guidelines, Aarhus University. [PDF](https://biomed.au.dk/fileadmin/www.facs.au.dk/Bacterial_Analysis_in_Flow_Cytometry.pdf)
- Stiefel P, Schmidt-Emrich S, Maniura-Weber K, Ren Q. 2015. Critical aspects of using bacterial cell viability assays with the fluorophores SYTO9 and propidium iodide. *BMC Microbiol* 15:36. [Search result](https://scholarhub.vn/publication/Critical-aspects-of-using-bacterial-cell-viability-assays-with-the-fluorophores-SYTO9-and-propidium-iodide/bf6228aa-8397-40c3-9dcd-ccbe06e61119)
- Thermo Fisher Scientific. LIVE/DEAD BacLight Bacterial Viability Kit manual ([MP 07007](https://assets.thermofisher.com/TFS-Assets/LSG/manuals/mp07277.pdf)).
- Lee JA, Spidlen J, Boyce K, et al. 2008. MIFlowCyt: the minimum information about a flow cytometry experiment. *Cytometry A* 73:926–930. [PubMed 18752282](https://pubmed.ncbi.nlm.nih.gov/18752282/)
