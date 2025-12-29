"""Simple CLI to run the pipeline and print summary results."""
import argparse
from utils.pipeline import run_pipeline


def main():
    parser = argparse.ArgumentParser(description="Run FX pipeline for a currency pair")
    parser.add_argument("pair", help="Currency pair file name without extension, e.g. USDINR")
    parser.add_argument("target_vol", type=float, help="Target volatility in percent, e.g. 8")
    parser.add_argument("--save-report", action="store_true", help="Save PDF report to reports/")
    args = parser.parse_args()

    results = run_pipeline(args.pair, args.target_vol, save_report=args.save_report)
    print("Pair:", args.pair)
    print("Regime:", results.get('regime'))
    print("FX Score:", round(results.get('fx_score', 0), 4))
    print("Position:", results.get('position'))
    print("Scenarios:\n", results.get('scenarios'))


if __name__ == '__main__':
    main()
