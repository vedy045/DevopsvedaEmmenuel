"""
ITLDO801 Assignment 3 — Selenium Test Logging
Student: Setako Vedaste | Registration: 20250203
Date: 2026-10-26
Run: python test_portfolio.py
Each run writes a unique timestamped log. TC-07 intentionally demonstrates a
negative test by recording the missing #missing-section as FAIL.
"""
import logging, platform, time
from datetime import datetime
from pathlib import Path
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

BASE_DIR = Path(__file__).resolve().parent
LOG_DIR = BASE_DIR / "logs"
SCREENSHOT_DIR = LOG_DIR / "screenshots"
LOG_DIR.mkdir(exist_ok=True)
SCREENSHOT_DIR.mkdir(exist_ok=True)
PORTFOLIO_URL = "https://vedy045.github.io/DevopsvedaEmmenuel/"
STAMP = datetime.now().strftime("%Y%m%d_%H%M%S")
LOG_PATH = LOG_DIR / f"selenium_run_{STAMP}.log"
logger = logging.getLogger("portfolio_tests")
logger.setLevel(logging.INFO)
logger.handlers.clear()
handler = logging.FileHandler(LOG_PATH, encoding="utf-8")
handler.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(message)s", datefmt="%Y-%m-%d %H:%M:%S"))
logger.addHandler(handler)
logger.propagate = False

TESTS = [
    ("TC-01", "Open portfolio homepage", "Homepage loads and has a non-empty title", "home"),
    ("TC-02", "Navigate to About", "About section exists and can be navigated to", "about"),
    ("TC-03", "Navigate to Expertise", "Services section exists and can be navigated to", "services"),
    ("TC-04", "Navigate to Portfolio", "Portfolio section exists and can be navigated to", "portfolio"),
    ("TC-05", "Navigate to Skills", "Skills section exists and can be navigated to", "skills"),
    ("TC-06", "Navigate to Contact", "Contact section exists and can be navigated to", "contact"),
    ("TC-07", "Negative test: missing section", "Missing section is detected and recorded as a failure", "missing-section"),
]

def main():
    run_start = time.perf_counter()
    passed = failed = 0
    driver = None
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1440,1000")
        driver = webdriver.Chrome(options=options)
        driver.get(PORTFOLIO_URL)
        browser = driver.capabilities.get("browserName", "unknown")
        version = driver.capabilities.get("browserVersion", "unknown")
        logger.info("RUN START | timestamp: %s | website: %s | browser: %s %s | OS: %s %s",
                    datetime.now().isoformat(timespec="seconds"), PORTFOLIO_URL, browser, version,
                    platform.system(), platform.release())
        wait = WebDriverWait(driver, 10)
        for test_id, description, expected, target in TESTS:
            test_start = time.perf_counter()
            actual, error, status = "", None, "FAIL"
            try:
                if target == "home":
                    wait.until(lambda d: d.title.strip() != "")
                    actual = f"Homepage loaded; title='{driver.title}'"
                    status = "PASS" if driver.current_url.startswith(PORTFOLIO_URL) and driver.title.strip() else "FAIL"
                elif target == "missing-section":
                    try:
                        driver.find_element(By.ID, target)
                        actual = "Unexpectedly found #missing-section"
                        error = "Negative test did not detect the expected missing section"
                    except Exception:
                        actual = "Missing #missing-section correctly detected by the negative check"
                        error = "Expected negative-test failure: element '#missing-section' does not exist"
                    status = "FAIL"
                else:
                    element = wait.until(EC.presence_of_element_located((By.ID, target)))
                    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
                    links = driver.find_elements(By.CSS_SELECTOR, f'a[href="#{target}"]')
                    actual = f"Section #{target} exists; matching navigation links: {len(links)}"
                    status = "PASS" if element.is_displayed() and len(links) > 0 else "FAIL"
                    if status == "FAIL":
                        error = "Section or matching navigation link was not visible/found"
            except Exception as exc:
                actual, error, status = f"{type(exc).__name__}: {exc}", str(exc), "FAIL"
            duration = time.perf_counter() - test_start
            if status == "PASS":
                passed += 1
                level = logging.INFO
            else:
                failed += 1
                level = logging.ERROR
                try:
                    shot = SCREENSHOT_DIR / f"{test_id}_fail_{STAMP}.png"
                    driver.save_screenshot(str(shot))
                    error = f"{error or 'Test assertion failed'} | screenshot: {shot.relative_to(BASE_DIR)}"
                except WebDriverException:
                    pass
            logger.log(level, "%s | %s | expected: %s | actual: %s | %s | duration: %.2fs | url: %s%s",
                       test_id, description, expected, actual, status, duration, driver.current_url,
                       f" | error: {error}" if error else "")
    except Exception as exc:
        failed += 1
        logger.exception("ERROR | Test setup or browser startup failed: %s", exc)
    finally:
        if driver:
            driver.quit()
        duration = time.perf_counter() - run_start
        logger.info("RUN END | total: %s | passed: %s | failed: %s | duration: %.2fs",
                    passed + failed, passed, failed, duration)
        for h in logger.handlers:
            h.flush()
            h.close()
        print(f"Log saved to: {LOG_PATH}")
        print(f"Summary: total={passed + failed}, passed={passed}, failed={failed}, duration={duration:.2f}s")

if __name__ == "__main__":
    main()
