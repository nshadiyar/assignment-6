# Assignment 6: Data-Driven and Cross-Browser Automated Testing

## Assignment Overview

This project implements **data-driven** and **cross-browser** automated UI tests for a login page. Test inputs and expected outcomes are read from an Excel file; the same login flow runs for each row. Tests can run **locally** (Chrome/Firefox) or on **Sauce Labs** cloud (Chrome and Firefox, latest).

## Tested Website

- **URL:** https://practicetestautomation.com/practice-test-login/

## Tech Stack

- **Python 3**
- **Selenium WebDriver**
- **openpyxl** (Excel `.xlsx` read)
- **Sauce Labs** (remote cross-browser execution)

## How Data-Driven Testing Works

1. **Test data** is stored in `test_data.xlsx` with columns: `username`, `password`, `expected_result`.
2. **expected_result** is either `SUCCESS` or `ERROR`.
3. The script reads all rows from the sheet, then for each row:
   - Opens the login page.
   - Fills username and password and submits.
   - Determines the **actual** result from the page (success message vs error message).
   - **Asserts** that actual result matches expected result.
   - Logs **PASSED** or **FAILED** (or **SKIPPED** for invalid rows) in the console.
4. The same test logic is reused for every row; only the data changes.

## Positive and Negative Test Cases

- **Positive (SUCCESS):** Valid credentials. Expected: page contains “Logged In Successfully”.
- **Negative (ERROR):** Invalid credentials (wrong username/password). Expected: page contains an “invalid” error message.

Example rows in `test_data.xlsx`:

| username   | password   | expected_result |
|-----------|------------|-----------------|
| student   | Password123| SUCCESS         |
| wronguser | wrongpass  | ERROR           |

## Sauce Labs Configuration and Setup

- **Credentials:** Read from environment variables (no hard-coded credentials):
  - `SAUCE_USERNAME` – your Sauce Labs username
  - `SAUCE_ACCESS_KEY` – your Sauce Labs access key (from [User Settings](https://app.saucelabs.com/user-settings))
- **Endpoint:** **US West** is used by default (`https://ondemand.us-west-1.saucelabs.com/wd/hub`). To use **EU Central**, set `SAUCE_ENDPOINT=eu` (uses `https://ondemand.eu-central-1.saucelabs.com/wd/hub`).
- **Mode:** Tests run in automated mode via Selenium Remote WebDriver against the Sauce Labs grid.
- **Test names:** Each run uses a meaningful name including dataset row number and expected result (e.g. `Login DDT - Row 1 (SUCCESS) - chrome`) so runs are easy to find in the dashboard.

## How to Run Tests Locally

1. Create a virtual environment and install dependencies:

   ```bash
   cd automation-ddt
   python3 -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. Ensure `test_data.xlsx` exists (create it with `python create_test_data.py` if needed).

3. Run the script (default: local Chrome):

   ```bash
   python test_login_ddt.py
   ```

4. Optional: use local Firefox:

   ```bash
   BROWSER=firefox python test_login_ddt.py
   ```

5. You need Chrome/GeckoDriver installed and on `PATH` for local runs.

## How to Run Tests on Sauce Labs

1. Set your Sauce Labs credentials:

   ```bash
   export SAUCE_USERNAME="your_username"
   export SAUCE_ACCESS_KEY="your_access_key"
   ```

2. Run with Sauce Labs (runs on Chrome and Firefox by default):

   ```bash
   RUN_SAUCE_LABS=1 python test_login_ddt.py
   ```

3. Optional: use EU data center:

   ```bash
   export SAUCE_ENDPOINT=eu
   RUN_SAUCE_LABS=1 python test_login_ddt.py
   ```

4. Optional: run on a single browser:

   ```bash
   RUN_SAUCE_LABS=1 BROWSER=chrome python test_login_ddt.py
   RUN_SAUCE_LABS=1 BROWSER=firefox python test_login_ddt.py
   ```

5. Each test run appears in the [Sauce Labs dashboard](https://app.saucelabs.com) under **Automated** → **Test Results**, with the test name (e.g. `Login DDT - Row 1 (SUCCESS) - chrome`) and build name `Assignment6-DDT`.

## Screenshots, Video Recordings, and Execution Logs in Sauce Labs

- Go to [Sauce Labs](https://app.saucelabs.com) → **Automated** (left panel) → **Test Results**.
- Open **Virtual Devices** (or **Real Devices** if applicable), then click a test to open its details.
- On the test details page you can find:
  - **Video:** Recording of the test run (often in a **Video** tab or section).
  - **Screenshots:** Captured during the run (in a **Screenshots** or **Assets** section).
  - **Logs:** Test log and option to download JSON log (e.g. **Logs** or **Commands** tab).
- Metadata (Job ID, test name, build, platform, browser) is shown on the same page. Videos are typically retained for a limited period (e.g. 30 days) per Sauce Labs policy.

## Project Structure

```
automation-ddt/
├── test_login_ddt.py    # Data-driven login tests (local + Sauce Labs)
├── create_test_data.py  # Creates sample test_data.xlsx
├── test_data.xlsx       # Excel test data (create via create_test_data.py)
├── requirements.txt
└── README.md
```

## Code Quality

- No hard-coded credentials; Sauce Labs uses `SAUCE_USERNAME` and `SAUCE_ACCESS_KEY` from the environment.
- Exception handling for missing file, missing env, timeouts, and WebDriver errors.
- Browser/driver is closed after each test case (in a `finally` block).
- Single-responsibility functions, clear naming, and comments where useful.
- Uses current Selenium options/capabilities (no deprecated APIs).
