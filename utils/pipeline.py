import logging
from utils.data_loader import load_data
from utils.regime import detect_regime
from utils.scorecard import fx_score
from utils.backtest import backtest
from utils.scenario import scenario_engine
from utils.sizing import volatility_target
from utils.report import generate_pdf


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")


def run_pipeline(pair, target_vol, save_report=True):
    try:
        df = load_data(pair)
        regime = detect_regime(df)
        score = fx_score(df, regime)
        df = backtest(df, score)
        position = volatility_target(df, target_vol)
        scenarios = scenario_engine(df)

        if save_report:
            try:
                generate_pdf(pair, score, regime, position, scenarios)
            except Exception as e:
                logger.warning("Failed to generate PDF report: %s", e)

        return {
            "df": df,
            "fx_score": score,
            "regime": regime,
            "position": position,
            "scenarios": scenarios,
        }
    except Exception as e:
        logger.exception("Pipeline failed for %s: %s", pair, e)
        raise
