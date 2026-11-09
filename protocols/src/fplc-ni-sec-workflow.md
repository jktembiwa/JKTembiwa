title: FPLC: Ni column then size-exclusion run (NGC system)
category: Protein biochemistry
tags: FPLC, Ni-NTA, SEC, protein purification, NGC, instrument
summary: Operating rules, priming, Ni column and SEC runs, clean-up, and column care for a Ni then size-exclusion purification on an NGC chromatography system.
source: Written from the lab's FPLC use outline for trained users (unpublished SOP), generalized. Instrument-specific; use only after being trained on your own system.
version: Version 1.0
---
## Before you start

These notes assume a Ni column followed by a size-exclusion (SEC) column. They are a reminder for people who have already been trained on the instrument, not a replacement for training.

**Rules to remember**

1. **Do not turn off the NGC (the large unit).** Leave it on, or condensation builds up inside. About once a month it is switched off at the side, unplugged for a hard reset, and turned back on after a few minutes.
2. **Bubbles are the enemy.** Prime the lines whenever you change buffers, always degas buffers, and run a system flush before every run.
3. **Always set pressure limits**, for manual and programmed runs. Each column's limit is listed in a table kept next to the computer.
4. **Keep both pump inlet lines in liquid** at all times. Never leave them in air.

**Buffers and filtering.** Use filtered, degassed buffers, ultrapure water and 20% ethanol. Filter buffers, water and ethanol with bottle-top filter units (reusable about 5 times; they do not need to stay sterile). Filter lysates (loaded in the DynaLoop) and purified protein (injected on SEC) through a 0.45 µm syringe filter, or spin twice. Spinning twice is usually faster than filtering lysate, which clogs.

Find a buffer your protein is soluble in by trial and error; a starting point is 50 mM Tris pH 7.5, 150 mM NaCl.

## Restarting the system

Normally the computer and the fraction collector stay on, and the NGC is never turned off. If the detector screen is white, tap OK on the touchscreen to wake it. If you have connection problems, did maintenance, or the software freezes, do a hard restart:

1. Turn off the fraction collector (switch at the back).
2. Turn off the NGC (green button on the right), then unplug it.
3. Shut down the computer from Windows and wait 2 minutes.
4. Turn on the computer, then the fraction collector, then re-plug and turn on the NGC (flat button on the right). Wait for "Detector initializing".

If only the fraction collector froze or was turned off, the NGC must be restarted and reconnected.

## Priming and equilibrating

If the system has been idle for more than a couple of days, one pump is on water and the other on 20% ethanol (here, ethanol on pump B).

1. Move the ethanol inlet line into purified water.
2. **Prime pump B:** unscrew the valve on top of the pump, attach a 10 mL syringe, and draw water through the lines and pump. Discard the liquid and repeat until no bubbles appear, then close the valve.
3. Move pump B's line into the Ni wash buffer and prime again.
4. **Prime every time you switch buffers.** When changing between two different salty buffers, or between ethanol and a salty buffer, prime with water in between. The purge button on the face plate also works (purge for 2 minutes, ideally right after priming).
5. Run a system flush (keep the column valve on bypass), so that the system and column are in the same liquid.

**Put the Ni column into water** (if it was stored in ethanol): run a "System flush pump A" method on water, then in the manual run tool select the Ni column position, tick the maximum column pressure box and enter the limit, and run water at 1 mL/min, isocratic, 0% B, 20 mL. Repeat with Ni wash buffer from pump B, then switch pump A to elution buffer, prime it, and put 10 mL of wash buffer through the column.

Start manual washes at 1 mL/min and let the pressure settle before raising the flow rate.

## DynaLoop: loading large lysate volumes

The DynaLoop holds up to about 90 mL, so it is used for lysate on the Ni column.

1. Remove the loop in the injection valve. Connect the DynaLoop bottom tube to loop port F and the top tube to loop port E.
2. Disconnect the tube from the column-switching valve (port 2) from the injection valve's luer port while loading.
3. If the DynaLoop is in ethanol, run the "cleaning dynaloop" program with water first (fill and expel once, up to 40 mL).
4. Clear the lysate (0.45 µm filter, or spin twice). Draw it into a luer-lock syringe, remove air, and connect it to the injection valve's luer port.
5. In manual mode, set the injection valve to "Manual load loop". Inject slowly; it is hard to push, and you will see the plunger rise.

## Ni column run

1. Find a Ni method and adjust it in the Method Editor. Enter the lysate volume to inject: most of it, but not the top layer where bubbles collect.
2. Wash with at least 3 column volumes (CV) of wash buffer (10–20 mM imidazole), then run a gradient up to about 200–500 mM imidazole over 3–7 CV, then elution buffer alone for 1–5 CV. With many contaminants, wash longer and use a longer gradient.
3. Turn on fraction collection during elution, and for some of the other steps in case you need to find your protein later.
4. Check that buffers are assigned to the correct pumps, save, and press start run. Set up the fraction tubes as shown in the run dialog, name the run with the protein and date, and save to your folder.
5. If "start run" is grayed out, cancel, go to manual mode, click the red X (clear), accept resetting the collection state, and start again from the Method Editor.

Maximum pressure for a Ni column: [73 psi]{.tbc}; the manual-run limit entered in the column box was [40]{.tbc}. These two numbers appear in the source without explanation; check them against the manufacturer's limit for your column.

**After the run**

1. Reattach the port-2 tube to the injection valve and remove the syringe.
2. Run 1.25 CV of **elution buffer** to wash the column. Do not run water straight after elution, because remaining protein can precipitate on the resin.
3. Switch pump A to water, prime, and run a system flush with both pumps on water.
4. Run 7 mL of water through the Ni column.
5. Run "wash dynaloop" with water twice, filling a bit beyond the lysate volume you used (for 40 mL of lysate, use at least 45 mL of water in one of the washes).
6. If the Ni column and DynaLoop will not be used for more than 3 days, store them in 20% ethanol; otherwise water is fine.
7. Analyze fractions on a gel, pool the ones you want, and buffer exchange to remove imidazole (which causes precipitation). If you will run SEC, exchange into the SEC buffer.

## SEC run

Most Ni-purified proteins contain some contaminants and unfolded protein, so the preparative SEC column (the large one) is used as a second step.

1. **Equilibrate.** In manual mode run 1.25 CV of water, then buffer, through the chosen SEC column. The large column takes several hours; write a program to do this overnight.
2. Detach the DynaLoop tubes and connect a loop big enough for your sample into ports E and F.
3. **Concentrate** the sample (about 5 mL for the large column, 0.25 mL for the small one). Spin 1–2 min at maximum speed in the cold to remove precipitate.
4. Copy and edit a method. A typical SEC method is just an injection followed by elution with buffer.
   - Flow rate: if the column is clean, about 2 mL/min for the large column and 1 mL/min for the small one. Slower gives better resolution but may be needed for sticky proteins.
   - Equilibration step: 1 CV if the column was on water only; delete or shorten it if the column is already in buffer.
   - Injection volume must match the loop.
   - Elution with the equilibration buffer for at least 1 CV, plus 0.5–1 CV of wash (or wash manually afterwards).
   - Fraction collection during elution. Most proteins come off between 0.2 and 0.7 CV.
5. Set the injection valve to "Manual load loop" and screw in the injection port.
6. **Load the syringe without bubbles.** For 1 mL or less, draw sample into a 1 mL syringe with the needle on, turn it upright, pull the plunger down to let air rise, tap, and push out the air. For larger volumes, fill the syringe without the needle (finger over the tip), insert the plunger, turn upright, expel air, then add the needle and expel any remaining air.
7. Inject without introducing air into the line, start the method, and place the fraction tubes.

## Cleaning up

1. System flush with water on both pumps (pump A first if it is already on water). Then move line B into the water bottle, prime pump B and flush with pump B.
2. Put line B in 20% ethanol and flush with ethanol.
3. Run 1.25 CV of water through the SEC column, then 1.25 CV of 20% ethanol for storage.
4. Wipe up spills around the fraction collector, NGC and fridge, and tidy the bench.
5. **Leave the NGC and the computer on.**

## Column care

**Pressure.** The resin beads are squishable. If too much pressure is applied, they are crushed and will not recover, and the column then loses resolution and becomes even more sensitive to pressure. When writing a method, set a pressure limit at about 85% of the manufacturer's maximum, with a program override that reduces the flow rate if the pressure is too high. Tick "control the flow rate to avoid overpressure on the column" in the system control/pressure tab. For manual runs, enter the limit in the column-switching valve box yourself. Particles in the column or tubing raise pressure, which is why everything is filtered. Glycerol raises pressure, so lower the flow rate with glycerol buffers. Pre-column pressure is approximately the system pressure; ΔCol is column pressure minus system pressure.

**Storage.**
- All columns are stored in 20% ethanol, which is stable and prevents bacterial growth. Put a column in ethanol if it will not be used for more than a week.
- Salty buffer plus ethanol can precipitate salt in the column, so always wash with water (1.25 CV) before ethanol (1.25 CV).
- Same buffer again the next day: wash with 2–3 CV of buffer and leave it in buffer for one day.
- Different buffer the next day: mix the two buffers in a beaker first, and only go straight from one to the other if nothing precipitates.
- Next use within a week: wash with water and store in water for up to a week.

**Connecting a new column.** Pick the column valve position, run water through the system with the software showing flow through that position but the column unattached (the top line will leak). Put a drop of water in the column's top inlet and connect the top while water is flowing (liquid to liquid, to avoid bubbles). When water starts to leak from the bottom after about a minute, connect the bottom lead; this one does not need to be liquid to liquid. Then run 5 mL of water.

## System parts

- **Pumps:** A (left) and B (right) pump buffer, water and ethanol. Prime whenever you move an inlet into a different liquid or air gets into the lines.
- **Injection valve:** sits between the pumps. Samples are loaded into a loop attached to its two side ports. Loops available: 100 µL, 250 µL [(source says 259 µL)]{.tbc}, 1 mL, 5 mL, and the DynaLoop.
- **Column-switching valve:** in our setup, position 1 is an analytical SEC column (ENrich SEC 650), 2 is a HiPrep S200 26/70 preparative SEC column, 3 is a Nuvia IMAC Ni column, and 5 is an ion-exchange column.
- **UV detector (four wavelengths):**
  - 215 nm: peptide backbone. Peaks first and is most useful when you have little protein, or a protein without Phe, Tyr or Trp; least useful with a lot of protein.
  - 255 nm: nucleic acids.
  - 280 nm: protein (aromatic side chains such as Trp and Phe).
  - 495 nm: GFP and sugars; also detergents, which have a characteristic peak here.
