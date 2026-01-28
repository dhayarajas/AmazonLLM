"""
COPY THIS ENTIRE CELL INTO YOUR NOTEBOOK
Add as a NEW CELL at the TOP (after imports, before any plots)
Run this cell ONCE, then run all your plotting cells
"""

# ============================================================================
# GLOBAL FONT CONFIGURATION - CONSISTENT FONTS FOR ALL PLOTS
# ============================================================================

import matplotlib.pyplot as plt
import matplotlib

# Close any existing plots
plt.close('all')

# Define consistent font configuration
FONT_CONFIG = {
    # Font family
    'font.family': 'sans-serif',
    'font.sans-serif': ['DejaVu Sans', 'Arial', 'Helvetica'],
    
    # Font sizes - ALL CONSISTENT
    'font.size': 18,              # Base
    'axes.titlesize': 26,         # Titles
    'axes.labelsize': 20,         # Axis labels  
    'xtick.labelsize': 16,        # X tick labels
    'ytick.labelsize': 16,        # Y tick labels
    'legend.fontsize': 16,        # Legend
    'legend.title_fontsize': 18,  # Legend title
    'figure.titlesize': 28,       # Figure title
    
    # Font weights - ALL BOLD
    'axes.titleweight': 'bold',
    'axes.labelweight': 'bold',
    'figure.titleweight': 'bold',
    
    # Resolution - HIGH QUALITY
    'figure.dpi': 600,
    'savefig.dpi': 600,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.2,
    
    # Line widths - CONSISTENT THICKNESS
    'axes.linewidth': 2,
    'grid.linewidth': 1.5,
    'lines.linewidth': 2.5,
    'patch.linewidth': 2,
    
    # Tick parameters - CONSISTENT SIZE
    'xtick.major.width': 2,
    'xtick.major.size': 8,
    'ytick.major.width': 2,
    'ytick.major.size': 8,
    
    # Grid - CONSISTENT STYLE
    'grid.alpha': 0.3,
    'grid.linestyle': '--',
    
    # Legend - CONSISTENT APPEARANCE
    'legend.framealpha': 0.95,
    'legend.edgecolor': 'black',
    'legend.fancybox': True,
}

# Apply configuration GLOBALLY to all plots
plt.rcParams.update(FONT_CONFIG)
matplotlib.rcParams.update(FONT_CONFIG)

# Also set for seaborn if you're using it
try:
    import seaborn as sns
    sns.set_context("notebook", font_scale=1.0)
    sns.set_style("whitegrid")
except ImportError:
    pass

# Verification
print("=" * 70)
print("✅ CONSISTENT FONT CONFIGURATION APPLIED TO ALL PLOTS")
print("=" * 70)
print(f"Font Family: {plt.rcParams['font.family']}")
print(f"Title Size: {plt.rcParams['axes.titlesize']}pt (bold)")
print(f"Label Size: {plt.rcParams['axes.labelsize']}pt (bold)")
print(f"Tick Size: {plt.rcParams['xtick.labelsize']}pt")
print(f"DPI: {plt.rcParams['figure.dpi']}")
print("=" * 70)
print("ℹ️  All plots created after this cell will use these settings!")
print("=" * 70)
