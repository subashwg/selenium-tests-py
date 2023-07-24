import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://astrareviews.com/")
driver.maximize_window()

# HEADER AND SEARCH BAR CASES
search = driver.find_element(By.CLASS_NAME, "search-toggle")
search = driver.find_element(By.TAG_NAME, "input").send_keys("rich")
search = driver.find_element(By.CLASS_NAME, "search-field").send_keys("rich"+ Keys.ENTER)
search = driver.implicitly_wait(20)
time.sleep(20)


search = driver.find_element(By.XPATH, "//input[@class = 'course-text']" ).send_keys("Skills" + Keys.ENTER)
time.sleep(5)

search = driver.find_element(By.XPATH, "//input[@id = 'course-text']" ).clear()

first_item = driver.find_element(By.CSS_SELECTOR, ".rt-tbody[]")
first_item.click()

login_item = driver.find_element(By.ID, "blossomthemes-email-newsletter-114")
login_item.click()

login_item = driver.find_element(By.XPATH, "//input[@id = 'blossomthemes-email-newsletter-114']" ).send_keys("testemail@sel.com" + Keys.ENTER)
login_item = driver.find_element(By.XPATH, "//input[@class = 'subscribe-submit-114']").click()

time.sleep(2000)
driver.quit()