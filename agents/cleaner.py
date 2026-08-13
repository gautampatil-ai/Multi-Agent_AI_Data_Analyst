import pandas as pd

def clean_data(df):

    df = df.drop_duplicates()

    for col in df.columns:

        if df[col].dtype == "object":
            df[col].fillna("Unknown", inplace=True)

        else:
            df[col].fillna(df[col].mean(), inplace=True)

    return df
