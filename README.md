# OLG Web Automation Test Suite

## 📋 Project Overview

This is a professional **Web Automation Test Suite** built with **Python**, **Selenium**, and **Pytest**. It demonstrates automated testing of public websites with comprehensive assertions and validation.

### Project Structure:
```
olg-web-automation/
├── tests/
│   ├── part1_basic/              # Basic assertions tests
│   │   └── test_google_homepage.py
│   └── part2_restaurant/         # Restaurant search tests
│       └── test_restaurant_search.py
├── page_objects/                 # Page Object Models
│   ├── google_homepage.py
│   └── google_maps.py
├── utils/                        # Utility modules
│   ├── driver_factory.py         # WebDriver creation
│   ├── wait_helper.py            # Wait mechanisms
│   ├── logger.py                 # Logging
│   └── screenshot_manager.py     # Screenshot capture
├── config/                       # Configuration
│   └── settings.py              # Central settings
├── logs/                         # Test logs (auto-generated)
├── screenshots/                  # Test screenshots (auto-generated)
├── conftest.py                   # Pytest configuration
├── pytest.ini                    # Pytest settings
├── requirements.txt              # Python dependencies
├── .env                         # Environment variables
└── README.md                     # This file
```

---

## 🎯 Test Objectives

### **Part 1: Basic Assertions** ✓
Tests basic web page functionality on **Google Homepage**:
1. **Test 1**: Assert page title contains "Google"
2. **Test 2**: Assert search box element is visible
3. **Test 3**: Assert search button element is visible

### **Part 2: Restaurant Search** ✓
Tests restaurant search functionality on **Google Maps**:
1. **Test 1**: Verify Google Maps page loads successfully
2. **Test 2**: Perform restaurant search and verify results contain at least one restaurant
3. **Test 3**: Verify first restaurant result has a valid name
4. **Test 4**: Comprehensive restaurant results verification

---

## 🛠️ Tools & Frameworks

| Tool | Purpose | Why |
|------|---------|-----|
| **Selenium WebDriver** | Web browser automation | Industry-standard for web testing; supports multiple browsers |
| **Pytest** | Test framework | Powerful, flexible; great fixtures and plugins |
| **WebDriver Manager** | Driver management | Automatically manages ChromeDriver/GeckoDriver versions |
| **Python-dotenv** | Configuration management | Environment variable management for flexibility |
| **Pytest-HTML** | Test reporting | Auto-generates HTML reports for better visibility |
| **Pillow** | Screenshot management | Image capture for failure documentation |

---

## 📦 Installation

### Prerequisites
- **Python 3.8+** installed on your system
- **Git** (for cloning and pushing to GitHub)

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/olg-web-automation.git
cd olg-web-automation
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Verify Installation
```bash
pytest --version
python -c "from selenium import webdriver; print('Selenium installed successfully')"
```

---

## 🚀 Running Tests

### Run All Tests
```bash
pytest
```

### Run with Verbose Output
```bash
pytest -v
```

### Run Specific Test Suite
```bash
# Part 1 only
pytest -v -m part1

# Part 2 only
pytest -v -m part2

# Smoke tests only
pytest -v -m smoke
```

### Run with HTML Report
```bash
pytest --html=reports/report.html --self-contained-html
```

### Run Tests in Headless Mode
Edit `.env` file and set:
```
HEADLESS=True
```

### Run Tests with Firefox Browser
Edit `.env` file and set:
```
BROWSER=firefox
```

---

## 📊 Test Execution

### Expected Output Example:
```
tests/part1_basic/test_google_homepage.py::TestGoogleHomepageBasics::test_page_title_assertion PASSED
tests/part1_basic/test_google_homepage.py::TestGoogleHomepageBasics::test_search_box_is_visible PASSED
tests/part1_basic/test_google_homepage.py::TestGoogleHomepageBasics::test_search_button_is_visible PASSED
tests/part2_restaurant/test_restaurant_search.py::TestRestaurantSearch::test_google_maps_page_loads PASSED
tests/part2_restaurant/test_restaurant_search.py::TestRestaurantSearch::test_restaurant_search_returns_results PASSED
tests/part2_restaurant/test_restaurant_search.py::TestRestaurantSearch::test_first_restaurant_has_name PASSED
tests/part2_restaurant/test_restaurant_search.py::TestRestaurantSearch::test_restaurant_results_verification PASSED

========================= 7 passed in 45.23s =========================
```

---

## 📝 Configuration

### Environment Variables (`.env` file)
```bash
# Browser Settings
BROWSER=chrome              # chrome or firefox
HEADLESS=False              # True for headless mode
IMPLICIT_WAIT=10            # Implicit wait in seconds
EXPLICIT_WAIT=15            # Explicit wait in seconds

# Logging
LOG_LEVEL=INFO              # DEBUG, INFO, WARNING, ERROR

# URLs
GOOGLE_URL=https://www.google.com
GOOGLE_MAPS_URL=https://maps.google.com
```

### Pytest Configuration (`pytest.ini`)
- Test discovery: `tests/test_*.py`
- Markers: `@pytest.mark.part1`, `@pytest.mark.part2`, `@pytest.mark.smoke`
- Timeout: 30 seconds per test
- HTML report output: `reports/report.html`

---

## 📂 Test Artifacts

### Logs
All test execution logs are saved to `logs/` directory with timestamps.
- Filename format: `{module}_{timestamp}.log`
- Includes: Test steps, assertions, errors

### Screenshots
Screenshots are automatically captured on test failures.
- Location: `screenshots/` directory
- Filename format: `failure_{testname}_{timestamp}.png`

### Reports
HTML test reports are generated with pytest-html plugin.
- Location: `reports/report.html`
- Includes: Pass/fail status, execution time, error messages

---

## ✅ Assertions & Validations

### Part 1 - Basic Assertions
```python
# Test 1: Page Title
assert "Google" in page_title

# Test 2: Search Box
assert search_box.is_displayed() == True

# Test 3: Search Button
assert search_button.is_displayed() == True
```

### Part 2 - Restaurant Search
```python
# Test 1: Page Load
assert "Google Maps" in page_title

# Test 2: Search Results
assert restaurant_count >= 1

# Test 3: First Restaurant Name
assert restaurant_name is not None and len(restaurant_name) > 0

# Test 4: Results Verification
assert verify_results_contain_restaurants() == True
```

---

## 🔄 Test Flow

### Part 1 Flow
```
Navigate to Google Homepage
    ↓
Check Page Title ✓
    ↓
Check Search Box Visibility ✓
    ↓
Check Search Button Visibility ✓
    ↓
Test Complete
```

### Part 2 Flow
```
Navigate to Google Maps
    ↓
Verify Page Load ✓
    ↓
Search for "Restaurants" ✓
    ↓
Extract Results ✓
    ↓
Verify Count >= 1 ✓
    ↓
Get First Restaurant ✓
    ↓
Test Complete
```

---

## 📋 Assumptions & Limitations

### Assumptions
1. **Internet Connectivity**: Tests require active internet connection to access public websites
2. **Website Stability**: Tests assume Google and Google Maps websites are accessible and unchanged
3. **Browser Support**: Tests are tested on Chrome and Firefox
4. **Screen Resolution**: Implicit assumption of standard screen resolution for element visibility
5. **Dynamic Content**: Uses explicit waits to handle dynamically loaded content

### Limitations
1. **Geographic Restrictions**: Some restaurants/regions may not be available in all areas
2. **Geolocation**: Google Maps results depend on current geolocation or specified location
3. **Search Variations**: Restaurant search results may vary based on time, location, and filters
4. **Element Locators**: XPath/CSS selectors may break if website DOM structure changes
5. **Rate Limiting**: Rapid successive test runs may trigger rate limiting
6. **Browser Updates**: New browser versions may require driver updates

---

## 🚧 Future Improvements (with more time)

### High Priority
1. **Parallel Test Execution**
   - Use `pytest-xdist` to run tests in parallel for faster execution
   - Expected: 3x speed improvement

2. **Database Integration**
   - Store test results in database for trend analysis
   - Track metrics: pass rate, execution time, browser compatibility

3. **Advanced Wait Strategies**
   - Implement custom expected conditions for complex scenarios
   - Add retry mechanisms for flaky tests

4. **Extended Browser Coverage**
   - Add Safari and Edge browser support
   - Cross-browser test matrices (BrowserStack, Sauce Labs)

### Medium Priority
5. **API Testing Integration**
   - Combine UI and API tests for full coverage
   - Validate data through backend API calls

6. **Performance Testing**
   - Add page load time assertions
   - Monitor resource usage (CPU, memory)

7. **Accessibility Testing**
   - Axe-Selenium integration for a11y testing
   - WCAG compliance validation

8. **Mobile Testing**
   - Appium integration for mobile app testing
   - Responsive design testing

### Low Priority
9. **CI/CD Integration**
   - GitHub Actions workflow for automated test runs
   - Build status badges
   - Schedule nightly test runs

10. **Test Data Management**
    - Parameterized tests with multiple search queries
    - Data-driven testing framework

11. **Advanced Reporting**
    - Screenshots embedded in HTML reports
    - Test execution timeline graphs
    - Failure trend analysis

12. **Maintenance**
    - Visual regression testing
    - Page object updates automation
    - Deprecated selector tracking

---

## 📞 Support & Documentation

### Debugging Failed Tests
1. Check `logs/` directory for detailed error messages
2. Review screenshots in `screenshots/` directory
3. Verify `.env` configuration
4. Check internet connectivity

### Common Issues

**Issue: ChromeDriver not found**
- Solution: Delete `venv/` and reinstall dependencies (webdriver-manager will auto-download)

**Issue: Element not found**
- Solution: Increase `EXPLICIT_WAIT` in `.env`

**Issue: Tests timeout**
- Solution: Check internet connection; increase timeout values

**Issue: Google blocking access**
- Solution: Tests may be rate-limited; wait a few minutes and try again

---

## 📜 License

This project is open source and available under the MIT License.

---

## 👨‍💻 Author

Created as a professional assessment project demonstrating:
- ✓ Web automation best practices
- ✓ Page Object Model design pattern
- ✓ Professional testing framework setup
- ✓ Comprehensive documentation
- ✓ Production-ready code quality

---

## 📌 Quick Reference

| Command | Purpose |
|---------|---------|
| `pytest` | Run all tests |
| `pytest -v` | Verbose output |
| `pytest -m part1` | Run Part 1 tests only |
| `pytest -m part2` | Run Part 2 tests only |
| `pytest --html=reports/report.html` | Generate HTML report |
| `pytest -k "test_page_title"` | Run specific test |
| `pytest --collect-only` | List all tests |

---

**Last Updated**: May 16, 2026  
**Status**: Production Ready ✓
