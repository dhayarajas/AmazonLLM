# Handling Large Files in Colab - Updated Solution

## Problem
The GitHub repository contains large files, causing git clone operations to timeout.

## Solution Implemented

### 1. **Shallow Clone (Recommended)**
- Uses `git clone --depth 1` to download only the latest commit
- **Much faster** and **smaller download size**
- Reduces download time significantly
- Timeout increased to **10 minutes** (600 seconds)

### 2. **Fallback to Full Clone**
- If shallow clone fails, automatically tries full clone
- Timeout increased to **20 minutes** (1200 seconds) for full clone

### 3. **Manual Clone Option**
- If both automatic methods timeout, provides clear instructions
- Recommends using `!git clone` command directly in a new cell
- This shows progress and doesn't have timeout restrictions

## Updated Behavior

### Automatic Clone (First Attempt)
```python
# Tries shallow clone first (faster)
git clone --depth 1 https://github.com/dhayarajas/AmazonLLM.git
# Timeout: 10 minutes
```

### Fallback (If Shallow Fails)
```python
# Tries full clone
git clone https://github.com/dhayarajas/AmazonLLM.git
# Timeout: 20 minutes
```

### Manual Option (If Timeout)
```python
# Run in a new cell - shows progress, no timeout
!git clone https://github.com/dhayarajas/AmazonLLM.git

# Or for faster clone:
!git clone --depth 1 https://github.com/dhayarajas/AmazonLLM.git
```

## Usage Instructions

### Option 1: Automatic (Recommended)
1. Run the first cell
2. It will automatically try shallow clone
3. If it times out, follow the instructions shown

### Option 2: Manual Clone (If Timeout)
1. Create a new cell
2. Run: `!git clone --depth 1 https://github.com/dhayarajas/AmazonLLM.git`
3. Wait for it to complete (you'll see progress)
4. Re-run the first cell

### Option 3: Full Manual Clone
1. Create a new cell
2. Run: `!git clone https://github.com/dhayarajas/AmazonLLM.git`
3. Wait for it to complete
4. Re-run the first cell

## Benefits of Shallow Clone

✅ **Faster**: Downloads only latest commit, not full history
✅ **Smaller**: Significantly reduced download size
✅ **Sufficient**: You only need the current files, not git history
✅ **Less likely to timeout**: Smaller download = faster completion

## What Gets Cloned

### Shallow Clone (`--depth 1`)
- ✅ All current files and folders
- ✅ Latest commit only
- ✅ All datasets and results
- ❌ Git history (not needed for running notebooks)

### Full Clone
- ✅ Everything including git history
- ⚠️ Takes longer and uses more space

## Troubleshooting

### Issue: Still Timing Out
**Solution**: Use manual clone in a new cell:
```python
!git clone --depth 1 https://github.com/dhayarajas/AmazonLLM.git
```

### Issue: Need Git History
**Solution**: Use full clone manually:
```python
!git clone https://github.com/dhayarajas/AmazonLLM.git
```

### Issue: Network is Slow
**Solution**: 
1. Try shallow clone manually: `!git clone --depth 1 https://github.com/dhayarajas/AmazonLLM.git`
2. If still slow, wait it out - it will eventually complete
3. Consider using Colab Pro for faster network speeds

## Timeout Values

- **Shallow Clone**: 10 minutes (600 seconds)
- **Full Clone**: 20 minutes (1200 seconds)
- **Git Pull**: 2 minutes (120 seconds)

## Notes

- Shallow clone is usually sufficient for running notebooks
- Manual `!git clone` commands show progress and don't timeout
- If automatic clone times out, the error message will guide you
- Repository will be cloned to `/content/AmazonLLM/` in Colab
