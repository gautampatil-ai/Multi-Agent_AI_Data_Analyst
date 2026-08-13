from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY"
)

def get_insights(df):

    sample = df.head().to_string()

    prompt = f"""
    Analyze this dataset:

    {sample}

    Give:
    1. Insights
    2. Trends
    3. Recommendations
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role":"user",
             "content":prompt}
        ]
    )

    return response.choices[0].message.content
