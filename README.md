# Web Automation Test Suite

Simple web automation testing framework using Python, Selenium, and Pytest.

## Overview

This project contains automated tests for web applications:
- **Part 1**: Basic assertions on Google homepage (3 tests - all passing ✅)
- **Part 2**: Restaurant search on Google Maps (4 tests - code ready)

## Quick Start

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run tests**
   ```bash
   pytest -v              # All tests
   pytest -v -m part1     # Part 1 only (3 tests)
   pytest -v -m part2     # Part 2 only (4 tests)
   ```

## Requirements

- Python 3.11+
- Chrome or Firefox browser
- Internet connection (for Part 2)

## What Gets Tested

### Part 1: Google Homepage
- ✅ Page title contains "Google"
- ✅ Search input box is visible
- ✅ Search button is visible

### Part 2: Google Maps Restaurant Search
- Google Maps page loads
- Restaurant search returns results
- First restaurant has a name
- Results are valid

## Project Structure

```
tests/
├── part1_basic/
│   └── test_google_homepage.py       (3 tests)
└── part2_restaurant/
    └── test_restaurant_search.py     (4 tests)

page_objects/
├── google_homepage.py                (Google page interactions)
└── google_maps.py                    (Maps page interactions)

utils/
├── driver_factory.py                 (Browser management)
├── logger.py                         (Test logging)
├── screenshot_manager.py             (Failure screenshots)
└── wait_helper.py                    (Smart waits)

config/
└── settings.py                       (Configuration)

conftest.py                           (Pytest fixtures)
pytest.ini                            (Test config)
requirements.txt                      (Dependencies)
.env                                  (Environment variables)
```

## Configuration

Modify `.env` to change test behavior:

```env
BROWSER=chrome              # chrome or firefox
HEADLESS=True              # False to see browser
EXPLICIT_WAIT=15           # Wait timeout (seconds)
LOG_LEVEL=INFO             # DEBUG for more details
```

## How It Works

### Page Object Model
Each website has a page class handling interactions:

```python
from page_objects.google_homepage import GoogleHomepage

page = GoogleHomepage(driver)
title = page.get_page_title()
is_visible = page.is_search_box_visible()
```

### WebDriver Factory
Manages browser creation and cleanup:
- Automatically downloads ChromeDriver/GeckoDriver
- Supports Chrome and Firefox
- Handles headless mode

### Test Fixtures
Pytest fixtures setup/teardown for each test:
- `driver` fixture: Creates new browser instance
- Automatically closes after test completes

### Logging
All actions logged to `logs/` directory with timestamps.

### Screenshots
Automatic screenshots on test failures saved to `screenshots/` directory.

## Running Tests

```bash
# Verbose output
pytest -v

# Only Part 1 (basic assertions)
pytest -v -m part1

# Only Part 2 (restaurant search)
pytest -v -m part2

# Generate HTML report
pytest --html=reports/report.html --self-contained-html

# Stop on first failure
pytest -x

# Debug mode (see browser)
HEADLESS=False pytest -v
```

## Troubleshooting

**Tests timeout?**
```env
EXPLICIT_WAIT=30        # Increase wait time
```

**Browser not opening?**
```bash
pip install --upgrade webdriver-manager
```

**Want to debug?**
```env
HEADLESS=False          # See what browser does
LOG_LEVEL=DEBUG         # More verbose logs
```

**Still having issues?**
- Check logs/ directory for detailed error messages
- Check screenshots/ directory for failure screenshots
- Ensure Chrome/Firefox is installed
- Check internet connection for Part 2

## Test Results

**Part 1 (Google Homepage)**
```
test_page_title_assertion ✅ PASSED
test_search_box_is_visible ✅ PASSED  
test_search_button_is_visible ✅ PASSED
```

**Part 2 (Restaurant Search)**
```
test_google_maps_page_loads - Ready
test_restaurant_search_returns_results - Ready
test_first_restaurant_has_name - Ready
test_restaurant_results_verification - Ready
```

## Tools Used

- **Selenium 4.15**: Web browser automation
- **Pytest 9.0**: Test framework
- **WebDriver Manager 4.0**: Automatic driver downloads
- **Python-dotenv 1.0**: Configuration management
- **Pytest-HTML 4.1**: Test reports
- **Pillow 10.0**: Screenshot capture

## Notes

- Part 2 requires Google Maps to load properly (internet dependent)
- Default browser is Chrome, switch to Firefox in .env
- All test logs saved to logs/ directory
- Failed test screenshots saved to screenshots/ directory
- HTML report generated to reports/report.html

## Design Patterns Used

- **Page Object Model**: Encapsulates page interactions
- **Singleton Pattern**: Logger instance management
- **Factory Pattern**: WebDriver creation
