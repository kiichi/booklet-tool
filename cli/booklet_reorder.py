#!/usr/bin/env python3
"""
booklet_reorder.py
Reorder a PDF for saddle-stitch / booklet printing.

Default: LEFT-OPEN (US/EU) booklet
- First sheet "front" spread becomes: [last_page | page_1]
  e.g. 8-page => 8,1,2,7,6,3,4,5

Optional: RIGHT-OPEN (JP-style) booklet via --right-open
- First sheet "front" spread becomes: [page_1 | last_page]
"""

from __future__ import annotations

import argparse
from pathlib import Path

try:
    from pypdf import PdfReader, PdfWriter
except ImportError:
    raise SystemExit("Missing dependency: pypdf\nInstall with: pip install pypdf")


def booklet_order_left_open(n: int) -> list[int | None]:
    """
    US/EU style (left-open):
    First outer spread: [last | 1]
    """
    if n <= 0:
        return []

    m = ((n + 3) // 4) * 4  # pad to multiple of 4

    def idx(i: int) -> int | None:
        return i if i < n else None

    order: list[int | None] = []
    left = 0
    right = m - 1

    while left < right:
        # Sheet front (outside): [right, left]
        order.append(idx(right))
        order.append(idx(left))
        # Sheet back (inside): [left+1, right-1]
        order.append(idx(left + 1))
        order.append(idx(right - 1))

        left += 2
        right -= 2

    return order


def booklet_order_right_open(n: int) -> list[int | None]:
    """
    JP style (right-open):
    First outer spread: [1 | last]
    """
    if n <= 0:
        return []

    m = ((n + 3) // 4) * 4

    def idx(i: int) -> int | None:
        return i if i < n else None

    order: list[int | None] = []
    left = 0
    right = m - 1

    while left < right:
        # Sheet front (outside): [left, right]
        order.append(idx(left))
        order.append(idx(right))
        # Sheet back (inside): [right-1, left+1]
        order.append(idx(right - 1))
        order.append(idx(left + 1))

        left += 2
        right -= 2

    return order


def add_blank_like(writer: PdfWriter, ref_page) -> None:
    w = float(ref_page.mediabox.width)
    h = float(ref_page.mediabox.height)
    writer.add_blank_page(width=w, height=h)


def main() -> None:
    ap = argparse.ArgumentParser(description="Reorder PDF pages for booklet printing.")
    ap.add_argument("input_pdf", type=Path, help="Input PDF path")
    ap.add_argument("output_pdf", type=Path, help="Output PDF path")
    ap.add_argument(
        "--right-open",
        action="store_true",
        help="Right-open (Japanese-style). Default is left-open (US/EU).",
    )
    args = ap.parse_args()

    if not args.input_pdf.exists():
        raise SystemExit(f"Input not found: {args.input_pdf}")

    reader = PdfReader(str(args.input_pdf))
    n = len(reader.pages)
    if n == 0:
        raise SystemExit("Input PDF has 0 pages.")

    order = booklet_order_right_open(n) if args.right_open else booklet_order_left_open(n)

    writer = PdfWriter()
    ref_page = reader.pages[0]

    for p in order:
        if p is None:
            add_blank_like(writer, ref_page)
        else:
            writer.add_page(reader.pages[p])

    args.output_pdf.parent.mkdir(parents=True, exist_ok=True)
    with open(args.output_pdf, "wb") as f:
        writer.write(f)

    padded_to = ((n + 3) // 4) * 4
    mode = "RIGHT-OPEN (JP)" if args.right_open else "LEFT-OPEN (US/EU)"
    print("Done.")
    print(f"Mode       : {mode}")
    print(f"Input pages : {n}")
    print(f"Output pages: {padded_to}")
    print(f"Saved to    : {args.output_pdf}")


if __name__ == "__main__":
    main()