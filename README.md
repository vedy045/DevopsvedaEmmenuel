# ITLDO801 Assignment 3 — Test Logging and Reporting with Selenium

**Student:** Setako Vedaste  
**Registration number:** 20250203  
**Date:** 26 October 2026

This assignment records what was tested, the expected and actual results, status, duration, and supporting details in timestamped log files.

- Portfolio: https://vedy045.github.io/DevopsvedaEmmenuel/
- Test plan: [TEST_PLAN.md](TEST_PLAN.md)
- Selenium test script: [test_portfolio.py](test_portfolio.py)
- Dependencies: [requirements.txt](requirements.txt)
- Logs: [logs/](logs/)

## Run locally
1. Install Python 3.10+ and Google Chrome.
2. Install dependencies: `python -m pip install -r requirements.txt`
3. Run: `python test_portfolio.py`

Selenium Manager may locate or download a compatible ChromeDriver automatically. The script creates a uniquely timestamped log for each run and saves screenshots for failures when possible. Run the script at least three times and commit the generated timestamped logs as evidence. Do not create or edit log entries by hand. TC-07 intentionally records a failure because `#missing-section` should not exist.
