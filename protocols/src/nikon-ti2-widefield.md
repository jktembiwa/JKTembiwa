title: Nikon Ti-2 widefield fluorescence microscope: use, training and filters
category: Imaging
tags: microscopy, widefield, fluorescence, Nikon Ti-2, phase contrast, instrument
summary: Start-up, finding focus at 20X and 100X, Köhler alignment checks, camera settings and saturation checks, ND acquisition, and the installed filter sets.
source: Written from the lab's Ti-2 use guide, training notes and filter list (unpublished SOPs), generalized. Instrument-specific; follow your facility's training and alignment sheet.
version: Version 1.0
---
## Training

Training is two sessions of 1.5–2 h each: one on brightfield microscopy, one on fluorescence microscopy. Before the first session, watch videos on numerical aperture, Köhler illumination, and preventing objective lens damage. Before the second, watch the fluorescence-microscopy videos your trainer assigns.

## Part 1. Turning it on

1. Camera on (wait until the small white light stops flashing).
2. Computer on (wait for it to boot).
3. Controller box under the microscope on. Do not wait; go straight to step 4.
4. Power switch on the right of the back of the microscope base. You should see an arch of green lights, some flashing, and hear gentle clicking as the filter cubes move. If the lights keep blinking, the cubes grind, or it beeps, turn off switch 4 then switch 3, wait 15 s, and turn them on again.

## Part 2a. Finding cells at 20X

Use 20X for large objects such as macrophages, and as the objective for Köhler alignment.

1. Press **ESC** on the base to lower the objectives before moving them, so they do not get scratched.
2. In NIS-Elements, click the 20X icon (top left). The 20X is an **air** objective: do not add oil.
3. Put the Phase 1 ring in place on the filter/phase wheel.
4. Fit the right holder. For a 96-well plate, swap the slide holder for the plate holder with the small Allen wrenches. If you use a slide, put it **upside down** so the coverslip faces the objective.
5. Click **DIA** (diascopic/brightfield) on the top bar, then the green arrow (starts live video and turns the light on). You should see a spot of light on the sample and objective.
6. Make sure the eye button on the base is green. Focus through the eyepieces with the focus knobs.
7. Check the illumination by closing the field diaphragm: a small octagon of light with crisp edges in the center of the field means the light is adjusted. Otherwise follow the Köhler illumination and phase contrast alignment sheet for the Ti-2.

## Part 2b. Finding cells at 100X

Use 100X for small objects such as bacteria.

1. Put the Phase 3 ring in place and click the 100X icon in NIS-Elements. Install the slide or plate holder.
2. The 100X is an **oil** objective. Put a drop of immersion oil on the center of the objective.
3. Place the sample (coverslip down). Raise the objective until the oil touches the coverslip, which gets you close to focus.
4. Click DIA, then the green arrow. If you cannot see a spot of light on the objective, check that the lamp is on, then open the field diaphragm until light reaches the objective, find focus, and adjust the light.
5. Focus through the eyepieces. You can also type a Z-drive value in the Ti-2 box in Elements and press Enter: for a slide with an agarose pad, in-focus values are usually about **1400–1700** (type about 1500, then focus manually); for a 96-well plate holder at 100X, about **4500–5000**.
6. Close the field diaphragm completely to check the light. The whole field should be lit, with a blue shadow on one side and an orange shadow on the opposite side.
7. If the light is only slightly off (colors not balanced), adjust the condenser focusing knob.
8. If that does not fix it, go back to 20X and realign: press ESC, switch to the 20X, put in the Phase 1 ring, press ESC again to bring the objective up, and follow the alignment sheet. When returning to 100X, press ESC first, switch to 100X, and put the Phase 3 ring back in.
9. Close the field diaphragm again to check, and tweak the condenser knob slightly until orange and blue are balanced at the edges. Open the diaphragm just enough to illuminate the field evenly with no colored light at the edges.

## Part 3. Taking images

1. On the base press **L** to send light to the camera instead of the eyepieces. With the light and video on, the image appears on screen.
2. Find the camera box (Prime 95B) in Elements. Usually use **no binning** and **12 bit**. For focusing in phase, exposure is typically about 10 ms.
3. Adjust the Ti-2 box lights until cells look good and the image is not saturated.
4. **Fluorescence:** find focus in phase, click the red square to stop the video, choose the channel (GFP, mCherry or DAPI), and take a snapshot with the saved settings.
5. **Check for saturation.** In a 12-bit image the maximum value is 4095; in a 16-bit image it is [65,535]{.tbc} (the source says 65,536). Hover over the brightest pixels and read the value in the bottom bar; the LUT on the right shows how many pixels have each intensity.
6. If pixels are saturated, or many are near the maximum, lower the light intensity (the lamp engine) or the exposure time.
7. **Use identical settings for everything you will compare**: bit depth, exposure time, light intensity. Make sure the settings do not saturate any sample in the series, and write them in your lab notebook.
8. **ND acquisition:** choose the image series (for endpoint assays, lambda, with the filter cubes you want). Save to your folder in a dated subfolder with information about the experiment. Name files `sample_condition_001.nd2`; the `_001` makes the software number files in series.
9. Switch back to DIA, turn on the video, find a new field and focus, then click "Run now" in the ND acquisition box. Repeat until you have enough images of the sample.

## Installed filter sets

| Set | Catalog no. | Excitation | Emission | Dichroic |
|---|---|---|---|---|
| GFP (hard coat, high S/N, zero shift) | 96362 | 470/40 nm (450–490) | 525/50 nm (500–550) | 495 nm |
| Texas Red (hard coat, high S/N, zero shift) | 96365 | 560/40 nm (540–580) | 630/70 nm (593–668) | 585 nm |
| DAPI (hard coat, high S/N, zero shift) | 96360 | 350/50 nm (325–375) | 460/50 nm (435–485) | 400 nm |

To check whether a fluorophore can be detected with these sets, use the [Thermo Fisher Fluorescence SpectraViewer](https://www.thermofisher.com/us/en/home/life-science/cell-analysis/labeling-chemistry/fluorescence-spectraviewer.html).

See also [Image management and integrity](image-management-and-integrity.html).
