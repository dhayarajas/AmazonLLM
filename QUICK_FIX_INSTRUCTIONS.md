# Quick Fix for FileNotFoundError

## The Problem
The notebook is looking in `/content` but your files are in `/Users/dhaya/PhD/Learnings/Amazon-LLM`.

## The Solution (Already Applied!)

I've updated both notebooks to **automatically use the correct path**. The first cell now has:

```python
BASE_DIR = Path('/Users/dhaya/PhD/Learnings/Amazon-LLM')
os.chdir(BASE_DIR)
```

This is now **uncommented and active** by default.

## What to Do

1. **Restart your kernel** (important!)
   - In Colab: Runtime → Restart runtime
   - Or click the restart button

2. **Run the first cell again**
   - It should now show: `✓ Using manually set BASE_DIR: /Users/dhaya/PhD/Learnings/Amazon-LLM`

3. **Continue with the rest of the notebook**

## Verification

After running the first cell, you should see:
```
✓ Using manually set BASE_DIR: /Users/dhaya/PhD/Learnings/Amazon-LLM

Base directory: /Users/dhaya/PhD/Learnings/Amazon-LLM
Dataset directory exists: True
Results directory exists: True

Found 4 CSV files in Dataset/:
  - amazon_categories.csv
  - amazon_products.csv
  - merged_df.csv
  - new_LLM_data.csv

Current working directory: /Users/dhaya/PhD/Learnings/Amazon-LLM
```

If you see this, everything is working! ✅

## If It Still Doesn't Work

1. Make sure you **restarted the kernel** after the update
2. Check that the path `/Users/dhaya/PhD/Learnings/Amazon-LLM` is correct for your system
3. Verify the Dataset folder exists at that location

## Files Updated

- ✅ `Proposed_SVD_28_11_24.ipynb` - First cell now sets path automatically
- ✅ `Traditional_SVD_28_11_24.ipynb` - First cell now sets path automatically

Both notebooks are ready to use!
