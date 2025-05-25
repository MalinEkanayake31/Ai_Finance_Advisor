from streamlit_echarts import st_echarts

def show_spending_chart(summary):
    options = {
        "xAxis": {"type": "category", "data": summary['Month'].astype(str).tolist()},
        "yAxis": {"type": "value"},
        "series": [{"data": summary['Amount'].tolist(), "type": "bar"}]
    }
    st_echarts(options=options)
