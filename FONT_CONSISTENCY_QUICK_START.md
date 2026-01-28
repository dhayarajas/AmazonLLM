# 🎯 Make All Plot Fonts Consistent - 2 Minute Guide

## The Problem
Your notebook has **inconsistent fonts** across different plots:
- Some titles are 16pt, others are 18pt, others 20pt
- Some labels are bold, others aren't
- Different plots use different font families
- Hard to maintain professional appearance

## The Solution (2 Steps)

---

## Step 1: Add Configuration Cell (1 minute)

### Open Your Notebook
```bash
jupyter notebook Proposed_SVD_28_11_24.ipynb
```

### Add a NEW cell at the TOP of your notebook
(After import cells, before first plot)

### Copy this code into the new cell:

```python
# ============================================================================
# GLOBAL FONT CONFIGURATION - Run this ONCE at the start
# ============================================================================
import matplotlib.pyplot as plt
import matplotlib

FONT_CONFIG = {
    'font.family': 'sans-serif',
    'font.sans-serif': ['DejaVu Sans', 'Arial', 'Helvetica'],
    'font.size': 18,
    'axes.titlesize': 26,
    'axes.labelsize': 20,
    'xtick.labelsize': 16,
    'ytick.labelsize': 16,
    'legend.fontsize': 16,
    'axes.titleweight': 'bold',
    'axes.labelweight': 'bold',
    'figure.dpi': 600,
    'savefig.dpi': 600,
    'axes.linewidth': 2,
    'grid.linewidth': 1.5,
    'lines.linewidth': 2.5,
}

plt.rcParams.update(FONT_CONFIG)
matplotlib.rcParams.update(FONT_CONFIG)

print("✅ Consistent fonts applied to ALL plots!")
```

### Run the cell
Click "Run" or press Shift+Enter

---

## Step 2: Clean Up Individual Plots (1 minute)

### Use Find & Replace to Remove Individual Font Settings

Press **Cmd+F** (Mac) or **Ctrl+F** (Windows)

### Remove these patterns (they override global settings):

1. **Find:** `, fontsize=18` → **Replace:** `` (empty)
2. **Find:** `, fontsize=16` → **Replace:** `` (empty)
3. **Find:** `, fontsize=14` → **Replace:** `` (empty)
4. **Find:** `, fontsize=20` → **Replace:** `` (empty)
5. **Find:** `, fontweight='bold'` → **Replace:** `` (empty)

**Click "Replace All" for each**

---

## Step 3: Run All Cells

Click: **Kernel** → **Restart & Run All**

---

## ✅ Done! All Plots Now Have:

| Element | Consistent Setting |
|---------|-------------------|
| **Font Family** | DejaVu Sans (everywhere) |
| **Titles** | 26pt, bold |
| **Axis Labels** | 20pt, bold |
| **Tick Labels** | 16pt |
| **Legends** | 16pt |
| **Line Width** | 2.5pt |
| **DPI** | 600 (high quality) |

---

## 🧪 Quick Verification Test

Add this test cell anywhere to verify consistency:

```python
# Test: All plots should look identical in style
import numpy as np

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8))

# Plot 1
ax1.bar(['A', 'B', 'C'], [10, 20, 15])
ax1.set_title('Plot 1 - Bar Chart')
ax1.set_xlabel('Categories')
ax1.set_ylabel('Values')

# Plot 2  
x = np.linspace(0, 10, 100)
ax2.plot(x, np.sin(x))
ax2.set_title('Plot 2 - Line Chart')
ax2.set_xlabel('X Values')
ax2.set_ylabel('Y Values')

plt.tight_layout()
plt.show()

print("✓ Both plots should have IDENTICAL font sizes and styles!")
```

If both plots look the same (same title size, same label size, same thickness), it's working! ✅

---

## 📊 Before vs After

### Before (Inconsistent):
```
Plot 1: Title 16pt, Labels 14pt, Arial
Plot 2: Title 20pt, Labels 16pt, Helvetica  
Plot 3: Title 18pt, Labels 14pt, DejaVu
❌ All different!
```

### After (Consistent):
```
Plot 1: Title 26pt, Labels 20pt, DejaVu Sans
Plot 2: Title 26pt, Labels 20pt, DejaVu Sans
Plot 3: Title 26pt, Labels 20pt, DejaVu Sans
✅ All identical!
```

---

## 🎨 Customization (Optional)

### Want Smaller Fonts?
Change in config cell:
```python
'font.size': 14,          # Instead of 18
'axes.titlesize': 20,     # Instead of 26
'axes.labelsize': 16,     # Instead of 20
```

### Want Different Font Family?
Change in config cell:
```python
'font.family': 'serif',
'font.serif': ['Times New Roman', 'Georgia'],
```

### Want Thinner Lines?
Change in config cell:
```python
'lines.linewidth': 1.5,   # Instead of 2.5
'axes.linewidth': 1,      # Instead of 2
```

---

## ⚠️ Important Rules

1. **Run config cell FIRST** (before any plots)
2. **Remove individual fontsize parameters** from plot code
3. **Restart kernel if plots still look different**
4. **Don't mix fontsize parameters** with global config

---

## 🚀 Alternative: Copy Entire Setup

If you want the complete setup with helper functions, see:
- `QUICK_FONT_CONSISTENCY_SETUP.py` - Copy this entire file content
- `CONSISTENT_FONT_CONFIGURATION.md` - Full documentation

---

## 📝 What Changed?

### In Your Notebook:
- ✅ Added 1 configuration cell (20 lines)
- ✅ Removed fontsize parameters from plots
- ✅ All plots now use same settings

### Result:
- ✅ Professional consistency
- ✅ Easy to maintain
- ✅ Change once, applies everywhere
- ✅ No more manual font setting per plot

---

## ✨ Benefits

1. **Consistency** - All plots look uniform
2. **Maintainability** - Change once, affects all plots
3. **Professional** - Publication-ready appearance
4. **Time-Saving** - No more tweaking individual plots
5. **Quality** - 600 DPI, proper sizing

---

**Time Required:** 2 minutes  
**Difficulty:** Very Easy  
**Impact:** High - Complete visual consistency  
**Status:** Ready to implement

---

## 📞 Troubleshooting

**Problem:** Plots still look different
- **Solution:** Make sure config cell runs BEFORE plot cells
- Try: Kernel → Restart & Run All

**Problem:** Fonts are too big/small
- **Solution:** Adjust sizes in FONT_CONFIG dictionary

**Problem:** Some plots ignore settings
- **Solution:** Check for individual fontsize parameters and remove them

---

**Next Step:** Open your notebook and add the configuration cell! 🚀
