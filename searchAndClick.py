import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://coerver.draftserver.com/players-club/")
driver.maximize_window()

search = driver.find_element(By.XPATH, "//input[@id = 'course-text']" ).send_keys("Skills" + Keys.ENTER)
time.sleep(5)

search = driver.find_element(By.XPATH, "//input[@id = 'course-text']" ).clear()

# first_item = driver.find_element(By.CSS_SELECTOR, ".rt-tbody[]")
# first_item.click()

# login_item = driver.find_element(By.ID, "login")
# login_item.click()

time.sleep(20)
driver.quit()