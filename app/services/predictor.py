import joblib

model = joblib.load("models/cashflow_model.pkl")

def predict_future_cash_flow(df):
    df['Month'] = df['Date'].dt.to_period('M')
    monthly = df.groupby('Month')['Amount'].sum().reset_index()
    future = model.predict(n_periods=3)
    return future
