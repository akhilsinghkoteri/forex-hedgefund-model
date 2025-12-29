import streamlit as st
from utils.pipeline import run_pipeline
import plotly.express as px

st.set_page_config(page_title="Hedge Fund FX Platform", layout="wide")
st.title("Hedge Fund FX Macro Platform")

pair = st.sidebar.selectbox("Currency Pair", ["USDINR","EURUSD","GBPUSD"])
target_vol = st.sidebar.slider("Target Volatility (%)", 5, 15, 8)

# In Streamlit UI, avoid creating a PDF on every interaction
results = run_pipeline(pair, target_vol, save_report=False)

col1, col2, col3 = st.columns(3)
col1.metric("FX Score", round(results['fx_score'],2))
col2.metric("Regime", results['regime'])
col3.metric("Position Size", round(results['position'],2))

st.plotly_chart(px.line(results['df'], x="date", y="cum_pnl", title="Strategy PnL"), use_container_width=True)
st.plotly_chart(px.line(results['df'], x="date", y="fx_rate", title="FX Rate"), use_container_width=True)

st.subheader("Scenario Analysis")
st.table(results['scenarios'])

st.success("Daily FX Note saved to /reports folder")
