# Notebook Local Setup Guide

Both notebooks have been updated to work with local file systems instead of Google Colab. This guide explains the changes and how to use them.

## Changes Made

### 1. Removed Colab-Specific Code
- Removed `drive.mount()` calls
- Removed `cd` commands
- Removed `!pip install` commands (commented out)
- Removed Colab-specific file paths

### 2. Added Local Path Setup
- Added automatic directory detection
- Added path verification
- Added error handling for missing files
- All paths are now relative to the notebook location

### 3. Updated File Loading
All file loading operations now:
- Check if files exist before loading
- Provide clear error messages if files are missing
- Use `Path` objects for better cross-platform compatibility

## File Structure Required

Your local directory should have this structure:
```
Amazon-LLM/
├── Traditional_SVD_28_11_24.ipynb
├── Proposed_SVD_28_11_24.ipynb
├── Dataset/
│   ├── merged_df.csv
│   ├── new_LLM_data.csv
│   ├── amazon_products.csv (optional)
│   └── amazon_categories.csv (optional)
└── results/
    ├── metrics.npy
    └── metrics_proposed.npy
```

## How to Use

### Option 1: Run from Local Directory
1. Navigate to the directory containing the notebooks
2. Open the notebook in Jupyter/Colab Local Runtime
3. Run the first cell which sets up the paths automatically
4. The notebook will detect the correct directory and load files

### Option 2: Specify Custom Path
If your files are in a different location, modify the `BASE_DIR` in the first cell:

```python
# Manually set base directory
BASE_DIR = Path('/path/to/your/project')
os.chdir(BASE_DIR)
```

## Key Features

### Automatic Directory Detection
The notebooks automatically:
1. Check if `Dataset/` exists in current directory
2. If not, check parent directory
3. If still not found, use current working directory
4. Print the detected directory for verification

### File Verification
Before loading any file, the notebooks:
- Check if the file exists
- Print confirmation messages
- Raise clear error messages if files are missing

### Error Messages
If a required file is missing, you'll see:
```
FileNotFoundError: Dataset file not found: Dataset/merged_df.csv. 
Please ensure the file exists.
```

## Updated Cells

### Traditional_SVD_28_11_24.ipynb
- **Cell 0**: Setup local paths
- **Cell 1**: Path detection and verification
- **Cell 3**: Directory listing (replaces `cd` command)
- **Cell 4**: Directory verification
- **Cell 6**: Package installation (commented out)
- **Cell 7**: Imports with path setup
- **Cell 14**: Dataset file verification
- **Cell 16**: Load merged_df with error handling
- **Cell 36**: Load data_LLM with error handling
- **Cell 40**: Load metrics with error handling

### Proposed_SVD_28_11_24.ipynb
- **Cell 0**: Setup local paths and imports
- **Cell 9**: Load merged_df with error handling
- **Cell 28**: Load data_LLM with error handling
- **Cell 34**: Load metrics with error handling

## Troubleshooting

### Issue: "Dataset directory not found"
**Solution**: Ensure you're running the notebook from the correct directory, or manually set `BASE_DIR` in the first cell.

### Issue: "File not found" errors
**Solution**: 
1. Check that all required CSV files exist in the `Dataset/` directory
2. Verify the file names match exactly (case-sensitive)
3. Ensure you've run the data preprocessing steps if needed

### Issue: "Results directory not found"
**Solution**: Create the `results/` directory manually:
```bash
mkdir results
```

### Issue: Metrics file not found
**Solution**: 
- If you haven't run the model yet, this is expected
- The notebook will use calculated metrics instead
- To save metrics, uncomment the `np.save()` lines

## Testing

To verify everything works:
1. Run the first cell - should print base directory
2. Run the dataset loading cell - should print file info
3. Check for any error messages

## Notes

- All paths use `Path` objects for cross-platform compatibility
- The notebooks work with both Windows and Unix-like systems
- File paths are relative to the detected base directory
- No changes needed if your files are in the standard locations
