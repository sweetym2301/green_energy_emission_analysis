#Project: Green Energy Production and CO₂ Emissions Analysis
#📌 Objective:
#Analyze and visualize trends in:
#Global energy production sources (fossil, solar, wind, nuclear)
#CO₂ emissions by country over time
#Identify top polluters vs. clean energy leaders


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the dataset
df = pd.read_csv("data/owid-energy-data.csv")
print(df.head())

# Print Shape of the Data Set
print("Shape of the dataset:" , df.shape)

# Print Column Names
print("\nColumn Names:")
print(df.columns.tolist())

# Check missing Percentage
missing_percentage = df.isnull().mean() * 100

# Columns with >50% missing
missing_over_50 = missing_percentage[missing_percentage > 50]
print("\nColumns with >50% missing values:")
print(missing_over_50.sort_values(ascending=False))

# Count of columns with >50% missing
print(f"\nTotal Columns with greater than 50% missing: {len(missing_over_50)}")

# Columns with <50% missing
missing_less_50 = missing_percentage[missing_percentage < 50]
print("\nColumns with <50% missing values:")
print(missing_less_50.sort_values(ascending=False))

# Count of columns with <50% missing
print(f"\nTotal Columns with less than 50% missing: {len(missing_less_50)}")

#Low missing %
keep_missing = missing_percentage[missing_percentage < 50].index
#Drop Low Variance Columns
low_var = df.nunique()
low_var_cols = low_var[low_var <=1].index
print(low_var)
# Keep only meaningful
useful_cols = set(keep_missing)-set(low_var_cols)
print("Possible Useful Columns : ",useful_cols)

# Keep only numeric columns
df_reduced = df[keep_missing]
df_numeric = df_reduced.select_dtypes(include=['float64', 'int64'])

print("Numeric columns selected for correlation heatmap:", df_numeric.columns.tolist())
# Compute correlation matrix
corr_matrix = df_numeric.corr()

print("\nCorrelation Matrix:")
print(corr_matrix.head())

# Take absolute correlation (for easy filtering)
corr_matrix_abs = corr_matrix.abs()

# Mask the diagonal (1.0 self-correlation)
np.fill_diagonal(corr_matrix_abs.values, 0)

# Find pairs where correlation > 0.7
strong_pairs = np.where(corr_matrix_abs > 0.7)

# Combine into a clean list of (row, column, value)
strong_corrs = []

for row, col in zip(*strong_pairs):
    if row < col:  # Avoid duplicate pairs (matrix is symmetric)
        strong_corrs.append(
            (corr_matrix.index[row],
             corr_matrix.columns[col],
             corr_matrix.iloc[row, col])
        )

# Show nicely
print("\nStrong correlations (>|0.7|):")
for row, col, corr_val in strong_corrs:
    print(f"{row} <--> {col} : {corr_val:.2f}")


# Create a new total fossil fuel production feature
df_reduced['total_fossil_production'] = (
    df_reduced['coal_production'] +
    df_reduced['oil_production'] +
    df_reduced['gas_production']
)

# Drop redundant columns
df_cleaned = df_reduced.drop([
    'coal_production',
    'oil_production',
    'gas_production',
    'primary_energy_consumption'
], axis=1)
print("Final Cleaned Data :", df_cleaned.shape)


# Save cleaned DataFrame
output_path = r"C:\Users\Dahiya2\Desktop\Project-1\green_energy_emissions\outputs\cleaned_green_energy.csv"
df_cleaned.to_csv(output_path, index=False)

print(f"✅ Cleaned data saved to: {output_path}")
