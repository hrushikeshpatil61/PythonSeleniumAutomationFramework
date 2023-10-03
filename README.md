# Here I have used dummy webite to build testing framework. 
  https://www.saucedemo.com/

# CompleteTestAutomaitonProject
  This project implements Selenium to build automation testing framework.
  Here pytest is used to design tests.

# When you are in your root directory run all tests using follwoing commands 
**1. to generate HTML REPORTS**
  pytest -s -v main.py --html=Reports\report.html --username standard_user --password secret_sauce

**2. to generate allure reports**
  pytest -s -v main.py --alluredir="reports" --username standard_user --password secret_sauce
