import plotly.express as px

def sales_bar_chart(df, x_col, y_col):

    fig = px.bar(
        df,
        x=x_col,
        y=y_col,
        color=y_col,
        template="plotly_dark"
    )

    return fig


def sales_line_chart(df, x_col, y_col):

    fig = px.line(
        df,
        x=x_col,
        y=y_col,
        markers=True,
        template="plotly_dark"
    )

    return fig


def sales_pie_chart(df, names_col, values_col):

    fig = px.pie(
        df,
        names=names_col,
        values=values_col
    )

    return fig


def correlation_heatmap(df):

    numeric_df = df.select_dtypes(
        include=["int64","float64"]
    )

    fig = px.imshow(
        numeric_df.corr(),
        text_auto=True,
        aspect="auto"
    )

    return fig
