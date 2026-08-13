import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# -----------------------------------------------------
# PAGE CONFIG
# -----------------------------------------------------

st.set_page_config(
    page_title="Multi-Agent AI Data Analyst",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------------------------------
# CUSTOM CSS
# -----------------------------------------------------

st.markdown("""
<style>
.main{
    padding-top:20px;
}

.metric-card{
    padding:15px;
    border-radius:12px;
}

h1,h2,h3{
    color:#1f2937;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------
# DATA CLEANER AGENT
# -----------------------------------------------------

def clean_data(df):

    df = df.drop_duplicates()

    for col in df.columns:

        if pd.api.types.is_numeric_dtype(df[col]):

            df[col] = df[col].fillna(
                df[col].mean()
            )

        else:

            df[col] = df[col].fillna(
                "Unknown"
            )

    return df

# -----------------------------------------------------
# EDA AGENT
# -----------------------------------------------------

def generate_summary(df):

    return {
        "Rows": df.shape[0],
        "Columns": df.shape[1],
        "Missing Values": df.isnull().sum().sum(),
        "Duplicates": df.duplicated().sum()
    }

# -----------------------------------------------------
# INSIGHT AGENT
# -----------------------------------------------------

def generate_insights(df):

    insights = []

    numeric_cols = df.select_dtypes(
        include=np.number
    ).columns

    if len(numeric_cols) > 0:

        for col in numeric_cols:

            insights.append(
                f"📊 Average {col}: {round(df[col].mean(),2)}"
            )

            insights.append(
                f"📈 Maximum {col}: {round(df[col].max(),2)}"
            )

            insights.append(
                f"📉 Minimum {col}: {round(df[col].min(),2)}"
            )

    return insights

# -----------------------------------------------------
# RECOMMENDATION AGENT
# -----------------------------------------------------

def generate_recommendations(df):

    recommendations = []

    numeric_cols = df.select_dtypes(
        include=np.number
    ).columns

    if len(numeric_cols) > 0:

        recommendations.append(
            "Focus on increasing high-performing metrics."
        )

        recommendations.append(
            "Investigate low-performing categories."
        )

        recommendations.append(
            "Monitor trends using monthly dashboards."
        )

        recommendations.append(
            "Use forecasting to predict future performance."
        )

    return recommendations

# -----------------------------------------------------
# VISUALIZATION AGENT
# -----------------------------------------------------

def show_visualizations(df):

    st.subheader("📊 Visual Analysis")

    numeric_cols = list(
        df.select_dtypes(include=np.number).columns
    )

    if len(numeric_cols) == 0:
        st.warning(
            "No numeric columns found."
        )
        return

    selected_col = st.selectbox(
        "Select Numeric Column",
        numeric_cols
    )

    tab1, tab2, tab3 = st.tabs(
        ["Histogram",
         "Box Plot",
         "Pie Chart"]
    )

    with tab1:

        fig = px.histogram(
            df,
            x=selected_col,
            color_discrete_sequence=["#6366f1"]
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with tab2:

        fig = px.box(
            df,
            y=selected_col,
            color_discrete_sequence=["#22c55e"]
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with tab3:

        if len(df) < 100:

            fig = px.pie(
                values=df[selected_col]
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

# -----------------------------------------------------
# APP HEADER
# -----------------------------------------------------

st.title("🤖 Multi-Agent AI Data Analyst")

st.markdown("""
Upload a CSV file and let multiple AI agents:

✅ Clean Data

✅ Analyze Data

✅ Generate Insights

✅ Create Visualizations

✅ Provide Recommendations
""")

# -----------------------------------------------------
# FILE UPLOADER
# -----------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

# -----------------------------------------------------
# MAIN EXECUTION
# -----------------------------------------------------

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    # DEBUG: show column types
    st.subheader("Column Data Types")
    st.write(df.dtypes)

    st.success("Dataset uploaded successfully")

    # DATA CLEANING
    df = clean_data(df)

    # --------------------------
    # RAW DATA
    # --------------------------

    with st.expander(
        "📄 View Raw Dataset"
    ):
        st.dataframe(df)

    # --------------------------
    # CLEANING AGENT
    # --------------------------

    st.header("🧹 Data Cleaning Agent")

    df = clean_data(df)

    st.success(
        "Data cleaned successfully"
    )

    # --------------------------
    # KPI DASHBOARD
    # --------------------------

    st.header("📈 EDA Agent")

    summary = generate_summary(df)

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Rows",
        summary["Rows"]
    )

    c2.metric(
        "Columns",
        summary["Columns"]
    )

    c3.metric(
        "Missing Values",
        summary["Missing Values"]
    )

    c4.metric(
        "Duplicates",
        summary["Duplicates"]
    )

    # --------------------------
    # DATA TYPES
    # --------------------------

    st.subheader("Column Information")

    info_df = pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes.astype(str)
    })

    st.dataframe(info_df)

    # --------------------------
    # DESCRIPTIVE STATS
    # --------------------------

    st.subheader(
        "Statistical Summary"
    )

    st.dataframe(
        df.describe()
    )

    # --------------------------
    # CORRELATION MATRIX
    # --------------------------

    numeric_df = df.select_dtypes(
        include=np.number
    )

    if numeric_df.shape[1] > 1:

        st.subheader(
            "Correlation Heatmap"
        )

        corr = numeric_df.corr()

        fig = px.imshow(
            corr,
            text_auto=True,
            color_continuous_scale="RdBu"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # --------------------------
    # VISUALIZATION AGENT
    # --------------------------

    st.header(
        "📊 Visualization Agent"
    )

    show_visualizations(df)

    # --------------------------
    # INSIGHT AGENT
    # --------------------------

    st.header(
        "🧠 Insight Agent"
    )

    insights = generate_insights(df)

    for item in insights:
        st.info(item)

    # --------------------------
    # RECOMMENDATION AGENT
    # --------------------------

    st.header(
        "💡 Recommendation Agent"
    )

    recommendations = generate_recommendations(df)

    for item in recommendations:
        st.success(item)

    # --------------------------
    # DOWNLOAD CLEAN DATA
    # --------------------------

    st.header(
        "⬇ Download Cleaned Dataset"
    )

    csv = df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="Download CSV",
        data=csv,
        file_name="cleaned_dataset.csv",
        mime="text/csv"
    )

else:

    st.info(
        "Upload a CSV file to start analysis."
    )
