def summarize_spending(df):
    df['Month'] = df['Date'].dt.to_period('M')
    summary = df.groupby('Month')['Amount'].sum().reset_index()
    top_categories = df.groupby('Category')['Amount'].sum().sort_values(ascending=False).head(5)
    return summary, top_categories
