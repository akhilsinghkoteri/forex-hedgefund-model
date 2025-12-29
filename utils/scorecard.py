import numpy as np


def fx_score(df, regime, lookback=12):
    """Compute a robust FX score.

    - Uses z-scores of recent values for `infl_diff`, `rate_diff`, `growth_diff`, and `vix`.
    - Inverts `vix` so higher implied vol reduces the score.
    - Applies lightweight regime adjustments and returns a normalized score in [-1, 1].
    """
    cols = {
        "valuation": "infl_diff",
        "rates": "rate_diff",
        "growth": "growth_diff",
        "risk": "vix",
    }

    window = max(1, min(len(df), lookback))
    features = {}
    for name, col in cols.items():
        if col not in df.columns:
            features[name] = 0.0
            continue
        s = df[col].dropna().tail(window)
        if s.empty:
            features[name] = 0.0
            continue
        last = s.iloc[-1]
        mu = s.mean()
        sigma = s.std(ddof=0)
        if sigma == 0 or np.isnan(sigma):
            z = 0.0
        else:
            z = (last - mu) / sigma
        # For risk (vix) higher = more negative
        if name == "risk":
            z = -z
        features[name] = float(z)

    weights = {"valuation": 0.35, "rates": 0.20, "growth": 0.30, "risk": 0.15}
    raw = sum(features[k] * weights[k] for k in weights)

    # regime adjustments (mild)
    if regime == "RISK-OFF":
        raw *= 0.8
    elif regime == "INFLATION SHOCK":
        raw *= 1.1

    # normalize to [-1, 1]
    score = float(np.tanh(raw))
    return score
