import pandas as pd

demographic_path = 'DEMO_L.XPT'
demo = pd.read_sas(demographic_path, format='xport') #, encoding='latin1')  # Try 'latin1' or 'iso-8859-1' if UTF-8 fails
demo

survey_huq_path = 'HUQ_L.XPT'
access = pd.read_sas(survey_huq_path, format='xport')
access

fasting_glucose_path = 'GLU_L.XPT'
glucose = pd.read_sas(fasting_glucose_path, format='xport')
glucose

crp_path = 'HSCRP_L.XPT'
crp = pd.read_sas(crp_path, format='xport')
crp

body_path = 'BMX_L.XPT'
body = pd.read_sas(body_path, format='xport')
body

bp_path = 'BPXO_L.XPT'
bp = pd.read_sas(bp_path, format='xport')
bp



### Question 1: "Is there an association between marital status (married or not married) and education level (bachelor’s degree or higher vs. less than a bachelor’s degree)?"
# Variables: DMDMARTZ (marital status) and DMDEDUC2 (education level). Recode as specified



from scipy.stats import chi2_contingency

#data = {
#    'demo'
    }

# Create a DataFrame
df = pd.DataFrame(demo)

# Create a contingency table
contingency_table = pd.crosstab(df['DMDMARTZ'], df['DMDEDUC2'])
print("Contingency Table:")
print(contingency_table)

# Perform Chi-Square test
stat, p_value, dof, expected = chi2_contingency(contingency_table)
print(f"\nChi-Square Test Statistic: {stat}, p-value: {p_value}")
print("Expected Frequencies:")
print(expected)

# Interpretation
if p_value > 0.05:
    print("\nNo significant association between marital status and education.")
else:
    print("\nSignificant association between marital status and education.")



#Question 2: "Is there a difference in the mean sedentary behavior time between those who are married and those who are not married?"
from scipy.stats import ttest_rel

# Example data
group1 = 'DMDMARTZ'  # Before treatment
group2 = 'DMDEDUC2'  # After treatment

# Perform paired t-test
stat, p_value = ttest_rel(group1, group2)
print(f"Paired t-Test Statistic: {stat}, p-value: {p_value}")

# Interpretation
if p_value > 0.05:
    print("No significant difference between the two conditions.")
else:
    print("Significant difference between the two conditions.")



#Question 3: "How do age and marital status affect systolic blood pressure?"
import pandas as pd
  import statsmodels.api as sm
  from statsmodels.formula.api import ols

  # Example data
  data = pd.DataFrame({
      'group1': 'RIDAGEYR',
      'group2': 'DMDMARTZ',
      'values': 'BPXOSY3']
  })

  # Perform 2-way ANOVA
  model = ols('values ~ C(group1) + C(group2) + C(group1):C(group2)', data=data).fit()
  anova_table = sm.stats.anova_lm(model, typ=2)
  print(anova_table)






# Question 4: "Is there a correlation between self-reported weight and minutes of sedentary behavior?"

from scipy.stats import pearsonr
x = "WHD020"
y = "PAD680"

# Calculate Pearson correlation coefficient
corr, p_value = pearsonr(x, y)
print(f'Pearson Correlation Coefficient: {corr}, p-value: {p_value}')

# Interpretation
if abs(corr) > 0.7:
    print("Strong linear relationship.")
else:
    print("Weak or non-linear relationship.")


