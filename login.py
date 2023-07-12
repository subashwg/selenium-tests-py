
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

os.environ['PATH'] += r"C:/SeleniumDrivers"
driver = webdriver.Chrome()


#login module element testing
driver.get("https://demoqa.com/login")

my_element = driver.find_element(By.ID, "userName")
my_element.send_keys("myusername")

my_second_element = driver.find_element(By.ID, "password")
my_second_element.send_keys("testpassword")

my_third_element = driver.find_element(By.ID, "login")
my_third_element.click()

time.sleep(10)

