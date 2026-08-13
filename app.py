import streamlit as st
import pandas as pd

from agents.cleaner import clean_data
from agents.eda import generate_summary
from agents.visualizer import create_chart

st.set_page_config(
    page_title="AI Data Analyst",
    layout="wide"
)

st.title("🤖 Multi-Agent AI Data Analyst")

file = st.file_uploader(
    "Upload dataset",
    type=["csv"]
)

if file:

    df = pd.read_csv(file)

    st.success("Dataset Loaded")

    df = clean_data(df)

    summary = generate_summary(df)

    col1,col2,col3 = st.columns(3)

    col1.metric("Rows",summary["Rows"])
    col2.metric("Columns",summary["Columns"])
    col3.metric(
        "Missing Values",
        summary["Missing Values"]
    )

    st.dataframe(df.head())

    fig = create_chart(df)

    if fig:
        st.plotly_chart(
            fig,
            use_container_width=True
        )
