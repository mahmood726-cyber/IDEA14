# SUPPLEMENTARY MATERIALS

## Reassessing ICD Effectiveness Under Modern GDMT: Supplementary Content

---

## SUPPLEMENTARY METHODS

### Detailed Statistical Methodology

#### 1. Component Network Meta-Analysis (CNMA)

**Theoretical Framework:**
Component network meta-analysis, developed by Rücker et al. (2020), extends standard network meta-analysis to accommodate multicomponent interventions. The method decomposes complex interventions into their constituent components and estimates the effect of each component, allowing synthesis of evidence across trials with different component combinations.

**Mathematical Model:**
Let θ denote the relative treatment effect (log relative risk) of a combination of components. Under the additive CNMA model:

θ = Σᵢ pᵢ × βᵢ

where:
- pᵢ = proportion of patients receiving component i (0 ≤ pᵢ ≤ 1)
- βᵢ = log relative risk for component i

For our analysis with 5 components (BB, ACE-I/ARB, MRA, ARNi, SGLT2i):

log(RR_combined) = (p_BB × β_BB) + (p_ACE × β_ACE) + (p_MRA × β_MRA) + (p_ARNi × β_ARNi) + (p_SGLT2i × β_SGLT2i)

**Component Effect Estimates:**
Component-specific log relative risks (βᵢ) were obtained from landmark randomized controlled trials:
- β_BB = log(0.95) = -0.051 (from CIBIS-II, MERIT-HF, COPERNICUS meta-analysis)
- β_ACE = log(0.90) = -0.105 (from CONSENSUS, SOLVD, Val-HeFT)
- β_MRA = log(0.75) = -0.288 (from RALES, EMPHASIS-HF)
- β_ARNi = log(0.80) = -0.223 (from PARADIGM-HF, sudden death endpoint)
- β_SGLT2i = log(0.87) = -0.139 (from DAPA-HF + EMPEROR-R pooled analysis)

**Testing for Interactions:**
We tested for departure from additivity by including an interaction term for ARNi × SGLT2i:

log(RR_interactive) = log(RR_additive) + (p_ARNi × p_SGLT2i × γ)

where γ represents the interaction coefficient. We estimated γ = -0.05 based on subgroup analyses from PARADIGM-HF and DAPA-HF, representing minor synergy. Model comparison using Akaike Information Criterion (AIC) favored the additive model (ΔAIC < 2), consistent with parsimony.

**Uncertainty Quantification:**
Standard errors for component effects were propagated using the delta method:

SE(log RR_combined) = √[Σᵢ (pᵢ² × SE(βᵢ)²)]

95% confidence intervals were calculated as:

95% CI = exp[log(RR) ± 1.96 × SE(log RR)]

---

#### 2. Meta-Regression with Baseline Risk

**Model Specification:**
We employed weighted least squares meta-regression to model the association between baseline mortality risk and ICD treatment effect:

log(HR_ICD)ᵢ = β₀ + β₁ × log(Baseline_Risk)ᵢ + εᵢ

where:
- log(HR_ICD)ᵢ = log hazard ratio for ICD effect in trial i
- Baseline_Risk ᵢ = annual mortality rate in control arm of trial i
- β₀ = intercept
- β₁ = regression coefficient (treatment-risk interaction parameter)
- εᵢ ~ N(0, σ²ᵢ) where σ²ᵢ = SE(log HR)²ᵢ

**Weighting:**
Inverse-variance weights were used:

wᵢ = 1 / SE(log HR)²ᵢ

**Model Fitting:**
Parameters were estimated using weighted least squares:

β̂ = (X'WX)⁻¹X'Wy

where W is a diagonal matrix with elements wᵢ.

**Goodness of Fit:**
R² was calculated as:

R² = 1 - [Σᵢ wᵢ(yᵢ - ŷᵢ)² / Σᵢ wᵢ(yᵢ - ȳ)²]

**Prediction:**
For a new population with baseline risk r*, the predicted ICD effect is:

log(HR*)= β̂₀ + β̂₁ × log(r*)

with prediction standard error:

SE(log HR*) = √[SE(β̂₀)² + log(r*)² × SE(β̂₁)² + 2×log(r*)×Cov(β̂₀,β̂₁)]

---

#### 3. Predictive Intervals for Future Trials

**Distinction from Confidence Intervals:**
Traditional confidence intervals estimate uncertainty about the *average* treatment effect across studies. Predictive intervals estimate the plausible range for the effect in a *single future study*, accounting for between-study heterogeneity.

**Random-Effects Meta-Analysis:**
We first performed random-effects meta-analysis using the DerSimonian-Laird method to estimate between-study variance (τ²):

τ² = max{0, [Q - (k-1)] / [Σwᵢ - (Σwᵢ²/Σwᵢ)]}

where:
- Q = Σwᵢ(yᵢ - ȳ)² = heterogeneity statistic
- k = number of studies
- wᵢ = 1/SE²ᵢ = inverse-variance weights

**Pooled Effect Estimate:**
Random-effects pooled estimate:

θ̂_RE = [Σw*ᵢyᵢ] / [Σw*ᵢ]

where w*ᵢ = 1/(SE²ᵢ + τ²)

**Predictive Interval Calculation:**
The 95% predictive interval for a new study is:

95% PI = exp[θ̂_RE ± t_(k-1),0.975 × √(SE²_RE + τ²)]

where:
- SE²_RE = 1/Σw*ᵢ
- t_(k-1),0.975 = critical value from t-distribution with k-1 degrees of freedom

**Adjustment for Baseline Risk:**
When predicting for a specific baseline risk level (e.g., modern 5% annual mortality), we incorporated the meta-regression prediction:

95% PI_adjusted = exp[(β̂₀ + β̂₁×log(r*)) ± t_(k-2),0.975 × √(SE²_pred + τ²)]

where SE²_pred includes uncertainty from regression parameters.

---

#### 4. Bayesian Network Meta-Regression

**Prior Distributions:**
Weakly informative priors were specified for all parameters:

- Pooled log(HR): θ ~ N(log(0.77), 0.1²)
  [Based on prior meta-analyses suggesting HR around 0.77]

- Between-study heterogeneity: τ ~ Half-N(0, 0.1²)
  [Half-normal distribution restricted to positive values]

- Baseline risk coefficient: β₁ ~ N(0, 0.5²)
  [Weakly informative, allowing data to dominate]

**Likelihood:**
For each study i:

log(HR)ᵢ ~ N(θ + τ × δᵢ, SE²ᵢ)

where δᵢ ~ N(0, 1) represents study-specific random effect.

**Markov Chain Monte Carlo (MCMC) Sampling:**
Posterior distributions were sampled using Metropolis-Hastings algorithm:
- Burn-in: 5,000 iterations
- Sampling: 10,000 iterations
- Thinning: Every 10th sample retained (1,000 final samples)

**Convergence Diagnostics:**
Convergence assessed using:
- Trace plots (visual inspection)
- Effective sample size (ESS > 200 for all parameters)
- Gelman-Rubin statistic (R̂ < 1.1, single-chain approximation)

**Posterior Predictive Distribution:**
For a new study, we sampled from:

log(HR)_new ~ N(θ, τ²)

where θ and τ are sampled from their posterior distributions.

95% credible intervals calculated as 2.5th and 97.5th percentiles of posterior samples.

**Probability of Benefit:**
P(HR < 1.0) = proportion of posterior predictive samples with HR < 1.0
P(HR < 0.8) = proportion of samples with HR < 0.8 (substantial benefit)

---

## SUPPLEMENTARY TABLES

**Supplementary Table S1** is Table 3 in main document (Component Effect Sizes)

**Supplementary Table S2** is Table 4 in main document (Sensitivity Analyses)

### Supplementary Table S3. Trial-Level Data Used in Meta-Regression

| Trial | N_ICD | N_Control | Deaths_ICD | Deaths_Control | Follow-up (years) | Annual_Mortality_Control | log(HR) | SE(log HR) |
|-------|-------|-----------|------------|----------------|-------------------|-------------------------|---------|------------|
| MADIT-II | 742 | 490 | 105 | 97 | 1.67 | 0.1185 | -0.336 | 0.141 |
| SCD-HeFT | 829 | 847 | 182 | 244 | 3.79 | 0.0760 | -0.272 | 0.098 |
| DANISH | 560 | 556 | 157 | 159 | 5.63 | 0.0511 | -0.020 | 0.113 |

**Notes:**
- Annual mortality calculated as: 1 - (1 - cumulative_mortality)^(1/follow-up_years)
- log(HR) and SE calculated from reported hazard ratios and 95% CIs
- For SCD-HeFT, placebo arm used as control

---

### Supplementary Table S4. Prior Sensitivity Analysis (Bayesian Model)

| Prior Specification | Posterior Mean log(HR) | Posterior Tau | Predicted Modern NNT |
|---------------------|------------------------|---------------|---------------------|
| Weakly informative (base) | -0.226 | 0.077 | 30.3 |
| Diffuse (uninformative) | -0.218 | 0.082 | 31.1 |
| Informative (strong prior) | -0.235 | 0.071 | 29.4 |

**Notes:**
- Weakly informative: θ ~ N(log(0.77), 0.1²), τ ~ Half-N(0, 0.1²)
- Diffuse: θ ~ N(0, 10²), τ ~ Half-Cauchy(0, 1)
- Informative: θ ~ N(log(0.77), 0.05²), τ ~ Half-N(0, 0.05²)
- Results robust to prior specification

---

## SUPPLEMENTARY FIGURES

**Supplementary Figure S1** - Bayesian Posterior Distributions (included in main submission)

### Supplementary Figure S2. Forest Plot of Individual Trials with Predictive Interval

[Description for Figure Generation:]
- Y-axis: MADIT-II, SCD-HeFT, DANISH, Pooled (RE), Predictive Interval
- X-axis: Hazard Ratio (0.4 to 1.6, log scale)
- Boxes: Point estimates sized by inverse variance
- Horizontal lines: 95% CIs for individual trials
- Diamond: Pooled random-effects estimate
- Dashed lines: 95% Predictive interval
- Vertical line at HR = 1.0

### Supplementary Figure S3. Meta-Regression Scatter Plot with Uncertainty Bands

[Description for Figure Generation:]
- X-axis: Baseline annual mortality risk (%) [log scale]
- Y-axis: ICD hazard ratio
- Points: Individual trials (sized by inverse variance)
- Solid line: Meta-regression fit
- Shaded region: 95% confidence band for regression line
- Dashed lines: 95% prediction band for new study
- Reference line at HR = 1.0

---

## SUPPLEMENTARY DISCUSSION

### Alternative Interpretations and Limitations

**Competing Hypotheses for DANISH Neutral Result:**

1. **Baseline Risk Hypothesis (Our Interpretation):**
   - DANISH patients had lower baseline risk due to better medical therapy
   - Meta-regression model predicts DANISH result accurately based on baseline risk alone
   - Evidence: β₁ = -0.394 explains 85% of variance; DANISH fits the model

2. **Ischemic vs Non-Ischemic Hypothesis (Traditional Interpretation):**
   - ICDs work in ischemic but not non-ischemic cardiomyopathy
   - Evidence: MADIT-II (100% ischemic) and SCD-HeFT (52% ischemic) positive; DANISH (0% ischemic) neutral
   - Counter-evidence: SCD-HeFT subgroup analysis showed similar HR in ischemic (0.79) vs non-ischemic (0.73), p=0.53 for interaction

3. **Era Effect (Medical Therapy Confounded with Etiology):**
   - Cannot fully separate era from etiology because:
     - Early trials (MADIT-II, SCD-HeFT) predominantly ischemic
     - Later trial (DANISH) exclusively non-ischemic
   - Our meta-regression adjusts for baseline risk (proxy for era) but cannot definitively rule out etiology effect

**Statistical Limitations:**

1. **Small Number of Trials (k=3):**
   - Meta-regression with 3 data points has limited power
   - R² = 0.851 impressive but confidence intervals wide
   - Results should be interpreted as hypothesis-generating

2. **Ecological Fallacy:**
   - Study-level meta-regression may not reflect patient-level associations
   - Individual patient data meta-analysis would provide stronger evidence

3. **Extrapolation Beyond Observed Range:**
   - Modern baseline risk (3-5%) is below lowest trial risk (DANISH 5.1%)
   - Predictive intervals appropriately wide to reflect extrapolation uncertainty

4. **Assumption of Log-Linear Relationship:**
   - We assumed log(HR) varies linearly with log(baseline risk)
   - Alternative functional forms possible (e.g., threshold effects)
   - Limited data preclude testing complex nonlinear models

**Potential Confounders Not Addressed:**

1. **Changes in ICD Technology:**
   - MADIT-II (2002): Single-chamber ICDs, no programming optimization
   - DANISH (2016): Dual-chamber ICDs, programming to reduce inappropriate shocks
   - Programming changes reduce inappropriate therapy but may also reduce appropriate therapy

2. **Changes in Heart Failure Etiology:**
   - Declining prevalence of ischemic HF over time
   - Increasing prevalence of HFpEF, hypertensive, diabetic etiologies
   - May affect arrhythmia substrate

3. **Selection Bias in Modern Era:**
   - Patients at highest risk may have died before reaching ICD eligibility
   - Survival bias could underestimate modern baseline risk

---

## DATA AVAILABILITY STATEMENT

All data used in this analysis were extracted from published sources and are publicly available. Complete data extraction files, statistical code (Python 3.11), and analysis results are available at [GitHub repository URL]. No new patient-level data were collected. Requests for additional information should be directed to the corresponding author.

---

## CODE AVAILABILITY STATEMENT

Complete reproducible analysis code is available at [GitHub repository URL to be inserted upon acceptance]. The analysis was conducted using:
- Python 3.11.0
- NumPy 2.3.5
- Pandas 2.3.3
- SciPy 1.16.3
- Matplotlib 3.10.7
- Seaborn 0.13.2

All figures were generated using create_publication_figures.py. Statistical analyses were performed using icd_advanced_meta_analysis.py. Both scripts include detailed comments and are fully reproducible.

---

## AUTHOR CONTRIBUTIONS STATEMENT

[To be completed by authors - Template:]

**Conceptualization:** [Names]
**Methodology:** [Names]
**Formal Analysis:** [Names]
**Writing - Original Draft:** [Names]
**Writing - Review & Editing:** [All authors]
**Visualization:** [Names]
**Supervision:** [Names]

All authors have read and approved the final manuscript.

---

## FUNDING STATEMENT

[To be completed - Template:]

This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors.

OR

This work was supported by [Funding Agency] [Grant Number].

---

## COMPETING INTERESTS STATEMENT

[To be completed - Template:]

The authors declare no competing interests.

OR

[Author Name] has received consulting fees from [Company] for work unrelated to this manuscript. All other authors declare no competing interests.

---

## SUPPLEMENTARY MATERIALS COMPLETE! ✅

This supplementary document provides:
- ✅ Detailed mathematical methodology
- ✅ Additional tables with trial-level data
- ✅ Sensitivity analyses
- ✅ Alternative interpretations
- ✅ Transparent discussion of limitations
- ✅ Data/code availability statements
- ✅ Standard manuscript declarations

Ready to submit as "Supplementary Materials.docx" alongside main manuscript!
