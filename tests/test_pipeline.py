import pytest

from utils.pipeline import run_pipeline


@pytest.mark.parametrize("pair", ["USDINR", "EURUSD", "GBPUSD"])
def test_run_pipeline(pair):
    # run pipeline without saving report
    results = run_pipeline(pair, 8, save_report=False)
    assert isinstance(results, dict)
    for k in ("df", "fx_score", "regime", "position", "scenarios"):
        assert k in results
    # df should have a date column and cum_pnl
    df = results["df"]
    assert "date" in df.columns
    assert "cum_pnl" in df.columns
