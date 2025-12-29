# FX Hedge Fund Platform

Lightweight FX analysis and backtest pipeline with Streamlit UI.

Usage
- Run the Streamlit app:

```bash
python3 -m streamlit run app.py
```

- Run pipeline from CLI (optionally save report):

```bash
python3 run_pipeline_cli.py USDINR 8 --save-report
```

Run tests:

```bash
pytest -q
```

Notes
- To push to GitHub, add a remote and `git push -u origin main`.
