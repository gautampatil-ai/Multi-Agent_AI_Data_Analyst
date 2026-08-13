import plotly.express as px

def create_chart(df):

    numeric_cols = df.select_dtypes(
        include=["int64","float64"]
    ).columns

    if len(numeric_cols):

        fig = px.histogram(
            df,
            x=numeric_cols[0]
        )

        return fig

    return None
