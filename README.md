# QA Brains Technical Assessment

This repository contains automated tests for the QA Brains practice website (https://practice.qabrains.com/). The tests cover authentication, e-commerce, and drag & drop functionalities.

## Project Structure
```
tests/
├── authentication/       # Authentication test cases
├── drag&drop/           # Drag and drop test cases
├── Form submission/     # Form submission test cases
└── eCommerce Test/      # E-commerce test cases
```

## Test Suites
1. **Authentication Tests**
   - Login with valid/invalid credentials
   - User registration
   - Password recovery
   - Feedback submission

2. **E-Commerce Tests**
   - Add items to cart
   - Add to favorites
   - Checkout process
   - Payment validation
   - Empty cart handling

3. **Drag & Drop Tests**
   - Basic drag and drop
   - Edge cases
   - Accessibility testing
   - Visual feedback

4. **Form Submission Tests**
   - Missing name validation
   - Form validation
   - Form submission handling

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/tanim1993edu/Technical_Assessment01.git
cd Technical_Assessment01
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Install Playwright browsers:
```bash
playwright install
```

## Running Tests

To run specific test suites:

1. Authentication Tests:
```bash
pytest tests/authentication --html=reports/authentication/report.html
```

2. E-Commerce Tests:
```bash
pytest "tests/eCommerce Test" --html=reports/ecommerce/report.html
```

3. Drag & Drop Tests:
```bash
pytest tests/drag&drop --html=reports/drag_and_drop/report.html
```

4. Form Submission Tests:
```bash
pytest "tests/Form submission" --html=reports/form_submission/report.html
```

To run all tests:
```bash
pytest tests/ -v --html=reports/all_tests/report.html
```

## Test Reports

HTML reports are generated in the `reports` folder:
- Authentication: `reports/authentication/report.html`
- E-commerce: `reports/ecommerce/report.html`
- Drag & Drop: `reports/drag_and_drop/report.html`
- Form Submission: `reports/form_submission/report.html`
- Combined: `reports/all_tests/report.html`

## Requirements
- Python 3.8+
- Playwright
- pytest
- pytest-html

## Test Data
Test data is stored in `data/test_data.json`