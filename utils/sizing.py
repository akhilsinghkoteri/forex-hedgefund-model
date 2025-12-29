import numpy as np


def volatility_target(df, target_vol):
    """Return a position size that targets `target_vol` (percent).

    - `target_vol` is given in percent (e.g., 8 for 8%).
    - We compute realized_vol as annualized volatility (decimal),
      then compute position = (target_vol/100) / realized_vol.
    - If realized_vol is zero or very small, return 0 to avoid blowups.
    - Cap position at 1.0 (100% notional) as a safety default.
    """
    realized_vol = df['fx_ret'].std() * (252 ** 0.5)
    if realized_vol is None or realized_vol == 0 or np.isnan(realized_vol):
        return 0.0
    position = (target_vol / 100.0) / realized_vol
    # Safety caps
    position = max(0.0, min(1.0, position))
    return position
