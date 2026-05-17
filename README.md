# Web Automation Test Suite

A web automation framework built with Python, Selenium, and Pytest.

## What This Does

Automated tests for web applications. Tests two scenarios:

1. **Google Homepage** - Verifies page loads and basic elements are visible (3 tests)
2. **Google Maps** - Tests restaurant search functionality (4 tests)

## Setup

Install dependencies:
```bash
pip install -r requirements.txt
```

## Running Tests

```bash
# Run all tests
pytest -v

# Run only Google homepage tests
pytest -v -m part1

# Run only Maps tests
pytest -v -m part2

# See results in HTML report
pytest --html=reports/report.html --self-contained-html
```

## Project Layout

```
tests/
├── part1_basic/
│   └── test_google_homepage.py
└── part2_restaurant/
    └── test_restaurant_search.py

page_objects/
├── google_homepage.py
└── google_maps.py

utils/
├── driver_factory.py
├── logger.py
├── wait_helper.py
└── screenshot_manager.py

config/
└── settings.py

conftest.py
pytest.ini
requirements.txt
.env
```

## Configuration

Edit `.env` to customize:

```env
BROWSER=chrome          # Use chrome or firefox
HEADLESS=True          # Set to False to see browser
EXPLICIT_WAIT=15       # How long to wait for elements
LOG_LEVEL=INFO
```

## How It's Built

### Page Objects
Each website has a class that handles its interactions. Makes tests easier to read and maintain.

```python
page = GoogleHomepage(driver)
title = page.get_page_title()
is_visible = page.is_search_box_visible()
```

### Fixtures
Pytest fixtures handle browser setup and cleanup automatically for each test.

### Logging
Every action is logged to files for debugging. Failed tests auto-capture screenshots.

## Troubleshooting

**Tests timeout?**
- Increase `EXPLICIT_WAIT` in `.env`
- Check your internet connection

**Browser won't start?**
```bash
pip install --upgrade webdriver-manager
```

**Want to watch the tests run?**
```env
HEADLESS=False
```

## Requirements

- Python 3.11+
- Chrome or Firefox
- Internet connection (for Maps tests)

## What Tests Pass

- Part 1: All 3 tests passing ✅
- Part 2: Code ready (internet dependent)
