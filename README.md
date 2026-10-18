# Sauce Demo - Playwright Test Automation

This repository contains an automated testing framework for the Sauce Demo e-commerce website. It is built using Python, Playwright, and Pytest.

## 🏗️ Architecture
The project strictly follows the Page Object Model (POM) design pattern to ensure clean, maintainable, and reusable code.

**Key Features:**
- **Separation of Concerns:** Independent classes for LoginPage, HomePage, and Checkout.
- **Dynamic Locators:** Implementation of f-strings for dynamic item selection (e.g., adding/removing specific products from the cart).
- **DRY Principle:** Reusable helper methods like `full_login()` to avoid code duplication in test setups.
- **CI/CD Pipeline:** Automated regression testing triggered on every `git push` using GitHub Actions.

## 🛠️ Tech Stack
- Python
- Playwright (Sync API)
- Pytest
- GitHub Actions (CI/CD)

## 🚀 How to Run Locally

**1. Clone the repository:**
```bash
git clone [https://github.com/Ad4mB3/sauce-demo-playwright-automation.git](https://github.com/Ad4mB3/sauce-demo-playwright-automation.git)
```

**2. Install dependencies:**
```bash
pip install -r requirements.txt
playwright install
```

**3. Run the tests:**
```bash
pytest
```

## 🧪 Test Coverage
The suite covers the core functionality of the e-shop:
- Successful and unsuccessful login attempts
- Dynamic addition and removal of items in the cart
- Application state reset and navigation
- Successful logout workflow