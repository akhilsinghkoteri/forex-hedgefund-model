import pandas as pd
import numpy as np

def load_data(pair):
    df = pd.read_csv(f"data/{pair}.csv", parse_dates=["date"])
    df['fx_ret'] = np.log(df['fx_rate']).diff()
    df['infl_diff'] = df['infl_dom'] - df['infl_for']
    df['rate_diff'] = df['rate_dom'] - df['rate_for']
    df['growth_diff'] = df['gdp_dom'] - df['gdp_for']
    return df.dropna()
