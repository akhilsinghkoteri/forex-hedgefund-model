import numpy as np


def detect_regime(df):
    df = df.copy()
    # defensive: ensure columns exist
    if 'vix' not in df.columns or 'infl_diff' not in df.columns:
        return 'UNKNOWN'

    # use a short rolling average for stability
    vix = df['vix'].dropna().tail(3).mean()
    infl = df['infl_diff'].dropna().tail(3).mean()

    if np.isnan(vix) or np.isnan(infl):
        return 'UNKNOWN'

    if vix > 25:
        return "RISK-OFF"
    elif infl > 0.03:
        return "INFLATION SHOCK"
    else:
        return "RISK-ON"
