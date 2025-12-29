def backtest(df, score):
    df = df.copy()
    signal_val = 1 if score > 0 else -1
    df['signal'] = signal_val
    df['signal'] = df['signal'].astype(int)
    df['strategy_ret'] = df['signal'].shift(1).fillna(0) * df['fx_ret']
    df['cum_pnl'] = df['strategy_ret'].cumsum().fillna(0)
    return df
