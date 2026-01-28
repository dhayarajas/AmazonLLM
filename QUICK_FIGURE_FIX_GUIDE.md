# 🚀 QUICK FIGURE FIX - 5 Minute Guide

## The Problem
Your figures have small fonts and low resolution - hard to read in print.

## The Solution (3 Simple Steps)

### Step 1: Open Your Notebook
```bash
jupyter notebook Proposed_SVD_28_11_24.ipynb
```

### Step 2: Find & Replace (Do These 3 Replacements)

**Press Cmd+F (Mac) or Ctrl+F (Windows) to open Find & Replace**

#### Replace #1: Increase DPI
- **Find:** `= 300`
- **Replace:** `= 600`
- **Click:** "Replace All" (should find ~4 matches)

#### Replace #2: Increase Figure Size  
- **Find:** `figsize=(14, 8)`
- **Replace:** `figsize=(18, 10)`
- **Click:** "Replace All"

Then:
- **Find:** `figsize=(16, 8)`
- **Replace:** `figsize=(20, 10)`
- **Click:** "Replace All"

Then:
- **Find:** `figsize=(12, 8)`  
- **Replace:** `figsize=(15, 10)`
- **Click:** "Replace All"

Then:
- **Find:** `figsize=(10, 6)`
- **Replace:** `figsize=(14, 9)`
- **Click:** "Replace All"

#### Replace #3: Enable Saving
- **Find:** `#plt.savefig(`
- **Replace:** `plt.savefig(`
- **Click:** "Replace All" (should find ~10 matches)

### Step 3: Run All Cells
- Click: **Kernel** → **Restart & Run All**
- Wait 2-3 minutes for completion
- Check `media/` folder for new high-quality PNGs

---

## ✅ Done!

Your figures are now:
- **2x higher resolution** (600 DPI instead of 300)
- **30% larger** (easier to see details)
- **Automatically saved** to media folder

---

## Font Size Bonus (Optional but Recommended)

If you want even bigger fonts, also do:

**Find:** `'font.size': 14`  
**Replace:** `'font.size': 18`

**Find:** `'axes.titlesize': 16`  
**Replace:** `'axes.titlesize': 24`

**Find:** `'axes.labelsize': 14`  
**Replace:** `'axes.labelsize': 20`

**Find:** `fontsize=18`  
**Replace:** `fontsize=24`

**Find:** `fontsize=16`  
**Replace:** `fontsize=20`

Then run all cells again.

---

## Verification

After running, check one of your saved figures:
1. Right-click any PNG in `media/` folder
2. Select "Get Info" (Mac) or "Properties" (Windows)
3. Look at dimensions - they should be 2x larger
4. Open the PNG - text should be clear and large

**Example:**
- Before: 4200 x 2400 pixels, ~300 KB
- After: 7200 x 4800 pixels, ~1.2 MB ✅

---

## Troubleshooting

**Problem:** Find & Replace doesn't find matches
- **Solution:** Make sure you're searching in "All Cells" not just "Current Cell"

**Problem:** Notebook crashes when running
- **Solution:** Restart kernel and run cells one-by-one instead of all at once

**Problem:** Figures not saving
- **Solution:** Check if `media/` folder exists, create it if needed:
  ```python
  from pathlib import Path
  Path('media').mkdir(exist_ok=True)
  ```

---

**Total Time:** 5 minutes
**Difficulty:** Very Easy  
**Result:** Professional publication-quality figures! 🎉
