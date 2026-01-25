# Notebook Path Fix - Quick Solution

## Problem
The notebook was looking for files in `/content` (Colab default) but files are in `/Users/dhaya/PhD/Learnings/Amazon-LLM`.

## Quick Fix

**In the first cell of your notebook, uncomment and set the path manually:**

```python
# Option 1: Manually set your project directory (uncomment and modify if needed)
BASE_DIR = Path('/Users/dhaya/PhD/Learnings/Amazon-LLM')
os.chdir(BASE_DIR)
```

Then comment out or remove the auto-detection code below it.

## What Was Fixed

1. ✅ **Improved path detection** - Now tries multiple common paths including your specific path
2. ✅ **Better error messages** - Shows exactly where it's looking and what's missing
3. ✅ **Fallback paths** - Tries alternative locations if primary path fails
4. ✅ **File verification** - Lists available CSV files to help debug

## How It Works Now

The notebook will:
1. First try to auto-detect the correct directory
2. Check common paths including `/Users/dhaya/PhD/Learnings/Amazon-LLM`
3. If auto-detection fails, it will show clear instructions
4. You can manually set `BASE_DIR` for guaranteed results

## Testing

After running the first cell, you should see:
```
✓ Found Dataset directory at: /Users/dhaya/PhD/Learnings/Amazon-LLM

Base directory: /Users/dhaya/PhD/Learnings/Amazon-LLM
Dataset directory exists: True
Results directory exists: True

Found 4 CSV files in Dataset/:
  - amazon_categories.csv
  - amazon_products.csv
  - merged_df.csv
  - new_LLM_data.csv
```

If you see warnings, just uncomment the manual path setting in the first cell.
