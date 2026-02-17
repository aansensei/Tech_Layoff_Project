import streamlit as st
import pandas as pd
import plotly.express as px

# page configuration
st.set_page_config(page_title="Layoff Forecaster",
                   page_icon="📉", layout="wide")

st.title("📉 Global Tech Layoffs & Macro-Economics Dashboard")
st.markdown(
    "**Author:** Nguyen, Cao Thien An | **Stack:** Python, Random Forest, Streamlit")
st.markdown("---")


@st.cache_data
def load_data():
    # phase 4 results
    df_pred = pd.read_csv('data/processed/model_predictions_for_tableau.csv')
    df_pred['Date'] = pd.to_datetime(df_pred['Date'])

    # Fix column name for predictions if needed
    if 'Predicted_Layoffs_RF' in df_pred.columns:
        df_pred.rename(
            columns={'Predicted_Layoffs_RF': 'Predicted_Layoffs'}, inplace=True)

    # phase 1-3 raw data (cleaned) for detailed exploration
    df_raw = pd.read_csv('data/processed/tech_layoffs_clean.csv')

    # --- FIX: Tự động chuẩn hóa tên cột ---
    df_raw.columns = df_raw.columns.str.strip()
    rename_map = {
        'date': 'Date', 'laid_off_date': 'Date',
        'Date_Added': 'Date', 'date_added': 'Date',
        'laid_off_count': 'Laid_Off_Count',
        'industry': 'Industry'
    }
    df_raw.rename(columns=rename_map, inplace=True)
    # -------------------------------------------

    df_raw['Date'] = pd.to_datetime(df_raw['Date'])
    return df_pred, df_raw


try:
    df_pred, df_raw = load_data()
except FileNotFoundError:
    st.error(
        "Data files not found. Please ensure CSV files are in 'data/processed/' directory.")
    st.stop()
except KeyError as e:
    st.error(
        f"Lỗi cấu trúc dữ liệu: {e}. Các cột hiện có: {pd.read_csv('data/processed/tech_layoffs_clean.csv').columns.tolist()}")
    st.stop()

# 3. SIDEBAR - FILTERS
st.sidebar.header("Configuration")
year_filter = st.sidebar.slider("Select Year Range:", 2020, 2026, (2022, 2025))

# filter data based on selected year range
filtered_pred = df_pred[(df_pred['Date'].dt.year >= year_filter[0]) & (
    df_pred['Date'].dt.year <= year_filter[1])]
filtered_raw = df_raw[(df_raw['Date'].dt.year >= year_filter[0]) & (
    df_raw['Date'].dt.year <= year_filter[1])]

# 4. main dashboard content

#  Key Metrics
col1, col2, col3 = st.columns(3)
total_layoffs = int(filtered_raw['Laid_Off_Count'].sum())
avg_layoffs = int(filtered_raw['Laid_Off_Count'].mean())
# Handle empty data case for max month
if not filtered_pred.empty:
    max_layoff_month = filtered_pred.loc[filtered_pred['Actual_Layoffs'].idxmax(
    )]['Date'].strftime('%B %Y')
else:
    max_layoff_month = "N/A"

col1.metric("Total Layoffs", f"{total_layoffs:,}")
col2.metric("Avg Layoffs / Month", f"{avg_layoffs:,}")
col3.metric("Peak Month", max_layoff_month)

st.markdown("---")

# part 2: AI Forecast vs Reality
st.subheader("AI(ML) Forecast vs. Reality: The 'Social Contagion' Gap")

fig_pred = px.line(filtered_pred, x='Date', y=['Actual_Layoffs', 'Predicted_Layoffs'],
                   labels={'value': 'Employees', 'variable': 'Metric'},
                   color_discrete_map={'Actual_Layoffs': 'black', 'Predicted_Layoffs': '#00CC96'})

fig_pred.update_layout(hovermode="x unified")
st.plotly_chart(fig_pred, use_container_width=True)

st.info("**Insight:** The gap between the Green line (Prediction) and Black line (Actual) in early 2025 represents the psychological 'Herd Mentality' factor.")

# Part 3: Explore by Industry
st.subheader("Explore Layoffs by Industry")

all_industries = sorted(df_raw['Industry'].astype(str).unique().tolist())
selected_industry = st.selectbox(
    "Select an Industry:", all_industries, index=0)

industry_df = filtered_raw[filtered_raw['Industry'] == selected_industry]
industry_group = industry_df.groupby(
    'Date')['Laid_Off_Count'].sum().reset_index()

fig_ind = px.bar(industry_group, x='Date', y='Laid_Off_Count',
                 color='Laid_Off_Count', title=f"Layoff Trends in {selected_industry}")
st.plotly_chart(fig_ind, use_container_width=True)

# Part 4: Raw Data Exploration...
with st.expander("See Raw Data"):
    st.dataframe(filtered_pred)
