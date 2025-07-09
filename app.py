# app.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Page config
st.set_page_config(
    page_title="Green Energy Production & Emissions Dashboard",
    layout="wide"
)

# Load cleaned data
data_path = r"C:\Users\Dahiya2\Desktop\Project-1\green_energy_emissions\outputs\cleaned_green_energy.csv"
df = pd.read_csv(data_path)

# Dashboard Title
st.title("🌍 Green Energy Production & Emissions Dashboard")

# Intro / Tooltip
st.markdown("""
This dashboard visualizes **green energy production, fossil fuel trends, and emissions** across countries.
**Note:** All production values are measured in **Terawatt-hours (TWh)**, where **1 TWh = 1 trillion watt-hours**.
""")

# Data Preview
st.subheader("🔍 Dataset Preview")
st.dataframe(df.head())

# Sidebar Filters
st.sidebar.header("📌 Filters")

# Country filter
countries = df['country'].dropna().unique()
selected_country = st.sidebar.selectbox(
    "Select Country:",
    sorted(countries)
)

# Year range filter
min_year = int(df['year'].min())
max_year = int(df['year'].max())
selected_years = st.sidebar.slider(
    "Select Year Range:",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year)
)

# Filtered DataFrame
filtered_df = df[
    (df['country'] == selected_country) &
    (df['year'] >= selected_years[0]) &
    (df['year'] <= selected_years[1])
]

st.write(f"**Showing data for:** {selected_country} ({selected_years[0]} - {selected_years[1]})")

# ------------------------------
# 📈 1. GDP over time
st.subheader(f"📈 GDP Trend for {selected_country}")
fig1, ax1 = plt.subplots(figsize=(10, 5))
sns.lineplot(data=filtered_df, x='year', y='gdp', ax=ax1)
ax1.set_ylabel("GDP (current US$)")
st.pyplot(fig1)

# ------------------------------
# 📈 2. Population over time
st.subheader(f"👥 Population Trend for {selected_country}")
fig2, ax2 = plt.subplots(figsize=(10, 5))
sns.lineplot(data=filtered_df, x='year', y='population', ax=ax2)
ax2.set_ylabel("Population")
st.pyplot(fig2)

# ------------------------------
# 📈 3. Total Fossil Production over time (TWh)
st.subheader(f"⚡ Total Fossil Fuel Production (TWh) - {selected_country}")
fig3, ax3 = plt.subplots(figsize=(10, 5))
sns.lineplot(data=filtered_df, x='year', y='total_fossil_production', ax=ax3)
ax3.set_ylabel("Total Fossil Production (TWh)")
st.pyplot(fig3)

# ------------------------------
# 📈 4. Coal, Gas, Oil Production Changes (TWh)
st.subheader(f"🔄 Annual Production Change - Coal, Gas, Oil (TWh)")
fig4, ax4 = plt.subplots(figsize=(12, 6))
sns.lineplot(data=filtered_df, x='year', y='coal_prod_change_twh', label='Coal', ax=ax4)
sns.lineplot(data=filtered_df, x='year', y='gas_prod_change_twh', label='Gas', ax=ax4)
sns.lineplot(data=filtered_df, x='year', y='oil_prod_change_twh', label='Oil', ax=ax4)
ax4.set_ylabel("Production Change (TWh)")
ax4.legend()
st.pyplot(fig4)

# ------------------------------
# 📈 5. Per Capita Production
st.subheader(f"👤 Per Capita Production - Coal, Gas, Oil")
fig5, ax5 = plt.subplots(figsize=(12, 6))
sns.lineplot(data=filtered_df, x='year', y='coal_prod_per_capita', label='Coal per Capita', ax=ax5)
sns.lineplot(data=filtered_df, x='year', y='gas_prod_per_capita', label='Gas per Capita', ax=ax5)
sns.lineplot(data=filtered_df, x='year', y='oil_prod_per_capita', label='Oil per Capita', ax=ax5)
ax5.set_ylabel("Production per Capita (TWh per person)")
ax5.legend()
st.pyplot(fig5)

# ------------------------------
# 📈 6. Energy Consumption Change
st.subheader(f"⚡ Energy Consumption Change")
fig6, ax6 = plt.subplots(figsize=(10, 5))
sns.lineplot(data=filtered_df, x='year', y='energy_cons_change_twh', label='Change (TWh)', ax=ax6)
sns.lineplot(data=filtered_df, x='year', y='energy_cons_change_pct', label='Change (%)', ax=ax6)
ax6.set_ylabel("Energy Consumption Change")
ax6.legend()
st.pyplot(fig6)

# ------------------------------
# 📉 7. GDP vs Total Fossil Production
st.subheader(f"💡 GDP vs Total Fossil Production")
fig7, ax7 = plt.subplots(figsize=(10, 5))
sns.scatterplot(data=filtered_df, x='total_fossil_production', y='gdp', ax=ax7)
ax7.set_xlabel("Total Fossil Production (TWh)")
ax7.set_ylabel("GDP")
st.pyplot(fig7)

# ------------------------------
# 🔗 8. Correlation Heatmap
st.subheader(f"📌 Correlation Heatmap")
numeric_df = filtered_df.drop(columns=['country', 'iso_code'])
corr = numeric_df.corr()
fig8, ax8 = plt.subplots(figsize=(12, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", ax=ax8)
st.pyplot(fig8)

# ------------------------------
# 📄 Filtered Data & Download
st.subheader("📂 Filtered Data Table")
st.dataframe(filtered_df)

st.download_button(
    label="⬇️ Download Filtered Data as CSV",
    data=filtered_df.to_csv(index=False).encode('utf-8'),
    file_name=f"{selected_country}_{selected_years[0]}_{selected_years[1]}.csv",
    mime='text/csv'
)
