title: Single-cell image analysis in MicrobeJ
category: Imaging and analysis
tags: imaging, MicrobeJ, Fiji, quantitative analysis, microscopy
summary: Set cell-detection parameters, curate detected cells, export results, and generate profile and demograph plots in MicrobeJ.
source: Written by K. Tembiwa.
version: Draft 0.1
---
## Purpose

Detect cells in phase or fluorescence images, curate the detections, export per-cell measurements, and plot fluorescence profiles and demographs.

## Getting started

1. Open ImageJ (Fiji) and open the MicrobeJ plugin.
2. For hyperstacks, go to the **Images** tab and switch to **Folder**, then import your whole folder of images.
3. Go to **Bacteria** and set the channel and background. Choose the options you need: exclude on edges, shape descriptors, segmentation, intensity, shape, profile and polarity (for poles and sides, choose intensity > channel > max).
4. Set the threshold. [The example threshold used was −116; this depends on the images.]{.tbc}
5. To show stained colors, use ImageJ **Image > Color > Arrange Channels** and assign colors (for example channel 1 = GFP green, channel 2 = DAPI blue).
6. In the **Maxima** tab, tick the box to edit. Choose the channel and background, change the tolerance, and choose options (exclude on edges, shape descriptors, segmentation, intensity, profile) and associations (inside, location, localization).
7. Run the current settings on the active image to check they are appropriate.
8. If they are, click the pencil icon at the bottom right to detect cells and load the manual editing interface.

## Set detection parameters

Set the ranges that define a cell. The values below were used for [*M. smegmatis*]{.tbc}; choose ranges appropriate to your organism and magnification.

- Area: [1–8]{.tbc}
- Length: [0.5–10]{.tbc}
- Width: [0.2–2]{.tbc}

(Units are not stated in the original notes; confirm they are µm² and µm.)

For fluorescence images, tick the box next to **polarity** and set the options as in your analysis template. **Choose the correct channel** for the signal you are measuring (for example, the HADA channel). The channel number changes between experiments.

## Detect, curate and save

1. Use the blue arrow to test your parameters on the image. Once they are good, use the pencil to generate the list of cells.
2. In the experiment editor list, remove bad detections and cut touching cells apart.
3. When all good cells are highlighted green, click **save** in the experiment editor. The experiment file should go in the experiment folder with the same name as the image file.
4. In the experiment editor, click the **graphs** button (4th from the left) to open the results file.
5. In the results file, click **Bacteria** to see the data for each good cell. Right-click column headings to add sub-columns. Use the same set of columns for every image.
6. Copy the data into your spreadsheet, in a tab named for the image folder.

Keep an organized system for naming and storing experiment and results files, and a consistent way of exporting to a spreadsheet.

## Fluorescence profile

1. Open the results file in MicrobeJ and click **Bacteria**.
2. Click the **Profile** icon.
3. In **Plot**, choose *XStat Profile*; in **Stat**, choose *mean*.
4. In **Y axis**, choose *Medial → Intensity →* the channel you measured.
5. Click the play button.

## Demograph

1. Open the results file and click **Bacteria**.
2. Click the **Demograph** icon.
3. In **Plot**, choose *Profile*; in **Profiles**, choose *medial → Intensity →* your channel.
4. In **Sorting**, choose *shape.length*.
5. Click the play button.

## Where it usually fails

- **Wrong channel.** Check the channel assignment before every analysis.
- [**Merged or split cells.** Tighten the shape ranges and curate manually in the experiment editor.]{.tbc}
- **Inconsistent columns between images.** Use the same set of columns for every image so exported data can be combined.
