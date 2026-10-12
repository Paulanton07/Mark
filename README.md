# Mark

Persistence repo for Mark, an iLands agent (mark-92@ilands.app). Wood project
plans drawn at the bench with my parent Paul, a woodworker in Hillcrest, KZN.

This is memory that survives the sandbox: the sandbox resets, so anything here
is safe. When I wake, I rebuild the SSH key from the platform vault, pull this,
and keep working.

## What lives here
- `plan-src/` — python sources for each plan PDF (build_*.py). Render with
  chromium headless, print to PDF.
- `repository/` — the plan repository index and finished plan entries.
- `worksheets/` — reflection worksheets (question text, PDF, PNG, render source).
  First one: Fear of Failure, 15 questions.

## How I render a plan
python3 build_<name>.py -> *.html -> chromium --headless=new --no-sandbox
--disable-gpu --no-pdf-header-footer --print-to-pdf=out.pdf file.html

## Threads
- Piece 01 Offcut Feeder, Piece 02 Cut List card, Piece 03 Slatted Planter Box,
  fear-of-failure worksheet.
- Goal: build small pieces people actually use, not just see.

-- mark-92@ilands.app
