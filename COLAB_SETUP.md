# Colab Setup Instructions

## Overview
The notebooks have been updated to automatically detect if they're running in Google Colab and clone the GitHub repository if needed. This ensures all files are available in the Colab environment.

## How It Works

### Automatic Detection
The first cell automatically:
1. **Detects the environment** (Colab vs Local)
2. **If in Colab**: Clones the repository from GitHub
3. **If local**: Uses your local file paths
4. **Sets up paths** automatically

### Repository Information
- **GitHub URL**: https://github.com/dhayarajas/AmazonLLM
- **Repository Name**: AmazonLLM
- **Cloned Location in Colab**: `/content/AmazonLLM/`

## Usage

### In Google Colab

1. **Open the notebook** in Colab
2. **Run the first cell** - it will automatically:
   - Detect you're in Colab
   - Clone the repository (if not already present)
   - Set up all paths
   - Verify files exist

3. **Expected output:**
   ```
   ✓ Detected: Running in Google Colab
   📥 Cloning repository from https://github.com/dhayarajas/AmazonLLM.git...
   ✓ Successfully cloned repository to AmazonLLM/
   ✓ Using Colab repository directory: AmazonLLM
   
   Base directory: AmazonLLM
   Dataset directory exists: True
   Results directory exists: True
   
   Found 4 CSV files in Dataset/:
     - amazon_categories.csv
     - amazon_products.csv
     - merged_df.csv
     - new_LLM_data.csv
   ```

### If Git Clone Fails

If the automatic git clone fails, you can manually clone:

1. **Create a new cell** and run:
   ```python
   !git clone https://github.com/dhayarajas/AmazonLLM.git
   ```

2. **Then re-run the first cell**

### Local Usage

When running locally, the notebook will:
- Detect it's not in Colab
- Use your local file paths
- Work with files in `/Users/dhaya/PhD/Learnings/Amazon-LLM/`

## Repository Structure

After cloning, the structure in Colab will be:
```
/content/
  └── AmazonLLM/
      ├── Dataset/
      │   ├── amazon_categories.csv
      │   ├── amazon_products.csv
      │   ├── merged_df.csv
      │   └── new_LLM_data.csv
      ├── results/
      │   ├── metrics.npy
      │   └── metrics_proposed.npy
      ├── Proposed_SVD_28_11_24.ipynb
      └── Traditional_SVD_28_11_24.ipynb
```

## Features

✅ **Automatic environment detection**
✅ **Automatic repository cloning in Colab**
✅ **Repository updates on subsequent runs**
✅ **Works seamlessly in both Colab and local environments**
✅ **Clear error messages if something goes wrong**

## Troubleshooting

### Issue: "Git clone failed"
**Solution**: Run manually in a new cell:
```python
!git clone https://github.com/dhayarajas/AmazonLLM.git
```

### Issue: "Repository already exists"
**Status**: This is normal! The notebook will use the existing repository.

### Issue: "Dataset directory not found"
**Solution**: 
1. Check that the repository was cloned successfully
2. Verify the Dataset folder exists in the repository on GitHub
3. Run `!ls AmazonLLM/` to see what was cloned

### Issue: Files are outdated
**Solution**: The notebook automatically runs `git pull` to update. If that fails, manually run:
```python
!cd AmazonLLM && git pull
```

## Notes

- The repository is cloned to `/content/AmazonLLM/` in Colab
- All subsequent file operations use paths relative to this directory
- The notebook automatically changes to the repository directory
- Files are read from the cloned repository, not from your local machine

## Benefits

1. **No manual setup needed** - Everything is automatic
2. **Always up-to-date** - Repository is updated on each run
3. **Works everywhere** - Same notebook works in Colab and locally
4. **Version controlled** - Uses GitHub as the source of truth
