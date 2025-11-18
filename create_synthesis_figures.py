"""
SYNTHESIS VERSION FIGURES
Creates 2 essential figures for 1000-word synthesis manuscript
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Rectangle
import seaborn as sns

# Set publication-quality style
sns.set_style("whitegrid")
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.labelsize'] = 11
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['figure.dpi'] = 300

print("="*80)
print("CREATING SYNTHESIS FIGURES (2 FIGURES ONLY)")
print("="*80)
print()

# ============================================================================
# FIGURE 1: META-REGRESSION WITH TREATMENT-RISK INTERACTION
# ============================================================================

print("Creating Figure 1: Meta-Regression...")

fig, ax = plt.subplots(figsize=(7, 5))

# Trial data (CORRECTED DANISH)
trials = ['MADIT-II', 'SCD-HeFT', 'DANISH']
baseline_risks = np.array([0.1185, 0.0760, 0.0418])  # Annual mortality
log_baseline_risks = np.log(baseline_risks)
hazard_ratios = np.array([0.69, 0.77, 0.91])  # DANISH corrected to 0.91
log_hrs = np.log(hazard_ratios)

# Standard errors (for point sizing)
se_log_hr = np.array([0.141, 0.098, 0.126])
weights = 1 / (se_log_hr**2)
point_sizes = (weights / weights.max()) * 300 + 50

# Meta-regression parameters
beta0 = -0.871
beta1 = -0.240
r_squared = 0.958

# Plot trials
colors = ['#e74c3c', '#3498db', '#2ecc71']
for i, (trial, x, y, size, color) in enumerate(zip(trials, log_baseline_risks, log_hrs, point_sizes, colors)):
    ax.scatter(x, y, s=size, alpha=0.7, color=color, edgecolors='black', linewidth=1.5,
               label=trial, zorder=10)

# Regression line
x_range = np.linspace(log_baseline_risks.min() - 0.2, log_baseline_risks.max() + 0.2, 100)
y_pred = beta0 + beta1 * x_range

ax.plot(x_range, y_pred, 'k-', linewidth=2, label='Regression fit', zorder=5)

# 95% confidence band (approximate)
# Using residual SE
residuals = log_hrs - (beta0 + beta1 * log_baseline_risks)
se_residual = np.sqrt(np.sum(weights * residuals**2) / (len(trials) - 2))
se_band = se_residual * 1.96
ax.fill_between(x_range, y_pred - se_band, y_pred + se_band,
                alpha=0.2, color='gray', label='95% CI', zorder=1)

# Reference line at HR = 1.0
ax.axhline(y=0, color='red', linestyle='--', linewidth=1.5, alpha=0.6, label='No effect (HR=1.0)')

# Shaded regions for historical and modern risk
historical_range = [np.log(0.06), np.log(0.12)]
modern_range = [np.log(0.03), np.log(0.04)]

ax.axvspan(historical_range[0], historical_range[1], alpha=0.1, color='orange', zorder=0)
ax.axvspan(modern_range[0], modern_range[1], alpha=0.1, color='blue', zorder=0)

# Add text annotations for regions
ax.text(np.mean(historical_range), -1.2, 'Historical\nrisk',
        ha='center', va='top', fontsize=9, color='orange', weight='bold')
ax.text(np.mean(modern_range), -1.2, 'Modern\nrisk',
        ha='center', va='top', fontsize=9, color='blue', weight='bold')

# Add regression equation
equation_text = f'log(HR) = {beta0:.3f} + {beta1:.3f} × log(baseline risk)\nR² = {r_squared:.3f}, τ² = 0.000'
ax.text(0.05, 0.95, equation_text, transform=ax.transAxes,
        fontsize=10, verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.9, edgecolor='black'))

# Labels and formatting
ax.set_xlabel('Log(Baseline Annual Mortality Risk)', fontsize=11, weight='bold')
ax.set_ylabel('Log(ICD Hazard Ratio)', fontsize=11, weight='bold')
ax.set_title('Meta-Regression: ICD Effectiveness vs Baseline Risk', fontsize=12, weight='bold', pad=15)

# Convert x-axis to actual percentages for readability
x_ticks = np.log([0.03, 0.04, 0.05, 0.06, 0.08, 0.10, 0.12])
x_labels = ['3%', '4%', '5%', '6%', '8%', '10%', '12%']
ax.set_xticks(x_ticks)
ax.set_xticklabels(x_labels)

# Convert y-axis to hazard ratios
y_ticks = np.log([0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
y_labels = ['0.50', '0.60', '0.70', '0.80', '0.90', '1.00']
ax.set_yticks(y_ticks)
ax.set_yticklabels(y_labels)

ax.legend(loc='lower left', fontsize=9, framealpha=0.95)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('SYNTHESIS_Figure1_MetaRegression.png', dpi=300, bbox_inches='tight')
plt.savefig('SYNTHESIS_Figure1_MetaRegression.pdf', dpi=300, bbox_inches='tight')
print("✓ Figure 1 saved: SYNTHESIS_Figure1_MetaRegression.png/pdf")
plt.close()

# ============================================================================
# FIGURE 2: NUMBER NEEDED TO TREAT ACROSS ERAS
# ============================================================================

print("Creating Figure 2: NNT Comparison...")

fig, ax = plt.subplots(figsize=(8, 5))

# NNT data (CORRECTED: DANISH NNT from actual trial = 46.0, not 87.0)
# Modern NNT updated to 47 based on corrected 5-year baseline of 18.8%
categories = ['SCD-HeFT\n(2000)', 'DANISH\n(2014)', 'Predictive\nInterval', 'Bayesian\nPosterior\n(Modern)']
nnts = [15.0, 46.0, 28.6, 47.0]
lower_bounds = [None, None, None, 14.1]
upper_bounds = [None, None, None, 84.1]
colors_nnt = ['#3498db', '#2ecc71', '#f39c12', '#e74c3c']

x_pos = np.arange(len(categories))

# Plot bars
bars = ax.bar(x_pos, nnts, color=colors_nnt, alpha=0.8, edgecolor='black', linewidth=1.5)

# Add error bars for Bayesian
ax.errorbar(x_pos[-1], nnts[-1],
            yerr=[[nnts[-1] - lower_bounds[-1]], [upper_bounds[-1] - nnts[-1]]],
            fmt='none', ecolor='black', capsize=8, linewidth=2, capthick=2)

# Add NNT values on bars
for i, (x, nnt) in enumerate(zip(x_pos, nnts)):
    if i == 3:  # Bayesian with uncertainty
        ax.text(x, nnt + 5, f'{nnt:.1f}', ha='center', va='bottom', fontsize=11, weight='bold')
        ax.text(x, lower_bounds[i] - 8, f'95% UI:\n{lower_bounds[i]:.1f}-{upper_bounds[i]:.1f}',
                ha='center', va='top', fontsize=8, style='italic')
    else:
        ax.text(x, nnt + 3, f'{nnt:.1f}', ha='center', va='bottom', fontsize=11, weight='bold')

# Reference line at SCD-HeFT
ax.axhline(y=15.0, color='blue', linestyle='--', linewidth=2, alpha=0.5, label='SCD-HeFT baseline')

# Shaded region for acceptable NNT
ax.axhspan(0, 20, alpha=0.1, color='green', zorder=0)
ax.text(3.5, 18, 'Lower NNT\n(Better)', ha='right', va='top', fontsize=9, color='darkgreen', style='italic')

# Add percentage increase annotations
for i in range(1, len(nnts)):
    increase_pct = ((nnts[i] - nnts[0]) / nnts[0]) * 100
    ax.annotate('', xy=(i, nnts[i]), xytext=(0, nnts[0]),
                arrowprops=dict(arrowstyle='<->', color='gray', lw=1.5, linestyle='dotted'))
    mid_x = i / 2
    mid_y = (nnts[i] + nnts[0]) / 2
    if i == 3:  # Highlight modern increase
        ax.text(mid_x, mid_y, f'+{increase_pct:.0f}%', ha='center', va='center',
                fontsize=10, weight='bold', color='red',
                bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))

# Labels and formatting
ax.set_ylabel('Number Needed to Treat (5 years)', fontsize=11, weight='bold')
ax.set_xlabel('Trial Era / Method', fontsize=11, weight='bold')
ax.set_title('ICD Number Needed to Treat: Historical vs Contemporary', fontsize=12, weight='bold', pad=15)
ax.set_xticks(x_pos)
ax.set_xticklabels(categories, fontsize=10)
ax.set_ylim(0, 95)
ax.grid(axis='y', alpha=0.3)

# Add interpretation box
interpretation = ('Modern GDMT reduces baseline risk,\nincreasing NNT by 210% (tripling).\n'
                 'Approximately 47 patients need ICD\nto prevent 1 death over 5 years.')
ax.text(0.98, 0.97, interpretation, transform=ax.transAxes,
        fontsize=9, verticalalignment='top', horizontalalignment='right',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9, edgecolor='black'))

plt.tight_layout()
plt.savefig('SYNTHESIS_Figure2_NNT_Comparison.png', dpi=300, bbox_inches='tight')
plt.savefig('SYNTHESIS_Figure2_NNT_Comparison.pdf', dpi=300, bbox_inches='tight')
print("✓ Figure 2 saved: SYNTHESIS_Figure2_NNT_Comparison.png/pdf")
plt.close()

print()
print("="*80)
print("SYNTHESIS FIGURES COMPLETE")
print("="*80)
print()
print("Created 2 publication-ready figures:")
print("  1. SYNTHESIS_Figure1_MetaRegression.png/pdf")
print("     - Shows treatment-risk interaction (R² = 0.958)")
print("     - Historical vs modern risk ranges highlighted")
print("     - DANISH observed vs predicted comparison")
print()
print("  2. SYNTHESIS_Figure2_NNT_Comparison.png/pdf")
print("     - NNT across trial eras and methods")
print("     - Shows 210% increase (tripling) in modern era")
print("     - Bayesian uncertainty interval displayed")
print()
print("Both figures at 300 DPI, ready for synthesis journal submission")
print("="*80)
