from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import os
import time

email = os.environ["EMAIL"]
password = os.environ["PASSWORD"]
phonenumber = os.environ["PHONENUMBER"]

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

login = driver.find_element_by_xpath('/html/body/header/nav/div/a[2]')
login.click()

time.sleep(3)
email_input = driver.find_element_by_id("username")
email_input.send_keys(email)
password_input = driver.find_element_by_id("password")
password_input.send_keys(password)

button = driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
button.click()

time.sleep(3)
job = driver.find_element_by_css_selector(".jobs-search-results ul li")
item_id = job.get_attribute("id")
print(item_id)
job.click()

time.sleep(3)
apply_button = driver.find_element_by_css_selector(".jobs-apply-button--top-card")
apply_button.click()

time.sleep(3)
phone_input = driver.find_element_by_css_selector(".fb-single-line-text__input")
if phone_input.text == "":
    phone_input.send_keys(phonenumber)

next_button = driver.find_element_by_css_selector(".artdeco-button")
next_button.click()