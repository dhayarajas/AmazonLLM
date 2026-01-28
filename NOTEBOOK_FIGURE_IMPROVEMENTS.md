# High-Quality Figure Improvements for Notebook

## Overview
This document contains the updated code to improve all figures in the notebook with:
- **Higher Resolution**: DPI 600 (instead of 300)
- **Larger Font Sizes**: 30-50% increase for better readability
- **Larger Figure Sizes**: Optimized dimensions for publication
- **Enabled Figure Saving**: Uncommitted all savefig commands

## Changes Needed

### 1. Update Global Matplotlib Parameters (Cell ~13)

**FIND THIS CODE:**
```python
matplotlib.rcParams['figure.dpi'] = 300
matplotlib.rcParams['savefig.dpi'] = 300
matplotlib.rcParams['savefig.bbox'] = 'tight'
plt.rcParams.update({
    'font.size': 14,
    'axes.titlesize': 16,
    'axes.labelsize': 14,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
    'legend.fontsize': 12,
    'figure.titlesize': 18
})
```

**REPLACE WITH:**
```python
# HIGH-QUALITY PUBLICATION SETTINGS - DPI 600, LARGER FONTS
matplotlib.rcParams['figure.dpi'] = 600  # ← INCREASED from 300
matplotlib.rcParams['savefig.dpi'] = 600  # ← INCREASED from 300
matplotlib.rcParams['savefig.bbox'] = 'tight'
matplotlib.rcParams['savefig.pad_inches'] = 0.2
plt.rcParams.update({
    'font.size': 18,           # ← INCREASED from 14
    'axes.titlesize': 24,       # ← INCREASED from 16
    'axes.labelsize': 20,       # ← INCREASED from 14
    'xtick.labelsize': 16,      # ← INCREASED from 12
    'ytick.labelsize': 16,      # ← INCREASED from 12
    'legend.fontsize': 16,      # ← INCREASED from 12
    'figure.titlesize': 26,     # ← INCREASED from 18
    'axes.linewidth': 2,        # ← NEW: Thicker axes
    'grid.linewidth': 1.5,      # ← NEW: Thicker grid
    'lines.linewidth': 2.5,     # ← NEW: Thicker lines
    'xtick.major.width': 2,     # ← NEW: Thicker ticks
    'ytick.major.width': 2,     # ← NEW: Thicker ticks
    'xtick.major.size': 8,      # ← NEW: Larger ticks
    'ytick.major.size': 8,      # ← NEW: Larger ticks
})
```

### 2. Update Figure 1: Top 10 Categories

**FIND:**
```python
plt.figure(figsize=(14, 8))
```

**REPLACE WITH:**
```python
plt.figure(figsize=(18, 10))  # ← INCREASED for better readability
```

**FIND:**
```python
#plt.savefig(output_dir / 'image6.png', dpi=300, bbox_inches='tight')
```

**REPLACE WITH:**
```python
plt.savefig(output_dir / 'image6.png', dpi=600, bbox_inches='tight')  # ← UNCOMMENTED & DPI 600
```

### 3. Update Figure 2: Price Distribution

**FIND:**
```python
plt.figure(figsize=(16, 8))
```

**REPLACE WITH:**
```python
plt.figure(figsize=(20, 10))  # ← INCREASED for better readability
```

**FIND:**
```python
# plt.savefig(output_dir / 'image4.png', dpi=300, bbox_inches='tight')
```

**REPLACE WITH:**
```python
plt.savefig(output_dir / 'image4.png', dpi=600, bbox_inches='tight')  # ← UNCOMMENTED & DPI 600
```

### 4. Update Figure 3: Rating Analysis

**FIND:**
```python
plt.figure(figsize=(12, 8))
```

**REPLACE WITH:**
```python
plt.figure(figsize=(14, 10))  # ← INCREASED for better readability
```

**FIND:**
```python
# plt.savefig(output_dir / 'image5.png', dpi=300, bbox_inches='tight')
```

**REPLACE WITH:**
```python
plt.savefig(output_dir / 'image5.png', dpi=600, bbox_inches='tight')  # ← UNCOMMENTED & DPI 600
```

### 5. Update Figure 4: Singular Values Comparison

**FIND:**
```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
```

**REPLACE WITH:**
```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8))  # ← INCREASED for better readability
```

**FIND:**
```python
# plt.savefig(output_dir / 'singular_values_comparison.png', dpi=300, bbox_inches='tight')
```

**REPLACE WITH:**
```python
plt.savefig(output_dir / 'singular_values_comparison.png', dpi=600, bbox_inches='tight')  # ← UNCOMMENTED & DPI 600
```

### 6. Update Figure 5: Proposed Metrics

**FIND:**
```python
plt.figure(figsize=(10, 6))
```

**REPLACE WITH:**
```python
plt.figure(figsize=(14, 10))  # ← INCREASED for better readability
```

**FIND:**
```python
# plt.savefig(output_dir / 'proposed_metrics.png', dpi=300, bbox_inches='tight')
```

**REPLACE WITH:**
```python
plt.savefig(output_dir / 'proposed_metrics.png', dpi=600, bbox_inches='tight')  # ← UNCOMMENTED & DPI 600
```

### 7. Update Figure 6: MSE Comparison

**FIND:**
```python
plt.figure(figsize=(10, 8))
```

**REPLACE WITH:**
```python
plt.figure(figsize=(14, 10))  # ← INCREASED for better readability
```

**FIND:**
```python
# plt.savefig(output_dir / 'image7.png', dpi=300, bbox_inches='tight')
```

**REPLACE WITH:**
```python
plt.savefig(output_dir / 'image7.png', dpi=600, bbox_inches='tight')  # ← UNCOMMENTED & DPI 600
```

### 8. Update Figure 7: RMSE Comparison

**FIND:**
```python
plt.figure(figsize=(10, 8))
```

**REPLACE WITH:**
```python
plt.figure(figsize=(14, 10))  # ← INCREASED for better readability
```

**FIND:**
```python
# plt.savefig(output_dir / 'image8.png', dpi=300, bbox_inches='tight')
```

**REPLACE WITH:**
```python
plt.savefig(output_dir / 'image8.png', dpi=600, bbox_inches='tight')  # ← UNCOMMENTED & DPI 600
```

### 9. Update Figure 8: SOTA Comparison

**FIND:**
```python
plt.figure(figsize=(14, 8))
```

**REPLACE WITH:**
```python
plt.figure(figsize=(18, 10))  # ← INCREASED for better readability
```

**FIND:**
```python
# plt.savefig(output_dir / 'image9.png', dpi=300, bbox_inches='tight')
```

**REPLACE WITH:**
```python
plt.savefig(output_dir / 'image9.png', dpi=600, bbox_inches='tight')  # ← UNCOMMENTED & DPI 600
```

### 10. Update Additional Analysis Figures

For any remaining figures (threshold sensitivity, frobenius norm, energy distribution):

**Pattern to find:**
```python
figsize=(X, Y)
```

**Increase by ~25-30%:**
```python
figsize=(X*1.3, Y*1.3)  # Round to nearest whole number
```

**Pattern to find:**
```python
# plt.savefig(...)
```

**Uncomment and update DPI:**
```python
plt.savefig(..., dpi=600, bbox_inches='tight')
```

## Quick Implementation Steps

1. **Open the notebook** in Jupyter/Colab
2. **Use Find & Replace (Ctrl/Cmd + F)** to locate each pattern
3. **Replace systematically** following the patterns above
4. **Run all cells** to regenerate figures
5. **Check the `media/` or `images/` folder** for high-quality outputs

## Expected Results

After applying all changes:

| Aspect | Before | After | Improvement |
|--------|--------|-------|-------------|
| **DPI** | 300 | 600 | 2x resolution |
| **Title Font** | 16-18 | 24-26 | 44% larger |
| **Axis Labels** | 14 | 20 | 43% larger |
| **Tick Labels** | 12 | 16 | 33% larger |
| **Figure Width** | 10-16" | 14-20" | ~30% larger |
| **Figure Height** | 6-8" | 8-10" | ~25% larger |
| **Line Width** | 1.0 | 2.5 | 2.5x thicker |
| **Saved Files** | Not saved | Saved at 600 DPI | ✓ Enabled |

## File Size Impact

⚠️ **Note:** High-resolution figures will be larger:
- **Before**: ~200-400 KB per figure (300 DPI)
- **After**: ~800-1600 KB per figure (600 DPI)
- **Total increase**: ~3-5x file size

This is **expected and normal** for publication-quality figures.

## Verification Checklist

After updates, verify:
- [ ] All figures display correctly in notebook
- [ ] Font sizes are clearly readable
- [ ] Axis labels are not cut off
- [ ] Figures are saved to `media/` or `images/` folder
- [ ] Saved PNG files are high resolution (check file properties)
- [ ] Grid lines are visible but not overwhelming
- [ ] Color contrast is maintained

## Alternative: Automated Update

If you prefer automated updates, you can use the standalone script:
```bash
python improved_figures_high_quality.py
```

This will generate all figures directly without modifying the notebook.

---

**Last Updated:** 2026-01-27
**Status:** Ready for implementation
**Estimated Time:** 15-20 minutes for manual updates
