#Practice with locators. 
#Create locators + search strategy for these page elements of Amazon Sign in page:
#Amazon logo
#Email field
#Continue button
#Conditions of use link
#Privacy Notice link
#Need help link
#Forgot your password link
#Other issues with Sign-In link
#Create your Amazon account button
#For example: 
#Email field, search by ID, “ap_email”

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
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fs%3Fk%3Dmug%26crid%3D3W4NQHWM7Y8EG%26sprefix%3Dmug%252Caps%252C245%26ref%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

#Amazon logo
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")

#Email field
driver.find_element(By.XPATH, "//input[@type='email']")

#Continue button
driver.find_element(By.XPATH, "//input[@id='continue']")

#Conditions of use link
driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_desktop_footer_cou?ie=UTF8&nodeId=508088']")

#Privacy Notice link
driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_desktop_footer_privacy_notice?ie=UTF8&nodeId=468496']")

#Need help link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

#Forgot your password link
driver.find_element(By.XPATH, "//a[@id='auth-fpp-link-bottom']")

#Other issues with Sign-In link
driver.find_element(By.XPATH, "//a[@id='ap-other-signin-issues-link']")

#Create your Amazon account button
driver.find_element(By.XPATH, "//a[@id='createAccountSubmit']")


driver.find_element(By.XPATH, "//h1[contains(text(), 'Sign in')]")