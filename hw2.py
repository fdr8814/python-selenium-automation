from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep





# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)


driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')


driver.find_element(By.XPATH, "//a[@href='/gp/css/order-history?ref_=nav_orders_first']").click()

expected_result = 'Sign in'
actual_result = driver.find_element(By.XPATH, "//h1[contains(text(), 'Sign in')]").text

assert expected_result == actual_result, f'expected esult {expected_result} did not match with an actual result {actual_result}'
driver.find_element(By.XPATH, "//input[@type='email']")

print('test case passed')

driver.quit()