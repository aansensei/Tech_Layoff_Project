import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Layoff Forecaster",
                   page_icon="📉", layout="wide")

st.title("📉 Global Tech Layoffs & Macro-Economics Dashboard")
st.markdown(
    "**Author:** Nguyen, Cao Thien An | **Stack:** Python, Random Forest, Streamlit")
st.markdown("---")


@st.cache_data
def load_data():
    df_pred = pd.read_csv('data/processed/model_predictions_for_tableau.csv')
    df_pred['Date'] = pd.to_datetime(df_pred['Date'])

    if 'Predicted_Layoffs_RF' in df_pred.columns:
        df_pred.rename(
            columns={'Predicted_Layoffs_RF': 'Predicted_Layoffs'}, inplace=True)

    df_raw = pd.read_csv('data/processed/tech_layoffs_clean.csv')

    df_raw.columns = df_raw.columns.str.strip()
    rename_map = {
        'date': 'Date', 'laid_off_date': 'Date',
        'Date_Added': 'Date', 'date_added': 'Date',
        'laid_off_count': 'Laid_Off_Count',
        'industry': 'Industry'
    }
    df_raw.rename(columns=rename_map, inplace=True)
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
        f"Data structure error: {e}. Please check column names in your CSV files.")
    st.stop()

st.sidebar.header("Configuration")
year_filter = st.sidebar.slider("Select Year Range:", 2020, 2026, (2022, 2025))

filtered_pred = df_pred[(df_pred['Date'].dt.year >= year_filter[0]) & (
    df_pred['Date'].dt.year <= year_filter[1])]
filtered_raw = df_raw[(df_raw['Date'].dt.year >= year_filter[0]) & (
    df_raw['Date'].dt.year <= year_filter[1])]

if filtered_raw.empty:
    st.warning(
        f"No data available for the period {year_filter[0]}-{year_filter[1]}. Please select a different range.")
else:
    col1, col2, col3 = st.columns(3)

    total_layoffs = int(filtered_raw['Laid_Off_Count'].sum())
    avg_layoffs = int(
        filtered_raw['Laid_Off_Count'].mean()) if not filtered_raw.empty else 0

    if not filtered_pred.empty:
        idx_max = filtered_pred['Actual_Layoffs'].idxmax()
        if pd.notna(idx_max):
            max_layoff_month = filtered_pred.loc[idx_max]['Date'].strftime(
                '%B %Y')
        else:
            max_layoff_month = "N/A"
    else:
        max_layoff_month = "N/A"

    col1.metric("Total Layoffs", f"{total_layoffs:,}")
    col2.metric("Avg Layoffs / Month", f"{avg_layoffs:,}")
    col3.metric("Peak Month", max_layoff_month)

    st.markdown("---")

    st.subheader("AI(ML) Forecast vs. Reality: The 'Social Contagion' Gap")

    colors = {'Actual_Layoffs': '#FF4B4B', 'Predicted_Layoffs': '#0083B8'}

    if not filtered_pred.empty:
        fig_pred = px.line(filtered_pred, x='Date', y=['Actual_Layoffs', 'Predicted_Layoffs'],
                           labels={'value': 'Employees', 'variable': 'Metric'},
                           color_discrete_map=colors)

        fig_pred.update_layout(hovermode="x unified")
        st.plotly_chart(fig_pred, use_container_width=True)

        st.info("**Insight:** The gap between the **Blue line (Prediction)** and **Red line (Actual)** in early 2025 represents the psychological 'Herd Mentality' factor.")
    else:
        st.info("No forecast data available for this period.")

    st.subheader("Explore Layoffs by Industry")

    all_industries = sorted(df_raw['Industry'].astype(str).unique().tolist())
    if all_industries:
        selected_industry = st.selectbox(
            "Select an Industry:", all_industries, index=0)

        industry_df = filtered_raw[filtered_raw['Industry']
                                   == selected_industry]

        if not industry_df.empty:
            industry_group = industry_df.groupby(
                'Date')['Laid_Off_Count'].sum().reset_index()

            fig_ind = px.bar(industry_group, x='Date', y='Laid_Off_Count',
                             title=f"Layoff Trends in {selected_industry}")
            st.plotly_chart(fig_ind, use_container_width=True)
        else:
            st.write(
                f"No data available for {selected_industry} in this period.")

with st.expander("See Raw Data"):
    st.dataframe(filtered_pred)
