# orangehrm-test-automation (Pytest + POM)
Leave and Recruitment Module Test Automation Suite

## Project Overview

This project is a Selenium automation framework built using Python, Pytest and Page Object Model (POM).

The framework automates the following scenarios:

- Login to OrangeHRM
- Add Leave Type
- Assign Leave
- Add Recruitment Vacancy
- Logout
- Generate HTML report

The framework is clean, maintainable and easy to scale.

## Tools and Technologies Used

- Python 3.x
- Selenium WebDriver
- Pytest
- Pytest-HTML
- Page Object Model (POM)
- Google Chrome
- PyCharm IDE

## Prerequisites

Before running this project, ensure:

- Python is installed
- Google Chrome is installed
- ChromeDriver matches Chrome version
- Virtual environment is created

## Setup Steps

1. Clone the repository or download project.
2. Navigate to project folder:

   cd PYTEST

3. Create virtual environment:

   python -m venv .venv

4. Activate virtual environment:

   Windows:
   .venv\Scripts\activate

5. Install dependencies:

   pip install selenium
   pip install pytest
   pip install pytest-html

## Test Execution Steps

Run test normally:

   pytest -v

Run test with HTML report:

   pytest -v --html=reports/report_org.html 

Report will be generated inside:

   reports/report_org.html

Open it in browser.

## Assumptions

- OrangeHRM demo site is available.
- Valid credentials are available
- ChromeDriver is properly configured.

## Limitations

- Test data is hardcoded.
- Framework currently supports Chrome only.
- No parallel execution configured.
- No CI/CD integration added.
