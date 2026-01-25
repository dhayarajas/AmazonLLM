"""
Improved figure generation code with higher resolution and larger fonts
for better readability in the manuscript
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
from pathlib import Path

# Set high DPI for better resolution
matplotlib.rcParams['figure.dpi'] = 300
matplotlib.rcParams['savefig.dpi'] = 300
matplotlib.rcParams['savefig.bbox'] = 'tight'

# Set larger font sizes for better readability
plt.rcParams.update({
    'font.size': 14,
    'axes.titlesize': 16,
    'axes.labelsize': 14,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
    'legend.fontsize': 12,
    'figure.titlesize': 18
})

# Create output directory for figures
output_dir = Path('media')
output_dir.mkdir(exist_ok=True)

def plot_top_categories(df, output_path='media/image6.png'):
    """Plot top 10 product categories with improved quality"""
    custom_palette = sns.color_palette("Greens_r", n_colors=10)
    
    plt.figure(figsize=(14, 8))
    top_categories = df['category_name'].value_counts().nlargest(10)
    sns.barplot(x=top_categories.values, y=top_categories.index, palette=custom_palette)
    plt.title('Top 10 Product Categories by Count', fontsize=18, fontweight='bold', pad=20)
    plt.xlabel('Products Count', fontsize=16, fontweight='bold')
    plt.ylabel('Category', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Saved figure to {output_path}")

def plot_price_distribution(df, output_path='media/image4.png'):
    """Plot price distribution by category with improved quality"""
    plt.figure(figsize=(16, 8))
    top_10_categories = df['category_name'].value_counts().nlargest(10).index
    sns.boxplot(x='category_name', y='price', data=df[df['category_name'].isin(top_10_categories)])
    plt.title('Price Distribution by Category (Top 10)', fontsize=18, fontweight='bold', pad=20)
    plt.xlabel('Category', fontsize=16, fontweight='bold')
    plt.ylabel('Price Value ($)', fontsize=16, fontweight='bold')
    plt.xticks(rotation=45, ha='right', fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Saved figure to {output_path}")

def plot_rating_analysis(df, output_path='media/image5.png'):
    """Plot average rating vs best seller status with improved quality"""
    custom_palette = sns.color_palette("Blues_r", n_colors=2)
    plt.figure(figsize=(12, 8))
    sns.boxplot(x='isBestSeller', y='stars', data=df, palette=custom_palette)
    plt.title('Analysis of Average Rating and Best Seller Status', fontsize=18, fontweight='bold', pad=20)
    plt.xlabel('Is Best Seller', fontsize=16, fontweight='bold')
    plt.ylabel('Rating (Stars)', fontsize=16, fontweight='bold')
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Saved figure to {output_path}")

def plot_mse_comparison(output_path='media/image7.png'):
    """Plot MSE comparison with improved quality"""
    models = ['Traditional SVD', 'Proposed SVD']
    mse_values = [0.4585, 0.3246]
    colors = ['#FF6B6B', '#4ECDC4']
    
    plt.figure(figsize=(10, 8))
    bars = plt.bar(models, mse_values, color=colors, width=0.6, edgecolor='black', linewidth=1.5)
    plt.title('Performance Analysis of MSE', fontsize=18, fontweight='bold', pad=20)
    plt.ylabel('MSE Value', fontsize=16, fontweight='bold')
    plt.xlabel('Model', fontsize=16, fontweight='bold')
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    
    # Add value labels on bars
    for bar, value in zip(bars, mse_values):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{value:.4f}',
                ha='center', va='bottom', fontsize=14, fontweight='bold')
    
    plt.grid(axis='y', alpha=0.3, linestyle='--')
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Saved figure to {output_path}")

def plot_rmse_comparison(output_path='media/image8.png'):
    """Plot RMSE comparison with improved quality"""
    models = ['Traditional SVD', 'Proposed SVD']
    rmse_values = [0.6771, 0.5696]
    colors = ['#FF6B6B', '#4ECDC4']
    
    plt.figure(figsize=(10, 8))
    bars = plt.bar(models, rmse_values, color=colors, width=0.6, edgecolor='black', linewidth=1.5)
    plt.title('Performance Analysis of RMSE', fontsize=18, fontweight='bold', pad=20)
    plt.ylabel('RMSE Value', fontsize=16, fontweight='bold')
    plt.xlabel('Model', fontsize=16, fontweight='bold')
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    
    # Add value labels on bars
    for bar, value in zip(bars, rmse_values):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{value:.4f}',
                ha='center', va='bottom', fontsize=14, fontweight='bold')
    
    plt.grid(axis='y', alpha=0.3, linestyle='--')
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Saved figure to {output_path}")

def plot_sota_comparison(output_path='media/image9.png'):
    """Plot SOTA comparison with improved quality"""
    models = ['Traditional\nSVD', 'UTER', 'MCNN', 'LightGCN', 'BERT4Rec', 'Proposed\nSVD']
    rmse_values = [0.6771, 0.9825, 0.9475, 0.6421, 0.6238, 0.5696]
    colors = ['#FF6B6B', '#FFA07A', '#FFD700', '#98D8C8', '#87CEEB', '#4ECDC4']
    
    plt.figure(figsize=(14, 8))
    bars = plt.bar(models, rmse_values, color=colors, width=0.7, edgecolor='black', linewidth=1.5)
    plt.title('Comparative Analysis of RMSE with State-of-the-Art Methods', 
              fontsize=18, fontweight='bold', pad=20)
    plt.ylabel('RMSE Value', fontsize=16, fontweight='bold')
    plt.xlabel('Model', fontsize=16, fontweight='bold')
    plt.xticks(fontsize=12, rotation=15, ha='right')
    plt.yticks(fontsize=14)
    
    # Add value labels on bars
    for bar, value in zip(bars, rmse_values):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{value:.4f}',
                ha='center', va='bottom', fontsize=12, fontweight='bold')
    
    # Highlight proposed method
    bars[-1].set_edgecolor('red')
    bars[-1].set_linewidth(3)
    
    plt.grid(axis='y', alpha=0.3, linestyle='--')
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Saved figure to {output_path}")

if __name__ == "__main__":
    # Load data
    df = pd.read_csv('Dataset/merged_df.csv')
    
    # Generate all improved figures
    print("Generating improved figures with high resolution and larger fonts...")
    plot_top_categories(df)
    plot_price_distribution(df)
    plot_rating_analysis(df)
    plot_mse_comparison()
    plot_rmse_comparison()
    plot_sota_comparison()
    print("All figures generated successfully!")
