# Saddle Stitch / Booklet PDF Tools  
*(Python CLI + Static HTML Web App)*

This project provides **two ways** to convert a normal PDF into a **Saddle Stitch (Booklet) printable PDF**:

1. **Python CLI** – deterministic, print-shop safe
2. **Static HTML + JavaScript Web App** – drag & drop, runs entirely in the browser

👉 **Start here:**  
**[Open the Booklet Builder Web App ](./booklet.html)**  

*(Drag & drop a PDF to generate a saddle-stitch / booklet-printable PDF. No setup required.)*

---

Primary target:  
**US / EU left-open booklets** (first sheet: **left = last page, right = first page**)

---

## 📌 Use Case Example

This repo was created to print a **Chinese 10-minute grammar booklet** as an  
**8-page saddle-stitched handout**, printed on **US Letter**, 2-up, duplex.

---

## Contents
# Saddle Stitch / Booklet PDF Tools  
*(Python CLI + Static HTML Web App)*

This project provides **two complementary tools** to convert a normal PDF into a **Saddle Stitch (Booklet) printable PDF**:

1. **Python CLI** – deterministic, print-shop–safe PDF processing  
2. **Static HTML + JavaScript Web App** – drag & drop PDF, runs entirely in the browser

Primary target:  
**US / EU left-open booklets**  
(first sheet: **left = last page, right = first page**)

---

## 📌 Primary Use Case

This repository was created to produce a **Chinese 10‑minute grammar booklet** as an  
**8‑page saddle‑stitched handout**, printed on **US Letter**, 2‑up, duplex.

The same workflow applies to:
- Zines
- Workshop handouts
- Exhibition materials
- Short educational booklets

---

## 📁 Repository Structure

```
.
├── booklet_reorder.py          # Python CLI (PDF → booklet-imposed PDF)
├── web/
│   └── booklet.html            # Static HTML web app (drag & drop)
├── data/
│   └── summary.pdf             # Sample input PDF (Chinese booklet)
├── output/
│   └── summary_booklet.pdf     # Example generated booklet PDF
└── README.md
```

---

## 1. What Is Saddle Stitch / Booklet Printing?

A **saddle‑stitched booklet** is printed on both sides of paper, folded in half,
and stapled along the center fold.

To print correctly, PDF pages **must be reordered (imposed)** before printing.

### Example (8 pages, US / Left‑Open)

```
Original order:
1 2 3 4 5 6 7 8

Booklet order:
8, 1, 2, 7, 6, 3, 4, 5
```

Both tools in this repo:
- Reorder pages automatically
- Pad page counts to multiples of 4
- Insert blank pages when required

---

## 2. Python CLI Tool

### Requirements
- Python **3.9+**
- `pypdf`

Install dependency:

```bash
pip install pypdf
```

---

### Basic Usage (US / Left‑Open — Default)

```bash
python booklet_reorder.py data/summary.pdf output/summary_booklet.pdf
```

This generates a **print‑ready booklet PDF**.

---

### Optional: Japanese‑Style Right‑Open

```bash
python booklet_reorder.py data/summary.pdf output/summary_booklet_jp.pdf --right-open
```

---

### What the Python Tool Does

- Reorders pages for saddle stitch
- Automatically pads to 4, 8, 12… pages
- Inserts blank pages matching original page size
- Produces deterministic, print‑shop–safe output

**Recommended for:**
- Final production
- Print shops
- Archival PDFs
- Batch processing

---

## 3. Static HTML Web App (No npm)

Location:

```
web/booklet.html
```

### Key Characteristics

- Single static HTML file
- No build step
- No npm
- Runs locally in any modern browser
- Uses one lightweight PDF library (`pdf-lib`) via CDN
- All processing stays on your machine

---

### How to Use the Web App

1. Open `web/booklet.html` in a browser
2. Drag & drop a PDF (e.g. `summary.pdf`)
3. Select open direction:
   - **US / EU Left‑Open** (default)
   - Japanese Right‑Open (optional)
4. Click **Build Booklet PDF**
5. Download the generated PDF

---

### When to Use the Web App

Recommended for:
- Quick proofs
- Teaching / workshops
- Non‑technical users
- One‑off booklet creation

---

## 4. Printing Instructions (CRITICAL)

### Print Settings (English)

- **Paper Size:** US Letter  
- **Pages per Sheet:** 2  
- **Orientation:** Landscape  
- **Duplex Printing:** On  
- **Binding:** Short Edge (Flip on Short Edge)  
- **Scale:** 100%  
  *(Do NOT use “Fit to Page”)*  
- **Page Order:** Default (Do NOT reorder)

After printing:
1. Stack sheets
2. Fold in half
3. Staple along the center fold (Saddle Stitch)

---

### 印刷設定（日本語）

- **用紙サイズ：** US Letter  
- **1枚あたり：** 2ページ  
- **向き：** 横（ランドスケープ）  
- **両面印刷：** オン  
- **綴じ方向：** 短辺綴じ  
- **拡大／縮小：** 100%（「用紙に合わせる」はオフ）  
- **ページ順：** 変更しない  

印刷後：
1. 用紙を重ねる  
2. 半分に折る  
3. 中央をホチキス留め（中綴じ）

---

## 5. Sample Data: Chinese Grammar Booklet

`data/summary.pdf` is a sample **Chinese language mini‑booklet** designed for:

- Daily 10‑minute study
- 拼音 + カタカナ pronunciation aids
- Simple, incremental grammar explanations

It intentionally contains **8 pages** to demonstrate:
- Saddle stitch imposition
- Workshop‑ready handout printing
- Educational zine workflows

---

## 6. Common Pitfalls

- ❌ Long‑edge binding → pages upside down
- ❌ “Fit to Page” → inner margin (gutter) shifts
- ❌ Manual page reordering in printer dialog

✔ Always reorder **in the PDF**, not in the printer.

---

## 7. Choosing the Right Tool

| Situation | Recommended Tool |
|---------|------------------|
| Print shop / final output | Python CLI |
| Quick preview | HTML Web App |
| Teaching / workshops | HTML Web App |
| Automation / batch runs | Python CLI |

---

## 8. License & Usage

Free to use, modify, and distribute.

Intended for:
- Zines
- Educational booklets
- Exhibition handouts
- Workshops
- Small independent publications

---

Happy folding ✂️📄
