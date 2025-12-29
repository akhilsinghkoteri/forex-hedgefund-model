import pandas as pd

def scenario_engine(df):
    base = df['fx_rate'].iloc[-1]
    return pd.DataFrame({
        "Scenario":["Base","High Inflation","Risk Shock"],
        "FX Move %":[0, 2.5, 4.8]
    })
