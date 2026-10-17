# Sauce Demo - Playwright Test Automation

This repository contains an automated testing framework for the [Sauce Demo e-commerce website](https://www.saucedemo.com/). It is built using **Python**, **Playwright**, and **Pytest**.

## 🏗️ Architecture
The project strictly follows the **Page Object Model (POM)** design pattern to ensure clean, maintainable, and reusable code. 

### Key Features:
* **Separation of Concerns:** Independent classes for `LoginPage`, `HomePage`, and `Checkout`.
* **Dynamic Locators:** Implementation of `f-strings` for dynamic item selection (e.g., adding/removing specific products from the cart).
* **DRY Principle:** Reusable helper methods like `fulllogin()` to avoid code duplication in test setups.

## 🛠️ Tech Stack
* Python
* Playwright (Sync API)
* Pytest

## 🚀 How to Run Locally
1. Clone the repository:
   ```bash
   git clone [https://github.com/Ad4mB3/sauce-demo-playwright-automation.git](https://github.com/Ad4mB3/sauce-demo-playwright-automation.git)
Install dependencies:

Bash
pip install -r requirements.txt
playwright install
Run the tests:

Bash
pytest
🧪 Test Coverage
The suite covers the core functionality of the e-shop:

Successful and unsuccessful login attempts

Dynamic addition and removal of items in the cart

Application state reset and navigation

Successful logout workflow
