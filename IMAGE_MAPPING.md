# Manuscript Image Mapping

**Date:** January 26, 2026  
**Manuscript:** Amazon_review.tex  
**Images Folder:** /images/

---

## All Figures in Manuscript

| Figure # | Label | Caption | Image File | Status |
|----------|-------|---------|------------|--------|
| 1 | `fig:overall_process` | Overall Process of Proposed Research | `images/EntireProcessModel.png` | ✅ |
| 2 | `fig:traditional_svd` | Process of Traditional Product Recommendation | `images/TraditionalProductRecommendations.png` | ✅ |
| 3 | `fig:proposed_model` | Entire Process of Proposed Model | `images/PipelineFlow.png` | ✅ |
| 4 | `fig:price_dist` | Price Distribution by Category | `images/PriceDistribution.png` | ✅ |
| 5 | `fig:rating_analysis` | Analysis of Average Rating and Best Seller Status | `images/BestSeller.png` | ✅ |
| 6 | `fig:categories` | Top 10 Product Categories by Count | `images/Top10Products.png` | ✅ |
| 7 | `fig:svd_comparison` | Singular Value Comparison (NEW!) | `images/SVDComparison.png` | ✅ NEW |
| 8 | `fig:performance_metrics` | Performance Analysis: MSE and RMSE | `images/proposedMetrics.png` | ✅ NEW |
| 9 | `fig:comparative` | Comparative Analysis with SOTA Methods | `images/ComparativeAnalysis.png` | ✅ NEW |

---

## Available Images Not Yet Used

The following images are in the `images/` folder but not currently referenced in the manuscript:

1. **ModelPerformance.png** - Could replace proposedMetrics.png if preferred
2. **TraditionalSVDModelPerformance.png** - Previously used for RMSE, now replaced

---

## Recent Updates

### Added (New Images)
1. ✅ **SVDComparison.png** - Shows singular value filtering (demonstrates novelty)
2. ✅ **proposedMetrics.png** - Combined MSE/RMSE comparison
3. ✅ **ComparativeAnalysis.png** - SOTA methods comparison

### Replaced
- **MSE Figure (Fig 7):** Separate MSE graph → Combined metrics graph
- **RMSE Figure (Fig 8):** Separate RMSE graph → Removed (now in combined)
- **Added SVD Comparison:** New figure showing threshold filtering

---

## Image Quality Specifications

All images should meet these requirements:
- **Resolution:** 300 DPI minimum
- **Format:** PNG with transparent background (or white)
- **Font sizes:** 12-18pt for labels
- **Dimensions:** 8-16 inches width recommended
- **Color scheme:** Professional (avoid bright colors)

---

## Manuscript Locations

### Section 3.4 (Methodology)
- Figure 1: Overall process (page 3)
- Figure 2: Traditional SVD (page 7)
- Figure 3: Proposed model (page 8)
- **Figure 7: SVD Comparison (page 10)** ← NEW! Shows filtering

### Section 4.2 (EDA)
- Figure 4: Price distribution (page 13)
- Figure 5: Best seller analysis (page 13)
- Figure 6: Top categories (page 14)

### Section 4.3 (Performance)
- **Figure 8: Performance metrics (page 14)** ← UPDATED! Combined MSE/RMSE
- **Figure 9: SOTA comparison (page 15)** ← NEW! All methods

---

## How to Regenerate Images

If you need to regenerate any images:

1. **From Notebook:**
   - Run the corresponding visualization cell
   - Save with: `plt.savefig('images/filename.png', dpi=300, bbox_inches='tight')`

2. **Required Images:**
   - `SVDComparison.png` - From cell showing singular value plot
   - `proposedMetrics.png` - From cell comparing MSE/RMSE
   - `ComparativeAnalysis.png` - From cell comparing all methods

3. **Settings for Consistency:**
   ```python
   matplotlib.rcParams['figure.dpi'] = 300
   matplotlib.rcParams['savefig.dpi'] = 300
   plt.rcParams['font.size'] = 14
   ```

---

## Verification

✅ All 9 figures referenced in manuscript exist in `images/` folder  
✅ All image paths use correct folder name (`images/` not `media/`)  
✅ All figures have proper captions and labels  
✅ New images demonstrate the novelty (filtering, comparison)  

---

## Next Steps

1. ✅ Images mapped and manuscript updated
2. ⏳ **Compile LaTeX** to verify all images render
3. ⏳ **Check image quality** in compiled PDF
4. ✅ Ready for submission (after notebook re-run verification)

---

**Status:** ✅ ALL IMAGES MAPPED AND MANUSCRIPT UPDATED
