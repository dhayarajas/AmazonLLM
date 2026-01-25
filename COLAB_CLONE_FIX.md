# Colab Git Clone Timeout Fix

## Problem
The automatic git clone times out after 30 minutes due to large files in the repository.

## Solution: Manual Clone (Recommended)

### Step 1: Clone Manually
Run this in a **new cell** in Colab (before running the first cell):

```python
!git clone --depth 1 https://github.com/dhayarajas/AmazonLLM.git
```

**OR** for full clone (if shallow clone doesn't work):

```python
!git clone https://github.com/dhayarajas/AmazonLLM.git
```

**Benefits of manual clone:**
- ✅ Shows real-time progress
- ✅ No timeout limit
- ✅ You can see what's happening

### Step 2: Re-run the First Cell
After the manual clone completes, re-run the first cell (Cell 0). It will:
- Detect that the repository already exists
- Skip the clone step
- Continue with path setup

## Alternative: If Clone Still Fails

### Option 1: Use Git LFS (if large files are tracked with Git LFS)
```python
!git lfs install
!git clone --depth 1 https://github.com/dhayarajas/AmazonLLM.git
```

### Option 2: Upload Files Directly
1. Upload `Dataset/merged_df.csv` directly to Colab
2. Create the directory structure manually
3. Skip the git clone entirely

### Option 3: Use Google Drive
1. Clone to Google Drive (persistent storage)
2. Create a symlink or copy files to Colab workspace

## What Changed in the Notebooks

1. **Increased timeouts:**
   - Shallow clone: 10 min → 30 min
   - Full clone: 20 min → 60 min

2. **Better detection:**
   - Checks if Dataset directory exists before cloning
   - Handles partial clones gracefully
   - Tries to update existing repository instead of re-cloning

3. **Clearer instructions:**
   - Shows manual clone commands when timeout occurs
   - Provides step-by-step guidance

## Quick Fix Commands

If you're stuck with a timeout, run these in order:

```python
# 1. Check if repository exists
import os
from pathlib import Path
if Path('AmazonLLM').exists():
    print("Repository exists")
    print(f"Dataset exists: {(Path('AmazonLLM') / 'Dataset').exists()}")
else:
    print("Repository not found - need to clone")

# 2. Manual clone (if needed)
# !git clone --depth 1 https://github.com/dhayarajas/AmazonLLM.git

# 3. Verify files
if Path('AmazonLLM/Dataset/merged_df.csv').exists():
    print("✓ Dataset file found!")
else:
    print("✗ Dataset file not found")
```

## Notes

- The repository contains large files (~273 MB for merged_df.csv)
- Shallow clone (`--depth 1`) is faster but may miss some files
- Full clone is more reliable but takes longer
- Manual clone is the most reliable method for large repositories
