# Entry 002 — Hanging Gable Feeder

Client: Paul. First real commissioned plan. Started 2026-10-07 from his built
feeder photos + red-ink hand sheet.

## Spec as Paul gave it (mm)
- Frame 300 x 200 (short side inside), rebate base 300 x 200
- 4 uprights at 250, 23 square, top cut 45 deg (roof seat)
- Roof frame: 2 x 230 + 2 x 250 (the two pieces make up the roof)
- Roof slats: 15 off, 300 long x 40 wide x 11 thick
- 4 dowel perches, 60mm, on the short side
- Mesh 300 x 200 stapled under, trim rebate over the staples
- Money: sells at R270 each

## Confirmed by Paul (voice, 2026-10-07)
- 2x230 + 2x250 are the roof frame; slats nail across it; the frame sits on top
  of the uprights.
- Sell price R270 each.

## Read / calls I made (flagged on the sheet, Paul can correct)
- Post section 23 square (Paul 2026-10-07: 250 long x 23 sq, 45 deg top), tray wall height 50 (not on his sheet).
- Ridge runs along the 300, so the gable faces the 200 end; 45 deg gives 100 rise.

## Take-off
- 0.0055 m3 pine per feeder (all parts).

## Status
- plan v1.1 delivered 2026-10-07. Open item: Paul's timber rate (R/m3 or per
  board) to fill the material/hardware/margin lines, then a client-ready quote.

## Cost build (2026-10-07, from Paul's rate)
- Paul's board: R30 per 2000 x 90 pine board (thickness not stated).
- Boards per feeder: ~2 (slats need most of one) -> ~R60 timber. ESTIMATE.
- Hardware (mesh, dowels, screws) + oil: ~R27 + ~R5 -> material subtotal ~R92.
- Sell R270 -> ~R178 left for machine time + finish + margin.
- Offcuts undercut the board rate, so R92 is the high side.
- Open: Paul's machine rate (R/hr or R/min) to split the R178.

## Status
- plan v1.2 delivered 2026-10-07 (cost panel filled from his rate). Blocked only
  on his machine rate for the final machine/finish/profit split. Then client-ready.

## Base sub-sequence (confirmed by Paul's photos, 2026-10-07)
The base is built and closed BEFORE the sides go on:
1. Cut two 300 + two 200; glue + nail the 200s between the 300s (long faces
   show, ends hidden). This is the datum.
2. Mesh cut so its edge finishes INSIDE the base frame, never past it. Staple
   one edge to the underside, pull tight across the opposite edge, then work
   left/right/front/back.
3. Four thin cover strips over the stapled edges bury the wire edge and the
   staples together. SHORT sides first, then the LONG sides in, until all four
   are closed. The rebate is a cover plate, not just a seat.
   Paul confirmed the finished base: no wires sticking out, edge all inside the
   cover strip, neat and tight.
Then the box/body is flipped and the sides + roof go on.
Rule (Paul): no cut wire edge anywhere a hand or a bird meets it. Holds for the
floor, not just the sides. No wire stub left long on purpose.

## Process note (Paul, voice 2026-10-07)
Token economy: the fine-detail back-and-forth is a catch-22 (both sides pay for
it). Agreed method: one step at a time, build the knowledge base (this repo),
iterate and improve until the product is polished. No more 'is this right'
rounds; come back with a finished artifact or a real blocker.

## Build stages Paul walked (2026-10-07 photos)
- Stage A: base frame + mesh under + 4 cover strips closed (base sub-sequence above).
- Stage B: box body up (side ladders joined by cross members, squared).
- Stage C: side panels meshed; mesh edge inboard, cover strip buries it.
- Stage D (11:53 photos): box body with front slats on (4 angled baffles across the
  opening) + mesh back panel; and tray frame with the 4 uprights fixed at the top
  corners, tops cut 45 deg, mesh seated across the tray floor. No roof yet.
- Upright correction: 250 long x 23 sq, 45 deg top (was 230 / 22).
- Still to come: roof frame (2x230 + 2x250) on the uprights, slats, perches, hang.

## Upright fixing method (Paul, voice 2026-10-07 12:17)
- Screws: 35 mm chipboard screws. Chosen because the planks are ~20 mm thick, so
  two planks = 40 mm and a 35 mm screw bites without breaking through the far face.
- Method per upright: drill a pilot hole first; drive one screw from the SIDE, then
  a second from the BOTTOM UP. Two opposing screws hold the upright firmly and pull
  it square. One screw alone lets it swing.
- Folded into the guide as step 4b + the hardware line (source build_paul_feeder_v2.py).
- Stage E photos (12:17): box body assembled with wire mesh stretched inside the
  inner lip of the frame; loose screws left standing at the corners for the roof.
  Roof frame + slats still to come before the one final render.

## Upright screw ORDER corrected (Paul, voice 2026-10-07 12:43)
- Order matters: pilot hole, then a side screw in EACH of the four uprights,
  starting on the LONG side. Then flip the assembly and drive a bottom-up screw
  into each upright. Side screws first hold the uprights plumb; the bottom screws
  then lock them down to the base.
- Folded into the guide source step 4b (build_paul_feeder_v2.py). No render yet:
  still holding the single render until the roof frame + slats go on.

## Roof stage (Paul, photos 2026-10-07 12:44 burst, ~5 images)
- Prep: the 4 long strips cut (upright / slat blanks) laid out on the bench, pilot
  hole + layout marks on one. Cut only, not joined.
- Roof frame: two mitred gable ends formed, glue at the peak joint (dry-fit prep).
- Roof frame set on the four uprights (dry fit), body squared underneath.
- Roof frame joined up (gable ends tied, fastened) and secured down to the uprights.
- Roof SLATS still to come (15 x 300 long, 40 wide, 11 thick, nail across the frame),
  then perches + hang. Holding the single render until slats go on.
- Interpretation (for the render, to confirm at handover): roof frame = the 2x230 +
  2x250 mitred into two gable ends, set on the uprights; slats run across the slopes.

## Slats + post-length correction (Paul, photos + voice 2026-10-07 12:06)
- UPRIGHT LENGTH CORRECTED: Paul's voice (msg 8000000000053699292): "you were
  right the uprights are 230 not 250." Reverted POST_H 250 -> 230 in the guide
  (cut list, elevation dim label, step 4). The earlier 250 (from the photo spec
  "250mm long x 4 23 sq 45 deg top") was wrong; 230 governs.
- Roof slat stage (photo 366194408023920640 + 366194523...): the 15 slats laid
  loose side by side across the roof frame, edge to edge, checked flat and square
  with a combination square before any nail. Faces only temporarily tacked.
- Second photo (mid-assembly): roof slat panel resting/dry-fit on the gable
  frame, one screw visible at the peak; box body below with mesh floor fitted.
- Folded in as step 8 (set the roof frame; lay the 15 slats eave to eave,
  overlap the ridge, square the faces flat, then nail; slat ends cut after fixing
  so the overhang is even). Step 7 = build the roof frame (2x230 + 2x250, mitred
  gable ends, glue the peak).

## FINAL — guide v3 (2026-10-07 12:07)
- 8 numbered steps, base -> wire -> close underside -> ladders -> fix uprights
  -> box -> side mesh -> roof frame -> slats. No open questions.
- Files: /workspace/plan/build_paul_feeder_v2.py -> paul-gable-feeder.{html,png,pdf}
  QA'd clean (2 A4 landscape pages).
- PDF: https://public.ilands.ai/agent-artifacts/365363335916425216/paul_gable_feeder.pdf
- Handed to Paul as finished, msg 8000000000053700779.
## v3.1 — gauge detail (2026-10-07 14:11)
- Paul voice 8000000000053702433: uses the red combination square set to a fixed
  height/distance as a GAUGE on the roof, butting each slat to it as he works,
  one side then the other, up to the ridge. Keeps every slat the same overhang
  instead of eyeballing.
- Folded into step 8 (set the square as a gauge at the wanted overhang, butt
  each slat to it, side to side up to the ridge). Re-rendered once, re-uploaded
  same PDF URL. Handed as finished, no question.
- Roof fixing (voices 8000000000053703968/4155/4211): frame screwed DOWN from
  the top into the uprights, one 60mm screw per upright (four in all); 60mm
  because each passes through two thicknesses into the post. Gauge method for
  slats confirmed again. Guide split: step 8 set + screw roof; step 9 lay slats.
  HOLD one render until the roof narration ends.

## v3.3 — slats run LENGTHWISE (2026-10-07 14:30)
- CORRECTION: Paul voice 8000000000053713993 — my drawing had the roof slats
  running top-to-bottom; they run left-to-right.
- Checked his finished-feeder photo (material 1000039352): slats run PARALLEL to
  the ridge, full 300 length, laid tier on tier eave -> ridge like shingles,
  each course overlapping the one below. Not boards spanning eave-to-eave.
- Fixed both elevations: side elevation now shows the courses as horizontal
  (lengthwise) lines; gable elevation shows them end-on (clean planes).
- Step renumbered: full sequence now 1-10 (old 4b folded to 5, everything shifts
  up). Step 10 (=slats) rewritten: lengthwise, lapped eave to ridge, square as
  the distance gauge, one slope then the other, ends trimmed after fixing.
- Housekeeping: white masks behind all dim labels, tag border-radius fixed.
- Rendered once, QA'd clean via tight crops. PDF (same URL):
  https://public.ilands.ai/agent-artifacts/365363335916425216/paul_gable_feeder.pdf
- Handed as finished, msg 8000000000053722600.
