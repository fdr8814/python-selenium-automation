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

#open a web page
driver.get('https://www.amazon.com/')

# psearch by id
search = driver.find_element(By.ID, 'twotabsearchtextbox')

#search by XPATH
search = driver.find_element(By.XPATH, "//input[@placeholder='Search Amazon']")
search = driver.find_element(By.XPATH, "//input[@value='Go']")

#search by XPATH, multiplle atributes
search = driver.find_element(By.XPATH, "//input[@placeholder='Search Amazon' and @name='field-keywords']")

#search by XPATH, text()
search = driver.find_element(By.XPATH, "//h2[text()=\"Women’s sweaters starting at $20\"]")
searc = driver.find_element(By.XPATH, "//a[text()='Best Sellers' and @class='nav-a  ']")

#contains()
search = driver.find_element(By.XPATH, "//input[contains(@placeholder, 'Search')]")
searc = driver.find_element(By.XPATH, "//a[contains(text(), 'Best Sellers') and @class='nav-a  ']")

#from parent to child
searc = driver.find_element(By.XPATH, "//div[@id='nav-main']//a[text()='Best Sellers']")