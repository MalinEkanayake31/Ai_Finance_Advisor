import pandas as pd

def parse_statement(file):
    if file.name.endswith('.csv'):
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date')
    return df
