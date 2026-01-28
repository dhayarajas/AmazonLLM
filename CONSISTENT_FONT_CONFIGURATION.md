# 🎨 Consistent Font Configuration for All Plots

## Problem
Different plots in your notebook may have inconsistent:
- Font sizes
- Font families
- Font weights
- Title formats
- Axis label styles

## Solution: Global Matplotlib Configuration

---

## 📋 Implementation Steps

### Step 1: Add Global Configuration Cell

**Add this cell at the TOP of your notebook** (after imports, before any plotting):

```python
# ============================================================================
# GLOBAL MATPLOTLIB CONFIGURATION - CONSISTENT FONTS FOR ALL PLOTS
# ============================================================================
# Run this cell ONCE at the beginning to ensure all plots have consistent fonts

import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager
import seaborn as sns

# Set the style
plt.style.use('default')
sns.set_palette("husl")

# ============================================================================
# PUBLICATION-QUALITY FONT SETTINGS
# ============================================================================

# Global font configuration
FONT_CONFIG = {
    # Font family (choose one - uncomment your preference)
    'font.family': 'sans-serif',
    'font.sans-serif': ['DejaVu Sans', 'Arial', 'Helvetica', 'Liberation Sans'],
    # 'font.serif': ['DejaVu Serif', 'Times New Roman', 'Liberation Serif'],
    
    # Font sizes (all in points)
    'font.size': 18,              # Base font size
    'axes.titlesize': 26,         # Figure title
    'axes.labelsize': 20,         # X & Y axis labels
    'xtick.labelsize': 16,        # X tick labels
    'ytick.labelsize': 16,        # Y tick labels
    'legend.fontsize': 16,        # Legend text
    'legend.title_fontsize': 18,  # Legend title
    'figure.titlesize': 28,       # Suptitle
    
    # Font weights
    'axes.titleweight': 'bold',   # Make titles bold
    'axes.labelweight': 'bold',   # Make axis labels bold
    'figure.titleweight': 'bold', # Make figure title bold
    
    # DPI and resolution
    'figure.dpi': 600,
    'savefig.dpi': 600,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.2,
    'savefig.format': 'png',
    
    # Line and border widths
    'axes.linewidth': 2,          # Axes border width
    'grid.linewidth': 1.5,        # Grid line width
    'lines.linewidth': 2.5,       # Plot line width
    'patch.linewidth': 2,         # Bar/patch border width
    'hatch.linewidth': 2,         # Hatch line width
    
    # Tick parameters
    'xtick.major.width': 2,       # X tick width
    'xtick.major.size': 8,        # X tick length
    'xtick.minor.width': 1.5,     # X minor tick width
    'xtick.minor.size': 4,        # X minor tick length
    'ytick.major.width': 2,       # Y tick width
    'ytick.major.size': 8,        # Y tick length
    'ytick.minor.width': 1.5,     # Y minor tick width
    'ytick.minor.size': 4,        # Y minor tick length
    
    # Grid styling
    'grid.alpha': 0.3,
    'grid.linestyle': '--',
    
    # Legend styling
    'legend.framealpha': 0.95,
    'legend.edgecolor': 'black',
    'legend.fancybox': True,
    'legend.shadow': False,
    'legend.frameon': True,
    
    # Figure layout
    'figure.autolayout': False,
    'figure.constrained_layout.use': False,
}

# Apply the configuration
plt.rcParams.update(FONT_CONFIG)
matplotlib.rcParams.update(FONT_CONFIG)

# ============================================================================
# CONSISTENT COLOR PALETTE
# ============================================================================

# Define consistent colors for all plots
COLORS = {
    'primary': '#4ECDC4',      # Turquoise
    'secondary': '#FF6B6B',    # Red
    'accent': '#FFE66D',       # Yellow
    'success': '#95E1D3',      # Light turquoise
    'warning': '#F38181',      # Pink
    'info': '#4A90E2',         # Blue
    'dark': '#2C3E50',         # Dark blue-gray
    'light': '#ECF0F1',        # Light gray
}

# Create color palettes for multi-category plots
PALETTE_SEQUENTIAL = ['#4ECDC4', '#45B8AC', '#3CA394', '#338E7C', '#2A7964']
PALETTE_DIVERGING = ['#FF6B6B', '#FFA07A', '#FFE66D', '#95E1D3', '#4ECDC4']
PALETTE_QUALITATIVE = ['#4ECDC4', '#FF6B6B', '#FFE66D', '#95E1D3', '#F38181', '#4A90E2']

# Set default seaborn palette
sns.set_palette(PALETTE_QUALITATIVE)

# ============================================================================
# HELPER FUNCTIONS FOR CONSISTENT FORMATTING
# ============================================================================

def format_plot(ax=None, title=None, xlabel=None, ylabel=None, 
                grid=True, legend=True, tight=True):
    """
    Apply consistent formatting to any matplotlib axis.
    
    Parameters:
    -----------
    ax : matplotlib axis, optional
        The axis to format. If None, uses current axis.
    title : str, optional
        Title text
    xlabel : str, optional
        X-axis label
    ylabel : str, optional
        Y-axis label
    grid : bool, default=True
        Whether to show grid
    legend : bool, default=True
        Whether to show legend
    tight : bool, default=True
        Whether to apply tight layout
    """
    if ax is None:
        ax = plt.gca()
    
    if title:
        ax.set_title(title, fontsize=26, fontweight='bold', pad=20)
    
    if xlabel:
        ax.set_xlabel(xlabel, fontsize=20, fontweight='bold', labelpad=10)
    
    if ylabel:
        ax.set_ylabel(ylabel, fontsize=20, fontweight='bold', labelpad=10)
    
    if grid:
        ax.grid(True, alpha=0.3, linestyle='--', linewidth=1.5)
    
    if legend and ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=16, loc='best', framealpha=0.95, 
                 edgecolor='black', fancybox=True)
    
    ax.tick_params(labelsize=16, width=2, length=8)
    
    for spine in ax.spines.values():
        spine.set_linewidth(2)
    
    if tight:
        plt.tight_layout()


def save_figure(filename, dpi=600, bbox_inches='tight', pad_inches=0.2):
    """
    Save figure with consistent settings.
    
    Parameters:
    -----------
    filename : str or Path
        Output filename
    dpi : int, default=600
        Resolution in dots per inch
    bbox_inches : str, default='tight'
        Bounding box setting
    pad_inches : float, default=0.2
        Padding around figure
    """
    plt.savefig(filename, dpi=dpi, bbox_inches=bbox_inches, 
                pad_inches=pad_inches, facecolor='white', edgecolor='none')
    print(f"✓ Saved: {filename}")


def create_bar_plot(x, y, title=None, xlabel=None, ylabel=None, 
                    color=None, figsize=(14, 10), save_path=None):
    """
    Create a consistently formatted bar plot.
    
    Parameters:
    -----------
    x : array-like
        X-axis data (categories)
    y : array-like
        Y-axis data (values)
    title : str, optional
        Plot title
    xlabel : str, optional
        X-axis label
    ylabel : str, optional
        Y-axis label
    color : str or list, optional
        Bar color(s). Uses default palette if None.
    figsize : tuple, default=(14, 10)
        Figure size in inches
    save_path : str or Path, optional
        If provided, saves figure to this path
    
    Returns:
    --------
    fig, ax : matplotlib figure and axis objects
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    if color is None:
        color = COLORS['primary']
    
    bars = ax.bar(x, y, color=color, edgecolor='black', linewidth=2)
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.2f}' if isinstance(height, float) else f'{height}',
                ha='center', va='bottom', fontsize=16, fontweight='bold')
    
    format_plot(ax, title=title, xlabel=xlabel, ylabel=ylabel)
    
    if save_path:
        save_figure(save_path)
    
    return fig, ax


# ============================================================================
# VERIFICATION
# ============================================================================

print("=" * 70)
print("✓ GLOBAL FONT CONFIGURATION APPLIED")
print("=" * 70)
print(f"\nFont Settings:")
print(f"  • Family: {plt.rcParams['font.family']}")
print(f"  • Base size: {plt.rcParams['font.size']}pt")
print(f"  • Title size: {plt.rcParams['axes.titlesize']}pt")
print(f"  • Label size: {plt.rcParams['axes.labelsize']}pt")
print(f"  • Tick size: {plt.rcParams['xtick.labelsize']}pt")
print(f"  • DPI: {plt.rcParams['figure.dpi']}")
print(f"\nAll plots will now use these consistent settings!")
print("=" * 70)
```

---

## Step 2: Update Existing Plot Cells

For **each existing plot cell**, you can either:

### Option A: Minimal Changes (Keep existing code, just ensure consistency)
Just make sure the cell runs AFTER the global configuration cell. No changes needed!

### Option B: Use Helper Functions (Recommended for new plots)

**OLD CODE:**
```python
plt.figure(figsize=(14, 8))
plt.bar(x, y)
plt.title('My Title', fontsize=18, fontweight='bold')
plt.xlabel('X Label', fontsize=16)
plt.ylabel('Y Label', fontsize=16)
plt.grid(True)
plt.tight_layout()
plt.savefig('output.png', dpi=300, bbox_inches='tight')
plt.show()
```

**NEW CODE (using helper):**
```python
fig, ax = create_bar_plot(
    x=x, 
    y=y,
    title='My Title',
    xlabel='X Label',
    ylabel='Y Label',
    figsize=(14, 10),
    save_path='output.png'
)
plt.show()
```

---

## Step 3: Remove Individual Font Settings

**Search and REMOVE** these lines from individual plot cells (they override global settings):

```python
# Remove these lines:
fontsize=18
fontweight='bold'
font_size=14
titlesize=16
labelsize=14
# etc.
```

Or replace with:
```python
# Use global settings instead
# (no fontsize parameter needed - uses global config)
```

---

## 📊 Consistency Checklist

After applying the configuration, ALL your plots will have:

- ✅ **Same font family** (DejaVu Sans)
- ✅ **Same title size** (26pt, bold)
- ✅ **Same axis label size** (20pt, bold)
- ✅ **Same tick label size** (16pt)
- ✅ **Same legend size** (16pt)
- ✅ **Same line thickness** (2.5pt)
- ✅ **Same axes thickness** (2pt)
- ✅ **Same DPI** (600)
- ✅ **Same color scheme** (consistent palette)
- ✅ **Same grid style** (dashed, 30% opacity)

---

## 🎨 Font Customization Options

### Want a Different Font?

**For Sans-Serif (Clean, Modern):**
```python
'font.family': 'sans-serif',
'font.sans-serif': ['Arial', 'Helvetica', 'DejaVu Sans'],
```

**For Serif (Traditional, Academic):**
```python
'font.family': 'serif',
'font.serif': ['Times New Roman', 'DejaVu Serif', 'Georgia'],
```

**For Monospace (Technical):**
```python
'font.family': 'monospace',
'font.monospace': ['Courier New', 'DejaVu Sans Mono'],
```

### Want Different Sizes?

Change these values in FONT_CONFIG:
```python
'font.size': 18,              # Increase/decrease by 2-4 points
'axes.titlesize': 26,         # Titles
'axes.labelsize': 20,         # Axis labels
'xtick.labelsize': 16,        # Tick labels
```

---

## 🧪 Quick Test

Add this test cell after the configuration to verify:

```python
# Test plot to verify consistent formatting
import numpy as np

fig, axes = plt.subplots(2, 2, figsize=(20, 16))
fig.suptitle('Font Consistency Test - All Plots Should Match', 
             fontsize=28, fontweight='bold')

# Test 1: Bar plot
ax1 = axes[0, 0]
ax1.bar(['A', 'B', 'C', 'D'], [10, 25, 15, 30], color=COLORS['primary'], edgecolor='black', linewidth=2)
ax1.set_title('Bar Plot Test')
ax1.set_xlabel('Categories')
ax1.set_ylabel('Values')
ax1.grid(True, alpha=0.3)

# Test 2: Line plot
ax2 = axes[0, 1]
x = np.linspace(0, 10, 100)
ax2.plot(x, np.sin(x), linewidth=2.5, color=COLORS['secondary'])
ax2.set_title('Line Plot Test')
ax2.set_xlabel('X Values')
ax2.set_ylabel('Y Values')
ax2.grid(True, alpha=0.3)

# Test 3: Scatter plot
ax3 = axes[1, 0]
ax3.scatter(np.random.rand(50), np.random.rand(50), s=100, 
            color=COLORS['accent'], edgecolor='black', linewidth=2)
ax3.set_title('Scatter Plot Test')
ax3.set_xlabel('X Values')
ax3.set_ylabel('Y Values')
ax3.grid(True, alpha=0.3)

# Test 4: Box plot
ax4 = axes[1, 1]
data = [np.random.normal(0, std, 100) for std in range(1, 5)]
ax4.boxplot(data, patch_artist=True, 
            boxprops=dict(facecolor=COLORS['success'], linewidth=2),
            medianprops=dict(color='red', linewidth=2))
ax4.set_title('Box Plot Test')
ax4.set_xlabel('Groups')
ax4.set_ylabel('Values')
ax4.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("✓ If all four plots have the same font sizes and styles, configuration is working!")
```

---

## 📝 Example: Converting Existing Plots

### Before (Inconsistent):
```python
# Plot 1 - Different fonts
plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.title('Title', fontsize=14)  # ← Size 14
plt.xlabel('X', fontsize=12)      # ← Size 12

# Plot 2 - Different fonts
plt.figure(figsize=(12, 8))
plt.bar(x, y)
plt.title('Title', fontsize=20)  # ← Size 20 (different!)
plt.xlabel('X', fontsize=16)      # ← Size 16 (different!)
```

### After (Consistent):
```python
# REMOVE individual font settings, let global config handle it

# Plot 1 - Uses global config
plt.figure(figsize=(14, 10))
plt.plot(x, y)
plt.title('Title')        # ← Uses 26pt from config
plt.xlabel('X')           # ← Uses 20pt from config
format_plot()             # ← Applies consistent formatting

# Plot 2 - Uses global config
plt.figure(figsize=(14, 10))
plt.bar(x, y)
plt.title('Title')        # ← Uses 26pt from config
plt.xlabel('X')           # ← Uses 20pt from config
format_plot()             # ← Applies consistent formatting
```

---

## ⚠️ Important Notes

1. **Run Configuration Cell First**
   - Must run BEFORE any plotting
   - Best to place after imports at top of notebook

2. **Remove Individual Font Settings**
   - Delete fontsize parameters from individual plots
   - Let global config control all fonts

3. **Restart Kernel If Needed**
   - If plots still look inconsistent
   - Kernel → Restart & Run All

4. **Check Seaborn**
   - Seaborn can override settings
   - The config includes seaborn compatibility

---

## ✅ Verification Steps

1. Add configuration cell at top
2. Run configuration cell
3. Run all plot cells
4. Check that all plots have:
   - Same font family
   - Same title size
   - Same label size
   - Same overall appearance

---

## 🎯 Expected Result

**Before:** Mixed fonts, sizes, styles across different plots
**After:** Uniform, professional appearance across ALL plots

---

**Status:** Ready to implement  
**Time:** 5-10 minutes  
**Difficulty:** Easy  
**Impact:** High - All plots will look professionally consistent
