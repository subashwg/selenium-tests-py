import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
    
driver.get("https://coerver.draftserver.com/players-club/account/")

driver.find_element(By.XPATH, "//input[@id = 'username']").send_keys ("coervertestme@dropjar.com")

driver.find_element(By.XPATH, "//input[@id = 'password']").send_keys ("Password123!@#")

driver.find_element(By.XPATH, "//*[contains(text(), 'Remember me')]").click()

driver.find_element(By.CSS_SELECTOR, "button[name ='account_login']").click()

time.sleep(20)
