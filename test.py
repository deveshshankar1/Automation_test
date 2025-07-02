from selenium import webdriver
import requests
import time
import datetime
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import argparse
parser = argparse.ArgumentParser()

email = input("Enter email: ")
password = input("Enter password: ")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://magento.softwaretestingboard.com/")

sign_in_button = driver.find_element(By.XPATH, "/html/body/div[2]/header/div[1]/div/ul/li[2]/a")
sign_in_button.click()

time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(email)
driver.find_element(By.XPATH, '//*[@id="pass"]').send_keys(password)

login_button = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div/div[2]/div[1]/div[2]/form/fieldset/div[4]/div[1]/button/span")
login_button.click()

time.sleep(2)

dropdown_button = driver.find_element(By.XPATH, "/html/body/div[2]/header/div[1]/div/ul/li[2]/span/button")
dropdown_button.click()

time.sleep(2)

account_button = driver.find_element(By.XPATH, "/html/body/div[2]/header/div[1]/div/ul/li[2]/div/ul/li[1]/a")
account_button.click()

time.sleep(5)

change_pass = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[2]/div[1]/div[3]/div[2]/div/div[2]/a[2]")
change_pass.click()

curr_pass=password
new_pass=input("Enter new password: ")
confirm_pass=new_pass

driver.find_element(By.XPATH, '//*[@id="current-password"]').send_keys(curr_pass)
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(new_pass)
driver.find_element(By.XPATH, '//*[@id="password-confirmation"]').send_keys(confirm_pass)

time.sleep(10)

save_button = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[2]/div[1]/form/div/div[1]/button/span")
save_button.click()

time.sleep(5)